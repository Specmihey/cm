PS C:\cloud_run_elder\cloud-django> cd C:\cloud_run_elder
PS C:\cloud_run_elder> .\Scripts\activate

Для запуска сервера наберите: python manage.py runserver
(cloud_run_elder) PS C:\cloud_run_elder\cloud-django> python manage.py runserver

http://localhost:8000/

{% url 'home' %} где 'home' - это name в urls.py


<!-- How to Highlight Active Links in your Django Website -->
https://valerymelou.com/blog/2020-05-04-how-to-highlight-active-links-in-your-django-website 
{% url 'about' as url %}
<li class="nav-item {% if request.path == url %}active{% endif %}">
  <a class="nav-link" href="{{ url }}">About</a>
</li>

https://github.com/Specmihey/cloud_run_elder.git

https://www.udemy.com/course/intro-to-django-with-python-for-web-development/learn/lecture/10071320#questions/9783308

https://www.youtube.com/watch?v=SEvR78OhGtw

# --- GIT upload
https://www.youtube.com/watch?v=oYVtGWhCZCc
git cd C:\code\djangoproject
https://github.com/Specmihey/cloud-django.git

Найти папку проекта на ПК, правой кл "GIT Bash here"
откроется консоль гита.
Чтобы создать локальный репозиторий пишем в терминале:
git init
"user@DESKTOP-0RUT73E MINGW64 /c/code/djangoproject (master)"

Переносим файлы проекта в репозиторий.
Чтобы добавить все файлы проекта в репозиторий пишем:
git add .

<!-- На этом этапе возможно понадобится добавить файл gitignore
"gitignore file for django project"
https://gist.github.com/santoshpurbey/6f982faf1eacdac153ffd86a3a694239
Создать такой файл в проекте, смотри cloud-django. -->

Все файлы проекта добавляются в отслеживаемые гитом.

Далее делаем коммит.
git commit -a -m "First commit"

Теперь командой git push перенесем все файлы на сервер.
git-remote - Управление набором отслеживаемых репозиториев
https://git-scm.com/docs/git-remote

git remote add origin https://github.com/Specmihey/cloud-django.git

<!-- Посмотреть все серверы, которые зарегистрированы:
user@DESKTOP-0RUT73E MINGW64 /c/code/djangoproject (master)
$ git remote -v
origin  https://github.com/Specmihey/cloud-django.git (fetch) загружаем в него
origin  https://github.com/Specmihey/cloud-django.git (push) выгружаем из него-->

Загружаем:
git push origin master

Все загрузилось в ветвь master https://github.com/Specmihey/cloud-django/tree/master

Для скачивания пишем: git pull origin master

Coding Medved
https://www.youtube.com/channel/UCkBGH1VXCWOrIzPpdV493sQ

Сайт на Django (модели)
https://www.youtube.com/watch?v=-kvoStX713Q&list=PLSWnD6rL-m9adebgpvvOLH5ASGJiznWdg&index=3


