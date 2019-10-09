from flask import Flask, request
import service

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/client/<client_id>/wallet', methods=['GET'])
def get_client_wallet_data(client_id):
    return service.ClientWalletService().get_wallet_data(client_id)


@app.route('/rm/<rm_id>/my_clients', methods=['POST', 'GET'])
def my_clients(rm_id):
    if request.method == 'POST':
        params = request.get_json()
        params['rm_id'] = rm_id
        return service.ClientService().new_client(params)
    elif request.method == 'GET':
        return service.ClientService().get_clients(rm_id)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
