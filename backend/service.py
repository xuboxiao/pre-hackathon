import models
import pandas as pd
import datetime


class ClientWalletService:
    def __init__(self):
        self.model = models.ClientWalletModel()

    def get_wallet_data(self, client_id):
        result = self.model.get_by_client_id(client_id);
        #return result.to_json(orient='records')
        return result. \
            loc[result['date_updated'].idxmax(),
                ['total_daily_credit_award', 'total_credit']] \
            .to_json()

    def daily_record(self):
        pass



class ClientService:
    def __init__(self):
        self.model = models.ClientModel()

    def new_client(self, params):
        result = self.model.create(params).loc[0]
        wallet_init_data = {
            'client_id': result.loc['client_id'].item(),
            'date_updated': datetime.datetime.now(),
            'total_daily_credit_award': 0,
            'total_credit': result.loc['base_credit'],
        }
        models.ClientWalletModel().create(wallet_init_data)
        return result.loc[['client_id', 'client_name', 'industry_name']].to_json()

    def get_clients(self, rm_id):
        result = self.model.get_by_rm_id(rm_id)
        return result.loc[:,['client_id', 'client_name', 'industry_name']].to_json(orient='records')


class TransactionService:
    def __init__(self):
        self.model = models.TransactionModel()
'''
    def new_transaction(self, params):
        transaction = self.model.create(params).loc[0]
        holdings = models.HoldingsModel().get_by_client_id(params['client_id'])x


'''
