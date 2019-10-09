import my_test
import models
import service

data = my_test.TestData()

'''

models.ClientWalletModel().create(data.wallet)
models.ClientModel().create(data.client)
print(service.ClientWalletService().get_wallet_data(1000))
print(service.ClientService().new_client(data.client))

'''

print(service.ClientService().get_clients(2))

