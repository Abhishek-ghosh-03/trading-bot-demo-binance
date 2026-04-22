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
