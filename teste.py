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
resultado, slots = acao.buscar_info_evento(slots)
print(resultado)
print(slots)