import requests
from tkinter import *
from tkinter import messagebox

def get_price():
    coin = entry.get().lower().strip()
    if not coin:
        messagebox.showerror("Input Error", "Please enter a cryptocurrency name (e.g., bitcoin)")
        return
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        if coin in data:
            price = data[coin]["usd"]
            result_label.config(text=f"{coin.capitalize()} price: ${price}")
        else:
            result_label.config(text=f"No data found for '{coin}'")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI setup
root = Tk()
root.title("Crypto Price Tracker")
root.geometry("400x200")
root.configure(bg="#121212")

title = Label(root, text="Crypto Price Tracker", font=("Arial", 16, "bold"), fg="#00FFAA", bg="#121212")
title.pack(pady=10)

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack()

button = Button(root, text="Get Price", command=get_price, font=("Arial", 12), bg="#00FFAA")
button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14), fg="white", bg="#121212")
result_label.pack(pady=10)

root.mainloop()
