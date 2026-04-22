Binance Futures Testnet Trading Bot

Features

- Clean Architecture : Modular structure with separation of concerns
- Robust Logging : All requests, responses, and errors are logged to `logs/app.log` with rotation
- Input Validation : Strict validation for symbols, sides, quantities, and prices 
- Error Handling : Graceful handling of API errors and network issues

Project Structure 


trading_bot/
 bot/
    client.py          
    orders.py          
    validators.py      
    logging_config.py  
    __init__.py

 cli.py                 
 README.md
 requirements.txt
 .env                   # Environment variables 


Setup Instructions

 Clone the repository (or navigate to the folder).
 Create a virtual environment:
   
   python -m venv venv
   .\venv\Scripts\activate

Install dependencies:

   pip install -r requirements.txt

Set up environment variables:
   
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret


Usage Examples

Place a MARKET BUY order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

Place a LIMIT SELL order

python cli.py --symbol ETHUSDT --side SELL --order_type LIMIT --quantity 0.1 --price 2500


`logs/app.log`

Validation Rules
- `symbol`: Must be a valid Binance Futures ticker
- `side`: Must be `BUY` or `SELL`
- `order_type`: Must be `MARKET` or `LIMIT`
- `quantity`: Must be a > 0
- `price`: Required if `order_type` is `LIMIT`, must be a positive number

-> Buying
---------------
<img width="1262" height="954" alt="Screenshot 2026-04-22 123813" src="https://github.com/user-attachments/assets/702c8181-de2a-4029-bbac-e168cb8c32fe" />

-> Virtual Env
---------------
<img width="1251" height="430" alt="Screenshot 2026-04-22 124012" src="https://github.com/user-attachments/assets/9b99c030-4e5b-43fc-8405-5336248a358c" />

-> logs ss
---------------
<img width="1256" height="422" alt="Screenshot 2026-04-22 124205" src="https://github.com/user-attachments/assets/d0f00682-a7a6-4ad7-af14-8c1029e34e28" />

-> Selling
---------------
<img width="1492" height="906" alt="Screenshot 2026-04-22 124114" src="https://github.com/user-attachments/assets/39a3a129-2c70-4c2c-aa7f-f88eee670f31" />

