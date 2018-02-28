from exchange_apis import *

from models import singleton
from models import currency
from models import market



class Exchange( object, metaclass=singleton.Singleton):
    
    def __init__(self, exchange_api):
        self._markets={}
        self._balances={}
        self._exchange_api=exchange_api
    
    
    def update_markets(self):
        market_list=exchange_api.get_market_list()
        for (c1, c2, market_stats) in market_list:
            market = self.get_market(c1, c2)
            
            if market_stats:
                market.set_market_stats(market_stats)
            else:
                market.update()
    
    
    def get_balances(self):
        return self._exchange_api.get_balances()
    
    def get_balance(self, currency):
        return self._exchange_api.get_balance(currency)
    
    
    def withdraw(self, currency, amount, withdrawal_address):
        return self._exchange_api.withdraw(currency, amount, withdrawal_address)
    
    def get_deposit_address(self, currency):
        return self.get_deposit_address(self, currency)
    
    
    def get_market(self, base_currency, quote_currency):
        
        if not self._exchange_api.is_valid_market(base_currency, quote_currency):
            return None
        
        key=self._get_market_key(base_currency, quote_currency)
        
        if key not in self._markets:
            self._markets[key] = market.Market(self._exchange_api, base_currency, quote_currency)
        
        return self._markets[key]


    def _get_market_key(self, base_currency, quote_currency):
        return str(base_currency) + "_" + str(quote_currency)
    
    
    def get_api():
        return self._exchange_api
    
    def __str__(self):
        return str(self._exchange_api)
    
    
    

#initialize a bunch of exchanges we might use
BITTREX = Exchange(bittrex.BittrexAPI())
ETHER_DELTA = Exchange(ether_delta.EtherDeltaAPI())
GATE_IO = Exchange(gate_io.GateIOAPI())
HUOBI = Exchange(huobi.HuobiAPI())
POLONIEX = exchange.Exchange(poloniex.PoloniexAPI())
STELLAR = exchange.Exchange(stellar.StellarAPI())
STRONGHOLD = exchange.Exchange(stronghold.StrongholdAPI())
LIQUI = exchange.Exchange(liqui.LiquiAPI())

        
    