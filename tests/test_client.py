from daphne.client import Client
from daphne.client import DaphneModeEnum
import os


def test_mode():
    client = Client(DaphneModeEnum.ENV)
    client.show_mode()

def test_environment():
    #環境変数を設定し実行する
    client = Client(DaphneModeEnum.ENV, ['Hello1', 'Hello2', 'Hello3'])
    client.set_env()
    print(client.items.Hello1)
    print(client.items.Hello2)
    print(client.items.Hello3)

def test_args():
    # sample実行
    # python3 app.py --Hello1 apple --Hello2 banana --Hello3 cherry
    client = Client(DaphneModeEnum.ARGS, ['Hello1', 'Hello2', 'Hello3'])
    client.set_args()
    print(client.items.Hello1)
    print(client.items.Hello2)
    print(client.items.Hello3)

def test_json():
    pass