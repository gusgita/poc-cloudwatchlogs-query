from datetime import datetime, timedelta
import boto3

from config_reader import read_config

logs_client = boto3.client('logs')
configs = read_config()
print(configs)

end_date = round((datetime.utcnow() - timedelta(seconds=1)).timestamp())
start_date = round((datetime.utcnow() - timedelta(hours=float(configs.window))).timestamp())

query = logs_client.start_query(
    logGroupName=configs.log_group_name,
    startTime=start_date,
    endTime=end_date,
    queryString=configs.query_string
)

query_id = query['queryId']

resp = logs_client.get_query_results(queryId=query_id)
print(resp['results'])