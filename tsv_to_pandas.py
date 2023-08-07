import pandas as pd

file_path = './data/avia_pana.tsv'

df = pd.read_csv(file_path, sep='\t')

# split the first column into multiple columns
df[['unit', 'tra_meas', 'rep_airp_time']] = df[df.columns[0]].str.split(',', expand=True)

# delete the original column
df = df.drop(df.columns[0], axis=1)

# filter the data
df_filtered = df[df['rep_airp_time'].str.startswith('PL_')]

# get the list of all column names
cols = list(df_filtered.columns)

# remove the columns 'unit', 'tra_meas', and 'rep_airp_time'
cols.remove('unit')
cols.remove('tra_meas')
cols.remove('rep_airp_time')

# rearrange the columns
df_filtered = df_filtered[['unit', 'tra_meas', 'rep_airp_time'] + cols]
print(df_filtered)