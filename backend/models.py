import config
import psycopg2 as pg
import pandas as pd


class TransactionModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def create(self, params):
        query = """
        INSERT INTO 
        Transactions
        (client_id, time_stamp, trade_type, product_id, units_traded)
        VALUES 
        (%(client_id)s, %(time_stamp)s, %(trade_type)s, %(product_id)s, %(units_traded)s)
        RETURNING transaction_id;
        """
        self.cur.execute(
            query,
            params
        )
        self.conn.commit()
        new_transaction_id = self.cur.fetchone()[0]
        return self.get_by_transaction_id(new_transaction_id)

    def list_items(self, where_clause=''):
        query = """
        SELECT 
        transaction_id, time_stamp, product_name, trade_type,
        units_traded, Client.client_id, client_name, rm_id, unit_daily_credit_award
        FROM 
        Transactions 
        INNER JOIN Product 
        ON Transactions.product_id = Product.product_id
        INNER JOIN Client 
        ON Transactions.client_id = Client.client_id
        
        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['transaction_id', 'time_stamp', 'product_name', 'trade_type',
                                     'units_traded', 'client_id', 'client_name', 'rm_id', 'unit_daily_credit_award'])

    def get_by_transaction_id(self, transaction_id):
        where_clause = f'WHERE transaction_id = {transaction_id}'
        return self.list_items(where_clause)

    def get_by_rm_id(self, rm_id):
        where_clause = f'WHERE rm_id = {rm_id}'
        return self.list_items(where_clause)

    def get_by_client_id(self, client_id):
        where_clause = f'WHERE Client.client_id = {client_id}'
        return self.list_items(where_clause)


class HoldingsModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def create(self, params):
        query = """
        INSERT INTO 
        Holdings
        (client_id, product_id, units_held, daily_credit_award)
        VALUES 
        (%(client_id)s, %(product_id)s, %(units_held)s, %(daily_credit_award)s)
        RETURNING holding_id;
        """
        self.cur.execute(
            query,
            params
        )
        self.conn.commit()
        new_holding_id = self.cur.fetchone()[0]
        return self.get_by_holding_id(new_holding_id)

    def update(self, holding_id, update_dict):
        set_query = ', '.join([f'{column} = {value}' for column, value in update_dict.items()])
        query = f'UPDATE Holdings ' \
                f'SET {set_query} ' \
                f'WHERE holding_id = {holding_id};'
        self.cur.execute(query)
        self.conn.commit()
        return self.get_by_holding_id(holding_id)

    def list_items(self, where_clause=''):
        query = """
        SELECT 
        holding_id, Client.client_id, client_name, Product.product_id,
        product_name, units_held, daily_credit_award, rm_id
        FROM 
        Holdings 
        INNER JOIN Product 
        ON Holdings.product_id = Product.product_id
        INNER JOIN Client 
        ON Holdings.client_id = Client.client_id

        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['holding_id', 'client_id', 'client_name', 'product_id',
                                     'product_name', 'units_held', 'daily_credit_award', 'rm_id'])

    def get_by_holding_id(self, holding_id):
        where_clause = f'WHERE holding_id = {holding_id}'
        return self.list_items(where_clause)

    def get_by_client_id(self, client_id):
        where_clause = f'WHERE Client.client_id = {client_id}'
        return self.list_items(where_clause)

    def get_by_rm_id(self, rm_id):
        where_clause = f'WHERE rm_id = {rm_id}'
        return self.list_items(where_clause)

    def get_by_client_product_id(self, client_id, product_id):
        where_clause = f'WHERE Client.client_id = {client_id} AND Product.product_id = {product_id}'
        return self.list_items(where_clause)


class ClientWalletModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def create(self, params):
        query = """
        INSERT INTO Client_Wallet
        (client_id, date_updated, total_daily_credit_award, total_credit)
        VALUES (%(client_id)s, %(date_updated)s, %(total_daily_credit_award)s, %(total_credit)s)
        RETURNING client_wallet_id;
        """
        self.cur.execute(
            query,
            params
        )
        self.conn.commit()
        new_client_wallet_id = self.cur.fetchone()[0]
        return self.get_by_client_wallet_id(new_client_wallet_id)

    def list_items(self, where_clause=''):
        query = """
        SELECT 
        client_wallet_id, date_updated, Client.client_id, client_name, 
        total_daily_credit_award, total_credit, rm.rm_team, Client.rm_id
        FROM 
        Client_Wallet 
        INNER JOIN Client 
        ON Client_Wallet.client_id = Client.client_id
        INNER JOIN RM 
        ON RM.rm_id = Client.rm_id

        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['client_wallet_id', 'date_updated', 'client_id', 'client_name',
                                     'total_daily_credit_award', 'total_credit', 'rm_team', 'rm_id'])

    def get_by_client_wallet_id(self, client_wallet_id):
        where_clause = f'WHERE client_wallet_id = {client_wallet_id}'
        return self.list_items(where_clause)

    def get_by_client_id(self, client_id):
        where_clause = f'WHERE Client.client_id = {client_id}'
        return self.list_items(where_clause)

    def get_by_client_id_latest(self, client_id):
        query_max_date = f'SELECT ' \
                            f'MAX(date_updated) ' \
                            f'FROM ' \
                            f'Client_Wallet ' \
                            f'WHERE client_id = {client_id} '
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['client_wallet_id', 'date_updated', 'client_id',
                                     'total_daily_credit_award', 'total_credit'])

    def get_by_rm_id(self, rm_id):
        query = f'SELECT ' \
                f'client_wallet_id, MAX(date_updated), Client.client_id, client_name, ' \
                f'total_daily_credit_award, total_credit, rm_team, Client.rm_id ' \
                f'FROM ' \
                f'Client_Wallet ' \
                f'INNER JOIN Client ' \
                f'ON Client_Wallet.client_id = Client.client_id ' \
                f'INNER JOIN RM ' \
                f'ON RM.rm_id = Client.rm_id '\
                f'WHERE Client.rm_id = {rm_id} ' \
                f'GROUP BY Client.client_id '

        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['client_wallet_id', 'date_updated', 'client_id', 'client_name',
                                     'total_daily_credit_award', 'total_credit', 'rm_team', 'rm_id'])

    def get_by_rm_team(self, rm_team):
        query = f'SELECT ' \
            f'client_wallet_id, MAX(date_updated), Client.client_id, client_name, ' \
            f'total_daily_credit_award, total_credit, rm_team, Client.rm_id ' \
            f'FROM ' \
            f'Client_Wallet ' \
            f'INNER JOIN Client ' \
            f'ON Client_Wallet.client_id = Client.client_id ' \
            f'INNER JOIN RM ' \
            f'ON RM.rm_id = Client.rm_id ' \
            f'WHERE Client.rm_team = {rm_team} ' \
            f'GROUP BY Client.client_id '

        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['client_wallet_id', 'date_updated', 'client_id', 'client_name',
                                     'total_daily_credit_award', 'total_credit', 'rm_team', 'rm_id'])


class ClientModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def create(self, params):
        query = """
        INSERT INTO Client
        (client_name, industry_id, rm_id, pwd)
        VALUES (%(client_name)s, %(industry_id)s, %(rm_id)s, %(pwd)s)
        RETURNING client_id;
        """
        self.cur.execute(
            query,
            params
        )
        self.conn.commit()
        new_client_id = self.cur.fetchone()[0]
        return self.get_by_client_id(new_client_id)

    def list_items(self, where_clause=''):
        query = """
        SELECT client_id, client_name, industry_name, base_credit, rm_id, pwd
        FROM 
        Client INNER JOIN Industry ON  Client.industry_id = Industry.industry_id

        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['client_id', 'client_name',
                                     'industry_name', 'base_credit', 'rm_id', 'pwd'])

    def get_by_client_id(self, client_id):
        where_clause = f'WHERE Client.client_id = {client_id}'
        return self.list_items(where_clause)

    def get_by_rm_id(self, rm_id):
        where_clause = f'WHERE rm_id = {rm_id}'
        return self.list_items(where_clause)


class IndustryModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def list_items(self, where_clause=''):
        query = """
        SELECT industry_id, industry_name, base_credit
        FROM 
        Industry

        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['industry_id',
                                     'industry_name', 'base_credit'])

    def get_by_industry_id(self, industry_id):
        where_clause = f'WHERE industry_id = {industry_id}'
        return self.list_items(where_clause)


class ProductModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def list_items(self, where_clause=''):
        query = """
        SELECT product_id, product_name, unit_daily_credit_award
        FROM 
        Product

        """ + where_clause + ';'
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['product_id',
                                     'product_name', 'unit_daily_credit_award'])

    def get_by_product_id(self, product_id):
        where_clause = f'WHERE product_id = {product_id}'
        return self.list_items(where_clause)


class RMModel:
    def __init__(self):
        self.conn = pg.connect(**config.connection_parameters)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def list_items(self, where_clause=''):
        query = """
        SELECT 
        rm_id, rm_name, rm_email, rm_team, 
        group_name, area_name, country_name, pwd
        FROM 
        RM

        """ + where_clause + ';'
        #print(query)
        self.cur.execute(query)
        return pd.DataFrame(self.cur.fetchall(),
                            columns=['rm_id',
                                     'rm_name', 'rm_email','rm_team',
                                    'group_name', 'area_name', 'country_name', 'pwd'])

    def get_by_rm_email(self, rm_email):
        where_clause = f'WHERE rm_email = \'{rm_email}\''
        return self.list_items(where_clause)