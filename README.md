# PROYECTO FINAL DE LA MATERIA DISEÑO Y ARQUITECTURA DE SOFTWARE #

LINK DEL VIDEO: https://youtu.be/RVCQ_3VRhiI 

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

9) Top 5 de caracteristicas de arquitectura del diseño actual del proyecto

      I. Modularidad:
          Este proyecto está estructurado en módulos claramente definidos como models.py para los modelos de datos, routes.py para los controladores, y plantillas HTML para las vistas. Esta separación facilita el                    mantenimiento y la escalabilidad.

      II. Uso de Patrones de Diseño:
          Cómo lo cumple:
          Active Record Pattern: La clase Item en models.py sigue el patrón Active Record.
          Model-View-Controller (MVC): La estructura de este proyecto sigue el patrón MVC con modelos en models.py, vistas en templates/, y controladores en routes.py.
          Singleton Pattern: La instancia db de SQLAlchemy sigue el patrón Singleton.
          Decorator Pattern: Flask utiliza decoradores para definir rutas.
          Factory Pattern: La función create_app() en __init__.py sigue el patrón Factory.

      III. Abstracción de la Base de Datos:
          Este proyecto utiliza SQLAlchemy como ORM, lo que proporciona una abstracción de las operaciones de base de datos. Esto permite realizar operaciones CRUD de manera eficiente y facilita cambios en el modelo de              datos sin afectar otras partes del sistema.

      IV. Uso de Blueprints:
          Utiliza Blueprints en Flask para modularizar las rutas, lo que permite organizar las rutas de manera modular, mejorando la mantenibilidad y la organización del código.

      V. Configuración Centralizada:
         La configuración de la aplicación se gestiona en un solo lugar (`config.py`), lo que facilita la gestión y modificación de las configuraciones, lo que simplifica la administración de la configuración y permite             cambios rápidos sin modificar múltiples archivos.

10) Top 5 Características de Arquitectura en una Migración a Microservicios

      I.Desacoplamiento de Servicios
            Justificación: Cada funcionalidad de la aplicación (gestión de inventario, autenticación, procesamiento de pagos, etc.) se implementaría como un servicio independiente. Esto permite desarrollar, desplegar y               escalar cada servicio de manera independiente, mejorando la flexibilidad y la escalabilidad. Por ejemplo, el servicio de gestión de inventario podría escalarse de forma independiente del servicio de                       autenticación, optimizando el uso de recursos.
            
      II. Comunicación basada en APIs
            Justificación: Los microservicios se comunicarían entre sí a través de APIs RESTful o mensajería asincrónica. Esto facilita la integración entre servicios y permite que cada servicio sea desarrollado en                   tecnologías diferentes si es necesario. Además, la comunicación basada en APIs estandariza las interacciones y facilita la colaboración entre equipos de desarrollo.

      III. Escalabilidad Independiente
            Justificación: Cada microservicio se puede escalar de manera independiente según las necesidades de carga. Esto optimiza el uso de recursos y mejora el rendimiento de la aplicación al permitir la                          escalabilidad selectiva de componentes críticos. Por ejemplo, si el servicio de conversión de monedas recibe más tráfico, solo este servicio puede escalarse sin necesidad de escalar toda la aplicación.

      IV. Despliegue Continuo (CI/CD)
            Justificación: Los microservicios facilitan la implementación de pipelines de integración y entrega continua (CI/CD), permitiendo despliegues rápidos y seguros. Esto acelera el ciclo de desarrollo y reduce el             tiempo de entrega de nuevas funcionalidades y correcciones. Cada microservicio puede ser desplegado independientemente, lo que minimiza el impacto en el sistema general y permite una rápida iteración.

      V. Resiliencia y Tolerancia a Fallos
            Justificación: La arquitectura de microservicios puede implementar patrones de diseño para mejorar la resiliencia, como circuit breakers y retry mechanisms. Esto mejora la disponibilidad y la robustez de la               aplicación al aislar fallos y gestionar mejor los errores y fallos de componentes individuales. Por ejemplo, si un microservicio falla, los demás pueden seguir funcionando, y se pueden aplicar estrategias                 de reintento y recuperación para minimizar el impacto del fallo.

    
