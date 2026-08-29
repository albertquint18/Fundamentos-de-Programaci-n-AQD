## Universidad Tecmilenio Querétaro
**Nombre:** Alberto Quintanar Domínguez
**Matricula:** 03087401
#### Avance de proyecto: Administración y uso de balones deportivos
**Introducción:**
Como proyecto final de la asignatura “fundamentos de programación”, se realizará un programa que dé solución a un problema de alguna empresa o institución, usando los conocimientos adquiridos durante el curso. En este avance se usarán las bases vistas de los temas 1 al 8, tales como los ciclos (for, while), entradas y salidas simples, estructuras de decisión, diagramas de PSeInt y depuradores.
**Requerimiento 1: Análisis organizacional:**
La institución escogida es la misma Universidad Tecmilenio, y el área que se busca mejorar es la deportiva, pues suele haber mucho problema y deficiencia a la hora de administrar los balones de cualquier deporte.
**Requerimiento 2: Definición de problema:**
En la universidad de Tecmilenio los alumnos pueden pedir balones de fútbol, basquetbol, y vóleibol, en caso de que estos no tengan uno y quieran hacer uso de las instalaciones deportivas. La cuestión es que el lugar donde tienen los balones suele variar cada cierto tiempo, a veces están en las oficinas del coordinador vive, otras veces en las oficinas de preparatoria y en ocasiones en el gimnasio, esto ya causa un problema, en el que el alumno no sabe a donde ir para pedir el balón y termina yendo a los 3 lugares, aparte de eso hay ocasiones en las que se pide el balón y resulta que ya lo habían prestado, haciendo que toda esa travesía de buscar donde dan el balón haya sido una pérdida de tiempo.
**Requerimiento 3: Listado de requerimientos:**
Lo principal que deberá de tener el programa es esto:
1.	Mostrar los tipos de balones disponibles, como fútbol, basquetbol y vóleibol.
2.	Mostrar el estado de cada balón, indicando si está disponible o si ya fue prestado.
3.	Cuando un balón esté ocupado, mostrar quién lo tiene, poniendo el nombre del alumno.
4.	Mostrar el semestre de la persona que tiene el balón.
5.	Indicar dónde están entregando los balones para que uno sepa a qué lugar debe ir.
6.	Permitir registrar los datos de la persona que solicita el balón
7.	Permitir registrar la devolución de un balón, poniendo que está disponible otra vez.
8.	Evitar que se pueda prestar un balón que ya se encuentre ocupado.
9.	Mantener el programa funcionando mediante un menú de opciones, hasta que la persona quiera salir.
**Requerimiento 4: Clasificación de datos:**
| Dato | Tipo de dato | Función |
| :--- | :--- | :--- |
| Nombre de la persona | input | Registrar el nombre de la persona que pide el balón |
| Semestre | int | Tener el registro de su semestre |
| Tipo de balón (fut, vóley, basket) | input | Elegir el balón que quieres usar |
| Estado del balón | int | Poner si el balón está disponible o no |
| Donde se entregan | input | Ver en qué zona del plantel están prestando los balones |
| Opción del menú | int | Poner las opciones del programa |
**Requerimiento 5: Operadores de lenguaje:**
Los matemáticos:
+: En caso de requerir una suma de datos como cuando regresen un balón
- : Cuando se realicen registros de que prestaron un balón
Los relacionales:
¡= : Para cuando haya algún dato diferente a otro
== : Cuando un dato sea igual a otro, como un balón seleccionado
> < :Para hacer comparaciones o validaciones como la del semestre
Los lógicos:
Or: para poner diferentes condiciones
And: para hacer que dos condiciones se cumplan
Not: para hacer que una condición no se cumple
**Requerimiento 6: Estructuras de control:**
Para que el programa funcione tiene que tener estructuras de decisión y de repetición
Condicionales:
If: para ver si un balón está disponible o si está ocupado
Elif: para poder elegir diferentes tipos de balones o diferentes opciones en el menú
Else: para cuando alguna condición no se cumpla
Repetición
While: fundamental para el menú y hacer varias acciones sin tener que reiniciar
For: para ver que balones están disponibles 
**Requerimiento 7: Diseño algorítmico :**
INICIO

    Mostrar menú:
        1. Ver balones
        2. Prestar balón
        3. Devolver balón
        4. Salir

    Pedir opción

    Mientras que: opción sea diferente de 4

        Si opción = 1 entonces:
            Mostrar los balones disponibles y ocupados

        Si opción = 2 entonces:
            Pedir número del balón
            Revisar si el balón está disponible

            Si está disponible entonces:
                Pedir nombre de la persona
                Mostrar lugar donde se entregará
                Registrar que el balón está ocupado
                Mostrar "Balón prestado correctamente"
            Si no:
                Mostrar "El balón ya está ocupado"

        Si opción = 3 entonces:
            Pedir número del balón
            Revisar si el balón está ocupado

            Si está ocupado entonces:
                Registrar que el balón está disponible
                Mostrar "Balón devuelto correctamente"
            Si no:
                Mostrar "El balón ya está disponible"

        Mostrar nuevamente el menú
        Pedir opción

    FIN mientras:

    Mostrar "Programa finalizado"

FIN
