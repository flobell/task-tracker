from setuptools import setup, find_packages

setup(
    version='1.0',
    packages=find_packages(),
    install_requires=None,
    entry_points={
        'console_scripts': [
            'task-cli = src.cli.commands:commands',
        ],
    },
)
