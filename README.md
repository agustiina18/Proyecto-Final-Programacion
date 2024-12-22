# Proyecto-Final-Programacion
# Gestión de Inventario

Este proyecto es una aplicación en Python que permite gestionar el inventario de una tienda. Incluye funcionalidades para registrar, visualizar, actualizar, eliminar y buscar productos, así como generar reportes de productos con bajo stock.

## Descripción

La aplicación utiliza SQLite como base de datos para almacenar la información de los productos. La interfaz de usuario es en línea de comandos, ofreciendo un menú para navegar entre las opciones.

## Requisitos Previos

- Python 3.6 o superior instalado en tu computadora.
- SQLite, viene incluido con Python, no es necesario instalarlo por separado
- (Opcional) Un editor de texto o IDE como Visual Studio Code para editar y ejecutar el código.

## Archivos Incluidos

1. inventario.py: Script principal de la aplicación.
2. inventario.db: Base de datos SQLite generada automáticamente.
3. README.txt: Este archivo de instrucciones.

## Instrucciones de Instalación y Ejecución

1. Descarga o clona el proyecto en tu computadora.
2. Asegúrate de que el archivo 'inventario.py' este en la misma carpeta que este archivo 'README.txt'.
3. Abre una terminal y navega hasta la carpeta del proyecto.
4. Ejecuta el siguiente comando para iniciar la aplicación:
5. Sigue las instrucciones del menú para utilizar las funcionalidades.

## Funcionalidades Implementadas

1. Registrar Producto: Agrega nuevos productos al inventario solicitando datos como nombre, descripción, cantidad, precio y categoría.
2. Visualizar Productos: Muestra todos los productos registrados con su información detallada.
3. Actualizar Producto: Permite modificar la cantidad disponible de un producto específico.
4. Eliminar Producto: Elimina un producto del inventario utilizando su ID.
5. Buscar Producto: Busca productos por ID (o por nombre/categoría, si está implementado).
6. Reporte de Bajo Stock: Genera un informe de productos con cantidad igual o inferior a un límite especificado.

## Créditos

Desarrollado como parte del Proyecto Final Integrador de Programación.
