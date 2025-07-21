# Gestion-de-mantenimiento-de-aeronaves

TÍTULO: Sistema gestión mantenimiento de aeronaves
DESCRIPCIÓN: Es una aplicación hecha en Python que usa programación orientada a objetos para simular y automatizar el mantenimiento de aviones en una aerolínea.
Permitiendo llevar el control de cada avión (como sus horas de vuelo y estado), registrar fallas, asignar técnicos y hangares disponibles, y gestionar los mantenimientos.
INTEGRANTES:
Brandon Enriquez Restrepo
Juan Sebastian Gallo Castañeda
Santiago Andrés Quintero Ramirez

INSTRUCCIONES SOBRE CÓMO CONFIGURAR, INSTALAR DEPENDENCIAS Y EJECUTAR LA APLICACIÓN
La aplicación está desarrollada en Python puro y no requiere instalación de dependencias externas. 
Empieza copiando y pegando el código en Visual Code Studio preferiblemente o cualquier otro entorno de desarrollo siempre y cuando tenga instalado python y guardalo como un archivo .py
Abre una terminal o consola de comandos y escribe:  “python” seguido de la ruta donde tienes guardado el archivo de python como “python sistema_mantenimiento.py” y luego el sistema ejecutará la aplicación.
El sistema te mostrará el estado de las aeronaves, las fallas detectadas, el mantenimiento requerido y los técnicos asignados, todo de forma automática en la terminal.
DESCRIPCIÓN GENERAL DE LAS CARACTERÍSTICAS DEL PROYECTO
Su objetivo principal es simular y automatizar la gestión del mantenimiento de aeronaves dentro de una aerolínea, asegurando una planificación eficiente, el seguimiento del estado operativo de las aeronaves y la optimización de recursos como técnicos y hangares.

Clases principales del sistema:
Avión: Contiene datos de cada aeronave, incluyendo su modelo, horas de vuelo desde el último mantenimiento, ciclos de vuelo desde el último mantenimiento, fecha del último mantenimiento y fecha de la última falla.
Falla: Representa una incidencia técnica registrada en una aeronave, con detalles como descripción y nivel de gravedad catalogada entre leve, media o crítica.
Mantenimiento: Servicio de mantenimiento que se le hace a una aeronave, respondiendo a fallas repentinas o al cumplimiento de las horas o ciclos de vuelo máximas antes de la revisión.
Técnico: Persona especializada en un tipo de mantenimiento, asignada a una aeronave dependiendo del lugar y la falla presentada.
Hangar: Administra la ubicación y disponibilidad de los hangares utilizados durante los mantenimiento.
El sistema funciona de forma que cuando en un avión surge una falla inesperada, este lo envia automaticamente a un hangar en Medellin o Bogota dependiendo si este está ocupado o desocupado, despues tambien le asigna un técnico para hacer el mantenimiento dependiendo del tipo de falla, si es revisión general o la ciudad, en adición el programa advertirá acerca de los aviones que están cercanos a un próximo mantenimiento cuando de manera inminente cumplirán sus horas o ciclos de vuelo máximo sin revisión.



