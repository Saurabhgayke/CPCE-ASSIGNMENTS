# -*- coding: utf-8 -*-
"""ASSIGNMENT : 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qm0lAyZo3lFdOtpx1WAD0b0kck7Bxnla

ASSIGNMENT : 8

Application of Python in the field of Water Supply Engineering
"""

print("Name: Saurabh Shyam Gayke ; Class and Division: BE-A ; Batch : C ; Roll No 21CV313")
# To determine alkalinity of given sample
H2SO4_req = float(input("Enter the volume of H2SO4 required in ml:"))
Sample = float(input("Enter the value of sample in liters:"))

# Alkalinity Removed = H2SO4_req
Alkalinity_Removed = H2SO4_req
print("Alkalinity Removed:", Alkalinity_Removed, "mg")

Alk_mg_per_lit = Alkalinity_Removed / Sample
print("Total Alkalinity:", Alk_mg_per_lit, "mg/liter")

OH = float(input("Enter the value of OH-Alkalinity present:"))

# Alkalinity removed till pH of 8.3
H2SO4_req = float(input("Enter the volume of H2SO4 required in ml:"))

Alkalinity_Removed = H2SO4_req
print("Alkalinity Removed:", Alkalinity_Removed, "mg")

CO3_Combined = Alkalinity_Removed / Sample
print("Carbonate Alkalinity up to pH 8.3:", CO3_Combined, "mg/liter")

CO3 = CO3_Combined - OH
print("Carbonate Alkalinity:", CO3, "mg/liter")

HCO3 = Alk_mg_per_lit - 2 * CO3 - OH
print("Bicarbonate Alkalinity:", HCO3, "mg/liter")