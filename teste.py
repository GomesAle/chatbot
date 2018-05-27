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
x = acao.buscar_info_palestra(slots)
print(x)