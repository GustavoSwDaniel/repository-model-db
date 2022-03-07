from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '0.1.11'
DESCRIPTION = 'repository-model-db'
LONG_DESCRIPTION = 'Models'
#
# Setting up
setup( 
    name="repository-model-db",
    version=VERSION,
    author="GustavoSwDaniel",
    author_email="<gustavodanieldetoledo@gmail.com.com>",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    url='https://github.com/GustavoSwDaniel/repository-model-db',
    install_requires=['SQLAlchemy', 'alembic', 'psycopg2-binary', 'wheel', 'Mako', 'click'],
    entry_points= {
    'console_scripts': [
        'init-repo = src.cli.commands:init_repository',
        'generate-repo = src.cli.commands:generate_repository'
        ],
    },
    keywords=['python'],
    packages=["src", "src.repositories", "src.cli", "src.templates"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
