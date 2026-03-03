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
There are three required arguments. 
1. The currency you want to convert from
2. The currency you want to convert to
3. The amount

***Example:*** <br />
python valuta.py USD DKK 100

On first use, you'll be asked to add your API key: *Please enter your ExchangeRate API key:* <br />
After hitting enter, your key will be saved and you won't be asked again. <br />


