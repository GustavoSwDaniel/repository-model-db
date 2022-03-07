import os
from pathlib import Path
from typing import List

import click
from mako.template import Template
from src.config import DIR_MODELS

dir = os.getcwd()


@click.command()
def init_repository():
    try:
        Path(dir + '/repository').mkdir(parents=True, exist_ok=True)
        Path(dir + '/repository/repositories').mkdir(parents=True, exist_ok=True)
        create_config_file()
    except FileExistsError:
        pass


def create_config_file():
    Path(dir + '/repository/config.py').touch(exist_ok=True)
    print(dir)
    mytemplate = Template(filename=str(Path(os.path.abspath(__file__)).parents[1]) + '/templates/config.mako')
    with open('repository/config.py', 'w') as out_file:
        out_file.write(mytemplate.render())


@click.command()
def generate_repository():
    get_config_file()
    get_file_models()

def get_config_file():
    with open(str(Path(os.path.abspath(__file__)).parents[1]) + '/config.py', 'r+') as file:
        file.seek(0)
        file.truncate()
        with open(dir + '/repository/config.py', 'r+') as config_file:
            for line in config_file:
                file.write(line)


def get_class_line(path: str):
    files = [x for x in path.iterdir() if x.is_file()]
    class_names = []
    for file in files:
        with file.open() as f:
            for line in f:
                if 'db.Model' in line:
                    class_names.append(line)

    
    return get_models_name(class_names=class_names)


def get_models_name(class_names: List):
    models_name = []
    for model in class_names:
        models_name.append(model.split(' ')[1].split('(')[0])

    return models_name


def get_file_models():
    if DIR_MODELS:
        path = Path(DIR_MODELS)
        models_name = get_class_line(path=path)
        create_repository(models_name=models_name)



def create_repository(models_name : List):
    mytemplate = Template(filename=str(Path(os.path.abspath(__file__)).parents[1]) + '/templates/repositoriy.mako')

    for name in models_name:
        try:
            f = open(dir + f'/repository/repositories/{name}Repository.py', 'x')

            with open(dir + f'/repository/repositories/{name}Repository.py', 'w') as file:
                file.write(mytemplate.render(model_name=name))
        except FileExistsError:
            pass
