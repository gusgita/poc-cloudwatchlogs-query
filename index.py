from datetime import datetime, timedelta
from time import sleep
import boto3

from config_reader import read_config

logs_client = boto3.client('logs')
configs = read_config()

# it looks like in the background, the library will automaticaly convert localtime into UTC
# therefore this should be in local time. if we set as utc time then it will be reduced again by timezone delta.
end_date = round((datetime.now() - timedelta(seconds=1)).timestamp())
start_date = round((datetime.now() - timedelta(hours=float(configs.window))).timestamp())

query = logs_client.start_query(
    logGroupName=configs.log_group_name,
    startTime=start_date,
    endTime=end_date,
    queryString=configs.query_string
)

query_id = query['queryId']

while True:
    resp = logs_client.get_query_results(queryId=query_id)
    if resp['status'] in ['Complete', 'Unknown']:
        break
    sleep(10)

print(resp['results'])