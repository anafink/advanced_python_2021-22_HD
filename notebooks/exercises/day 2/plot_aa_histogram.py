path = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"
fasta = []
newfasta = []
with open(path) as f:
    for line in f:
        fasta.append(line)

for pos, seq in enumerate(fasta):
    if seq[0] == ">":
        fasta.pop(pos)
    
newfasta = [x[:-1] for x in fasta]

from collections import Counter
fastastr = ""
fastastr = ''.join(newfasta)

fastac = {}
fastac = Counter(fastastr)
print(fastac)

with open("fastacount.csv", "w") as output:
    output.write(str("aa, count \n"))
    for  aa, num in Counter(fastastr).items():
        output.write(str(str(aa) + ", " + str(num) + "\n"))

import matplotlib.pyplot as plt

plt.figure(figsize=(15,5))
plt.bar(fastac.keys(), fastac.values(), width=.5, color='g', align="center")

plt.savefig('histofaahuman.pdf')
