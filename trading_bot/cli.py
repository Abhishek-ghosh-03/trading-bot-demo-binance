import argparse, os, sys
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.validators import validate_positive_float, validate_inputs
from bot.client import BinanceFuturesClient
from bot.orders import place_futures_order

load_dotenv()

def run():
    log = setup_logging()
    p = argparse.ArgumentParser()
    
    p.add_argument("--symbol", type=str, required=True)
    p.add_argument("--side", type=str, required=True)
    p.add_argument("--order_type", type=str, required=True)
    p.add_argument("--quantity", type=validate_positive_float, required=True)
    p.add_argument("--price", type=validate_positive_float)

    args = p.parse_args()

    try:
        validate_inputs(args)
    except Exception as e:
        print(f"Error: {e}"); sys.exit(1)

    key = os.getenv("BINANCE_API_KEY")
    sec = os.getenv("BINANCE_API_SECRET")

    try:
        bot = BinanceFuturesClient(key, sec)
    except Exception as e:
        print(f"Conf error: {e}"); sys.exit(1)

    res = place_futures_order(bot, args.symbol, args.side, args.order_type, args.quantity, args.price)

    if isinstance(res, dict) and res.get("error"):
        print(f"\nFailed: {res.get('message')}")
    else:
        print("\nSuccess!")
        print(f"ID: {res.get('orderId')}")
        print(f"Status: {res.get('status')}")
        print(f"Qty: {res.get('executedQty')}")
        print(f"Avg: {res.get('avgPrice', '0.00')}")

if __name__ == "__main__":
    run()
