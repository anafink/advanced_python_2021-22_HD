#example for animali kingdom: mus musculus (mouse)
mpath = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/uniprot-reviewed_yes+organism__Mus+musculus+(Mouse)+[10090]_.fasta"
mfasta = []
mnewfasta = []
with open(mpath) as f:
    for line in f:
        mfasta.append(line)

for pos, seq in enumerate(mfasta):
    if seq[0] == ">":
        mfasta.pop(pos)
    
mnewfasta = [x[:-1] for x in mfasta]

from collections import Counter
mfastastr = ""
mfastastr = ''.join(mnewfasta)

mfastac = {}
mfastac = Counter(mfastastr)
print(mfastac)

with open("mfastacount.csv", "w") as output:
    output.write(str("aa, count \n"))
    for  aa, num in Counter(mfastastr).items():
        output.write(str(str(aa) + ", " + str(num) + "\n"))

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

fig1 = plt.figure(figsize=(15,5))
fig1 = plt.bar(mfastac.keys(), mfastac.values(), width=.5, color='g', align="center")

#example for plantae kingdom: Zea mays (maize)

ppath = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/uniprot-reviewed_yes+organism__Zea+mays+(Maize)+[4577]_.fasta"
pfasta = []
pnewfasta = []
with open(ppath) as f:
    for line in f:
        pfasta.append(line)

for pos, seq in enumerate(pfasta):
    if seq[0] == ">":
        pfasta.pop(pos)
    
pnewfasta = [x[:-1] for x in pfasta]

from collections import Counter
pfastastr = ""
pfastastr = ''.join(pnewfasta)

pfastac = {}
pfastac = Counter(pfastastr)
print(pfastac)

with open("pfastacount.csv", "w") as output:
    output.write(str("aa, count \n"))
    for  aa, num in Counter(pfastastr).items():
        output.write(str(str(aa) + ", " + str(num) + "\n"))

fig2 = plt.figure(figsize=(15,5))
fig2 = plt.bar(pfastac.keys(), pfastac.values(), width=.5, color='g', align="center")


#example for archea kingdom: Halobacterium salinarum
apath = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/uniprot-reviewed_yes+organism__Halobacterium+salinarum+(HALSI)+[2242--.fasta"
afasta = []
anewfasta = []
with open(apath) as f:
    for line in f:
        afasta.append(line)

for pos, seq in enumerate(afasta):
    if seq[0] == ">":
        afasta.pop(pos)
    
anewfasta = [x[:-1] for x in afasta]

from collections import Counter
afastastr = ""
afastastr = ''.join(anewfasta)

afastac = {}
afastac = Counter(afastastr)
print(afastac)

with open("afastacount.csv", "w") as output:
    output.write(str("aa, count \n"))
    for  aa, num in Counter(afastastr).items():
        output.write(str(str(aa) + ", " + str(num) + "\n"))

fig3 = plt.figure(figsize=(15,5))
fig3 = plt.bar(afastac.keys(), afastac.values(), width=.5, color='g', align="center")

#example for bacteria kingdom: Thermus aquaticus
bpath = "/Users/anafink/OneDrive - bwedu/Bachelor MoBi/5. Fachsemester/Python Praktikum/uniprot-reviewed_yes+organism__Thermus+aquaticus+(THEAQ)+[271]_.fasta"
bfasta = []
bnewfasta = []
with open(bpath) as f:
    for line in f:
        bfasta.append(line)

for pos, seq in enumerate(bfasta):
    if seq[0] == ">":
        bfasta.pop(pos)
    
bnewfasta = [x[:-1] for x in bfasta]

from collections import Counter
bfastastr = ""
bfastastr = ''.join(bnewfasta)

bfastac = {}
bfastac = Counter(bfastastr)
print(bfastac)

fig4 = plt.figure(figsize=(15,5))
fig4 = plt.bar(bfastac.keys(), bfastac.values(), width=.5, color='g', align="center")

with open("bfastacount.csv", "w") as output:
    output.write(str("aa, count \n"))
    for  aa, num in Counter(bfastastr).items():
        output.write(str(str(aa) + ", " + str(num) + "\n"))




from matplotlib.backends.backend_pdf import PdfPages

aaking = PdfPages('Aa histograms of all kingdoms.pdf')
aaking.savefig(fig1)
aaking.savefig(fig2)
aaking.savefig(fig3)
aaking.savefig(fig4)
aaking.close()
