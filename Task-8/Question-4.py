#Thi program capitalises the first letters of each element in a series.
import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])

output = ser.str.capitalize()
print("Series with first letter of each element capitalised in index form:\n", output)

print("\nAs a sentence,")
for i in ser:
    print(i.capitalize(),end=' ')
