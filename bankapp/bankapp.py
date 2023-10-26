import tkinter as tk

# Functions 
# ========================================================================================
def deposit():
    try:
        amount = float(deposit_entry.get())
        if amount < 0:
            raise ValueError
        current_balance = float(balance_var.get())
        new_balance = current_balance + amount
        balance_var.set(f"{new_balance:.2f}")
        transaction_log.append(f"Deposit: +R{amount}")
        update_transaction_log()
        deposit_entry.delete(0, tk.END)
        save_data()  
    except ValueError:
        error_label.config(text="Invalid input. Please enter a valid amount.")

def withdraw():
    try:
        amount = float(withdraw_entry.get())
        if amount < 0:
            raise ValueError
        current_balance = float(balance_var.get())
        if current_balance < amount:
            error_label.config(text="Insufficient funds.")
        else:
            new_balance = current_balance - amount
            balance_var.set(f"{new_balance:.2f}")
            transaction_log.append(f"Withdrawal: -R{amount}")
            update_transaction_log()
            withdraw_entry.delete(0, tk.END)
            save_data()  
    except ValueError:
        error_label.config(text="Invalid input. Please enter a valid amount.")

def update_transaction_log():
    transaction_log_text.config(state=tk.NORMAL)
    transaction_log_text.delete(1.0, tk.END)
    for transaction in transaction_log:
        transaction_log_text.insert(tk.END, transaction + "\n")
    transaction_log_text.config(state=tk.DISABLED)

def save_data():
    with open('Bank Data.txt', 'w') as f:
        f.write(balance_var.get())
    with open('Transaction Log.txt', 'a') as f:
        for transaction in transaction_log:
            f.write(transaction + "\n")

def calculator():
    pass


# GUI
# ========================================================================================
root = tk.Tk()
root.title("Banking App")
frame = tk.Frame(root)
frame.pack(pady=10)

# Bank Name label 
bank_name_label = tk.Label(frame, text="Codex Bank App")
bank_name_label.grid(row=0, columnspan=2, pady=15)

# Deposit Entry 
deposit_entry = tk.Entry(frame)
deposit_entry.grid(row=1, column=0)

# Deposit Button 
deposit_button = tk.Button(frame, text="Deposit", command=deposit, width=8)
deposit_button.grid(row=1, column=1, padx=10)

# Withdraw Entry 
withdraw_entry = tk.Entry(frame)
withdraw_entry.grid(row=2, column=0)

# Withdraw Button 
withdraw_button = tk.Button(frame, text="Withdraw", command=withdraw, width=8)
withdraw_button.grid(row=2, column=1, padx=10)

# balance label 
balance_var = tk.StringVar(value="0.00")
balance_label = tk.Label(root, textvariable=balance_var)
balance_label.pack(pady=5)

# error label 
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=0)

# transaction log label 
transaction_log_text = tk.Text(root, width=40, height=10)
transaction_log_text.pack(padx=10, pady=10)
transaction_log_text.config(state=tk.DISABLED)


# Load initial balance from file
# ========================================================================================
try:
    with open('Bank Data.txt', 'r') as f:
        initial_balance = f.read().strip()
        balance_var.set(initial_balance)
except FileNotFoundError:
    initial_balance = "0.00"

transaction_log = []

def load_transaction_log():
    try:
        with open('Transaction Log.txt', 'r') as f:
            transaction_log.extend([line.strip() for line in f.readlines()])
            update_transaction_log()
    except FileNotFoundError:
        pass  # If the file doesn't exist, there are no logs to load

# Load initial balance and transaction logs
load_transaction_log()

# run main
# ========================================================================================
root.mainloop()
