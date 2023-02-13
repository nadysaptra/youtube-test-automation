from setuptools import setup

setup(
    name='yt_automation',
    version='0.1',
    description='A test automation for YouTube',
    packages=['tests'],
    install_requires=[
        'selenium',
        'pytest',
    ],
    tests_require=[
        'pytest',
    ],
)
