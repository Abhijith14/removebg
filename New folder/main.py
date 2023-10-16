import pandas as pd


df = pd.read_excel('mail.xlsx')


# Initialize new columns
new_columns = ['CLC', 'Stage', 'Cat']
column_counter = 1

# Iterate over each row and combine values for each student
for index, row in df.iterrows():
    clc_column = f'CLC{column_counter}'
    stage_column = f'Stage{column_counter}'
    cat_column = f'Cat{column_counter}'
    
    # Combine values for the current student
    clc_values = df.loc[df['Student Name'] == row['Student Name'], 'Choose your Items in Cultural and Literary Competitions']
    stage_values = df.loc[df['Student Name'] == row['Student Name'], 'On-Stage/Off-Stage']
    cat_values = df.loc[df['Student Name'] == row['Student Name'], 'Cat']
    
     # Assign the combined values to the new columns
    df.at[index, clc_column] = ', '.join(clc_values)
    df.at[index, stage_column] = ', '.join(stage_values)
    df.at[index, cat_column] = ', '.join(cat_values)
    
    # Increase the column counter for the next set of columns
    column_counter += 1


# Drop duplicates based on 'Student Name' column and keep the first occurrence
# df = df.drop_duplicates(subset='Student Name', keep='first')

# Drop the original columns that are no longer needed
# df.drop(['Choose your Items in Cultural and Literary Competitions', 'On-Stage/Off-Stage', 'Cat'], axis=1, inplace=True)

# Save the modified DataFrame to a new Excel file
# df.to_excel('output_file.xlsx', index=False)

print(df)