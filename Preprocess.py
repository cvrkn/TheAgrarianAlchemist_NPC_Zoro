import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv("Crop_Data.csv")

# Drop unnecessary columns
df.drop(columns=["State", "Area"], inplace=True)

# Encode categorical columns (convert categories into numbers)
category_mappings = {
    "Soil Type": {"Alluvial Soil": 0, "Black Soil": 1, "Laterile Soil": 2, "Red/Yellow Soil": 3},
    "Pesticide Usage": {"Low": 0, "Average": 1, "High": 2},
    "pH": {"Low": 0, "Average": 1, "High": 2},
    "Temperature": {"Low": 0, "Medium": 1, "High": 2},
    "Fertilizer Usage": {"Low": 0, "Medium": 1, "High": 2}
}

for column, mapping in category_mappings.items():
    df[column] = df[column].map(mapping)

# Normalize numerical columns
numerical_columns = ["Price", "Rainfall"]
scaler = MinMaxScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save processed data
df.to_csv("Processed_Crop_Data.csv", index=False)

print("Preprocessing complete! Data saved as 'Processed_Crop_Data.csv'")
