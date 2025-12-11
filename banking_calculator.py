"""
Banking Rate Calculator GUI
Author: Sheraz Shah
Description: Calculates interest rates based on balance and shows balance after deduction
"""

import tkinter as tk
from tkinter import ttk, messagebox

def calculate_interest_rate(balance):
    """
    Determine interest rate based on balance:
    - > $50,000: 7%
    - $25,000 - $49,999.99: 5%
    - $1,000 - $24,999.99: 3%
    - Otherwise: 0%
    """
    if balance > 50000:
        return 0.07
    elif balance >= 25000:
        return 0.05
    elif balance >= 1000:
        return 0.03
    else:
        return 0.00
class BankingCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Banking Rate Calculator")
        self.window.geometry("500x400")
        # Title
        title = tk.Label(window, text="Bank Rate Qualification Calculator",
                        font=("Arial", 16, "bold"), pady=10)
        title.pack()
        # Input Frame
        input_frame = tk.Frame(window, padx=20, pady=10)
        input_frame.pack()
        # Customer Name
        tk.Label(input_frame, text="Customer Name:", 
                font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8)
        self.name_entry = tk.Entry(input_frame, width=30, font=("Arial", 11))
        self.name_entry.grid(row=0, column=1, pady=8, padx=(10, 0))
        # Balance
        tk.Label(input_frame, text="Balance Amount ($):", 
                font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8)
        self.balance_entry = tk.Entry(input_frame, width=30, font=("Arial", 11))
        self.balance_entry.grid(row=1, column=1, pady=8, padx=(10, 0))
        # Results Frame
        self.result_frame = tk.LabelFrame(window, text="Results", 
                                         padx=15, pady=15, font=("Arial", 11))
        self.result_frame.pack(pady=15, padx=20, fill="both", expand=True)
        self.rate_label = tk.Label(self.result_frame, text="Rate is = ", 
                                  font=("Arial", 11, "bold"))
        self.rate_label.pack(anchor="w")
        self.result_label = tk.Label(self.result_frame, text="", 
                                    font=("Arial", 11), wraplength=400, justify="left")
        self.result_label.pack(anchor="w", pady=10)
        # Buttons
        button_frame = tk.Frame(window, pady=10)
        button_frame.pack()
        tk.Button(button_frame, text="Calculate", command=self.calculate,
                 font=("Arial", 11), bg="#2196F3", fg="white", 
                 padx=25, pady=5).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear,
                 font=("Arial", 11), bg="#9E9E9E", fg="white",
                 padx=25, pady=5).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Exit", command=window.quit,
                 font=("Arial", 11), bg="#F44336", fg="white",
                 padx=25, pady=5).grid(row=0, column=2, padx=5)
    def calculate(self):
        """Calculate and display results"""
        try:
            # Get inputs
            name = self.name_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Required", "Please enter customer name")
                return
            balance_str = self.balance_entry.get().strip()
            if not balance_str:
                messagebox.showwarning("Input Required", "Please enter balance amount")
                return
            # Validate balance
            balance = float(balance_str)
            if balance < 0:
                messagebox.showerror("Invalid Input", "Balance cannot be negative")
                return
            # Calculate
            rate = calculate_interest_rate(balance)
            rate_percent = rate * 100
            deduction = balance * rate
            actual_balance = balance - deduction
            # Display results (exact format from assignment)
            self.rate_label.config(text=f"Rate is = {rate_percent:.1f}%")
            
            result = (f"{name}, your balance is ${balance:,.2f} and "
                     f"your actual balance after deduction is ${actual_balance:,.2f}")
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for balance")
    def clear(self):
        """Clear all fields"""
        self.name_entry.delete(0, tk.END)
        self.balance_entry.delete(0, tk.END)
        self.rate_label.config(text="Rate is = ")
        self.result_label.config(text="")
        self.name_entry.focus()
def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = BankingCalculator(root)
    root.mainloop()
if __name__ == "__main__":
    main()
