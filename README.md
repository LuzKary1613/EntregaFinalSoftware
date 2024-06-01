# proyecto_final_arquitectura
Proyecto final de arquitectura
Sigues una estructura (top-layering) tecnica o de dominio.
-Si ya que la estructura general del proyecto contiene carpeta de test, donde se almacenan los codigos para pruebas unitarias
 y test en general, una carpeta page donde esta la funcionalidad del proyecto y dentro de page una carpeta templates
 con los html para el proyecto y en la carpeta principal solo documentos esenciales como main o config. 

# Tu proyecto cuenta con toda la funcionalidad descrita.
-si

# Tu proyecto cuenta con al menos 5 pruebas unitarias de la funcionalidad de tu software.
-si

# Tu proyecto sigue las buenas practicas de SOLID 
-si
--Single Responsibility Principle (SRP):
  Cada función en routes.py tiene una única responsabilidad. Por ejemplo, add_item() solo se ocupa de agregar un artículo 
  a la base de datos, mientras que delete_item() solo se encarga de eliminar un artículo.
  
--Open/Closed Principle (OCP):
  Las funciones son abiertas para la extensión pero cerradas para modificación. Por ejemplo, si necesitas cambiar la forma
  en que se agregan artículos (como agregar validación adicional), puedes hacerlo sin modificar la función add_item() 
  directamente, extendiéndola o agregando funcionalidad antes o después de la llamada a esta función en otro lugar del código.
  
--Liskov Substitution Principle (LSP):
  Este principio se aplica a través de la herencia en ORM. Item hereda de db.Model, lo que significa que debe poder 
  sustituir db.Model sin afectar la funcionalidad.
  
--Interface Segregation Principle (ISP):
  Flask y SQLAlchemy naturalmente promueven un diseño donde las interfaces son pequeñas y específicas a través del 
  uso de funciones dedicadas para rutas específicas, como se ve en el código proporcionado.
  
--Dependency Inversion Principle (DIP):
  Este principio se manifiesta en cómo las dependencias (como la base de datos y las configuraciones externas) 
  están desacopladas de las funciones de alto nivel y pueden ser inyectadas o modificadas sin cambiar las dependencias 
  de nivel superior. Flask permite inyectar configuraciones y cambiar detalles de la base de datos sin necesidad de 
  modificar el código de las rutas directamente.
  
# Tu proyecto sigue al menos 4 patrones de diseño.
--Active Record Pattern:
  La clase Item es un ejemplo del patrón Active Record, que es común en ORM como SQLAlchemy. Este patrón 
  permite que el objeto contenga tanto los datos (campos de la base de datos) como los comportamientos 
  (como to_dict() para serializar la información).
  
--Model-View-Controller (MVC):
  Se utiliza al momento de:
  Model: Representado por las entidades en models.py que interactúan con la base de datos.
  View: Las plantillas HTML en el directorio Templates que presentan la información al usuario.
  Controller: Los manejadores de rutas en routes.py que actúan como mediadores entre modelos y vistas.
  
--Singleton Pattern:
  La instancia db de SQLAlchemy() utilizada en models.py y referenciada en toda la aplicación sigue el patrón Singleton. 
  Esta instancia se configura una sola vez y se reutiliza en todo el proyecto, asegurando que solo existe una conexión a la 
  base de datos manejada por esta instancia.
  
--Decorator Pattern:
  Flask utiliza ampliamente el patrón Decorator para definir rutas. Las funciones como @app.route son decoradores que 
  modifican las funciones de manejo de las rutas, proporcionando una forma poderosa y flexible de extender la funcionalidad 
  de las funciones de manejo de rutas sin modificar el código.
  
--Adapter Pattern:
  Se puede considerar la función que convierte los precios de los productos a diferentes monedas como parte de un patrón Adaptador. 
  Esta función actúa como un intermediario que adapta la API de un servicio de tasas de cambio externo para ser utilizada en la 
  aplicación, permitiendo que el resto de la aplicación interactúe con APIs de terceros de una manera más coherente en el
  diseño interno.
  
--Factory Pattern:
  Utilice un patrón de fábrica con la función create_app() en el archivo __init__.py. Este patrón es típico en aplicaciones 
  Flask para crear instancias de la aplicación dependiendo del entorno de configuración o de otros parámetros que pueden variar.

El archivo README.md ademas de documentar las practicas de SOLID y patrones de diseño debera responder a las siguientes preguntas 
sobre caracteristicas de arquitectura:

# ¿Cuales son el top 5 de caracteristicas de arquitectura del diseño actual de tu proyecto? Justifica tu respuesta.
--Modularidad:
  La aplicación está estructurada en módulos claramente definidos (modelos, vistas, controladores), lo cual facilita el 
  mantenimiento y la escalabilidad. Cada módulo tiene una responsabilidad única, acorde con el principio de responsabilidad 
  única de SOLID.

--Uso de Patrones de Diseño:
  Se utilizan varios patrones de diseño, como MVC, Singleton, y Factory, lo que contribuye a un código organizado y reutilizable,
  y facilita la integración de nuevas funcionalidades.

--Abstracción de la Base de Datos:
  La utilización de SQLAlchemy como ORM permite una abstracción eficaz de las operaciones de base de datos, lo que facilita 
  cambios en el modelo de datos sin afectar otras partes del sistema.

--Separación de la lógica de negocio del manejo de la interfaz de usuario:
  El uso de plantillas HTML para la presentación y rutas Flask para la lógica de control asegura que la lógica de negocio esté 
  bien separada de la interfaz de usuario, siguiendo el principio de separación de intereses.

--Configurabilidad y Despliegue:
  La aplicación permite una configuración externa a través del archivo config.py, lo que facilita la adaptación del software a 
  diferentes entornos sin necesidad de cambiar el código fuente, lo cual es ideal para despliegues en diferentes entornos.

# ¿Si la aplicacion migrara a una arquitectura de microservicios, ¿Cuales serian el top 5 de caracteristicas de arquitectura? Justifica tu respuesta
--Desacoplamiento:
  Los microservicios estarían diseñados para ser altamente desacoplados y autónomos. Cada servicio gestionaría una parte 
  específica de la funcionalidad del negocio, como el manejo de productos, las conversiones de moneda, o la autenticación 
  de usuarios. Esto permitiría que los equipos desarrollen, desplieguen y escaleen sus servicios de manera independiente.
  
--Escalabilidad:
  La escalabilidad sería una característica inherente, permitiendo que cada microservicio se escale de forma independiente 
  en respuesta a las demandas específicas del servicio. Esto es especialmente útil en operaciones que pueden experimentar 
  picos de demanda variables.
  
--Resiliencia:
  Los microservicios favorecen una mayor resiliencia, pues cada servicio puede manejar sus propios fallos de manera aislada, 
  minimizando el impacto global en el sistema. 
  
--Rapidez en la entrega y flexibilidad en la implementación:
  La adopción de microservicios permite actualizar componentes específicos del sistema sin tener que rediseñar o 
  redesarrollar aplicaciones enteras. Esto facilita la implementación de mejoras continuas y la integración/deployment 
  continuo (CI/CD), permitiendo a los equipos lanzar nuevas características de manera más rápida y segura.
  
--Independencia Tecnológica:
  Cada microservicio puede ser desarrollado utilizando el stack tecnológico que mejor se adapte a sus necesidades, 
  lo que incluye diferentes lenguajes de programación, bases de datos o herramientas de almacenamiento. 
  Esto permite optimizar cada microservicio de manera individual para obtener el mejor rendimiento y escalabilidad posibles.
