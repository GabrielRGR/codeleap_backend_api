# CodeLeap Django API Test

Este projeto é uma API REST construída com Django e Django REST Framework para o teste técnico da CodeLeap.

## Como rodar localmente

1. Clone o repositório
2. Crie um ambiente virtual e ative
3. Instale as dependências:
pip install -r requirements.txt

4. Rode as migrações:
python manage.py makemigrations
python manage.py migrate

5. Inicie o servidor:
python manage.py runserver

## Funcionalidades

- CRUD de posts (`/api/careers/`)
- Likes com verificação por `username`
- Ordenação por data ou título