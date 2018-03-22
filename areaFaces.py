#print(repr(round(Gui.Selection.getSelectionEx()[0].SubObjects[0].Area/1000000,2)))
# area = 0
# area = area + Gui.Selection.getSelectionEx()[0].SubObjects[0].Area/1000000
##
area = 0
for face in Gui.Selection.getSelectionEx()[0].SubObjects:
    area = area + face.Area
print("area = " + repr(area/1000000) + " m2")
