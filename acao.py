from gerenciador_banco import GerenciadorBanco

class Acao:
    def __init__(self):
        self.gerenciador_banco = GerenciadorBanco()
    
    def buscar_eventos(self, slots):
        x = self.gerenciador_banco.executar_sql('select * from evento',[])
        return str(x), slots

    def buscar_info_palestra(self, slots):
        params = []

        if slots['evento'] != "":
            sql = "select * from palestra where id in (select idPalestra from palestraevento where idEvento = ?)"
            params = [(slots['evento'])]
        else:
            sql = '''select * from palestra where nome like ? 
                                            and descricao like ?
                                            and assunto like ?
                                            and data like ?
                                            and hora like ?'''
            params = [('%'+slots["nome"]+'%'), ('%'+slots["descricao"]+'%'),
                        ('%'+slots["assunto"]+'%'), ('%'+slots["data"]+'%'),
                        ('%'+slots["hora"]+'%')]

        registros = self.gerenciador_banco.executar_sql(sql, params)
        resultado = ""
        for registro in registros:
                resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[5] + '\n\n'
        return resultado, slots

    def buscar_info_palestrante(self, slots):
        params = []
        if slots['evento'] != "":
            sql = "select * from palestrante where id in (select idPalestrante from palestrantepalestra where idPalestra = ?)"
            params = [(slots['evento'])]
        else:
            sql = '''select * from palestrante where nome like ? 
                                            and descricao like ?
                                            and assunto like ?'''
            params = [('%'+slots["nome"]+'%'), ('%'+slots["descricao"]+'%'),
                        ('%'+slots["assunto"]+'%')]
        
        registros = self.gerenciador_banco.executar_sql(sql, params)
        resultado = ""
        for registro in registros:
                resultado +=  'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n\n'
        return resultado, slots

    def buscar_info_evento(self, slots):
        print("buscar_info_evento")
        resultado = ""

        #registros = self.gerenciador_banco.executar_sql('''select * from evento''', [])
        registros = self.gerenciador_banco.executar_sql('''select * from evento where nome like ? and descricao like ? and assunto like ? and data like ? and hora like ? and local like ?''', [('%'+slots["nome"]+'%'), ('%'+slots["descricao"]+'%'), ('%'+slots["assunto"]+'%'), ('%'+slots["data"]+'%'), ('%'+slots["hora"]+'%'), ('%'+slots["local"]+'%')])
        for registro in registros:
            resultado += 'Nome: ' + registro[1] + '\n' + 'Descrição: ' + registro[2] + '\n' + 'Assunto: ' + registro[3] + '\n' + 'Data: '+registro[4] + ' - ' + registro[6] + '\n' + 'Local: ' + registro[5] + '\n\n'
        return resultado, slots

    def buscar_mais_info_palestra(self, slots):
        registros = self.gerenciador_banco.executar_sql('''select id from palestra where nome like ? 
                                                and descricao like ?
                                                and assunto like ?
                                                and data like ?
                                                and hora like ?'''
                                                ,[('%'+slots["nome"]+'%'),
                                                ('%'+slots["descricao"]+'%'), ('%'+slots["assunto"]+'%'),
                                                ('%'+slots["data"]+'%'), ('%'+slots["hora"]+'%')])
        slots['palestra'] = registros[0][0]
        return 'O que você quer saber?', slots

    def buscar_mais_info_palestrante(self, slots):
        registros = self.gerenciador_banco.executar_sql('''select id from palestrante where nome like ? 
                                                and descricao like ?
                                                and assunto like ?
                                                and data like ?
                                                and hora like ?
                                                and local like ?''',[('%'+slots["nome"]+'%'),
                                                ('%'+slots["descricao"]+'%'),('%'+slots["assunto"]+'%'),
                                                ('%'+slots["data"]+'%')])
        slots['palestrante'] = registros[0][0]
        return 'O que você quer saber?', slots

    def buscar_mais_info_evento(self, slots):
        registros = self.gerenciador_banco.executar_sql('''select id from evento where nome like ? 
                                                and descricao like ?
                                                and assunto like ?
                                                and data like ?
                                                and hora like ?
                                                and local like ?''',[('%'+slots["nome"]+'%'),
                                                ('%'+slots["descricao"]+'%'),('%'+slots["assunto"]+'%'),
                                                ('%'+slots["data"]+'%'),('%'+slots["hora"]+'%'),
                                                ('%'+slots["local"]+'%')])
        slots['evento'] = registros[0][0]
        return 'O que você quer saber?', slots

    def oferecer_ajuda(self, slots):
        return "Como posso ajudar?", slots
