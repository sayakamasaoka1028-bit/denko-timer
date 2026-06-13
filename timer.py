import tkinter as tk
from tkinter import messagebox

TOTAL_TIME = 40 * 60  # 40分

class DenkoTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡第二種電気工事士 実技タイマー")
        self.root.geometry("400x300")

        self.running = False
        self.remaining = TOTAL_TIME

        tk.Label(
            root,
            text="⚡第二種電気工事士 実技タイマー",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.time_label = tk.Label(
            root,
            text="40:00",
            font=("Arial", 40)
        )
        self.time_label.pack(pady=20)

        self.status_label = tk.Label(
            root,
            text="準備完了",
            font=("Arial", 12)
        )
        self.status_label.pack()

        self.start_btn = tk.Button(
            root,
            text="開始",
            font=("Arial", 14),
            command=self.start_timer
        )
        self.start_btn.pack(pady=10)

        self.reset_btn = tk.Button(
            root,
            text="リセット",
            font=("Arial", 14),
            command=self.reset_timer
        )
        self.reset_btn.pack()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.countdown()

    def reset_timer(self):
        self.running = False
        self.remaining = TOTAL_TIME
        self.time_label.config(text="40:00", fg="black")
        self.status_label.config(text="準備完了")

    def countdown(self):
        if not self.running:
            return

        minutes = self.remaining // 60
        seconds = self.remaining % 60

        self.time_label.config(text=f"{minutes:02}:{seconds:02}")

        elapsed = TOTAL_TIME - self.remaining

        if elapsed == 20 * 60:
            self.status_label.config(text="⚠️ 半分経過しました")
            self.root.bell()

        if self.remaining == 5 * 60:
            self.status_label.config(text="🚨 残り5分")
            self.time_label.config(fg="red")
            self.root.bell()

        if self.remaining <= 0:
            self.running = False
            self.time_label.config(text="00:00")
            self.status_label.config(text="🏁 終了")
            self.root.bell()
            messagebox.showinfo(
                "終了",
                "実技試験時間終了です！"
            )
            return

        self.remaining -= 1
        self.root.after(1000, self.countdown)

root = tk.Tk()
app = DenkoTimer(root)
root.mainloop()
