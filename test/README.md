# Pruebas unitarias en ficheros independientes

En este directorio se disponibilizan una serie de métodos de acceso a la base de datos de DynamoDB de manera independiente y unas pruebas unitarias asociadas.
Dichas pruebas unitarias ejecutan contra la librería moto y contra una imagen de docker de DynamoDB levantada en un contexto local.

Para poder llevarlas a cabo se han de cumplir los siguientes requisitos:
 * Librerías
    * Python3.7
    * moto 
    * boto3
 * Imagen de Docker
    * DynamoDB oficial de AWS. 
 



Pasos para ejecutar DynamoDB en local
```
docker run -p 8000:8000 amazon/dynamodb-local
```
Pasos para ejecutar las pruebas
```
test$ coverage run -m TestToDo
.One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
..One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
..One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
One or more parameter values were invalid: An AttributeValue may not contain an empty string
One or more parameter values were invalid: An AttributeValue may not contain an empty string
One or more parameter values were invalid: An AttributeValue may not contain an empty string
....One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
One or more parameter values were invalid: An AttributeValue may not contain an empty string
One or more parameter values were invalid: An AttributeValue may not contain an empty string
.
----------------------------------------------------------------------
Ran 10 tests in 1.010s

OK

test$ coverage report -m
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
TestToDo.py            101      0   100%
ToDoCreateTable.py      11      2    82%   32, 38
ToDoDeleteItem.py       17      1    94%   32
ToDoGetItem.py          17      1    94%   31
ToDoPutItem.py          19      1    95%   38
ToDoUpdateItem.py       19      1    95%   48
--------------------------------------------------
TOTAL                  184      6    97%
```