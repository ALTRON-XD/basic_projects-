import requests

def convert_currency(from_currency, to_currency, amount):
    api_key = 'your_API'  # Replace with your API key from exchangerate-api.com
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"

    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        converted_amount = data['conversion_result']
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion failed. Please check currency codes or API key.")

from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., INR): ").upper()
amount = float(input("Enter the amount: "))

convert_currency(from_currency, to_currency, amount)
