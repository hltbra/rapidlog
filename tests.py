#! coding:utf-8
'''

@author: rmuslimov
@date: 26.06.2012

'''

import logging
import unittest

class TestRabbitService(unittest.TestCase):

    def setUp(self):
        # load demo project
        import demo

    def testRabbitConnection(self):
        # make sure that saving to rabbit works properly
        logger = logging.getLogger(name='rapid')
        logger.info('info')
        logger.debug('debug')
        logger.error('error')
        logger.warn('warn')

if __name__ == '__main__':
    unittest.main()
