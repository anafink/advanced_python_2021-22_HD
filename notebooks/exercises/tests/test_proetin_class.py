import sys
from pathlib import Path

import protein_class

def test_protein_class():
    ex_protein = protein("Some Protein", 1234, ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"])
    ex_plot = ex_protein.plot
    assert ex_plot == open("notebooks/exercises/day 5/example_protein.png")
