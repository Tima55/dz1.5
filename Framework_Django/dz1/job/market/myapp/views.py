# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


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
