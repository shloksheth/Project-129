import pandas as pd

df2 = pd.read_csv("bright_stars.csv")
df1 = pd.read_csv("brown_dwarf_stars.csv")

df1.fillna(' ', inplace=True)

for index, mass_val in enumerate(df1["Mass"]):
    df1.at[index, 'Mass'] = float(mass_val)
    df1.at[index, 'Mass'] = mass_val * 0.000954588

for index, dis_val in enumerate(df1["Distance"]):
    df1.at[index, 'Distance'] = float(dis_val)

for index, dis_val2 in enumerate(df2["Distance"]):
    df2.at[index, 'Distance'] = float(dis_val2.replace(',', ''))

for index, dis_val2 in enumerate(df2["Mass"]):
    df2.at[index, 'Mass'] = float(dis_val2)

for index, dis_val2 in enumerate(df2["Radius"]):
    if isinstance(dis_val2, str):
        df2.at[index, 'Radius'] = float(dis_val2.replace(',', ''))

for index, rad_val in enumerate(df1["Radius"]):
    if str(rad_val).strip():
        df1.at[index, 'Radius'] = float(rad_val) * 0.102763

print("df1:")
print(df1)
print("\ndf2:")
print(df2)

headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]

print(df3)