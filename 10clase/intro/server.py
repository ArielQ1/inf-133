from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"


@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1:
        return(
            jsonify({"error": "Se requiere un num1 o num2 en los parámetros de la URL."}),
            400,
        )
    if not num2:
        return(
            jsonify({"error": "Se requiere un num1 o num2 en los parámetros de la URL."}),
            400,
        )
    
    return jsonify({"mensaje": f"la suma es, {int(num1)+int(num2)}"})


@app.route("/palindromo", methods=["GET"])
def palindromo():
    palabra = request.args.get("cadena").lower()
    
    if not palabra:
        return(
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    if palabra == palabra[::-1]:
        return jsonify({"mensaje": f"la palabra {palabra}, es palindroma"})
    return jsonify({"mensaje": f"la palabra {palabra}, no es palindroma"})
    
@app.route("/contar", methods=["GET"])    
def contarVocal():
    contador_vocal = 0
    cadena = request.args.get("cadena").lower()
    vocal = request.args.get("vocal").lower()
    if not cadena:
        return(
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    if not vocal:
        return(
            jsonify({"error": "Se requiere una vocal en los parámetros de la URL."}),
            400,
        )
    contador_vocal = cadena.count(vocal)
    
    return jsonify({"mensaje": f"la palabra {cadena} tiene {contador_vocal} vocales {vocal}"})
    
if __name__ == '__main__':
    app.run()