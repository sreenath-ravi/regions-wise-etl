import pandas as pd
import json

def parse_promotion_discount(discount):
    try:
        discount_data = json.loads(discount)
        return discount_data.get("CurrencyCode", ""), float(discount_data.get("Amount", 0))
    except json.JSONDecodeError:
        return "", 0.0

def transform_data(df_a, df_b):
  
    df_a['Region'] = 'A'
    df_b['Region'] = 'B'
    print(df_a)
    print(df_b)


    combined_df = pd.concat([df_a, df_b], ignore_index=True)




    combined_df['TotalSales'] = combined_df['QuantityOrdered'] * combined_df['ItemPrice']
    combined_df[["CurrencyCode", "PromotionDiscountAmount"]] = combined_df["PromotionDiscount"].apply(parse_promotion_discount).apply(pd.Series)
  
 
    combined_df['NetSales'] = combined_df['TotalSales'] - combined_df['PromotionDiscountAmount']


    combined_df = combined_df.groupby('Region').apply(lambda x: x.drop_duplicates(subset=['OrderId']))

    combined_df = combined_df[combined_df['NetSales'] > 0]
    combined_df['ID'] = combined_df['OrderId'] + '-' + combined_df['Region']

    cols = ['ID'] + [col for col in combined_df.columns if col != 'ID']
    combined_df = combined_df[cols]
    print(combined_df)
    return combined_df
