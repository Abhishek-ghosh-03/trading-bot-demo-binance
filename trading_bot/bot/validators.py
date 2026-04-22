import argparse

def validate_positive_float(v):
    try:
        val = float(v)
        if val <= 0: raise argparse.ArgumentTypeError(f"{v} must be > 0")
        return val
    except:
        raise argparse.ArgumentTypeError(f"{v} invalid float")

def validate_inputs(args):
    s, t = args.side.upper(), args.order_type.upper()
    
    if s not in ["BUY", "SELL"]:
        raise ValueError(f"Bad side: {s}")

    if t not in ["MARKET", "LIMIT"]:
        raise ValueError(f"Bad type: {t}")

    if t == "LIMIT" and (args.price is None or args.price <= 0):
        raise ValueError("Price required for LIMIT")

    return True
