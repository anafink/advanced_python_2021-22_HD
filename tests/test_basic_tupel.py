#alles was in der zelle steht wird in das file geschrieben
import sys
from pathlib import Path
# -------- START of inconvenient addon block --------
# This block is not necessary if you have installed your package
# using e.g. pip install -e (requires setup.py)
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    str(Path(__file__).parent.parent.resolve())
)
# It make import peak_finder possible
# This is a demo hack for the course :)
# --------  END of inconvenient addon block  --------

import peak_finder
#tests müssen immer mit test anfangen
def test_find_peaks_tupel():
    peaks = peak_finder.basic.find_peaks([(5,0,0),(20,0,0),(0,2,2),(0,19,0),(5,0,0)])
    assert peaks == [(20, 0, 0), (0, 19, 0)]
