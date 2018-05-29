from acao import Acao

slots = {
    "nome" : "",
    "descricao" : "",
    "assunto" : "segurança",
    "data" : "",
    "hora" : "",
    "local" : "",
    "evento" : "1",
    "palestra" : "",
    "palestrante" : ""
}

acao = Acao()
resultado, slots = acao.buscar_mais_info_palestra(slots)
print(resultado)
print(slots)