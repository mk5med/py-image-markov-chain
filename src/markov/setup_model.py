import sys
import os

# Fix import
sys.path.insert(0, os.getcwd())

from src.markov.calculate_statistics import calculate_statistics
from src.markov.create_model import create_model


def setup_model(text: str):
    (wc, sc) = calculate_statistics(text)
    model = create_model(wc, sc)
    return model
