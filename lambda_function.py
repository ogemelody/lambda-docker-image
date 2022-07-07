import json
import awswrangler as wr
import pandas as pd
from datetime import datetime
import urllib.parse

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']        #stores bucket name
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')   #stores the name of file uploaded
    destination = "d2b-internal-dev-melody-poc-output"
    
    date_of_entry = datetime.now()
    year = date_of_entry.year
    month = date_of_entry.month
    day = date_of_entry.day
    data = wr.s3.read_csv(path=f"s3://{bucket}/{key}", parse_dates=['date_of_visits'])
    data= data.rename(columns={'number_of_vists': 'number_of_visits'}, inplace=True)
    df= pd.DataFrame(data)
    output_filename = 'business_data.parquet'
    data_p = wr.s3.to_parquet(df=df, path=f"s3://{destination}/YEAR={year}/MONTH={month}/DAY={day}/{output_filename}")
