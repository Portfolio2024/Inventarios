# Inventarios Trujillo - CodeLatin
Bienvenido a nuestra plataforma de gestión de inventario. Aquí podrás realizar un seguimiento de tus productos, actualizar inventarios y gestionar tus existencias de manera eficiente.

# Pasos de instalación

##### 1) Clonar el repositorio del proyecto en un directorio de tu computador o servidor

##### 2) Crear un entorno virtual para la instalación de las librerías del proyecto

Para windows:

```bash
python3 -m venv env 
```

Para linux:

```bash
virtualenv venv -ppython3 
```
##### 3) Activar el entorno virtual de nuestro proyecto

Para windows:

```bash
cd venv\Scripts\activate.bat 
```

Para Linux:

```bash
source venv/bin/active
```

##### 4) Instalar todas las librerias del proyecto que se encuentran en la carpeta principal

```bash
pip install -r requirements.txt
```
##### 5) Crear la tablas de la base de datos a partir de las migraciones de django

```bash
python manage.py makemigrations
python manage.py migrate
```
##### 6) Iniciar el servidor del proyecto

```bash
python manage.py runserver 
```

##### 7) Iniciar sesión en el sistema (Puedes crear la clave y usuario)

------------

🤗💪¡Muchas Gracias!💪🤗

**Puedes apoyarme de la siguiente manera.**

