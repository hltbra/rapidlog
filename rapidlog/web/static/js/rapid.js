function setupheight() {
    // Some ui setup, fix it future
    var height = window.innerHeight-2*60;

    $(".stratch").css("height", height);
    $("#daemons.sidebar-nav").css("height", height/4 );

    var infoheight = window.innerHeight/2;
    $("div#info").css("height", infoheight );
};

function addtext(text, loggername, level) {
    var el = $('<span>').html(text+'\n').css("display", 'none');
    if (level=='ERROR')
        el.css("color", "red");
    else if (level=="WARNING")
        el.css("color", "purple");
    else if (level=="INFO")
        el.css("color", "green");

    var curpanel = $("pre#log[logger="+loggername+"]");
    if (curpanel.find("span").length>1000)
        curpanel.empty();

    curpanel.prepend(el);
    curpanel.find("span:first").fadeIn('fast');

    $("#scrolling").scrollspy('refresh');
};

function ws_init(url) {
	console.log("connecting to " + url + "...");
	ws = new WebSocket(url);

	ws.onopen = function(){
		console.log("Connection established");
	};
	ws.onmessage = function(msg){
        var obj = jQuery.parseJSON(msg.data);
        addtext(obj.msg, obj.loggername, obj.level)
	};
	ws.onclose = function(){
        setTimeout(function() {ws_init(url)}, 5000)
	}
};


$(document).ready(function(){
    $("li[logger]").bind("call_logger", function(evt, params) {

        $("div[logger="+params.prev.attr("logger")+"]").hide();
        $("div[logger="+params.loggername+"]").show();
    });

    // Setup scrolling area
    $("#scrolling").scrollspy();

    // Set first logger as active
    var active_logger = $("li[logger]:first")
    if (active_logger.length) {
        active_logger.attr("class", "active");

        // Setup websocket connection
        ws_init("ws://"+window.location.host+"/ws");
    }
    // call pages setup function
    setupheight();

    $("div[logger="+active_logger.attr("logger")+"]:first").show();

    // Change active logger on click
    $("li[logger]").click(function(evt) {
        var prev = $("li.active[logger]");
        var cur = $(this);
        var loggername = cur.attr("logger");

        prev.attr("class", "");
        cur.attr("class", "active");

        // call this event for handle in single/monitoring modes
        $(this).trigger("call_logger", {prev: prev, loggername: loggername});
    })
})
