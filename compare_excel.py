import pandas as pd

file1 = "file1.xlsx"  # Replace with the path to the first Excel file
file2 = "file2.xlsx"  # Replace with the path to the second Excel file
parameter_limit = 0.05 # match rows within ±5%

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Function to check if a row matches within parameter limit.  Three columns are age, weight and gait
def is_match(row1, row2):
    return (
        abs(row1['age'] - row2['age']) <= parameter_limit * row1['age'] and
        abs(row1['weight'] - row2['weight']) <= parameter_limit * row1['weight'] and
        abs(row1['gait'] - row2['gait']) <= parameter_limit * row1['gait']
    )

# Find matches from df1 in df2
matches = []
for _, row1 in df1.iterrows():
    for _, row2 in df2.iterrows():
        if is_match(row1, row2):
            matches.append(row1)

# Convert matches to a DataFrame
matches_df = pd.DataFrame(matches)

# Save the matching rows to an Excel file
output_file = "matches.xlsx"
matches_df.to_excel(output_file, index=False)

print(f"Matching rows saved to {output_file}")
