import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
k_apps = df['Category'].value_counts()

print(k_apps['BUSINESS'])
# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.

# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.

rating = df.groupby(by='Type')['Rating'].mean()
paid =rating['Paid']
#4.25
# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.
free =rating['Free']
result = round(paid-free,2)
print(result)
#0.00


# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?

# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?

