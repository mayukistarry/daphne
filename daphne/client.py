import os
import argparse
import json

class DaphneModeEnum:
    ENV = 0
    ARGS = 1
    JSON = 2
    INPUT = 3
    DB = 4

class Items:
    pass


class Client:
    #エラーメッセージをもう少しわかりやすくする
    def __init__(self, mode, value_declares, is_strict=True):
        #modeも上手く使って、どのモードで実行しているかを判定できるようにする
        self.mode = mode
        self.__value_declares = value_declares
        self.__is_strict = is_strict
        self.__parser = argparse.ArgumentParser(description='このプログラムの説明')
        self.__items = Items()
    
    @property
    def items(self):
        return self.__items
    
    def show_mode(self):
        if self.mode == DaphneModeEnum.ENV:
            print('環境変数モードです')
        elif self.mode == DaphneModeEnum.ARGS:
            print('引数モードです')
        elif self.mode == DaphneModeEnum.JSON:
            print('JSONモードです')
        elif self.mode == DaphneModeEnum.INPUT:
            print('入力モードです')
        elif self.mode == DaphneModeEnum.DB:
            print('DBモードです')
        else:
            raise Exception('不正な値です。')
    
    def set_env(self):
        for declaration in self.__value_declares:
            try:
                value = os.environ[declaration]
                setattr(self.__items, declaration, value)
            except KeyError:
                if self.__is_strict:
                    raise Exception('環境変数が設定されていません。')
                else:
                    #ログ系の何かはあった方がいいか
                    continue
  
    def set_args(self):
        #decalareをclass化して汎用化した方がいいか？
        for declaration in self.__value_declares:
            self.__parser.add_argument(f'--{declaration}')
        self.__items = self.__parser.parse_args()
        self.__validate_args()
    
    def __validate_args(self):
        if self.__is_strict:
            for declaration in self.__value_declares:
                if getattr(self.__items, declaration) is None:
                    raise Exception('引数が設定されていません。')
    
    def set_json(self, path):
        with open(path) as f:
            file_data = f.read()
        json_data = json.loads(file_data)

        for declaration in self.__value_declares:
            try:
                value = json_data[declaration]
                setattr(self.__items, declaration, value)
            except KeyError:
                if self.__is_strict:
                    raise Exception('JSONが設定されていません。')
                else:
                    #ログ系の何かはあった方がいいか
                    continue
    
    def set_input(self):
        for declaration in self.__value_declares:
            value = input(f'{declaration}:')
            setattr(self.__items, declaration, value)
    
    def set_db(self):
        pass