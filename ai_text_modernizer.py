#!/opt/homebrew/bin/python3.9

# import the OpenAI Python library for calling the OpenAI API
from pprint import pprint
import openai

MODEL = "gpt-4"
openai.api_key_path = "openai_api_key.txt"

#system = "You hold advanced degrees in Italian literature from Princeton. You will be given baroque Italian text, copied from Google Sheets. Modernize the spelling and capitalization. Keep the capitalization the same unless it would be weird in modern Italian. Leave all punctuation and linebreaks as is. Whitespace is significant! Your output will be consumed programmatically, so always follow my directions."
system = "You will be given baroque Italian text. Humbly identify any typos."

user = """
Così si fa
Se potese qui nascoso
Ogni momento dicon le donne
O pazzo, o pazzo, o pazzo, pazzissimo Biondello!
Siano pronte alle gran nozze
S'oggi, oh Dei, sperar mi fate
Su via, putti, presto, presto!
Alto, all'armi, o miei soldati!
Ho un pensiero
Se fosse qui nascoso
Ogni momento dicon le donne
Che parli, che dica
S'oggi, oh Dei, sperar mi fate
"""

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user},

    ],
    temperature=0.9,
)

# pprint(response)
print(response['choices'][0]['message']['content'])



