import sys

findmajorScale = ["C", "G", "D", "A", "E", "H", "Fis", "Cis", "Gis", "Dis", "B", "F"]
findminorScale = ["A mi", "E mi", "H mi", "Fis mi", "Cis mi", "Gis mi", "Dis mi", "B mi", "F mi", "C mi", "G mi", "D mi"]
finddimisScale = ["H dim", "Fis dim", "Cis dim", "Gis dim", "Dis dim", "B dim", "F dim", "C dim", "G dim", "D dim", "A dim", "E dim"]

scales = {"scales": [{"name":"Ionian",     "index":"majorSidx", "shift": 0}, 
                     {"name":"Lydian",     "index":"majorSidx", "shift": 1},
                     {"name":"Myxolydian", "index":"majorSidx", "shift": -1}, 
                     {"name":"Aeonian",    "index":"minorSidx", "shift": 0}, 
                     {"name":"Dorian",     "index":"minorSidx", "shift": 1}, 
                     {"name":"Phrygian",   "index":"minorSidx", "shift": -1}, 
                     {"name":"Locryan",    "index":"dimisSidx", "shift": 0} 
                    ]
         }

while True:
  tone = input("Enter scale name (" + ', '.join(findmajorScale) + ", k-end): ")
  if tone == 'k':
    sys.exit(0)
  if tone in findmajorScale:
    break

majorSidx = findmajorScale.index(tone)
minorSidx = findminorScale.index(tone + " mi")
dimisSidx = finddimisScale.index(tone + " dim")

print (f"\n@@@ Scale {tone} @@@")
for i in scales["scales"]:
  print (f"\n@ {i['name']}: \n ---------------")
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
  
  print (f"  Major:  {findmajorScale[ileft]:6}   {findmajorScale[idx]:6}   {findmajorScale[iright]:6}")
  print (f"  Minor:  {findminorScale[ileft]:6}   {findminorScale[idx]:6}   {findminorScale[iright]:6}")
  print (f"  Dimis:           {finddimisScale[idx]:6}")


