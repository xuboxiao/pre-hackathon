import requests

host = '0.0.0.0'
port = '8082'
base_url = 'http://' + host + ':' + port

client_data_1 = {
    'client_name': 'Alice',
    'industry_id': '1',
    'pwd': 'yes'
}

client_data_2 = {
    'client_name': 'Bob',
    'industry_id': '4',
    'pwd': 'yes2'
}

# RM2 on-boarded client1 Alice
requests.post(base_url+'/rm/2/my_clients', json=client_data_1)

# RM2 on-boarded client2 Bob
print(requests.post(base_url+'/rm/2/my_clients', json=client_data_2).content)
# response: b'{"client_id":2,"client_name":"Bob","industry_name":"Real Estate"}'

