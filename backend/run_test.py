import my_test
import models
import service
import datetime

data = my_test.TestData()

'''

models.ClientWalletModel().create(data.wallet)
models.ClientModel().create(data.client)
print(service.ClientWalletService().get_wallet_data(1000))
print(service.ClientService().new_client(data.client))
print(service.ClientService().get_clients(2))
print(service.ClientService().check_credentials({'client_id': 1, 'pwd': 'no'}))
print(service.RMService().check_rm_credentials({'rm_email': 'RM1@db.com', 'pwd': 'xx'}))
'''

'''
print(
    service.TransactionService().new_transaction(
        {
            'product_id': 1,
            'units_traded': 100,
            'trade_type': 'sell',
            'time_stamp': datetime.datetime.now(),
            'client_id':1
        }
    )
)
'''

print(service.TransactionService().get_trade_history(1))



# print(service.TransactionService().is_in_holdings(1, 2))

# print(2 in models.HoldingsModel().get_by_client_id(1).loc[:, 'product_id'].unique())

# print(models.HoldingsModel().list_items().to_json())
# print(models.HoldingsModel().get_by_client_id(1).loc[:, 'product_id'])


