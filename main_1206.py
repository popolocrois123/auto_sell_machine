import tkinter as tk
import tkinter.ttk as ttk

from model_1206 import Zaiko, Money, Auto_machine, Service
from view_1206 import VMoney, VDrink, Roulette
from backyard import Backyard

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("自動販売機")       # ウィンドウタイトル
        self.master.geometry("1200x500") # ウィンドウサイズ(幅x高さ)
        self.font = ("MSゴシック", "14")

        # maintenance
        self.maintenance_flag = False

        # ルーレットフレームの追加
        self.ru = Roulette(self)

        # csvファイル
        self.service = Service()
        
        # 商品リスト
        self.auto_machine = Auto_machine()

        # 在庫クラス
        self.zaiko = Zaiko()

        # 飲み物クラス
        self.v_drink = VDrink(self)
        # self.v_drink.place(relx=0.3, rely=0.2, width=700, height=300)

       

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
        # self.v_money.place(relx=0.03, rely=0.2, width=300, height=300)
        

    def maintenance_button(self):

         # メンテナンスのフレーム
        self.label_frame2 = tk.LabelFrame(root, text="メンテナンス", bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.label_frame2.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")
        # 売上ボタン
        # self.label_frame2 = self.v_money.label_frame2
        self.total_sales = tk.Button(self.label_frame2, text="maintenance", font=self.font, command=self.mainte)
        self.total_sales.grid(column=2,row=1,padx=5, pady=5)


    def mainte(self):
        back_yard = Backyard(self)
        back_yard.open_sub_window()
        # if self.maintenance_flag:
        #     self.maintenance_flag = False
        # else:
        #     self.maintenance_flag = True
        # new_window = tk.Toplevel(self)
        # new_window.title("メンテナンス")

        # self.v_money.update_maintenance_menu(new_window)
        # self.v_drink.update_maintenance_menu(new_window)

    #     close_btn = tk.Button(new_window, text="このウィンドウを閉じる", command=new_window.destroy)
    #     close_btn.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

    # # 

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()