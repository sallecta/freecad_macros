length = 0
for selObj in Gui.Selection.getSelectionEx():
    for edge in selObj.SubObjects:
        length = length + edge.Length
print("length = " + repr(length) + " mm")
