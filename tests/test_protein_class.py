import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent.resolve()), 
)

from protein_class import protein

def test_protein_plot():
    ex_protein = protein("Some Protein", 1234, ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"])
    ex_plot = ex_protein.plot
    assert ex_plot == open("../notebooks/exercises/day 5/example_protein.png")

def test_protein_pos():
    ex_protein = protein("Some Protein", 1234, ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"])
    ex_pos = ex_protein.get_aa_pos
    assert ex_pos == list(range(1,len(["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"])+1))
