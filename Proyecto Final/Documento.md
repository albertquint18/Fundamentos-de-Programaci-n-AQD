## Proyecto Final: Balones Tecmilenio
**Nombre:** Alberto Quintanar Domínguez
**Matricula:** 03087401
**Curso:** Fundamentos de programación
**Proyecto:** Final, uso de balones en la universidad Tecmilenio
**Fecha de entrega:** 25 de septiembre del 2025
#### Introducción:
En la universidad Tecmilenio los ulumnos pueden pedir prestados balones para poder realizar deporte, tales como fútbol, básquetbol y vóleibol, la situación aquí es que muchas veces no se sabe si el balon esta ocupado o no, haciendo que el alumno pierda tiempo llendo a preguntar si se tiene balon o si ya lo prestaron, por esto el proyecto consiste en el desarrollo de un sistema de administración y uso de balones de la universidad. El programa tiene como objetivo facilitar el control de los balones de fútbol, básquetbol y vóleibol, permitiendo consultar su disponibilidad, registrar préstamos y devoluciones, así como consultar la información almacenada en archivos de texto.
El sistema fue hecho en Python con diferentes recursos como listas, diccionarios, ciclos, estructuras condicionales, manejo de excepciones, archivos de texto y programación con hilos, logrando realizar diferentes operaciones que el usuario requiera.
#### Objetivos:
**Objetivo general:** Desarrollar un sistema en Python que permita administrar el préstamo, devolución y consulta de balones deportivos mediante un menú interactivo y el almacenamiento de información en archivos de texto.
**Objetivos especificos:** Registrar los datos necesarios para que se pueda realizar un préstamo de un balon, mostrar la disponibilidad de los balones, registrar cuando se devuleven los balones, Consultar la información que esta almacenada en los archivos, validar los datos introducidos por el usuario, manejar los posibles errores con excepciones, usar funciones definidas para organizar el código, contar con un control de inactividad en el menú principal.
#### Descripción general de como funciona:
Al iniciar, el programa te solicita un nombre de usuario y posteriormente se muestra una pantalla de carga, después se crean los archivos necesarios para almacenar la información de los balones, siempre checando previamente si estos archivos ya existen.
Cuando ya se inicia el sistema, se muestra un menú principal con cinco opciones:

-Mostrar balones
-Prestar balón
-Devolver balón
-Consultar archivos
-Salir

El usuario elige una opción mediante una función que valida que la entrada corresponda con una opción disponible. Después de ejecutar la operación seleccionada, el programa regresa al menú principal.
#### Criterios de diseño lógico:
El programa cuenta con varias funciones definidas para asi poder separar varias acciones en el sistema, esto para evitar que el codigo sea mas facil de modificar.
Algunas de las funciones son las siguientes:
| Función | Uso dentro del programa |
|---|---|
| **nom_usuario()** | Solicita el nombre del usuario y valida que no esté vacío. |
| **pedir_semestre()** | Solicita el semestre y valida que sea un número entero entre 1 y 8. |
| **fecha()** | Solicita y valida una fecha en formato día/mes/año. |
| **pedir_opcion()** | Valida que la opción ingresada se encuentre dentro del rango permitido. |
| **pantalla_carga()** | Muestra una pantalla de carga antes de iniciar el sistema. |
| **crear_archivos()** | Crea los archivos de texto necesarios para almacenar la información de los balones. |
| **mostrar_balones()** | Muestra el estado actual de los balones de fútbol, básquetbol y vóleibol. |
| **prestar_balon()** | Permite seleccionar un balón, registrar los datos del alumno y guardar la información del préstamo. |
| **devolver_balon()** | Registra la devolución de un balón y actualiza su estado a disponible. |
| **consultar_archivo()** | Permite seleccionar y consultar el contenido de los archivos de texto. |
| **cont_temp()** | Controla el tiempo de inactividad del usuario mediante un ciclo `for` y un temporizador. |
| **mostrar_menu()** | Muestra las opciones disponibles en el menú principal. | 
#### Estructura de datos utilizadas:
**Listas:** se hicieron listas para almacenar información que puede recorrerse mediante ciclos, como por ejemplo la lista que era para representar los 3 tipos de balones:
balones = [
    ["1", "Fútbol", "balones_futbol.txt"],
    ["2", "Básquetbol", "balones_basquetbol.txt"],
    ["3", "Vóleibol", "balones_voleibol.txt"]
]
**Diccionario:** se usaron diccionarios para relacionar el nombre de cada archivo con el contenido que se debe almacenar, como por ejemplo:
archivos = {
    "balones_futbol.txt":
        "BALONES DE FÚTBOL\n\nEstado: Disponible\n",
    ...
}
#### Manejo de los erores:
Para poder evitar que el codigo se rompiera inesperadamente por datos erroneos se metieron los try-except, donde por ejemplo cuando se pide el semestre con int(), al estar dentro de un try, identifica si el dato que se introduce es erroneo, como un número flotante. Por ejemplo: 
try:
    semestre = int(input("Ingresa tu semestre: "))
except ValueError:
    print("Error: debes ingresar un número entero")
Algunos de los except que se usaron fueron ValueError, que significa que la entrada no puede convertirse en lo que piden. Otro fue FileNotFoundError que es cuando un archivo es inexistente.
#### Manejo de archivos:
El codigo necesita usar archivos de texto (.txt) para asi poder almacenar la información de los balones, se utiliza el modo r para leer el archivo y w para escribir o actualizar la información de los balones. Antes de crear archivos se utiliza os.path.exist() para revisar si el archivo ya existe o no.
#### Control de inactividad:
Esta función esta hecha para que el tiempo solo corra mientras se encuntra en el menú, para que el codigo pueda realizar dos acciones al mismo tiempo que son mostrar el menu, preguntar que se desea realizar y que el temporizador este activo, se uso un threading, el ciclo for realiza 600 iteraciones, con una pausa de un segundo en cada una, equivalente a diez minutos.
#### Funcionamiento con pruebas:
En el codigo, se busco cubirir los problemas que pudieran llegar a ser más comunes, en la siguiente lista se pueden ver algunos ejemplos:
| Prueba | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Nombre vacío | `""` | Mostrar un mensaje de error y solicitar nuevamente el nombre. | Correcto |
| Semestre fuera de rango | `10` | Mostrar un mensaje de error porque el semestre debe estar entre 1 y 8. | Correcto |
| Semestre no numérico | `"abc"` | Mostrar un mensaje de error y solicitar nuevamente el semestre. | Correcto |
| Fecha inválida | `30/02/2026` | Mostrar un mensaje de error porque el día no es válido para febrero. | Correcto |
| Fecha con formato incorrecto | `30-02-2026` | Mostrar un mensaje indicando que se utilice el formato día/mes/año. | Correcto |
| Opción fuera de rango | `8` | Mostrar un mensaje de error y solicitar nuevamente una opción. | Correcto |
| Mostrar balones | Opción `1` | Mostrar el estado de los balones de fútbol, básquetbol y vóleibol. | Correcto |
| Prestar balón | Opción `2` | Solicitar los datos del alumno y registrar el préstamo en el archivo correspondiente. | Correcto |
| Prestar balón ya prestado | Seleccionar un balón prestado | Mostrar un mensaje indicando que el balón ya está prestado. | Correcto |
| Devolver balón | Opción `3` | Solicitar la fecha y registrar la devolución del balón. | Correcto |
| Devolver balón disponible | Seleccionar un balón disponible | Mostrar un mensaje indicando que el balón ya está disponible. | Correcto |
| Consultar archivo | Opción `4` | Mostrar el contenido del archivo seleccionado. | Correcto |
| Archivo inexistente | Archivo no encontrado | Mostrar un mensaje indicando que el archivo no existe. | Correcto |
| Control de inactividad | Sin actividad durante 10 minutos | Mostrar el mensaje de inactividad después de 600 segundos. | Correcto |
| Salir del sistema | Opción `5` | Mostrar un mensaje de despedida y finalizar el programa. | Correcto |
#### Conclusiones:
El desarrollo de este código impulso el uso de las herramientas vistas a lo latgo del curso `Fundamentos de programación`, principalmente el uso de funciones, estructuras de datos, ciclos, condicionales, manejo de excepciones y archivos.
La división del programa en funciones permitió organizar las diferentes operaciones del sistema y facilitar sus modificaciones. Además, la implementación de archivos de texto permitió conservar la información relacionada con los balones.
