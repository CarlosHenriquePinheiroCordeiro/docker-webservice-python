# docker-webservice-python
Repositório para trabalho final do componente curricular Sistemas Distribuídos - Construção de WebServices em Python, distribuídos em containers Docker, com persistência de dados em MongoDB também em Docker.

O trabalho consiste na concepção de três WebServices e um Cliente que irá consumir um destes, no contexto de um simples sistema de consulta, inclusão e exclusão de contatos, em Python.

O primeiro WebService - "facade-ws" - se trata de uma "faixada", ou Facade, que o Cliente irá consumir para realizar as ações que desejar dentro do sistema proposto. O segundo, "bo-ws" se trata do serviço de BusinessObject do sistema, e o terceiro "persistencia-ws" caracteriza o serviço de persistência dos dados. Cada um deste containerizado em Docker, que levanta estas aplicações.

Para a concepção do WebService em si, será brevemente utilizado a biblioteca CherryPy.

Referente a persistência, será utilizado o banco de dados não relacional MongoDB, também containerizado.

Conforme o arquivo do docker-compose, devem ser criadas as imagens:
    py-ws-facade            (Dockerfile da pasta "facade-ws")
    py-ws-bo                (Dockerfile da pasta "bo-ws")
    py-ws-persistencia      (Dockerfile da pasta "persistencia-ws")
    mg-i, mg-ii e mg-iii    (Dockerfile da pasta "mongodb")
Para então, serem estruturados um container para cada imagem criada.