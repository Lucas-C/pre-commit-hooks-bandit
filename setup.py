from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks-bandit',
    description='A pre-commit hook to find common security issues in your Python code',
    url='https://github.com/Lucas-C/pre-commit-hooks-bandit',
    version='1.0.5',

    author='Lucas Cimon',
    author_email='lucas.cimon@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
        'bandit',
    ],
    entry_points={
        'console_scripts': [
            'bandit_analyzer = pre_commit_hooks.bandit_analyzer:main',
        ],
    },
)
