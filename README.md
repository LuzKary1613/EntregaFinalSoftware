# PROYECTO FINAL DE LA MATERIA DISEÑO Y ARQUITECTURA DE SOFTWARE #

1) Descripción

      Este proyecto es una aplicación web para gestionar un inventario de comestibles, permitiendo a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los ítems del inventario. La aplicación       está construida con Flask, utiliza SQLAlchemy para la interacción con la base de datos y permite la carga de datos desde archivos CSV.

3) Estructura del Proyecto

      Este proyecto sigue una estructura técnica (top-layering) para organizar el código de manera clara y modular:

5) El proyecto cuenta con las siguientes funcionalidades:

      I. Agregar ítems al inventario.
      II. Editar ítems del inventario.
      III. Eliminar ítems del inventario.
      IV. Listar ítems del inventario.
      V. Convertir precios de ítems a diferentes monedas utilizando una API externa.


6) El proyecto cuenta con 5 pruebas unitarias que verifican la funcionalidad del software. Las pruebas se encuentran en el archivo `test/test_page.py`.

      I. `def test_index(client, init_database):`
      II. `def test_add_item(client, init_database):`
      III. `def test_get_item(client, init_database):`
      IV. `def test_delete_item(client, init_database):`
      V. `def test_edit_item(client, init_database):`

7) Prácticas de SOLID

      I.Principio de Responsabilidad Única (SRP)
          Cada clase y función en este proyecto tiene una única responsabilidad. 
          Ejemplo: La clase `Item` en `models.py` es responsable de representar un ítem en la base de datos, y las funciones en `routes.py` manejan las solicitudes HTTP correspondientes.

      II. Principio de Abierto/Cerrado (OCP)
          El código está diseñado para ser extensible sin modificar el código existente.
          Ejemplo: Se puede agregar nuevos modelos o rutas sin cambiar las clases existentes. Por ejemplo, al agregar una nueva ruta en `routes.py` o un nuevo modelo en `models.py`.

      III. Principio de Sustitución de Liskov (LSP)
          Las clases derivadas pueden reemplazar a las clases base sin afectar la funcionalidad del programa.
          Ejemplo: Herencia adecuada y uso de interfaces claras en `models.py` asegura que las clases derivadas pueden sustituir a las clases base sin problemas.

      IV. Principio de Segregación de Interfaces (ISP)
          Las interfaces están diseñadas de manera que los clientes no dependan de interfaces que no utilizan.
          Ejemplo: En `routes.py`, los métodos son específicos para cada funcionalidad, evitando que los clientes dependan de métodos que no usan.

      V. Principio de Inversión de Dependencia (DIP)
          El proyecto depende de abstracciones en lugar de implementaciones concretas.
          Ejemplo: SQLAlchemy se utiliza para interactuar con la base de datos, lo que permite cambiar el backend de la base de datos sin modificar el código del negocio.

8) Patrones de Diseño

      I. Patrón de Diseño MVC (Model-View-Controller)
          El proyecto sigue el patrón MVC, donde:
              Modelos: Definidos en models.py, representan la estructura de los datos.
              Vistas: Definidas en las plantillas HTML, como index.html, add_item.html, y edit_item.html.
              Controladores: Definidos en routes.py, manejan la lógica de negocio y la interacción entre el modelo y las vistas.
   
      II. Patrón de Diseño Singleton
          La configuración de la base de datos a través de SQLAlchemy en models.py sigue el patrón Singleton, asegurando que solo haya una instancia de la conexión a la base de datos.

      III. Patrón de Diseño Factory
          El método create_app en __init__.py actúa como una fábrica para crear instancias de la aplicación Flask con las configuraciones necesarias.

      IV. Patrón de Diseño Repository
          La interacción con la base de datos a través de SQLAlchemy sigue el patrón Repository, proporcionando una abstracción para el acceso a los datos.

9) Características de Arquitectura

      I. Modularidad:
          Este proyecto está estructurado en módulos claramente definidos como models.py para los modelos de datos, routes.py para los controladores, y plantillas HTML para las vistas. Esta separación facilita el                    mantenimiento y la escalabilidad.

      II. Uso de Patrones de Diseño: La estructura sigue el patrón MVC, separando la lógica de negocio, la presentación y los datos.
          Justificación: Mejora la organización del código y facilita el mantenimiento y la escalabilidad.

      III. Dependencia en SQLAlchemy: Utiliza SQLAlchemy como ORM para la interacción con la base de datos.
          Justificación: Proporciona una capa de abstracción sobre la base de datos, facilitando las operaciones CRUD y permitiendo cambiar el backend de la base de datos con facilidad.

      IV. Configuración Centralizada: La configuración de la aplicación se gestiona en un solo lugar (`config.py`), lo que facilita la gestión y modificación de las configuraciones.
          Justificación: Simplifica la administración de la configuración y permite cambios rápidos sin modificar múltiples archivos.

      V. Uso de Blueprints: Utiliza Blueprints en Flask para modularizar las rutas.
          Justificación: Permite organizar las rutas de manera modular, mejorando la mantenibilidad y la organización del código.
