# Página Web

Repositorio para el EJ2 de IDS [TP: página web](https://github.com/francisreyy/EjercicioPractico2-PaginaWeb) de la materia: **Introducción al Desarrollo de Software - FIUBA**

## Integrantes
- Francis Rey 102785
- José Adrián 104675

## Dependencias para ejecutar la página web
- blinker==1.8.2
- click==8.1.8
- flask==3.0.3
- importlib-metadata==8.5.0
- itsdangerous==2.2.0
- jinja2==3.1.6
- MarkupSafe==2.1.5
- werkzeug==3.0.6
- zipp==3.20.2
- flask-mail==0.10.0 **(luego del script por el enunciado del trabajo)**

## Dependencias para editar la página web
- completar 

___


## ① Crear entorno 
- Ejecutar el siguiente script en la terminal **(sólo la primera vez)**

Ubuntu
```bash
bash ./EjPractico2.sh
```

## ② Preparación de archivos **(sólo la primera vez)**
- Descargar el repo de github de la rama deploy y pegar el contenido de la carpeta TP2-IDS en la misma carpeta TP2-IDS creada por el script.

___


## ③ Ejecutar la página

- Activa el entorno virtual

```shell
source .venv/bin/activate
```

- Instalar Flask-Mail en el entorno **(sólo la primera vez)**

```shell
pip install Flask Flask-Mail
```

- Crear carpeta .env con un archivo llamado mailpassword **(sólo la primera vez)**
```shell
mkdir .env
cd .env
touch mailpassword
```
- E introducir en `mailpassword` `MAIL_PASSWORD=<contraseña de aplicación>` **(sólo la primera vez)**

- Cargar la contraseña como variable de entorno
```shell
export MAIL_PASSWORD=$(cat .env/mailpassword | grep MAIL_PASSWORD | cut -d '=' -f2)
```

- Activa el servidor de flask, con el puerto especificado y en el modo debug

```shell
flask run --port=5050 --debug
```

Entrar a la página en el navegador con la dirección: `localhost:5050`

___


## Template
- [Template: Soccer – Free Bootstrap HTML5 Sports Website Template](https://themewagon.com/themes/free-bootstrap-html5-sports-website-template-soccer/) de colorlib

Rey, Adrián 2025