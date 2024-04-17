# materiales-TAN
Repositorio asociado a los materiales docentes sobre Traducción Automática Neuronal

Para ejecutar los programas de este repositorio necesitas tener Python version 3 instalado en tu sistema. Si tienes dudas sobre la instalación de Python puedes consultar este enlace: [https://xwiki.recursos.uoc.edu/wiki/matm21564es/view/1.%20Introducci%C3%B3n%20/](https://xwiki.recursos.uoc.edu/wiki/matm21564es/view/1.%20Introducci%C3%B3n%20/)

En cada uno de los directorios tendrás el archivo requirements.txt que indica qué requisitos se tienen que instalar para ejecutar los programas. En este punto cabe recordar que puede ser recomendable crear [entornos virtuales](https://docs.python.org/es/3/tutorial/venv.html) de Python para evitar incompatibilidades entre las diferentes librerías y módulos que vayas instalando, aunque esto no es estrictamente necesario.

Si decides no utilizar entornos virtuales de Python, para instalar los requisitos de cada uno de los programas escribe

`pip install -r requirements.txt`

o

`pip3 install -r requirements.txt`

En Linux es posible que tengas que utilizar sudo antes de la instrucción.

Si en cambio decides crear entornos virtuales haz:

Para crear el entorno virtual:

`python -m venv env`

o

`python3 -m venv env`

(puedes cambiar env por cualquier nombre que quieras utilizar para el entorno virtual y también indicar una ruta concreta para el entorni virtual)

Para activar el entorno virtual:

En Windows, ejecuta:

`env\Scripts\activate`

En Unix o MacOS, ejecuta:

`source env/bin/activate`

Ahora, si te fijas, en el Terminal aparece (env), indicando que estás utilizando este entorno.

Ahora estarás utilizando una copia de Python que se guarda en el directorio env (o como lo hayas llamado). Puedes instalar cosas sin afectar al Python general instalado en el sistema. Este entorno lo puedes utilizar en cualquier momento, o si no lo necesitas más, borrarlo eliminando el directorio.

Para instalar los prerequisitos en el entorno virtual puedes hacer:

`python -m pip install -r requirements.txt`


