# python_api_restful
API com django

_______________________________________
#BAIXE AS DEPEDENCIAS:
pip install django 

pip install djangorestframework

pip install django-cors-headers
_______________________________________

#COMANDOS DJANGO#

#Criar Projeto

Para criar um projeto no Django, utilizamos o seguinte comando no terminal:

django-admin startproject nome_do_projeto

#Criar Aplicação

Após criar um projeto, precisamos criar uma (ou mais) aplicações para o projeto. Para isso, utilizamos o seguinte comando:

python manage.py startapp nome_da_app

#Criar Migrações

Após determinar quais serão as entidades que utilizaremos em nosso projeto, precisamos criar as tabelas que representam estas entidades no banco de dados. Para isso, utilizamos o seguinte comando:

python mananage.py makemigrations

#executar Migrações

Após criar os arquivos que definem a estrutura de cada entidade no banco de dados, precisamos executar estas migrações. Para isso, utilizamos o seguinte comando:

python manage.py migrate

#Executar Servidor de Desenvolvimento

Para executar o servidor de desenvolvimento do Django e, assim, testar nosso projeto, utilizamos o seguinte comando:

python manage.py runserver

#Limpar Banco de Dados

Quando estamos desenvolvendo nossa aplicação, é comum que queiramos limpar todos os dados do banco de dados para realizar novos testes. Para realizar este procedimento, utilizamos o seguinte comando:

python manage.py flush

#Abrir Shell do Banco de Dados Configurado

Se quisermos manipular o banco de dados diretamente do shell do SGBD, podemos utilizar o seguinte comando para criar uma conexão com o mesmo:

python manage.py dbshell


#Mapear BD existente para o projeto Django

Caso você possua um banco de dados já existente e queira mapeá-lo para seu projeto Django, o seguinte comando resolve esta necessidade:

python manage.py inspectdb > nome_da_app.models.py

___________________________________________________________________________________________________________________________________________________________________________________________________

##django + postgresql##

#baixe as depedencias:

pip install psycopg2

pip install psycopg2-binary

#edite o database no settings.py


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db name>',
        'USER':'<user>',
        'PASSWORD':'<password>',
        'HOST':'<server>',
        'PORT':'5432'
    }
}
