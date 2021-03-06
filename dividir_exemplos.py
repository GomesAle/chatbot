import json, codecs
from os import listdir

for arquivo in listdir('data'):
    nome_arquivo = arquivo
    json_data = open('data/' + nome_arquivo, encoding='utf-8').read()

    data = json.loads(json_data)

    n = len(data['rasa_nlu_data']['common_examples'])

    # treinamento
    antes = '''{"rasa_nlu_data": {"regex_features": [], "entity_synonyms": [], "common_examples":['''
    depois = "]}}"
    meio = ""

    for i in range(0, int(n/2)):
        meio += str(data['rasa_nlu_data']['common_examples'][i]).replace("'",'"') + ","
    meio = meio[:-1]
    
    fim = antes + meio + depois
    with open('data_treino/'+nome_arquivo.split('.')[0] + "_treino.json", 'w', encoding='utf-8') as outfile:
        json.dump(json.loads(fim), outfile, ensure_ascii=False)

    # teste
    antes = '''{"rasa_nlu_data": {"regex_features": [], "entity_synonyms": [], "common_examples":['''
    depois = "]}}"
    meio = ""
    for i in range(int(n/2), n):
        meio += str(data['rasa_nlu_data']['common_examples'][i]).replace("'",'"') + ","
    meio = meio[:-1]
    print(meio)
    fim = antes + meio + depois

    with open('data_teste/'+nome_arquivo.split('.')[0] + "_teste.json", 'w', encoding='utf-8') as outfile:
        json.dump(json.loads(fim), outfile, ensure_ascii=False)