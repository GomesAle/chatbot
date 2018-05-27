import json

class Config:
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)
    
    def salvar(self, chave, valor):
        self.config[chave] = valor
        with open('config.json', 'w') as outfile:
            json.dump(self.config, outfile)
