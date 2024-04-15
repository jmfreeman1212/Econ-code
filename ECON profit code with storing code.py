#econ code with storing past inputs
import tkinter as tk

# Create lists to store inputs and outputs
inputs = []
outputs = []

def calculate_values():
    try:
        # Get input values
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        wage = float(wage_entry.get())
        labor = int(labor_entry.get())
        rent = int(rent_entry.get())
        capital = int(capital_entry.get())

        # Store input values
        inputs.append({
            "price": price,
            "quantity": quantity,
            "wage": wage,
            "labor": labor,
            "rent": rent,
            "capital": capital
        })

        # Calculate values
        total_revenue = price * quantity
        total_cost = (wage * labor) + (rent * capital)
        average_cost = total_cost / quantity
        profit = total_revenue - total_cost

        # Store output values
        outputs.append({
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "average_cost": average_cost,
            "profit": profit
        })

        # Update labels
        total_revenue_label.config(text=f"The total revenue is ${total_revenue}")
        total_cost_label.config(text=f"The total cost is ${total_cost}")
        average_cost_label.config(text=f"Average cost is ${average_cost}")
        profit_label.config(text=f"Profit is ${profit}")

    except ValueError:
        error_label.config(text="Please enter valid numerical values.")

# Create the Tkinter window
window = tk.Tk()
window.title("Economics Calculator")

# Function to create labels and entry widgets
def create_input_fields(label_text):
    label = tk.Label(window, text=label_text)
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    return entry

# Input fields for price, quantity, wage, labor, rent, and capital
price_entry = create_input_fields("Enter price:")
quantity_entry = create_input_fields("Enter quantity:")
wage_entry = create_input_fields("Enter wage:")
labor_entry = create_input_fields("Enter labor:")
rent_entry = create_input_fields("Enter rent:")
capital_entry = create_input_fields("Enter capital:")

# Button to calculate values
calculate_button = tk.Button(window, text="Calculate", command=calculate_values)
calculate_button.pack()

# Labels to display calculated values or errors
total_revenue_label = tk.Label(window, text="", fg = "blue")
total_revenue_label.pack()

total_cost_label = tk.Label(window, text="", fg = "green")
total_cost_label.pack()

average_cost_label = tk.Label(window, text="", fg = "yellow")
average_cost_label.pack()

profit_label = tk.Label(window, text="")
profit_label.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

window.mainloop()

# Access stored inputs and outputs if needed
print("Stored Inputs:", inputs)
print("Stored Outputs:", outputs)


def create_gui():
    # Create the main window
    root = tk.Tk()

    # Set the window size
    root.geometry("800x600")  # You can adjust the size as needed

    # Set the window title
    root.title("Red, White, and Blue GUI")

    # Set the background color to white
    root.configure(bg='white')

    # Create a label with a larger font size and red text
    label = tk.Label(root, text="Hello, this is a larger display!", font=('Arial', 16), fg='red', bg='white')
    label.pack(pady=20)

    # Create a button with blue color
    button = tk.Button(root, text="Click me", font=('Arial', 12), command=on_button_click, bg='blue', fg='white')
    button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

def on_button_click():
    print("Button clicked!")

# Call the function to create the GUI
create_gui()