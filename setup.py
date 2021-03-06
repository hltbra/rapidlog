#!

from glob import glob
from setuptools import setup

setup(
    name='rapidlog',
    author='Rustem Muslimov',
    author_email='r.muslimov@gmail.com',
    version='0.1',
    url='https://github.com/rmuslimov/rapidlog',
    packages=['rapidlog', 'rapidlog.handlers', 'rapidlog.web'],
    description='Handler for logging, and simple web client on tornado',
    entry_points={
        'console_scripts': [
            'rapidagent = rapidlog.web.webagent:main'
            ],
        },
    include_package_data=True,
    data_files=[('rapidlog/web/templates', ['rapidlog/web/templates/index.html']),
                ('rapidlog/web/static/css', glob('rapidlog/web/static/css/*')),
                ('rapidlog/web/static/images', glob('rapidlog/web/static/images/*')),
                ('rapidlog/web/static/js', glob('rapidlog/web/static/js/*')),
                ],
    install_requires=[
        'pika>=0.9.5',
        'tornado>=2.3',
        'wsgiref>=0.1.2',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
        ]
    )
