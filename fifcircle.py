import sys

findmajorScale = ["C", "G", "D", "A", "E", "B", "Fis", "Cis", "Gis", "Dis", "Bes", "F"]
findminorScale = ["A mi", "E mi", "B mi", "Fis mi", "Cis mi", "Gis mi", "Dis mi", "Bes mi", "F mi", "C mi", "G mi", "D mi"]
finddimisScale = ["B dim", "Fis dim", "Cis dim", "Gis dim", "Dis dim", "Bes dim", "F dim", "C dim", "G dim", "D dim", "A dim", "E dim"]

scales = {"scales": [{"name":"ionian",     "index":"majorSidx", "shift": 0}, 
                     {"name":"lydian",     "index":"majorSidx", "shift": 1},
                     {"name":"myxolidian", "index":"majorSidx", "shift": -1}, 
                     {"name":"aeonian",    "index":"minorSidx", "shift": 0}, 
                     {"name":"dorian",     "index":"minorSidx", "shift": 1}, 
                     {"name":"phrygian",   "index":"minorSidx", "shift": -1}, 
                     {"name":"locryan",    "index":"dimisSidx", "shift": 0} 
                    ]
         }

while True:
  tone = input("Enter scale name (C, G, D, A, E, B, F, Fis, Cis, Gis, Dis, Bes, k-end): ")
  if tone == 'k':
    sys.exit(0)
  if tone in findmajorScale:
    break

majorSidx = findmajorScale.index(tone)
minorSidx = findminorScale.index(tone + " mi")
dimisSidx = finddimisScale.index(tone + " dim")

for i in scales["scales"]:
  print (i["name"])
  idx = eval(i["index"]) + i["shift"]
  if idx > (len(findmajorScale) - 1):
    idx = 0
  if idx < 0:
    idx = len(findmajorScale) - 1


  ileft  = idx - 1
  iright = idx + 1

  if ileft > (len(findmajorScale) - 1):
    ileft = 0
  if ileft < 0:
    ileft = len(findmajorScale) - 1

  if iright > (len(findmajorScale) - 1):
    iright = 0
  if iright < 0:
    iright = len(findmajorScale) - 1
  
  print (f"Major:  {findmajorScale[ileft]} - {findmajorScale[idx]} - {findmajorScale[iright]}")
  print (f"Minor:  {findminorScale[ileft]} - {findminorScale[idx]} - {findminorScale[iright]}")
  print (f"Dimis:      - {finddimisScale[idx]} - ")
  

