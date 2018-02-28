import time

INTERVAL_DELAY=1


def main_loop():
    
    active_strategies=get_active_strategies()
    update_current_state(active_strategies)
    
    for strategy in active_strategies:
        strategy.run()
    

def update_current_state(active_strategies):
    exchanges=set([strategy.get_exchanges() for strategy in strategies])
    markets=set([strategy.get_markets() for strategy in strategies])
    
    for exchange in exchanges:
        exchange.update_state()
        
    for market in makets:
        market.update_state()
    


def get_active_strategies():
    pass




while(True):
    main_loop()
    time.sleep(INTERVAL_DELAY)