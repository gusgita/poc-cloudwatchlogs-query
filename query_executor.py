from time import sleep

def execute_query(logs_client, start_date, end_date, logGroupName, queryString):  
    query = logs_client.start_query(
        logGroupName=logGroupName,
        startTime=start_date,
        endTime=end_date,
        queryString=queryString
    )

    query_id = query['queryId']

    while True:
        resp = logs_client.get_query_results(queryId=query_id)
        if resp['status'] in ['Complete', 'Unknown']:
            break
        sleep(10)

    return resp['results']
