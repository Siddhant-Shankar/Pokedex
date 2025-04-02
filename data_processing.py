import pandas as pd
import os


def load_pokemon_data(): 
    df = pd.read_csv('data/pokemon.csv')
    return df
if __name__ == "__main__":
    df = load_pokemon_data()
# What is the purpose of this code snippet?