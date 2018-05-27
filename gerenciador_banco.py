import sqlite3

class GerenciadorBanco:
    def __init__(self):
        self.conn = sqlite3.connect("bot.db")
    
    def executar_sql(self, sql, parametros):
        cursor = self.conn.cursor()
        cursor.execute(sql, parametros)
        # if len(parametros) > 0:
        #     # generates SELECT quote(?), quote(?), ...
        #     cursor.execute("SELECT " + ", ".join(["quote(?)" for i in parametros]), parametros)
        #     quoted_values = cursor.fetchone()
        #     for quoted_value in quoted_values:
        #         s = s.replace('?', quoted_value, 1)
        # print("SQL command: " + s)
        return cursor.fetchall()
