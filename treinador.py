from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import json
from config import Config

def main():
    x = Config()
    model_directory = x.config['model_directory']

    training_data = load_data('data')
    trainer = Trainer(RasaNLUConfig("config-spacy.json"))
    trainer.train(training_data)
    trained_model_directory = trainer.persist(model_directory) 

    x.salvar('trained_model_directory', trained_model_directory)

if __name__ == "__main__":
    main()