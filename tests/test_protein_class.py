import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent.resolve()), 
)

from protein_class.protein_class import Protein
