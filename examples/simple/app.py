#! coding:utf-8
'''

Simple loggers with rapidlog handlers of rapidlog

@author: rmuslimov
@date: 24.06.2012

'''

from logging import config as _config
import logging

cfg = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timed': {
            'format': '[%(asctime)s %(levelname)s] %(message)s',
            'datefmt': '%y %b %d, %H:%M:%S',
            },
    },
    'handlers': {
        'rabbit': {
            'class': 'rapidlog.handlers.RabbitHandler',
            'host': 'localhost',
            'queue': 'logging',
            'formatter': 'timed'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'timed',
        }
    },
    'loggers': {
        'rapid': {
            'handlers': ['rabbit', 'console'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

if __name__ == '__main__':
    # setup logging conf
    _config.dictConfig(cfg)

    logger = logging.getLogger(name='rapid')
    logger.info('hello world')
    logger.warn('hello world')
    logger.error('hello world')
