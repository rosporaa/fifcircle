import sys

majorScale = ["C", "G", "D", "A", "E", "B", "Fis", "Cis", "Gis", "Dis", "Bes", "F"]  #0
minorScale = ["A mi", "E mi", "B mi", "Fis mi", "Cis mi", "Gis mi", "Dis mi", "Bes mi", "F mi", "C mi", "G mi", "D mi"]             #1
dimisScale = ["B dim", "Fis dim", "Cis dim", "Gis dim", "Dis dim", "Bes dim", "F dim", "C dim", "G dim", "D dim", "A dim", "E dim"] #2

# v ktorej o kolko
#major
ionian = [0,0] # v major o nula posun
lydian = [0,1]
myxoltdian = [0,-1]
#minor
aeolian = [1, 0]
dorian = [1, 1]
phrygian = [1, -1]
#dimished
locryan = [2, 0]

while True:
  tone = input("Enter scale name (C, G, D, A, E, B, F, Fis, Cis, Gis, Dis, Bes, k-koniec): ")
  if tone == 'k':
    sys.exit(0)
  if tone in majorScale:
    break

majorSidx = majorScale.index(tone)
minorSidx = minorScale.index(tone + " mi")
dimisSidx = dimisScale.index(tone + " dim")

print (f"{majorScale[majorSidx]}, {minorScale[minorSidx]}, {dimisScale[dimisSidx]}")


