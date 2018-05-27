from rasa_nlu.model import Metadata, Interpreter
from config import Config
import sys
from gerenciador_banco import GerenciadorBanco

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

gerenciador_banco = GerenciadorBanco()

def buscar_info_palestra(slots):
    gerenciador_banco.executar_sql("select * from palestra")
    resultado = ""
    for registro in registros:
            resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n\n'
    return resultado, slots

def buscar_info_palestrante(slots):
    gerenciador_banco.executar_sql("select * from palestrante")
    resultado = ""
    for registro in registros:
            resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n\n'
    return resultado, slots

def buscar_info_evento(slots):
    resultado = ""
    if slots["nome"] == "" \
        and slots["descricao"] == "" \
        and slots["assunto"] == "" \
        and slots["data"] == "" \
        and slots["hora"] == "" \
        and slots["local"] == "":
        registros = gerenciador_banco.executar_sql("select * from evento", [])
        resultado = ""
        for registro in registros:
            resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n' + 'Local: ' + registro[5] + '\n\n'
    else:
        registros = gerenciador_banco.executar_sql('''select * from evento where nome like ? 
                                            and descricao like ?
                                            and assunto like ?
                                            and data like ?
                                            and hora like ?
                                            and local like ?''',[('%'+slots["nome"]+'%'),
                                            ('%'+slots["descricao"]+'%'),('%'+slots["assunto"]+'%'),('%'+slots["data"]+'%'),
                                            ('%'+slots["hora"]+'%'),('%'+slots["local"]+'%')])
        for registro in registros:
            resultado = 'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n' + 'Local: ' + registro[5] + '\n\n'
    return resultado, slots

def buscar_mais_info_evento(slots):
    registros = gerenciador_banco.executar_sql('''select * from evento where nome like ? 
                                            and descricao like ?
                                            and assunto like ?
                                            and data like ?
                                            and hora like ?
                                            and local like ?''',[('%'+slots["nome"]+'%'),
                                            ('%'+slots["descricao"]+'%'),('%'+slots["assunto"]+'%'),('%'+slots["data"]+'%'),
                                            ('%'+slots["hora"]+'%'),('%'+slots["local"]+'%')])
    slots['evento'] = registros[0][0]
    return 'O que você quer saber?', slots

def oferecer_ajuda(slots):
    return "Como posso ajudar?", slots

def responder(intencao, slots):
    if intencao == 'saudar':
        return oferecer_ajuda(slots)
    if intencao == 'pedir_info_evento':
        return buscar_info_evento(slots)
    if intencao == 'pedir_info_palestra':
        return buscar_info_palestra(slots)
    if intencao == 'pedir_info_palestrante':
        return buscar_info_palestrante(slots)
    if intencao == 'pedir_mais_info_evento':
        return buscar_mais_info_evento(slots)

def main():
    x = Config()
    trained_model_directory = x.config['trained_model_directory']

    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load(trained_model_directory )

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

    entrada = input("Como posso ajudar?")
    while entrada != "SAIR":
        saida = interpreter.parse(entrada)
        resultados.write('resultado: ' + str(saida))
        resultados.flush()
        
        print(saida)
        intencao = saida['intent']['name']
        
        for hash_entity in saida['entities']:
            #global slots
            slots[hash_entity['entity']] = hash_entity['value']
        resposta, slots = responder(intencao, slots)
        print(resposta)
        entrada = input()

if __name__ == "__main__":
    main()