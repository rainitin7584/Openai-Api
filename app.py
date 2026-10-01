from openai import OpenAI
from dotenv import load_dotenv 
from os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

reponse = client.responses.create(
  model= "gpt-5.6-luna",
  input="Expalin artificial intelligence is one simple paragraph."
)

print(response.output_text)
