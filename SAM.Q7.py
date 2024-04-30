# NAME: REPUDI SAMUEL HONEY
# USN: 22BTRCL126

import pandas as pd

housing_data = pd.read_csv("housing.csv")
census_data = pd.read_csv("modified_file.csv")

relevant_columns = [
    "District Name",
    "Rural/Urban",
    "Total Number of households",
    "Total Number of Livable",
    "Total Number of Dilapidated",
    "Latrine_premise"
]

relevant_data = housing_data[relevant_columns]

print(relevant_data.head())


merged_data = pd.merge(housing_data, census_data, on="District Name")


merged_data['Absolute Dilapidated'] = merged_data['Total Number of households'] * merged_data['Total Number of Dilapidated'] / 100
merged_data['Absolute Latrine_premise'] = merged_data['Total Number of households'] * merged_data['Latrine_premise'] / 100

relevant_columns = [
    "District Name",
    "Rural/Urban",
    "Absolute Dilapidated",
    "Absolute Latrine_premise"
]


print(merged_data[relevant_columns].head())
