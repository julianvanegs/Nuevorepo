from transformers import pipeline

# Cargar un modelo de Question Answering
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Definir un contexto (texto donde buscar la respuesta)
contexto = """
Barranquilla es una ciudad ubicada en la región Caribe de Colombia. 
Es conocida por su carnaval, uno de los más importantes del mundo, 
y por ser un puerto clave sobre el río Magdalena.
"""

# Hacer una pregunta
pregunta = "¿Dónde está ubicada Barranquilla?"

# Obtener respuesta
respuesta = qa_model(question=pregunta, context=contexto)

print(respuesta)
