import os
import openai
from dotenv import load_dotenv
load_dotenv()
#exibindo o valor associado à chave OPENAI_API_KEY
#print (os.getenv('OPENAI_API_KEY'))

openai.api_key = os.getenv('OPENAI_API_KEY')

pergunta_padrao = 'Qual o sentimento na seguinte frase? Responda com apenas uma palavra: Positivo, Negativo ou Neutro. Eis a frase: '

frase_do_usuario = input('Escreva uma frase para enviarmos ao ChatGPT\n')

prompt = f'{pergunta_padrao}{frase_do_usuario}'

resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt
)

print(resposta.choices[0].text)

