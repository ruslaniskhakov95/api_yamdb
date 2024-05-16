# Проект YaMDb
Проект YaMDb собирает отзывы пользователей на произведения, но сами произведения в YaMDb не хранятся. Произведения делятся на категории: «Книги», «Фильмы», «Музыка», список категорий может быть расширен. Произведению может быть присвоен жанр из списка предустановленных. Добавлять произведения, категории и жанры может только администратор. Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти, из пользовательских усредненных оценок формируется рейтинг. Пользователи могут оставлять на одно произведение только один отзыв, а так же могут оставлять комментарии к отзывам. Безопасность данных обеспечивается при помощи проверки подлинности и авторизации. Для аутентификации используются JWT-токены. Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи. У неаутентифицированных пользователей доступ к API только на чтение.

## Использованные технологии:
```
requests==2.26.0
Django==3.2
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
django-filter==23.1
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
```

## Клонируем проект:
git clone  ....

## Переходим в папку с проектом:
api_yamdb

## Устанавливаем виртуальное окружение:
python -m venv venv

## Активируем виртуальное окружение:
source venv/Scripts/activate

## Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Применяем миграции в папке api_yamdb:
```
python manage.py makemigrations
python manage.py migrate
```

## Устанавливаем Postman-коллекцию для проверки API согласно файлу postman_collection/READ.md :
`Ymdb-collection.postman_collection.json`

## Реализуем импорт данных из csv файлов в папке api_yamdb:
python manage.py importcsv

## Запускаем проект в папке api_yamdb:
python manage.py runserver

## Тестируем и добавляем данные через Postman.

#### Примеры запросов:

1) Получение списка всех произведений: GET http://127.0.0.1:8000/api/v1/titles/

2) Создание произведения: POST http://127.0.0.1:8000/api/v1/titles/
```
{
"name": "string",
"year": 0,
"description": "string",
"genre": [
"string"
],
"category": "string"
}
```
Подтверждение создания записи:
```
{
"id": 0,
"name": "string",
"year": 0,
"rating": 0,
"description": "string",
"genre": [
{}
],
"category": {
"name": "string",
"slug": "^-$"
}
}
```
3) Удаление категории: DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/


## Запуск тестов:
pytest


#### Команда № 3:
```
Руслан Исхаков - team lead
Виктория Финкель
Татьяна Романенко
```
