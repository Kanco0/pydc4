import pandas as pd
import os 

c_dir = os.path.dirname(os.path.abspath(__file__))


churn_path = os.path.join(c_dir, 'telecom_customer_churn.csv')
pop_path = os.path.join(c_dir, 'telecom_zipcode_population.csv')

df_churn = pd.read_csv(churn_path)
df_pop = pd.read_csv(pop_path)

print("---Churn---")
print(df_churn.columns.tolist())

print("---Population---")
print(df_pop.columns.tolist())

df_final = pd.merge(df_churn, df_pop, on='Zip Code', how='left')

print(f"total columns: {len(df_final.columns)}")
print("-" * 30)
print(" 'Population' exists?", 'Population' in df_final.columns)
missing_data = df_final.isnull().sum()
print(missing_data[missing_data > 0])
print("--- Dataset Info ---")
df_final.info()
missing_cols = df_final.columns[df_final.isnull().any()]
print("\n--- Data types of columns with missing values ---")
print(df_final[missing_cols].dtypes)
print("Unique values in 'Offer':")
print(df_final['Offer'].unique())

print("\nUnique values in 'Churn Category':")
print(df_final['Churn Category'].unique())
print(df_final.groupby('Customer Status')['Churn Category'].apply(lambda x: x.isnull().sum()))

df_final['Churn Category'] = df_final['Churn Category'].fillna('None')
df_final['Churn Reason'] = df_final['Churn Reason'].fillna('None')

print("Churn Category unique values after filling:")
print(df_final['Churn Category'].unique())

df_final['Offer'] = df_final['Offer'].fillna('No Offer')

df_final['Avg Monthly GB Download'] = df_final['Avg Monthly GB Download'].fillna(0)
df_final['Avg Monthly Long Distance Charges'] = df_final['Avg Monthly Long Distance Charges'].fillna(0)


total_missing = df_final.isnull().sum().sum()

if total_missing == 0:
    print("Congratulations! The dataset is 100% clean. No missing values left.")
else:
    print(f"There are still {total_missing} missing values. Let's find them!")
    print(df_final.isnull().sum()[df_final.isnull().sum() > 0])


internet_cols = [
    'Internet Type', 'Online Security', 'Online Backup', 
    'Device Protection Plan', 'Premium Tech Support', 
    'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data'
]

for col in internet_cols:
    df_final[col] = df_final[col].fillna('No Internet Service')

df_final['Multiple Lines'] = df_final['Multiple Lines'].fillna('No Phone Service')

print("Remaining missing values:")
print(df_final.isnull().sum().sum())
print("Unique values in 'Offer' column:")
print(df_final['Offer'].unique())

print("\nCounts for each Offer type:")
print(df_final['Offer'].value_counts())

print(df_final.columns.tolist())
important_categorical_cols = [
    'Gender', 'Married', 'City', 'Offer', 'Phone Service', 
    'Multiple Lines', 'Internet Service', 'Internet Type', 
    'Contract', 'Paperless Billing', 'Payment Method', 'Customer Status'
]

print("--- Spelling & Consistency Check ---")
for col in important_categorical_cols:
    print(f"Column: {col}")
    print(df_final[col].unique())
    print("-" * 30)

output_path = os.path.join(c_dir, 'telecom_customer_churn_CLEAN.csv')

df_final.to_csv(output_path, index=False)

print(f"Done! Cleaned data saved at: {output_path}")