import tkinter as tk
from model_1206 import Zaiko

class Backyard:
    def __init__(self, root) -> None:
        self.root = root
        self.zaiko = Zaiko()
        # 飲み物と在庫の辞書
        self.li = self.zaiko.li
        self.queue_dict = self.zaiko.queue_dict
        


    def open_sub_window(self):
        new_window = tk.Toplevel(self.root.master)
        new_window.title("メンテナンス")
        new_window.geometry('300x500')

        # フレーム
        self.label_frame = tk.LabelFrame(new_window, text = "在庫",
                                         bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.label_frame.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        
        # 在庫フレームの中に飲み物の名前　在庫の数　add ボタンの追加
        span = 0
        for name in self.li.keys():
            # 飲み物の名前の表示
            name_lbl = tk.Label(self.label_frame, text=f"{name}: ")
            name_lbl.grid(column=0, row=span, padx=10, pady=10, sticky="nsew")

            # 在庫の表示
            zaiko_num = str(self.queue_dict[name].qsize())
            zaiko_lbl = tk.Label(self.label_frame, text=f"{zaiko_num }")
            zaiko_lbl.grid(column=1, row=span, padx=10, pady=10, sticky="nsew")

            # 在庫追加のボタン
            zaiko_add_btn = tk.Button(self.label_frame, text="追加", command=lambda x=name: self.push_tuika(x))
            zaiko_add_btn.grid(column=2, row=span, padx=10, pady=10, sticky="nsew")
            span += 1
        
    def push_tuika(self, name):
        zaiko = Zaiko()
        zaiko.get_product_size(name)
        zaiko.add_product(name)
        self.update_zaiko_label(name)

    def update_zaiko_label(self, name):
        print(self.zaiko.queue_dict[name].qsize())




