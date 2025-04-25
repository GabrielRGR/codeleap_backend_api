# CodeLeap Django API Test

Este projeto é uma API REST construída com Django e Django REST Framework para o teste técnico da CodeLeap.

## Como rodar localmente 

1. Clone o repositório

   - git clone https://github.com/GabrielRGR/codeleap_backend_api.git

2. Crie um ambiente virtual e ative:

    - python -m venv venv

    - venv\Scripts\activate  # Windows

    - source venv/bin/activate  # Linux/macOS

3. Instale as dependências:

    - pip install -r requirements.txt

4. Rode as migrações:

    - python manage.py makemigrations

    - python manage.py migrate

5. Inicie o servidor:

    - python manage.py runserver

## Endpoint da api: http://127.0.0.1:8000/api/

## Funcionalidades

- CRUD de posts (`/api/careers/`)
- Endpoint para dar like (`/api/careers/{career ID}/like/`)
- Likes com verificação por `username`
- Ordenação por data ou título
