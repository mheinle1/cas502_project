def join_csv_files(file1, file2, key1='GEO_ID' , key2='GEOIDFQ', output_file= 'joined.csv'):
    # Load CSV files into Pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    # Perform the join
    merged_df = df1.merge(df2, left_on=key1, right_on=key2, how='inner')
    # Save to a new CSV file
    merged_df.to_csv(output_file, index=False)
    
join_csv_files(file1, r"C:\Users\zachh\Downloads\tl_2024_us_county\tl_2024_us_county.csv", key1='GEO_ID', key2='GEOIDFQ', output_file= joined.csv)
print(f"Join complete! Merged file saved as {output_file}")
