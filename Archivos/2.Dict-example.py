# Diccionario de preguntas
cuestionario = {
    1: {
        "pregunta": "¿Qué tipo de tipado tiene Python?",
        "respuesta": "Dinámico",
        "puntuacion": 1,
        "retroalimentacion": "Correcto, Python permite cambiar el tipo de una variable en tiempo de ejecución."
    },
    2: {
        "pregunta": "¿Cuál de estos es un lenguaje compilado?",
        "respuesta": "C",
        "puntuacion": 1,
        "retroalimentacion": "Bien, los lenguajes compilados traducen el código a binario antes de ejecutarse."
    },
    3: {
        "pregunta": "¿Qué estructura de datos no permite repetidos?",
        "respuesta": "Conjunto",
        "puntuacion": 1,
        "retroalimentacion": "Exacto, los conjuntos almacenan elementos únicos sin orden definido."
    }
}

# Ejemplo de acceso:
print(cuestionario[1]["pregunta"])
print("Respuesta correcta:", cuestionario[1]["respuesta"])