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
4. Создайте / Примените миграции:
   python manage.py makemigrations / python manage.py migrate
5. Создайте суперпользователя для доступа к админке:
   python manage.py createsuperuser
6. Создайте таксы по ссылке https://dashboard.stripe.com/test/tax-rates
7. Создайте купоны, для получения скидки https://dashboard.stripe.com/test/coupons
8. Активируйте таксы и купоны в админке в соответсвующих полях http://127.0.0.1:8000/admin/
9. Запустите сервер:
   python manage.py runserver
10. Перейдите по адресу http://127.0.0.1:8000/payments/create-checkout-session/<int:order_id>/ для получения сессии 
11. Перейдите по адресу http://127.0.0.1:8000/payments/create-checkout-session/<int:order_id>/ для получения информации о заказе с последующим перенаправлением в платежную систему
