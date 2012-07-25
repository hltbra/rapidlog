#!

from glob import glob
from distutils.core import setup

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
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
        ]
    )
