#!/usr/bin/env python3

import connexion
from wordsegment import load

from swagger_server import encoder


def main():
    # wordsegment load function reads and parses the unigrams and bigrams data from disk.
    # Loading the data only needs to be done once.
    load()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Did You Mean API'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
