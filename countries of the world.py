import pandas as pd
import matplotlib.pyplot as plt


file_path = 'countries of the world.csv'
df = pd.read_csv(file_path, encoding='latin1')

df.columns = ['Country', 'Region', 'Population', 'Area', 'Density', 'Coastline', 'Net migration',
              'Infant mortality', 'GDP', 'Literacy', 'Phones', 'Arable', 'Crops', 'Other', 'Climate',
              'Birthrate', 'Deathrate', 'Agriculture', 'Industry', 'Service']
columns_to_convert = ['Population', 'Net migration', 'GDP', 'Literacy', 'Phones']

for column in columns_to_convert:
    if df[column].dtype == object: 
        df[column] = pd.to_numeric(df[column].str.replace(',', ''), errors='coerce')


countries = df['Country'][:10]  
population = df['Population'][:10]
net_migration = df['Net migration'][:10]
gdp = df['GDP'][:10]
literacy = df['Literacy'][:10]
phones = df['Phones'][:10]


fig, axes = plt.subplots(3, 2, figsize=(15, 20))
fig.suptitle('Факторы, влияющие на качество жизни населения', fontsize=16)

axes[0, 0].bar(countries, population, color='skyblue')
axes[0, 0].set_title('Численность населения')
axes[0, 0].set_xticklabels(countries, rotation=90)

axes[0, 1].bar(countries, net_migration, color='salmon')
axes[0, 1].set_title('Уровень миграции')
axes[0, 1].set_xticklabels(countries, rotation=90)

axes[1, 0].bar(countries, gdp, color='lightgreen')
axes[1, 0].set_title('Показатель ВВП')
axes[1, 0].set_xticklabels(countries, rotation=90)

axes[1, 1].bar(countries, literacy, color='lightcoral')
axes[1, 1].set_title('Уровень грамотности')
axes[1, 1].set_xticklabels(countries, rotation=90)

axes[2, 0].bar(countries, phones, color='gold')
axes[2, 0].set_title('Количество телефонов')
axes[2, 0].set_xticklabels(countries, rotation=90)


fig.delaxes(axes[2, 1])

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
