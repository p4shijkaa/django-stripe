# Django Stripe Payments

### **Этот проект реализует интеграцию Stripe Checkout в Django для оплаты товаров.**

Требования :

Python 3.9+

Django 4.0+

Stripe аккаунт (тестовый или реальный)

Docker (опционально, для запуска через контейнеры)



## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/p4shijkaa/django-stripe-payments.git
   cd django-stripe-payments
2. Установите зависимости:
   pip install -r requirements.txt
3. Создайте файл .env в корне проекта и добавьте Stripe ключи:
   STRIPE_SECRET_KEY=sk_test_ваш_секретный_ключ
STRIPE_PUBLIC_KEY=pk_test_ваш_публичный_ключ
4. Примените миграции:
   python manage.py migrate
5. Создайте суперпользователя для доступа к админке:
   python manage.py createsuperuser
6. Запустите сервер:
   python manage.py runserver
7. Перейдите по адресу http://127.0.0.1:8000/buy/<item_id>/
   http://127.0.0.1:8000/item/<item_id>/