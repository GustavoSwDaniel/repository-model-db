from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '0.0.2'
DESCRIPTION = 'Models'
LONG_DESCRIPTION = 'Models'
#
# Setting up
setup( 
    name="modelspackage",
    version=VERSION,
    author="Gustavo",
    author_email="<gustavodanieldetoledo@gmail.com.com>",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    install_requires=['SQLAlchemy', 'alembic', 'psycopg2-binary', 'wheel'],
    keywords=['python'],
    packages=["src", "src.repositories"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
