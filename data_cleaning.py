import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')

# Виведи інформацію про всі DataFrame, щоб дізнатися, які стовпці потребують очищення
# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?
df.info()

null_apps = df[pd.isnull(df["Rating"])]
print(len(null_apps))
# Заміни порожнє значення ('NaN') рейтингу ('Rating') для таких програм на -1.
df['Rating'].fillna(-1, inplace=True)
# Визнач, яке ще значення розміру ('Size') зберігається в датасеті крім Кілобайтів та Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.
print(df['Size'].value_counts())

def clean_size(size):
    if size[-1] == "M":
        return float(size[:-1])
    elif size[-1] == "k": 
        return float(size[:-1]) / 1024
    return -1

df['Size'] = df['Size'].apply(clean_size)
df.info()
# Чому дорівнює максимальний розмір ('Size') додатків з категорії ('Category') 'TOOLS'?
tools  = df[df['Category']=='TOOLS']
print(tools['Size'].max())
# Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').

def clean_installs(installs):
    if installs[-1] == "+":
        string = installs[:-1].replace(",", "")
        return int(string)
    else:
        return 0
    
df['Installs'] = df['Installs'].apply(clean_installs)
df.info()
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто, якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000

# Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди клітинку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї клітинки?

# У якої програми не вказаний тип ('Type')? Який тип там потрібно записати залежно від ціни?

# Виведи інформацію про все DataFrame, щоб переконатися, що очищення пройшло успішно

def clean_price(size):
    if size[0] == "$":
        return float(size[1:])
    return 0

df['Price'] = df['Price'].apply(clean_price)

df['Profit'] = df['Installs'] * df['Price']

def create_month(date):
    if date != '':
        month = date.split()[0]
        return month
    else:
        return ''

df['Month'] = df['Last Updated'].apply(create_month)
df.to_csv("cleaned.csv", index=False)
