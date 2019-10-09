import datetime


class TestData:
    def __init__(self):
        self.transaction = {
            'client_id' : 11,
            'time_stamp' : datetime.datetime.now(),
            'trade_type' : 'buy',
            'product_id' : 1,
            'units_traded' : 200
        }
        self.client = {
            'client_name' : 'CCcc',
            'industry_id' : 2,
            'rm_id' : 2,
            'pwd': 'yes'
        }
        self.wallet = {
            'client_id' : 1000,
            'date_updated' : datetime.datetime.now(),
            'total_daily_credit_award' : 100,
            'total_credit': 1000,
        }



