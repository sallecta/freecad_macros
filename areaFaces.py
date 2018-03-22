#print(repr(round(Gui.Selection.getSelectionEx()[0].SubObjects[0].Area/1000000,2)))
# area = 0
# area = area + Gui.Selection.getSelectionEx()[0].SubObjects[0].Area/1000000
##
area = 0
for selObj in Gui.Selection.getSelectionEx():
    for face in selObj.SubObjects:
        area = area + face.Area
print("area = " + repr(area/1000000) + " m2"
