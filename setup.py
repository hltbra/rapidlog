#!

from setuptools import setup

setup(
    name='rapidlog',
    author='Rustem Muslimov',
    author_email='r.muslimov@gmail.com',
    version='0.1',
    url='https://github.com/rmuslimov/rapidlog',
    py_modules=['handlers.rabbit', 'web.webagent'],
    description='Handler for logging, and simple web client on tornado',
    entry_points={
        'console_scripts': [
            'rapidagent = web.webagent:main'
            ],
        },
    zip_zafe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
        ]
    )
