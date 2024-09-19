# Generador de Formularios en HTML

Este proyecto es un ejemplo básico de cómo utilizar módulos en Python para generar formularios HTML dinámicos. Incluye dos archivos principales: `formodul.py`, donde se define la clase `Formulario`, y `ar.py`, que utiliza esta clase para generar un formulario HTML.

## Descripción

El módulo `formodul.py` contiene la clase `Formulario`, que permite crear un formulario con diferentes tipos de campos como texto, email, textarea y select. La clase proporciona un método para generar el HTML correspondiente al formulario, y permite añadir validaciones como campos requeridos, `maxlength` y `placeholder`.

### Funcionalidades

- **Agregar campos al formulario**: Se pueden agregar diferentes tipos de campos (texto, email, textarea, select).
- **Validaciones**: Se pueden definir campos como obligatorios, establecer un `maxlength` y un `placeholder` personalizado.
- **Generar HTML**: La clase `Formulario` genera el HTML del formulario dinámicamente.

### Archivos principales

1. **formodul.py**: 
   Contiene la clase `Formulario` que maneja la creación de campos y la generación del HTML.

   ```python
   class Formulario:
       def __init__(self, nombre):
           self.nombre = nombre
           self.campos = []

       def agregar_campo(self, tipo, nombre, etiqueta, opciones=None, requerido=False, placeholder=None, maxlength=None):
           campo = {
               "tipo": tipo,
               "nombre": nombre,
               "etiqueta": etiqueta,
               "opciones": opciones,
               "requerido": requerido,
               "placeholder": placeholder,
               "maxlength": maxlength
           }
           self.campos.append(campo)

       def generar_html(self):
           html = "<form>"
           for campo in self.campos:
               if campo["tipo"] == "texto":
                   html += f"<label for='{campo['nombre']}'>{campo['etiqueta']}</label>"
                   html += f"<input type='text' id='{campo['nombre']}' name='{campo['nombre']}'"
                   if campo['placeholder']:
                       html += f" placeholder='{campo['placeholder']}'"
                   if campo['maxlength']:
                       html += f" maxlength='{campo['maxlength']}'"
                   if campo['requerido']:
                       html += " required"
                   html += ">"
           html += "</form>"
           return html
   
  2. **ar.py**:
     Este archivo importa la clase `Formulario` del modulo `formodul.py` y la utiliza para crear un formulario HTML simple con campos de texto y email.

     ```python
     from formodul import Formulario
     
     formulario = Formulario('Formulario de contacto')
     formulario.agregar_campo("texto", "nombre", "Nombre", requerido=True, placeholder="Ingresa tu nombre", maxlength=50)
     formulario.agregar_campo("email", "email", "Correo electrónico", requerido=True, placeholder="Ingresa tu correo electrónico")

     html = formulario.generar_html()

     # Guardar el HTML en un archivo
     with open("formulario.html", "w") as archivo:
         archivo.write(html)
     
     print("Formulario guardado como 'formulario.html'.")```
     
### Instalación

1. Clona este repositorio
     ```bash
       git clone https://github.com/procristancho/formulario-generador.git
       cd formulario-generador


2. Ejecuta el script `ar.py` que puedes abrir en cualquier navegador
    ```bash
     python ar.py
         
Esto generará un archivo `formulario.html` que puedes abrir en cualquier navegador.

### Mejoras y Faracterísticas Futros
  * Agregar más tipos de campos(como radio buttons, checkboxes, etc.).
  * Soporte para estilos CSS personalizados.
  * Validaciones más avanzadas(ej.validación de formato email).

### Contribuciones 
  Las contribuciones son bienvenidas. Si deseas contribuir, por favor crea un fork des repositorio y abre un pull request con tus cambios.

### Licencia
  Este proyecto está bajo la Licencia MIT.
