
conversions = [
    lambda t: t * 1000,            # tonnes to kilograms
    lambda kg: kg * 1000,           # kilograms to grams
    lambda g: g * 1000,             # grams to milligrams
    lambda mg: mg * 0.00000220462   # milligrams to pounds
]


tonnes = float(input("Enter weight in tonnes: "))


kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print("\nConverted weights:")
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
