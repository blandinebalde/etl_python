from google.cloud import bigquery
import os

client = bigquery.Client(project='blandine-384809')
target_table = 'blandine-384809.sample_dataset.city_housing'

sql = "select * from sample_dataset.movies_rating limit 10"

#WRITE_APPEN load the data whithout deleting initial data from the table it kinda just add it
#Write_truncate
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

cur_path = os.getcwd()
file = 'city_housing.csv'
file_path = os.path.join(cur_path, 'files', file)
#print(file_path)
#rb is read binary mode , in this methode we read the file
with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        target_table,
        job_config=job_config)

load_job.result()

destination_table = client.get_table(target_table)
print(f'you have {destination_table.num_rows} rows in your table')















