"""
Discount Calculator

This script calculates the final price of an item after applying a discount.
If the discount percentage is 20% or higher, the discount is applied; otherwise,
the original price remains unchanged.

Usage:
- Run the script.
- Enter the original price of the item.
- Enter the discount percentage.
- The script will calculate and display the final price or indicate no discount was applied.

Error Handling:
- Validates that inputs are numeric.
- Displays an error message if invalid inputs are provided.

Author: Bill Glinton
"""

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.

    Returns:
    float: The final price after applying the discount if it is 20% or higher,
           otherwise the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    # Display the result
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
