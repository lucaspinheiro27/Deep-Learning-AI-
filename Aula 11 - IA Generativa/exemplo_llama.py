import requests
import json
import time
url = "http://localhost:11434/api/generate"

pergunta = input("o que deseja saber?")
print("Aguarde...carregando...")
input_json = {
    "model": "llama3.1",
    "prompt": pergunta
}
inicio = time.time()
response = requests.post(url, json=input_json)

# Dividir a string em linhas
linhas = response.text.strip().split('\n')
print("Linhas: ", linhas)
# Lista para armazenar os valores de 'response'
valores_response = []
# Processar cada linha como um objeto JSON
for linha in linhas:
    # Carregar a linha como um dicionário Python
    obj = json.loads(linha)
    # Obter o valor da chave 'response'
    resposta = obj.get('response')
    # Adicionar à lista de valores de 'response'
    valores_response.append(resposta)
print("valores_response", valores_response)
# Juntar os valores de 'response' em uma única string
nova_string = ''.join(valores_response)

# Exibir a nova string resultante
print(nova_string)

print("Tempo: ", time.time() - inicio)