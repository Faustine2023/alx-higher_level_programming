#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    for nom in sorted(dir(hidden_4)):
        if not nom.startswith('__'):
            print(nom)
