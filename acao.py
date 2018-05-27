from gerenciador_banco import GerenciadorBanco
class Acao:
    def __init__(self):
        self.gerenciador_banco = GerenciadorBanco()

    def buscar_info_palestra(self, slots):
        self.gerenciador_banco.executar_sql("select * from palestra where id in (select idPalestra from eventopalestra where idEvento = ?)", [(slots['evento'])])
        resultado = ""
        for registro in registros:
                resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n\n'
        return resultado, slots

    def buscar_info_palestrante(self, slots):
        self.gerenciador_banco.executar_sql("select * from palestrante")
        resultado = ""
        for registro in registros:
                resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n\n'
        return resultado, slots

    def buscar_info_evento(self, slots):
        resultado = ""
        if slots["nome"] == "" \
            and slots["descricao"] == "" \
            and slots["assunto"] == "" \
            and slots["data"] == "" \
            and slots["hora"] == "" \
            and slots["local"] == "":
            registros = self.gerenciador_banco.executar_sql("select * from evento", [])
            resultado = ""
            for registro in registros:
                resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n' + 'Local: ' + registro[5] + '\n\n'
        else:
            registros = self.gerenciador_banco.executar_sql('''select * from evento where nome like ? 
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

    def buscar_mais_info_evento(self, slots):
        registros = self.gerenciador_banco.executar_sql('''select * from evento where nome like ? 
                                                and descricao like ?
                                                and assunto like ?
                                                and data like ?
                                                and hora like ?
                                                and local like ?''',[('%'+slots["nome"]+'%'),
                                                ('%'+slots["descricao"]+'%'),('%'+slots["assunto"]+'%'),('%'+slots["data"]+'%'),
                                                ('%'+slots["hora"]+'%'),('%'+slots["local"]+'%')])
        slots['evento'] = registros[0][0]
        return 'O que você quer saber?', slots

    def oferecer_ajuda(self, slots):
        return "Como posso ajudar?", slots
