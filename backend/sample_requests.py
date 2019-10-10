import requests

host = '0.0.0.0'
port = '8082'
base_url = 'http://' + host + ':' + port


# ---------------------------- client data api ----------------------
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
requests.post(base_url+'/rm/2/my_clients', json=client_data_2)
# response: {"client_id":2,"client_name":"Bob","industry_name":"Real Estate"}

# display all clients of RM2
requests.get(base_url+'/rm/2/my_clients')
# response: [{"client_id":1,"client_name":"Alice","industry_name":"Environmental Services and Recycling"},{"client_id":2,"client_name":"Bob","industry_name":"Real Estate"}]


# --------------------------- trade data api -------------------------
trade_data_1 = {
    'product_id': 1,
    'units_traded': 100,
    'trade_type': 'buy'
}

trade_data_2 = {
    'product_id': 1,
    'units_traded': 100,
    'trade_type': 'sell'
}

trade_data_3 = {
    'product_id': 4,
    'units_traded': 100,
    'trade_type': 'buy'
}

# client1 buys 100 shares of product1
requests.post(base_url+'/client/1/trade', json=trade_data_1)
# response: {"holding_id":1,"client_name":"Alice","product_name":"Tox free solutions","units_held":100.0,"daily_credit_award":100.0}

# client1 buys 100 shares of product1 again
requests.post(base_url+'/client/1/trade', json=trade_data_1)
# response: {"holding_id":1,"client_name":"Alice","product_name":"Tox free solutions","units_held":200.0,"daily_credit_award":200.0}

# client1 sells 100 shares of product1
requests.post(base_url+'/client/1/trade', json=trade_data_2)

# client2 buys 100 shares of product4
requests.post(base_url+'/client/2/trade', json=trade_data_3)