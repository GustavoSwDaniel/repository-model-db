import os
from pathlib import Path
from typing import List, Dict

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


def get_file_models_line(path: str):
    files = [x for x in path.iterdir() if x.is_file()]
    file_path = []
    for file in files:
        with file.open() as f:
            for line in f:
                if '__tablename__' in line:
                    file_path.append(str(file))

    return get_class_names(path_models=file_path)

def get_class_names(path_models: List):
    imports_models = {}
    for path_file in path_models:
        with open(path_file, 'r+') as file:
            for line in file:
                if '(Base)' in line or ',Base)' in line or '(Base,' in line:
                    string_import = generate_import(path=path_file.split('site-packages/')[1])
                    imports_models[get_models_name(class_model=line)] = string_import.replace('.py', '')

    return  imports_models

def get_models_name(class_model: str):
    return class_model.split(' ')[1].split('(')[0]


def generate_import(path: str):
    path = path.split('/')
    return '.'.join(path)

def get_file_models():
    if DIR_MODELS:
        path = Path(DIR_MODELS)
        data_models = get_file_models_line(path=path)
        print(data_models)
        create_repository(data_models)

def create_repository(data_models: Dict):
    mytemplate = Template(filename=str(Path(os.path.abspath(__file__)).parents[1]) + '/templates/repositoriy.mako')

    for key, item in data_models.items():
        print(key, '.', item)
        try:
            f = open(dir + f'/repository/repositories/{key}Repository.py', 'x')

            with open(dir + f'/repository/repositories/{key}Repository.py', 'w') as file:
                file.write(mytemplate.render(model_name=key, imports=item))
        except FileExistsError:
            pass
