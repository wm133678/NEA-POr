import requests


def run_query(query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': 'YOUR API KEY'}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


query = """
query{
  bitcoin{
    blocks{
      count
    }
   }
}
"""
result = run_query(query)  # Execute the query
print("'Result - {}'.format(result)")
