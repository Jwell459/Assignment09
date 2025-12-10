#!/usr/bin/env python3

# stockwell_assign5.py
# Author: James Stockwell
# Title: Provide a Laptop Market Analysis
# Date: 12/10/2025

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    laptop_df = pd.read_csv('laptops_cleaned.csv')

    # 1 - Clean the data
    laptop_df = laptop_df.rename(columns={"old_price": "normal_price"}) # Rename a column
    print("#1 - Data has been cleaned\n")

    # 2 - Number of brands
    brand_count = laptop_df["brand"].nunique()
    print("#2 - Number of Brands: ", brand_count, '\n')
    print()

    #3 - Names and Prices of the most and least expensive laptops
    expensive_index = laptop_df["normal_price"].idxmax()
    expensive_cost = laptop_df.loc[expensive_index, "normal_price"]
    expensive_name = laptop_df.loc[expensive_index, "laptop_name"]
    cheap_index = laptop_df["normal_price"].idxmin()
    cheap_cost = laptop_df.loc[cheap_index, "normal_price"]
    cheap_name = laptop_df.loc[cheap_index, "laptop_name"]
    
    print("#3 - The Most and Least Expensive Laptops:")
    print("Most Expensive: ", expensive_name, "at $", expensive_cost)
    print("Least Expensive: ", cheap_name, "at $", cheap_cost)
    print('\n')

    #4 - Laptop Price Distribution
    print("#4 - Laptop Price Distribution (Display Histogram)")
    laptop_df["normal_price"].plot(kind='hist', bins=10, title="Laptop Price Distribution")
    plt.show()
    print("Laptops are mostly sold on the cheaper " \
    "end ($1000 - $4000) with laptops becoming less and " \
    "less frequent as price increases.\n")

    #5 - Min, Max, and Mean Display Sizes
    display_min = laptop_df["display_size"].min()
    display_max = laptop_df["display_size"].max()
    display_mean = laptop_df["display_size"].mean()

    print("#5 - Min, Max, and Mean Display Sizes")
    print("Min :", display_min)
    print("Max :", display_max)
    print("Mean :", round(display_mean, 2))
    print('\n')

    #6 - Average Price by Brand
    print("#6 - Average Laptop Price of Each Brand")
    print(laptop_df.groupby("brand")["normal_price"].mean().round(2))
    print("Most brands are on the cheaper of end of $2000- $4000 " \
    "with a few a very high prices from $5000-$9000")
    print('\n')

    #7 - Average Price by Processor Brand
    print("#7 - Average Laptop Price of Each Processor Brand")
    print(laptop_df.groupby("processor_brand")["normal_price"].mean().round(2))
    print("Intel procesor laptops are roughly twice as expanesive on average" \
    "than those with AMD laptops")
    print('\n')

    #8 - Average Rating by Brand
    print("#8 - Average Laptop Rating of Each Brand")
    print(laptop_df.groupby("brand")["ratings"].mean().round(2))
    print("Rating averages are overall fairly low with the range being about 0.5 to 2.5." \
    "Maybe brand is not a good indicator of quality.")
    print('\n')

    #9 - Average Price by Graphics Card Brand
    print("#9 - Average Laptop Price of Each Graphics Card Brand")
    print(laptop_df.groupby("graphics_brand")["normal_price"].mean().round(2))
    print("Graphics card brand has huge effect on the price. " \
    "AMD and Intel were cheaper, but Radeon were incredibly expensive")
    print('\n')

    #10 - Number of Laptops with a Discount Price
    discount_count = (laptop_df["has_discount"] == True).sum()
    print("#10 - Number of laptops with a discount price: ", discount_count, "\n")

    #11 - Disk Space vs Price
    print("#11 - Disk Space vs Price (Barplot)")
    sns.barplot(data=laptop_df, x="disk_capacity_GB", y="normal_price")
    plt.show()
    print("Variability was pretty high. Disk space might not be a huge" \
    "factor when considering laptop price.")
    print('\n')

    #12 - Display Size vs Price
    print("#12 - Display Size vs Price (Barplot)")
    sns.barplot(data=laptop_df, x="display_size", y="normal_price")
    plt.show()
    print("Variability is also high. Display size might not be a major factor" \
    "when considering laptop price. ")
    print('\n')

    # Conclusion
    print("The laptop would indicate that the largest factors that contrinute to "
    "a laptop's price is its brand and its gpu brand. There is a large range of prices"
    "for laptops, but they are vastly more sold at the cheaper end of the spectrum. While "
    "there is a notable difference with the customer rating of various brands (Huawei and Apple" \
    "being the best) it is wise to consider other factors when picking a laptop as all brands "
    "rate on average below 3.")

if __name__ == "__main__":
    main()