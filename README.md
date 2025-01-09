# Proyecto Urban Grocers 

#### Daniela Contreras M. (Cohort 22)

### Archivos del Proyecto:
- configuration.py: Almacena la URL y las rutas de solicitud.
- data.py: Contiene los cuerpos necesarios para las solicitudes.
- sender_stand_request.py: Contiene las funciones para crear un nuevo usuario y un nuevo kit.
- create_kit_name_kit_test.py: Se almacenan todas las funciones y tests para crear un nuevo kit.
- README.md: Contiene una descripción breve del proyecto.
- .gitignore: Incluye los archivos que deben ser ignorados por git

---

### Descripción del proyecto:

En este proyecto se realizarán pruebas para crear un nuevo kit de productos de la app Urban Grocers. 
Se probará específicamente el campo "Name" basandose en sus requisitos para su creación. Se realizarán pruebas positivas y negativas esperando que cada respuesta coincida con el código esperado.

---

### Lista de comprobación de pruebas:

**№	Description	ER:**
1.	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2.	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3.	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
4.	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
5.	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6.	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7.	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8.	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
9.	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400

---

### Tecnologías utilizadas:

- Pytest
- Requests

Para su instalación hay que abrir la terminal de Pycharm y ejectutar los comandos:
- pip install pytest
- pip install requests

---

### Instrucciones 

- Ejecuta todas las pruebas del proyecto a través de la terminal de PyCharm: escribe pytest create_kit_name_kit_test.py en la terminal.
- Ejecuta todas las pruebas a través de la interfaz de PyCharm haciendo clic en el botón con un triángulo verde en la parte superior.
- Asegúrate de ejecutarlas en el archivo correcto, una forma sencilla de hacer esto es ir al archivo y seleccionar "Current File" antes de hacer clic en el botón con un triángulo verde.
- Otra forma de ejecutar las pruebas es haciendo clic en las flechas verdes junto a las pruebas en el código.
- Algunas pruebas devolverán FAILED como resultado; no te preocupes, es un comportamiento esperado dentro de la lista de comprobaciones.