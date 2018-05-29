from rasa_nlu.model import Metadata, Interpreter
from config import Config
import sys
from acao import Acao

slots = {
    "nome" : "",
    "descricao" : "",
    "assunto" : "",
    "data" : "",
    "hora" : "",
    "local" : "",
    "evento" : "",
    "palestra" : "",
    "palestrante" : ""
}

acao = Acao()

def responder(intencao, slots):
    if intencao == 'saudar':
        return acao.oferecer_ajuda(slots)
    if intencao == 'pedir_info_evento':
        return acao.buscar_info_evento(slots)
    if intencao == 'pedir_info_palestra':
        return acao.buscar_info_palestra(slots)
    if intencao == 'pedir_info_palestrante':
        return acao.buscar_info_palestrante(slots)
    if intencao == 'pedir_mais_info_evento':
        return acao.buscar_mais_info_evento(slots)
    if intencao == 'pedir_mais_info_palestra':
        return acao.buscar_mais_info_palestra(slots)

def main():
    x = Config()
    trained_model_directory = x.config['trained_model_directory']

    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load(trained_model_directory)

    resultados = open('resultados.txt', 'a')

    slots = {
        "nome" : "",
        "descricao" : "",
        "assunto" : "",
        "data" : "",
        "hora" : "",
        "local" : "",
        "evento" : "",
        "palestra" : "",
        "palestrante" : ""
    }

    entrada = input("Como posso ajudar?\n")
    while entrada != "SAIR":
        saida = interpreter.parse(entrada)
        resultados.write('resultado: ' + str(saida) + '\n')
        resultados.flush()
        
        print(saida)
        intencao = saida['intent']['name']
        
        for hash_entity in saida['entities']:
            #global slots
            slots[hash_entity['entity']] = hash_entity['value']
        resposta, slots = responder(intencao, slots)
        if resposta == "":
            print("Eu não tenho resposta para esse pedido.")
        else:
            print(resposta)
        
        entrada = input()

if __name__ == "__main__":
    main()