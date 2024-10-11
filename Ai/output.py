from Ai import chatbot
while True:
  response = chatbot()
  response = response.text.split("```")
  response = response[1][3::]
  print(response)
