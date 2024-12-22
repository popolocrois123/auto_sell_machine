import queue
import pandas as pd

# 自動販売機クラス
class Auto_machine:

    def __init__(self):
        # csvファイル
        
        self.service = Service()
        self.drink_list = self.service.drink_price_dict()
        # self.df2 = self.service.zaiko_dict(file_path)

class Money:

    def __init__(self) -> None:
        self.total_money = 0

    def cal_total(self, val):
        self.total_money += val

    def get_total_money(self):
        return self.total_money

class Zaiko:
    def __init__(self) -> None:
        # self.tea = queue.Queue()
        # self.juice = queue.Queue()
        # self.beer = queue.Queue()
        self.queue_dict = dict()
        self.service = Service()
        self.li = self.service.zaiko_dict()
        zaiko_name = self.li.keys()
        for name in zaiko_name:
            self.q = queue.Queue()
            self.queue_dict[name] = self.q

        # 初期在庫
        for name in self.li.keys():
            for z in range(self.li[name]):
                self.queue_dict[name].put(name)

        # for _ in range(self.zaiko_num):
        #     self.tea.put('TEA')

        # for _ in range(self.zaiko_num):
        #     self.juice.put('JUICE')

        # for _ in range(self.zaiko_num):
        #     self.beer.put('BEER')

    def get_product(self, name):
        if self.queue_dict[name].qsize() > 0:
            self.queue_dict[name].get()

    def get_product_size(self, name):
        if self.queue_dict[name].qsize() > 0:
            return True
        else:
            return False
    # 在庫追加
    def add_product(self, name):
        self.queue_dict[name].put(name)

# controllerを介してmodelにcsvファイルを渡す役割
# 参考 chatgpt
class Service():
    def __init__(self):
        self.file_path = "drink_list.csv"
        self.df = pd.read_csv(self.file_path)
    
    def drink_price_dict(self):
        drink_list = dict(zip(self.df["drink"], self.df["price"]))
        return drink_list
    
    def zaiko_dict(self):
        zaiko_list = dict(zip(self.df["drink"], self.df["zaiko"]))
        return zaiko_list
        

if __name__ == '__main__':

    q = Zaiko()

    for i in range(5):
        q.get_product('TEA')

    for i in range(5):
        q.get_product('BEER')

    if q.get_product_size('TEA'):
        print(f'お茶の在庫あり')
    else:
        print(f'お茶売り切れ')

    if q.get_product_size('BEER'):
        print(f'ビールの在庫あり')
    else:
        print(f'ビール売り切れ')
    