import pandas as pd 
import numpy as np
data = pd.read_csv('practice/products.csv')
print(data)
print("Starting 5 rows")
print(data.head())
print("Ending 5 rows")
print(data.tail())
print("Shape of the data:", data.shape)
print("Columns in the data:", data.columns)
print("Data types:", data.dtypes)
print("Summary:",data.info())
print("Descriptive Statistics:", data.describe())


print("Average Price:", data['CostPrice'].mean())
print("Maximum Price:", data['CostPrice'].max())
print("Minimum Price:", data['CostPrice'].min())
print("Total Cost Price:", data['CostPrice'].sum())

data_sorted = data.sort_values(by='CostPrice', ascending=True)
print("Data sorted by CostPrice:")
print(data_sorted)

print("Null values in each column:")
print(data.isnull().sum())

unit_price = data["UnitPrice"].to_numpy()
cost_price = data["CostPrice"].to_numpy()
units_sold = data["UnitsSold"].to_numpy()
stock_qty = data["StockQuantity"].to_numpy()
ratings = data["Rating"].to_numpy()
categories = data["Category"].to_numpy()

profit_per_unit = unit_price - cost_price
print("Profit per unit for each product:")
print(profit_per_unit)

total_profit = profit_per_unit * units_sold
print("Total profit for each product:")
print(total_profit)

reversed_ratings = ratings[::-1]
print("Reversed ratings:", reversed_ratings)

#UNIQUE CATEGORIES AND MOST FREQUENT CATEGORY
unique_cats, counts_cats = np.unique(categories, return_counts=True)
most_frequent_cat = unique_cats[np.argmax(counts_cats)]
print("Most frequent category:", most_frequent_cat)
indices = np.where(categories == most_frequent_cat)[0]
print("Indices of products in the most frequent category:", indices)

high_rating_mask = ratings > 4.5
high_rated_prices = unit_price[high_rating_mask]
print(high_rating_mask)
print("Prices of products rated above 4.5:", high_rated_prices)
print("Count of highly-rated products:", np.sum(high_rating_mask))

updated_data = data.copy()
updated_data['ProfitPerUnit'] = profit_per_unit
updated_data['TotalProfit'] = total_profit
updated_data.to_csv('practice/updated_products.csv', index=False)
print("Updated Data with Profit columns:", updated_data.head())


sales_grid = units_sold.reshape(6, 5)
print("Sales grid (6 rows, 5 columns):", sales_grid)
print("Total sales across all products:", np.sum(sales_grid))
print("Mean sales:", np.mean(sales_grid))
print("Max units sold:", np.max(sales_grid))

print("Total sales per column (axis 0):", np.sum(sales_grid, axis=0))
print("Total sales per row (axis 1):", np.sum(sales_grid, axis=1))

max_pos = np.unravel_index(np.argmax(sales_grid), sales_grid.shape)
print("Row & Column index of highest sales item:", max_pos)

def calculate_financial_metrics(data) :
    df_out = pd.DataFrame()
    df_out["ProfitPerUnit"] = (updated_data["UnitPrice"] - updated_data["CostPrice"]).round(2)
    df_out["ProfitMargin%"] = ((updated_data["ProfitPerUnit"] / updated_data["UnitPrice"]) * 100).round(2)
    df_out["TotalRevenue"] = (updated_data["UnitPrice"] * updated_data["UnitsSold"]).round(2)
    df_out["TotalProfit"] = (updated_data["ProfitPerUnit"] * updated_data["UnitsSold"]).round(2)
    return df_out

df_out = calculate_financial_metrics(data)
print("Financial metrics:", df_out.head())
df_out.to_csv('practice/financial_metrics.csv', index=False)