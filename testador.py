#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from config import Config

# testa em relação aos dados 
#The evaluation script evaluate.py allows you to test your models performance for intent classification and entity recognition.
x = Config()
model_directory = x.config['trained_model_directory']
os.system('python -m rasa_nlu.evaluate --data data_teste --c config-spacy.json --model ' + model_directory)