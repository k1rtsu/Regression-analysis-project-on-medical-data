#!/usr/bin/env python3
import numpy as np
import pandas as pd
import os

dirname = os.path.dirname(__file__)

def get_data():
    file = os.path.join(dirname, 'fram.txt')
    fram = pd.read_csv(file, sep='\t')
    return fram

def rescale(s):
    std = s.std()
    mean = s.mean()

    resc = (s - mean) / (2 * std)

    return resc


def main():
    data = get_data()
    print(rescale(data['AGE']))

if __name__ == "__main__":
    main()
