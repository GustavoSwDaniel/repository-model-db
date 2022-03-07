from pathlib import Path

import os

class Repositore(object):
    def __init__(self, base) -> None:
        self.__base = base
        self.__dir = os.getcwd()

    def create_repositories_folder(self):
        try:
            Path(self.__dir + '/repositories').mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass
    