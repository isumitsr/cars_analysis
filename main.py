import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('cars_2010_2020.csv')

def rename_add_id(df):
    df.columns = df.columns.str.replace(' ','_').str.lower()
    if 'car_id' not in df.columns:
        df.insert(0, 'car_id', range(1, len(df) + 1))
    return df
    
rename_add_id(df)

# Unique no of models for each make/ company
model_counts = df.groupby('make')['model'].nunique().reset_index()
model_counts.columns=["make/company", "model"]
#model_counts

#how many unique fuel type models for each make?
fuel_type_count = df.groupby(['make','fuel_type']).size().unstack(fill_value = 0).reset_index()
fuel_type_count.columns = ["company", "Diesel", "Electric", "Hybrid", "Petrol"]
#fuel_type_count

df_2020 = df[(df['year'] == 2020 )]
df_price_count = df_2020.groupby(["make","model"]).agg(total_price = ("price_(usd)", "sum"), count=("model","size")).reset_index()
dominating_model = df_price_count.loc[df_price_count.groupby("make")["total_price"].idxmax()]

sns.set_style('darkgrid')
sns.set_theme(rc={'figure.figsize':(10.7,8.27)})
sns.barplot( x = 'make', y= 'total_price', data = dominating_model)

plt.savefig("dominating_cars.pdf", format='pdf')
