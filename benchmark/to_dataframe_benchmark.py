from google.cloud import bigquery
table = bigquery.TableReference.from_string('bigquery-public-data.new_york_taxi_trips.tlc_fhv_trips_2015')
client = bigquery.Client()
rows = client.list_rows(table)
#rows.to_dataframe(progress_bar_type='tqdm')
rows.to_dataframe()
