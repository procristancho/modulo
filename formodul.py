class Formulario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.campos = []

    def agregar_campo(self, tipo, nombre, etiqueta, opciones=None):
        """Agrega un campo al formulario con el tipo, nombre, etiqueta y opciones (si aplica)."""
        campo = {
            "tipo": tipo,
            "nombre": nombre,
            "etiqueta": etiqueta,
            "opciones": opciones
        }
        self.campos.append(campo)

    def generar_html(self):
        """Genera el código HTML del formulario, incluyendo todos los campos."""
        html = "<form>"
        for campo in self.campos:
            html += self._generar_campo(campo)
        html += "<button type='submit'>Enviar</button>"
        html += "</form>"
        return html

    def _generar_campo(self, campo):
        """Genera el HTML para un campo específico según su tipo."""
        html = ""
        if campo["tipo"] == "texto":
            html += f"<label for='{campo['nombre']}'>{campo['etiqueta']}</label>"
            html += f"<input type='text' class='form-control' id='{campo['nombre']}' name='{campo['nombre']}'>"
        elif campo["tipo"] == "email":
            html += f"<label for='{campo['nombre']}'>{campo['etiqueta']}</label>"
            html += f"<input type='email' class='form-control' id='{campo['nombre']}' name='{campo['nombre']}'>"
        elif campo["tipo"] == "textarea":
            html += f"<label for='{campo['nombre']}'>{campo['etiqueta']}</label>"
            html += f"<textarea class='form-control' id='{campo['nombre']}' name='{campo['nombre']}'></textarea>"
        elif campo["tipo"] == "select" and campo["opciones"]:
            html += f"<label for='{campo['nombre']}'>{campo['etiqueta']}</label>"
            html += f"<select class='form-control' id='{campo['nombre']}' name='{campo['nombre']}'>"
            for opcion in campo["opciones"]:
                html += f"<option value='{opcion}'>{opcion}</option>"
            html += "</select>"
        return html
