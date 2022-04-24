from google.from google.cloud import bigquery



def bq(query):

    client = bigquery.Client()



    dataframe = (
        bqclient.query(query)
        .result()
        .to_dataframe(
            # Optionally, explicitly request to use the BigQuery Storage API. As of
            # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
            # API is used by default.
            create_bqstorage_client=True,
        )
    )

    return dataframe



