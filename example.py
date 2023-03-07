import openai
from apikey import APIKEY
openai.api_key = APIKEY


output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
             "Write me a script for hosting a \
             conference on technology"}]
)

print(output)