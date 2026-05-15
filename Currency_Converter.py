import requests

print("===================================")
print("        CURRENCY CONVERTER        ")
print("===================================")

# Free Exchange Rate API
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:

    # Fetch API data
    response = requests.get(url)

    # Convert response to JSON
    data = response.json()

    # Get exchange rates dictionary
    rates = data["rates"]

    # User input
    from_currency = input("\nEnter FROM currency (e.g. USD): ").upper()
    to_currency = input("Enter TO currency (e.g. INR): ").upper()

    amount = float(input("Enter amount: "))

    # Check if currency exists
    if from_currency not in rates:
        print("❌ Invalid FROM currency code.")

    elif to_currency not in rates:
        print("❌ Invalid TO currency code.")

    else:

        # Convert amount to USD first
        amount_in_usd = amount / rates[from_currency]

        # Convert USD to target currency
        converted_amount = amount_in_usd * rates[to_currency]

        print("\n===================================")
        print(f"{amount} {from_currency} = "
              f"{converted_amount:.2f} {to_currency}")
        print("===================================")

except requests.exceptions.RequestException:
    print("❌ Error connecting to exchange rate API.")

except ValueError:
    print("❌ Please enter a valid numeric amount.")

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)

finally:
    print("\nProgram execution completed.")