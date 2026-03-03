# Valuta CLI

Simple CLI program for Exchange Rate Calculation via ExchangeRate API.

## Installation

1. Clone repository
2. Create virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

4. Install dependencies:

   pip install -r requirements.txt

## How to use

Example:
python valuta.py --from USD --to DKK --amount 100

On the first run, you'll be asked to add your API key as such:
        Please enter your ExchangeRate API key:
After hitting enter, your key will be saved and you won't be asked again. 
