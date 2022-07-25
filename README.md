# Repository-model-db


This project aims to assist in the use of the repository pattern. Repository generation of models created by sqlalchemy and provides basic methods for database access, isolating database accesses from the application


## Configurations
In config.py file created by **repo-init** must add the model files directory

### Exemple
DIR_MODELS=src/models

## Commands
```shell
$ repo-init
```

**repo-init**

This command create a folder of root directory of your project with a file to configurations directory os models of your database and create a folder where the repository files will be create

```shell
$ generate-repo
```
This command will create all repository files based on your model files
