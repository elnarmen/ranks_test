## Как запустить
Склонируйте репозиторий:
```
git clone https://github.com/elnarmen/ranks_test.git
```

Перед запуском Docker Compose в корне репозитория создайте файл `.env` со следующими переменными:

``` bash
SECRET_KEY='some_secret_key'
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
DATABASE_URL=postgresql://db_user:db_password@postgres:5432/db_name
STRIPE_PUBLISHABLE_KEY=<Publishable key для API Stripe>
STRIPE_SECRET_KEY=<Secret key для API Stripe>
```
`STRIPE_PUBLISHABLE_KEY` и `STRIPE_SECRET_KEY` можно получить после регистрации аккаунта на сайте платежной 
системы [Strip](http://stripe.com) в разделе `Developers`.

Скачайте и соберите докер-образы с помощью Docker Сompose:

```shell
$ make build
```

Примените миграции и создайте суперюзера:
```shell
$ make first_start
```

Запустите приложение командой:

```shell
$ make run
```

## Доступны следующие ссылки:

http://127.0.0.1:8000/admin/ - администраторский Web UI

http://127.0.0.1:8000/payment/item/{item_id}/ - Страница оплаты продукта

http://127.0.0.1:8000/payment/api/buy/{item_id}/ - API-эндпоинт для получения Stripe Session Id

Техзадание: https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

## Дополнительно выполненные задания
1. Запуск используя Docker
2. Использование environment variables
3. Просмотр Django Моделей в Django Admin панели
4. реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям
5. удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.
