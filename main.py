from rasa_nlu.model import Metadata, Interpreter
from config import Config
import sys
from acao import Acao
import sys
import time
import telepot
from telepot.loop import MessageLoop

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

acao = Acao()

bot = telepot.Bot(x.config['token'])

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

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        entrada = msg['text']
        saida = interpreter.parse(entrada)
        resultados.write('resultado: ' + str(saida) + '\n')
        resultados.flush()
        
        print(saida)
        intencao = saida['intent']['name']
        
        for hash_entity in saida['entities']:
            global slots
            slots[hash_entity['entity']] = hash_entity['value']
        resposta, slots = responder(intencao, slots)
        print(slots)
        if resposta == "":
            bot.sendMessage(chat_id, 'Eu não sei lidar com esse tipo de informação.')
        else:
            bot.sendMessage(chat_id, resposta)
        #entrada = input()
    else:
        bot.sendMessage(chat_id, 'Eu não sei lidar com esse tipo de informação.')

def main():
    # Telegram
    print("Como posso ajudar?\n")
    MessageLoop(bot, handle).run_as_thread()

    while 1:
        time.sleep(10)

    # # Console
    # x = Config()
    # trained_model_directory = x.config['trained_model_directory']

    # # where `model_directory points to the folder the model is persisted in
    # interpreter = Interpreter.load(trained_model_directory)

    # resultados = open('resultados.txt', 'a')

    # slots = {
    #     "nome" : "",
    #     "descricao" : "",
    #     "assunto" : "",
    #     "data" : "",
    #     "hora" : "",
    #     "local" : "",
    #     "evento" : "",
    #     "palestra" : "",
    #     "palestrante" : ""
    # }

    # entrada = input("Como posso ajudar?\n")
    # while entrada != "SAIR":
    #     saida = interpreter.parse(entrada)
    #     resultados.write('resultado: ' + str(saida) + '\n')
    #     resultados.flush()
        
    #     print(saida)
    #     intencao = saida['intent']['name']
        
    #     for hash_entity in saida['entities']:
    #         #global slots
    #         slots[hash_entity['entity']] = hash_entity['value']
    #     resposta, slots = responder(intencao, slots)
    #     if resposta == "":
    #         print("Eu não tenho resposta para esse pedido.")
    #     else:
    #         print(resposta)
        
    #     entrada = input()

if __name__ == "__main__":
    main()