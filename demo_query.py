from datetime import datetime, timedelta
from time import sleep
import boto3

from config_reader import read_config
from query_executor import execute_query

logs_client = boto3.client('logs')
configs = read_config()

# it looks like in the background, the library will automaticaly convert localtime into UTC
# therefore this should be in local time. if we set as utc time then it will be reduced again by timezone delta.
end_date = round((datetime.now() - timedelta(seconds=1)).timestamp())
start_date = round((datetime.now() - timedelta(hours=float(configs.window))).timestamp())

print(execute_query(logs_client, start_date, end_date, configs.log_group_name, configs.query_string))
