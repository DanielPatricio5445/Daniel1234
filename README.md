## Passo a passo para abrir o Projeto 

Abra o repositório, na seção "CODE", e copiar o link


No seu VS Code, abra o terminal de comando e dê um git clone link

Ai você dá esses comandos nessa ordem, dentro do terminal:

py -m venv ambienteVirutal - instala o ambienteVirtual

ambienteVirutal\Scripts\activate - ativa o ambiente virtual

py -m pip install Django - instala o Django
py -m pip install matplotlib Pillow - instala o Pillow
py -m pip install requests - instala os requests
py -m pip install djangorestframework django-cors-headers - instala o djangoframework 


py -m manage runserver - roda o server



## Outros comandos 
---
> py manage.py makemigrations

> py manage.py migrate

> py manage.py sqlmigrate appHome 0001

> py manage.py shell

> from appHome.models import sua model

> Usuario.objects.all()

> py manage.py createsuperuser
