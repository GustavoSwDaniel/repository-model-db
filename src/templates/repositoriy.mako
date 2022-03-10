## commands auto generated  - please adjust! ###
## This repository is relative the ${name} model
from ${imports} import ${model_name}

from src.repositories.sql_repository import SqlRepository


class ${model_name}Repository(SqlRepository):
    model = ${model_name}
