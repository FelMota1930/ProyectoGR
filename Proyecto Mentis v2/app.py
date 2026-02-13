from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario con los datos de los abogados
abogados_db = {
    "1010": {
        "nombre": "Dr. Miguel Tovar",
        "foto": "alberto.jpg",
        "correo": "miguel_tovar@gr-asociados-mentis.com",
        "telefono": "+19497345982",
        "descripcion": "Especialista en Derecho de Inmigración con más de 15 años de experiencia en procesos de residencia y ciudadanía."
    },
    "2020": {
        "nombre": "Dr. Justin Harvey",
        "foto": "justin.jpg",
        "correo": "harveyj.davidson@gr-asociados-mentis.com",
        "telefono": "+12135557652",
        "descripcion": "Especialista en Derecho de Inmigración con más de 20 años de experiencia en procesos de residencia y ciudadanía."
    }
}

@app.route('/servicio/<id_servicio>')
def mostrar_servicio(id_servicio):
    # Esto simplemente abre el archivo servicio.html 
    # y le "pasa" el ID (ej: familia-usa) a la página
    return render_template('servicio.html', servicio_id=id_servicio)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    codigo = request.form.get('codigo_abogado')
    # Buscamos en nuestra "base de datos"
    abogado = abogados_db.get(codigo)
    
    if abogado:
        return render_template('resultado.html', abogado=abogado)
    else:
        # Si no existe, puedes crear un error simple o volver a consulta
        return "<h3>Abogado no encontrado. Verifique el código 1010.</h3><a href='/consulta'>Volver a intentar</a>", 404

if __name__ == '__main__':
    app.run(debug=True)