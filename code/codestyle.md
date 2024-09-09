# Código de Estilo - Proyecto en Python

Este documento define el estándar de codificación para proyectos en Python (PEP8). Todos los miembros del equipo deben adherirse a estas reglas, y cualquier cambio debe ser consensuado y actualizado en este archivo.

## Convenciones Generales

1. **Indentación:**
   - Usar **4 espacios** por nivel de indentación. No se permiten tabulaciones.

2. **Nombres de Variables y Funciones:**
   - Usar **snake_case** para nombres de variables y funciones:
     ```python
     variable_de_ejemplo = 42
     def funcion_de_ejemplo():
         pass
     ```
   - Los nombres de clases deben estar en **PascalCase**:
     ```python
     class MiClaseEjemplo:
         pass
     ```

3. **Comentarios:**
   - Los comentarios deben ser claros y concisos. Explican el **por qué**, no el **cómo**.
   - Usar comentarios en inglés o en español según la decisión del equipo, pero ser consistente en todo el proyecto.
   - Para comentarios de una línea, usar `#` seguido de un espacio:
     ```python
     # Esto es un comentario de ejemplo.
     ```
   - Para bloques de comentarios, usar docstrings (`"""` o `'''`) dentro de funciones y clases.
     ```python
     """
     Este es un comentario de bloque o docstring.
     Describe de manera general la clase o función.
     """
     ```

4. **Estructura del Código:**
   - Se deben dejar **2 líneas en blanco** entre funciones y clases de nivel superior, y **1 línea en blanco** entre métodos dentro de una clase.
   - El código debe estar organizado en bloques lógicos. Usar líneas en blanco para separar bloques de código relacionados.

5. **Cadenas de Texto (Strings):**
   - Usar comillas simples `' '` o dobles `" "` de manera consistente para cadenas de texto. Recomendamos usar comillas simples, excepto cuando la cadena contenga comillas simples.
   - Usar **f-strings** (formato literal) para la interpolación de variables en cadenas:
     ```python
     nombre = "Mundo"
     print(f"Hola, {nombre}")
     ```

6. **Espaciado:**
   - Usar un espacio alrededor de los operadores (asignación, comparadores, etc.):
     ```python
     a = b + c
     if a == 2:
         pass
     ```

7. **Importaciones:**
   - Las importaciones deben hacerse en la parte superior del archivo, en bloques separados:
     - Importaciones estándar de Python.
     - Importaciones de terceros.
     - Importaciones locales del proyecto.
     ```python
     import os
     import sys

     import requests

     from mi_proyecto.modulo import MiClase
     ```

   - Usar solo **importaciones absolutas** en lugar de relativas para evitar confusiones:
     ```python
     from mi_modulo import MiClase  # Correcto
     ```

## Convenciones Específicas para Funciones y Clases

1. **Funciones:**
   - Las funciones deben ser cortas y realizar una única tarea. Si una función es demasiado larga, considera dividirla en funciones más pequeñas.
   - Si una función devuelve múltiples valores, considera usar **tuplas** o **objetos** para mayor claridad:
     ```python
     def obtener_datos():
         return nombre, edad, direccion  # Uso de tupla
     ```

2. **Clases:**
   - Usar **PascalCase** para los nombres de las clases.
   - Cada clase debe tener un docstring que explique su propósito y uso.
   - Los métodos que no modifiquen el estado del objeto deben declararse como **@staticmethod** o **@classmethod** según corresponda.

## Documentación

1. **Docstrings:**
   - Todas las funciones, clases y métodos deben tener un **docstring** que explique su propósito.
   - Seguir el formato de **Google Style** o **reStructuredText** para los docstrings:
     ```python
     def mi_funcion(parametro1, parametro2):
         """
         Realiza una operación específica con los parámetros dados.

         Args:
             parametro1 (str): El primer parámetro.
             parametro2 (int): El segundo parámetro.

         Returns:
             bool: Verdadero si la operación es exitosa, Falso en caso contrario.
         """
         return True
     ```

2. **Anotaciones de Tipo:**
   - Siempre que sea posible, agregar **anotaciones de tipo** para variables y funciones:
     ```python
     def sumar(a: int, b: int) -> int:
         return a + b
     ```

## Manejo de Errores

1. **Excepciones:**
   - Manejar siempre las excepciones de manera explícita y específica:
     ```python
     try:
         resultado = operacion()
     except ValueError as e:
         print(f"Error: {e}")
     ```

2. **No capturar excepciones genéricas:**
   - Evitar usar `except Exception:` de manera genérica a menos que sea absolutamente necesario.

## Formato Automático

1. **Formatos de Código:**
   - Usar herramientas de formato automático como **Black** para garantizar que el código siga un estilo consistente:
     ```bash
     black nombre_del_archivo.py
     ```

2. **Linting:**
   - Utilizar **flake8** o **pylint** para revisar la calidad del código y mantener el estilo de codificación correcto:
     ```bash
     flake8 nombre_del_archivo.py
     ```

## Revisiones y Actualización

1. **Revisiones de Código:**
   - Todo el código nuevo debe ser revisado a través de **pull requests** (PR) antes de ser fusionado a la rama principal.
   - Las revisiones deben enfocarse tanto en la calidad del código como en el cumplimiento del estilo definido en este archivo.

2. **Actualización de CODESTYLE.md:**
   - Cualquier cambio en las reglas de estilo debe ser consensuado por el equipo y reflejado en este documento.