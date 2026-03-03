import argparse
import requests
import os
from dotenv import load_dotenv, set_key
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

def main():
    parser = argparse.ArgumentParser(
        description="Currency Exchange Calc - simple currency converter",
        usage="python valuta.py --from USD --to DKK --amount 600")
    parser.add_argument("--key", help="ExchangeRate API key")
    parser.add_argument("--from", dest="from_currency", required=True,
                        help="Currency to convert from (USD, EUR, etc.)")
    parser.add_argument("--to", dest="to_currency", required=True,
                        help="Currency to convert to (DKK, EUR, etc.)")
    parser.add_argument("--amount", type=float, required=True, help="Amount to convert")

    args = parser.parse_args()

    api_key = None

    if args.key: 
        api_key = args.key
        set_key(env_path, "API_KEY", api_key)

    if not api_key:
        api_key = os.getenv("API_KEY")
    
    if not api_key:
        api_key = input("Please enter your ExchangeRate API key: ")
        if not env_path.exists():
            env_path.touch()
        set_key(env_path, "API_KEY", api_key)

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{args.from_currency}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"Call failure: {e}")
        exit()

    if data.get("result") != "success":
        print(f"Currency '{args.from_currency}' not found.")
        exit()
        
    rate = data["conversion_rates"].get(args.to_currency)
    if not rate:
        print(f"Currency '{args.to_currency}' not found.")
        exit()

    result = rate * args.amount
    print(f"{args.amount} {args.from_currency} = {result:.2f} {args.to_currency}")


if __name__ == "__main__":
    main()