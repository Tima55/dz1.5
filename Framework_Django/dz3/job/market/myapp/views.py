from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from myapp.models import Order, Client
from django.utils import timezone
from datetime import datetime, date, time, timedelta

logger = logging.getLogger(__name__)


# Home work 1
def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main = '''
1.  необходимо создать и активировать виртуальное окружение<br>
<br>
- <i>python -m venv .venv</i>
- /.venv/Scrypts/activae.ps1
<br>
2. установка Django
- pip install django<br>
- django-admin startproject market<br>
- cd market<br>
- python3 manage.py startapp myapp</i><br>
<br>
3. Откройте файл settings.py и добавьте 'myapp' в список установленных приложений:<br>
<br>
INSTALLED_APPS = [ <br>
  ... <br>
  'myapp', <br>
  ... <br>
]<br>

4. Далее прописываем маршруты<br>
<br>
5. Теперь вы можете запустить свой сайт с помощью команды в терминале:<br>
<br>
- <i>python manage.py runserver</i><br>
<br>
Вы должны увидеть сообщение о том, что сервер работает. <br>Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000/ , чтобы увидеть главную страницу вашего интернет-магазина.<br>
    '''
    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Я студент в сфере IT,<br>
    и мне ни за что, с пути не сойти..<br>
    буду я профи, в backend разработке,<br>
    и будет доход минимальный 3 стоки!!!</h2><br>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)


## Home work 2
def all_orders(request):
    order = Order.objects.all()
    return HttpResponse(order)


## Home work 3

# - Доработаем задание про клиентов,
# товары и заказы.
# - Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# -Подготовьте необходимый маршрут и представление.


def index_extend_base(request):
    return render(request, 'myapp/index.html')


# вывод заказа по ID
def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_id = Order.objects.get(pk=order_id).pk
    order_date = Order.objects.get(pk=order_id).date_order
    client = Order.objects.get(pk=order_id).customer.name
    summ_price_order = Order.objects.get(pk=order_id).summ_price_order
    order_products = Order.objects.get(pk=order_id).products.all()

    return render(
        request, 'myapp/order.html', {
            'order': order,
            'order_id': order_id,
            'order_date': order_date,
            'order_products': order_products,
            'client': client,
            'summ_price_order': summ_price_order,
        })


# Вывод списка заказов по ID-client, с переходом на содержимое заказа
def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    return render(request, 'myapp/client_orders.html', {
        'client': client,
        'orders': orders
    })


# Вывод списка всех продуктов по ID-client
def client_all_products(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    all_orders = Order.objects.filter(customer=client)

    return render(request, 'myapp/client_all_products.html', {
        'client': client,
        'all_orders': all_orders,
    })


# сортировка заказов клиента за последние "count_day" дней
def orders_order_by(request, client_id, count_day):
    client = get_object_or_404(Client, pk=client_id)
    all_orders = Order.objects.filter(customer=client)
    date_now = timezone.now()
    # print(f'текущая дата - {date_now}')
    start_date = date_now - timedelta(days=count_day)
    # print(f'дата {count_day} назад - {start_date}')
    list_filter_orders = []
    for order in all_orders:
        if start_date <= order.date_order:
            list_filter_orders.append(order)
    return render(
        request, 'myapp/orders_order_by.html', {
            'count_day': count_day,
            'client': client,
            'list_filter_orders': list_filter_orders,
        })
