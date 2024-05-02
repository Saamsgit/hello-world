# name: visvajit Velan.R
# USN: 22btrcl170

import pandas as pd


# Reading the csv file
df = pd.read_csv("government_hospitals.csv", skiprows=2)
print(df)



# Define the new column names
new_column_names = ['State/UT', 'Rural_Government_Hospitals', 'Rural_Government_Beds',
                    'Urban_Government_Hospitals', 'Urban_Government_Beds', 'Last_Updated']

# Assign the new column names to the DataFrame
df.columns = new_column_names

# Save the DataFrame with updated column names to a new CSV file
df.to_csv('updated_government_hospitals.csv', index=False)
