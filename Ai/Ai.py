import google.generativeai as genai
import base64
import json


def chatbot(user_):

    # Set your API key
    API_KEY = "AIzaSyCpGakEZsf5MbEPH5keSnLQLwrDrnZcjTc"

    # Configure the client library by providing your API key.
    genai.configure(api_key=API_KEY)

    model = "gemini-1.5-pro-latest"  # @param {isTemplate: true}
    contents_b64 = "W10="  # @param {isTemplate: true}
    generation_config_b64 = "eyJ0ZW1wZXJhdHVyZSI6MSwidG9wX3AiOjAuOTUsInRvcF9rIjowLCJtYXhfb3V0cHV0X3Rva2VucyI6ODE5Miwic3RvcF9zZXF1ZW5jZXMiOltdfQ=="  # @param {isTemplate: true}
    safety_settings_b64 = "W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d"  # @param {isTemplate: true}
    user_input_b64 = ""  # @param {isTemplate: true}

    contents = json.loads(base64.b64decode(contents_b64))
    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    user_input = base64.b64decode(user_input_b64).decode()
    stream = False

    usr = "convert to Sql Query : \" " + user_ +" \"" + " : without any eplanation"
    gemini = genai.GenerativeModel(model_name=model)
    chat = gemini.start_chat(history=contents)
    print(usr)
    response = chat.send_message(usr, stream=stream)
    print(response.text)
    response = response.text[6:-4:1]
    return response
