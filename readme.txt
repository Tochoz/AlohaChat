# Тестовое задание Chat
Данное приложение, результат выполнения тестового задания, для отбора на backend интенсив компании SimbirSoft.

**ТЗ лежит в корне репоpитория**

## Запуск
Для запуска веб приложения после клонирования выполнить команды в коренной директории проекта
```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Веб-приложение будет доступно по адресу: 127.0.0.1:8000
Для работы WebSocket необходимо запустить Redis server на порту 6379

## Нереализованные фичи
- Выделение сообщений от вошедшего пользователя
- Присвоение id пользователям с одинаковым именем
- forwarded messages (выделение лс)
- отображение пользователей онлайн
- отображение прочитано ли сообщение
