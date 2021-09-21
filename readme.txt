Для запуска веб приложения после клонирования выполнить команды в коренной директории проекта
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver

Веб-приложение будет доступно по адресу: 127.0.0.1:8000
Для работы WebSocket необходимо запустить Redis server на порту 6379
