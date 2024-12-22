import tkinter as tk
import tkinter.ttk as ttk

from model_1206 import Zaiko, Money, Auto_machine, Service
from view_1206 import VMoney, VDrink, Roulette

class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        self.title("自動販売機")       # ウィンドウタイトル
        self.geometry("1200x500") # ウィンドウサイズ(幅x高さ)
        self.font = ("MSゴシック", "14")

        # maintenance
        self.maintenance_flag = False

        # ルーレットフレームの追加
        self.ru = Roulette(self)
        # self.ru.place(relx=0.05, rely=0, width=400, height=90)

        # # csvファイル
        # file_path = "drink_list.csv"
        # self.service = Service()
        # # self.df = self.service.drink_price_dict(file_path)
        # self.df2 = self.service.zaiko_dict(file_path)

        # 商品リスト
        self.auto_machine = Auto_machine()

        # 在庫クラス
        self.zaiko = Zaiko()

        # 飲み物クラス
        self.v_drink = VDrink(self)
        self.v_drink.place(relx=0.3, rely=0.2, width=700, height=300)

        # お金クラス
        self.initial_money()
        # self.v_money.place(relx=0.1, rely=0.2, width=100, height=300)

        # self.v_money = VMoney(self)
        # self.v_money.place(relx=0.03, rely=0.1, width=100, height=300)

        # メンテナンス切り替        
        self.maintenance_button()

    def initial_money(self):
        self.m_money = Money()
        self.v_money = VMoney(self)
        self.v_money.place(relx=0.03, rely=0.2, width=300, height=300)
        

    def maintenance_button(self):
        # 売上ボタン
        self.total_sales = tk.Button(self, text="maintenance", font=self.font, command=self.mainte)
        self.total_sales.place(x=100, y= 280)

    def mainte(self):
        if self.maintenance_flag:
            self.maintenance_flag = False
        else:
            self.maintenance_flag = True

        self.v_money.update_maintenance_menu()
        self.v_drink.update_maintenance_menu()

    # 

if __name__ == '__main__':
    app = Application()
    app.mainloop()