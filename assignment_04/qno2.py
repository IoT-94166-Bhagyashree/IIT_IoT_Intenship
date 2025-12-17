
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.

def distance_converter(distance, conversion_type, func):
    result = func(distance)
    print(f"{distance} ({conversion_type.split(' to ')[0]}) = {result} ({conversion_type.split(' to ')[1]})")



distance = float(input("Enter distance: "))

print("\n--- Distance Conversions ---")
distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_converter(distance, "feet to inches", feet_to_inches)
distance_converter(distance, "inches to cm", inches_to_cm)
