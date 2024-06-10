# I convert 'body_weight' to number sort of stuff, 
data['body_weight'] = pd.to_numeric(data['body_weight'].str.extract('(\d+)', expand=False), errors='coerce')

# I group by 'oem' and calculate the mean weight
avg_weight_by_oem = data.groupby('oem')['body_weight'].mean().sort_values(ascending=False)

# I get the OEM with the highest average weight
highest_avg_weight_oem = avg_weight_by_oem.idxmax()
highest_avg_weight_oem, avg_weight_by_oem[highest_avg_weight_oem]

# I filter rows where 'launch_announced' and 'launch_status' are not NaN
data_filtered = data.dropna(subset=['launch_announced', 'launch_status'])

# I extract years from 'launch_announced' and 'launch_status'
data_filtered['announced_year'] = data_filtered['launch_announced'].str.extract('(\d{4})', expand=False).astype(int)
data_filtered['released_year'] = data_filtered['launch_status'].str.extract('(\d{4})', expand=False).astype(int)

# I filter phones announced in one year and released in another
phones_different_year = data_filtered[data_filtered['announced_year'] != data_filtered['released_year']]
phones_different_year = phones_different_year[['oem', 'model']]
phones_different_year_list = phones_different_year.values.tolist()
phones_different_year_list

# Count the number of sensors for each phone
data['num_sensors'] = data['features_sensors'].str.split(',').apply(len)

# Filter phones with only one sensor
phones_one_sensor = data[data['num_sensors'] == 1].shape[0]
phones_one_sensor

# Extract year from 'launch_announced'
data['announced_year'] = data['launch_announced'].str.extract('(\d{4})', expand=False).astype(int)

# Filter data for years in the 2000s
data_2000s = data[(data['announced_year'] >= 2000) & (data['announced_year'] < 2010)]

# Count the number of phones launched each year
phones_by_year = data_2000s['announced_year'].value_counts()

# Get the year with the most launches
most_launches_year = phones_by_year.idxmax()
most_launches_year, phones_by_year[most_launches_year]

