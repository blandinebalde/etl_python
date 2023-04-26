from google.cloud import bigquery


client = bigquery.Client('blandine-384809')

sql = "select * from sample_dataset.movies_rating limit 10"

query_job = client.query(sql)

results = query_job.result()

for r in results:
    print(r.year, r.title, r.genre, r.avg_vote)













