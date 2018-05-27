from gerenciador_banco import GerenciadorBanco

x = GerenciadorBanco()
print(x.executar_sql("select * from evento where nome like '%%'")
 \
                                            and descricao like '%%' \
                                            and assunto like '%segurança%' \
                                            and data like '%%' \
                                            and hora like '%%' \
                                            and local like '%%'", []))