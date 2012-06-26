#! coding:utf-8
'''

Tests of rapidlog

@author: rmuslimov
@date: 24.06.2012

'''

import os
import sys

# Setup env
project_path = os.path.abspath(__file__).split()[0]
sys.path.insert(0, os.path.abspath(
    os.path.join(project_path, '..', '..', '..')
    ))


cfg = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
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
            'queue': 'logging'
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


# Use dict-like config PEP 381
import dictconfig
dictconfig.dictConfig(cfg)

import logging
logger = logging.getLogger(name='rapid')

logger.info('test rapid tests')
