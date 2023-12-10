import openai

# Configura tu clave de API
openai.api_key = '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'
# openai.api_key = 'b64b3ced-91b1-483e-8d63-2043143efa44'

# Realiza una llamada a la API para obtener una respuesta
response = openai.Completion.create(
  engine="text-davinci-003",  # Puedes probar otros motores
  prompt="Escribe aquí tu pregunta o texto.",
  max_tokens=150  # Puedes ajustar este valor según tu necesidad
)

# Imprime la respuesta generada
print(response.choices[0].text.strip())
