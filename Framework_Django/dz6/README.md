# <b>Фреймворк Django
# <i>Home work 6</b> (Развёртывание проекта)</i>



# <b><i>Задание:</i></b>
## <b>Разместить проект в интернете:</b>

## <b>Deploy project Django in www.pythonanywhere.com</b>
********************
*******************
********************
## <b> 1. Создание проекта! </b>
- <b>Инструкция первого запуска:</b>
- - mkdir name_directory
- - cd name_directory 
- - python -m venv .venv
- - .venv/Scripts/activate.ps1
- - pip install django
- - django-admin startproject name_project
- - cd name_project
- - python manage.py runserver
- <b>Создание файла с зависимостями:</b>
- - pip freeze > requirements.txt
*******************
*******************
## <b> 2. Регистрация на сервере! </b>
- - <b>Регистрируемся согласно инструкции: </b>
- Примечание: Username будет чатью доменного имени
*******************
*******************
## <b> 3. Подготовка и настройка проекта к deploy </b>
settings.py<br>
----------&#5125;
-  <b> Для работы с переменными окружения: </b>
- - import os
- <b> Режим отладки отключаем:</b>
- - DEBUG = False
- <b> Вынос пароля в переменную окружения: </b>
- - SECRET_KEY = os.getenv('SECRET_KEY')</br>
   ####SECRET_KEY = 'Какойто ключ'
- <b> Прописываем имя хоста или ip для того что бы нас видели в интернете: </b>
- - ALLOWED_HOSTS = ['127.0.0.1', 'username.pythonanywhere.com']
- <b>Доп настройки безопасности:</b>
- - SESSION_COOKIE_SECURE = True
- - CSRF_COOKIE_SECURE = True
- <b>Устанавливае корневую папку со статическими файлами:</b>
- - STATIC_ROOT = BASE_DIR / 'static/'
- <b>Настройка СУБД если это требуется:</b><br>
---DATABASES = {<br>
------'default': {<br>
---------'ENGINE': 'django.db.backends.mysql',<br>
---------'NAME': 'username$default',<br>
---------'USER': 'user_name',<br>
- <b>Вынос пароля в переменную окружения</b><br>
---------'PASSWORD': os.getenv('MYSQL_PASSWORD'),<br>
---------###'PASSWORD': 'какойто пароль',<br>
---------'HOST': 'sevenkapsul.mysql.pythonanywhere-services.com',<br>
---------'OPTIONS': {<br>
------------'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8mb4',
---------},<br>
------}<br>
---}
*******************
*******************
## <b>4. Перенос чистого проекта на сервер</b> 
- <b>средствами git считается более предпочтительным</b>
- - git init
- - gitignore
- - - /media/
- - - /static/
- - - *.sqlite3
- - - *.log
- - - *.pyc
- - git add .
- - git commit -m "Initial commit"
- <b>Создаём пустой репозиторий на сайте https://github.com/</b>
- - git remote add origin https://github.com/username/myproject.git
- - git push -u origin master
- - git clone https://github.com/myusername/myproject.git
*******************
*******************
## <b>5. Создание витруального окружения для проекта</b>
- - mkvirtualenv --python=/usr/bin/python3.10 virtualenv
*******************
*******************
## <b>6. Установка зависимостей проекта</b>
- - cd myproject
- - pip install -r requirements.txt
*******************
*******************
## <b>7. Установка СУБД (если встроеного SQLite недостаточно)</b>
- <b>в рамках данного сервера она подгружается через интерфейс:
- достаточно установить модуль для работы с СУБД</b>
- - pip install mysqlclient
*******************
*******************
## <b>8. Настройка и подготовка СУБД</b>
- <b>Команда установки кодировки:</b>
- - ALTER DATABASE username$default CHARACTER SET utf8 COLLATE utf8_general_ci;
*******************
*******************
## <b>10. Создание и настройка WEB-приложения</b>
- <b>указание нужных путей к проекту, виртуальному окружению, к статическим файлам</b>
*******************
*******************
## <b>11. настройка wsgi.py</b>
- <b>можно оставить для ткстового запуска базовые настройки..
- для работы с переменными окружения код будет таким:</b>

> - import os
> - import sys
> - from dotenv import load_dotenv
> - project_folder = os.path.expanduser('~/name_project')
> - load_dotenv(os.path.join(project_folder, '.env'))
> - path = '/home/user_name/name_project'
> - if path not in sys.path:
> - - sys.path.append(path)
> - os.environ['DJANGO_SETTINGS_MODULE'] = 'name_main_app.settings'
> - from django.core.wsgi import get_wsgi_application
> - application = get_wsgi_application()
*******************
*******************
## <b>12. Применение миграций для создания таблиц в БД</b>
- python manage.py migrate
*******************
*******************
## <b>13. Сбор статических файлов</b>
- python manage.py collectstatic
*******************
*******************
## <b>14. Создание суперпользователя</b>
- python manage.py createsuperuser
*******************
*******************
## <b>15. Создание переменных окружения для безопасного хранения паролей</b>
- - python
- - import secrets
- <b>генерация секретного токена</b>
- - secrets.token_hex()
- - '1f324bd65cb75fc925f852d8e66f058833cc'
- -  exit()
- <b>Создание переменных окружения</b>
- - echo "export SECRET_KEY=1f324bd65cb75fc925f852d8e66f058833cc" >> .env
- - echo "export MYSQL_PASSWORD=пароль" >> .env
- <b>активайия переменных окружения</b>
- - echo 'set -a; source ~/name_project/.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate
## <b>16. Долгожданный финиш, если всё заработало, ты красавчик!!!</b>
*******************
*******************
*******************
*******************
*******************
*******************
*******************
*******************
