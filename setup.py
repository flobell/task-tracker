from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="1.0.0",
    description="A command-line tool for managing your tasks efficiently",
    packages=find_packages(),
    install_requires=None,
    author="Pedro",
    author_email="manuelflores1795@gmail.com",
    url="https://github.com/flobell/task-tracker.git",
    py_modules=["src"],
    entry_points={
        'console_scripts': [
            'task-cli=src.cli.commands:commands',
        ],
    },
    tests_require=[
        "unittest",
    ],
    python_requires=">=3.9",
)
