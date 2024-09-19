from formodul import Formulario

# Crear el formulario
formulario = Formulario('Formulario de contacto')

# Agregar campos de diferentes tipos
formulario.agregar_campo("texto", "nombre", "Nombre")
formulario.agregar_campo("email", "email", "Correo electrónico")
formulario.agregar_campo("textarea", "mensaje", "Mensaje")
formulario.agregar_campo("select", "opcion", "Selecciona una opción", opciones=["Opción 1", "Opción 2", "Opción 3"])

# Generar el HTML del formulario
html = formulario.generar_html()

# Imprimir el HTML generado
print(html)
