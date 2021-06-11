import requests

'''
Makes a request to an API endpoint
Takes authorization header if needed
'''

url = "http://127.0.0.1:8000/api/test"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'token' # Specify an access token if needed
}

response = requests.request("GET", url, headers=headers, data=payload)

print('Status: {}'.format(response.status_code))
print(response)
