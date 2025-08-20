price = float(input("Enter the input of the price: "))
discount_percentage = float(input("Enter the discount percentage offered: "))

def calculate_discount(price, discount_percentage):
    if discount_percentage > 20:
        return price - (price * discount_percentage / 100)
    return (f"the original price remains Ksh.{price}")

discount = calculate_discount(price, discount_percentage)
print("The discount is: ", discount)

