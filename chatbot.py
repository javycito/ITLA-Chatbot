from preguntas import respuestas

def inicio_chatbot():
    print("¡Bienvenido! Dime en que te ayudOoO (nota: Si no necesitas ayuda, escribe 'salir' y me voy)")
    
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == 'salir':
            print("¡Gracias por usar el chatbot! Hasta luego.")
            break
        
        respuesta = obtener_respuesta(pregunta)
        print("Chatbot: " + respuesta)

def obtener_respuesta(pregunta):
    pregunta_normalizada = pregunta.lower()
    
    for pregunta_esperada, respuesta in respuestas.items():
        if pregunta_normalizada in pregunta_esperada.lower():
            return respuesta
    
    return "Lo siento, no tengo una respuesta para esa pregunta."
inicio_chatbot()