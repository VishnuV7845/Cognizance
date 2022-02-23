list=[[1, "Abc", 90],
   [2, "Def", 95],
   [3, "Ghi", 85]]

print ("{:<8} {:<8} {:<8}".format('Roll No','Name','Marks'))
for header in list:
    Roll, name, marks = header
    print ("{:<8} {:<8} {:<8}".format( Roll, name, marks))