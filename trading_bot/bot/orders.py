import logging

logger = logging.getLogger("trading_bot")

def place_futures_order(client, symbol, side, o_type, quantity, price=None):
    path = "/fapi/v1/order"
    
    payload = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": o_type.upper(),
        "quantity": quantity
    }
    
    if o_type.upper() == "LIMIT":
        payload.update({
            "price": price,
            "timeInForce": "GTC"
        })

    logger.info(f"Placing {o_type} {side} on {symbol}...")
    return client.send_signed_request("POST", path, payload)
