# Harry, para mejorar tu salud mental.

Buscamos crear un asistente móvil para mejorar el bienestar mental de los usuarios.

## How to run

```bash
$ # Descargar el código
$
$
$ #Activar virtualenv en Windows
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Activar virtualenv en sistemas basados en Unix (como MacOS)
$ #virtualenv env
$ #source env/bin/activate
$
$ # Instalar modulos de python.
$ pip3 install -r requirements.txt
$
$ # Migrar
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Iniciar la aplicación
$ python manage.py runserver # Dirección default: http://localhost:8000/
```