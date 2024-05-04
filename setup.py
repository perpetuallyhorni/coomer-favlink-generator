# setup.py
from setuptools import setup, find_packages

setup(
    name='coomer_favlink_generator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'coomer_favlink_generator=coomer_favlink_generator.link_generator:main',
        ],
    },
    install_requires=[
    ],
)
