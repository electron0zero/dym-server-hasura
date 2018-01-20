#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
from wordsegment import load

if __name__ == '__main__':
    # wordsegment load function reads and parses the unigrams and bigrams data from disk.
    # Loading the data only needs to be done once.
    load()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Your very own did you mean feature in Google Search'})
    app.run(port=8080)
