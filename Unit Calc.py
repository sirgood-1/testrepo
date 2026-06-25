# Temp Conversion

unit = input("Is this Temp in cel or Frht? (C/F): ")
temp = float(input("Enter the temp: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
elif unit == "F":
    pass
else:
    print(f"{unit} is an invalid unit of msmnt")
