import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?

paid = df[df['Type'] == "Paid"]
min_price = paid['Price'].min()

print(min_price)
# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?

art = df[df["Category"] == "ART_AND_DESIGN"]
art_installs = art['Installs'].median()
print(round(art_installs))

# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
free = df[df['Type'] == "Free"]
max_free = free["Reviews"].max()
max_paid = paid["Reviews"].max()
print( max_free-max_paid)

# result = round(numberA)
# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?


# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
