from setuptools import setup, find_packages

setup(
    name='whut',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'whut = whut.cli:main',
        ],
    },
    install_requires=[
        'requests',
        'google-api-python-client',
    ],
)