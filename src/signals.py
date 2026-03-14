import numpy as np

def calculate_volatility(prices):
    if len(prices) < 2: return 0
    # Log Returns: ln(Pt / Pt-1)
    returns = np.diff(np.log(prices))
    return np.std(returns)

def keyle_lambda(price_change, net_order_flow):
    # net_order_flow = Vol_buy - Vol_sell
    # price_change = post_price - pre_price
    if not net_order_flow:
        return price_change/net_order_flow
    else:
        raise ValueError("Net Order Flow is Zero")

def order_book_imbalance(bid_vol, ask_vol):
    return (bid_vol-ask_vol)/(bid_vol+ask_vol)

def micro_price(bid, bid_vol, ask, ask_vol):
    return (bid*ask_vol+ask*bid_vol)/(bid_vol+ask_vol)