from models import order_book
from models import order
from models import currency
from models import market_stats


class ExchangeAPI:
    """
        Interface for implementing various exchanges
        should encapsulate all exchange-dependent features,
        rest of application is exchange agnostic
    """
    
    _currency_pairs=None
    
    #returns a list of currency pair tuples with optional stats and order book
    def get_market_list(self) -> list(tuple(currency.Currency, currency.Currency, market_stats.MarketStats)):
        pass

    
    def get_market_stats(self, base_currency, quote_currency) -> market_stats.MarketStats:
        pass
    
    
    def get_order_book(self, base_currency, quote_currency) -> order_book.OrderBook:
        pass
    
    
    def is_valid_market(self, base_currency, quote_currency) -> bool:
        #can also try to pull from server, this should be quicker if run more than once
        if not self._currency_pairs:
            self._currency_pairs=[]
            server_market_list = self.get_market_list()
            for (c1, c2, ms) in  server_market_list:
                self._currency_pairs.append((base_currency,quote_currency))
        
        return (base_currency, quote_currency) in self._currency_pairs
    
    def get_open_orders(self, base_currency, quote_currency) -> list(order.Order):
        pass

    #deposits, withdrawals

    
    def get_deposit_address(self, currency) -> str:
        return None
    
    def get_deposit_max(self, currency) -> float:
        pass
    
    def get_withdrawal_max(self, currency) -> float:
        pass
    
    def get_balances(self) -> list(curreny.Currency, float):
        pass
    
    def get_balance(self, currency) -> float:
        pass
    
    def withdraw(self, currency, amount, address):
        pass
    




    #trading

    def get_maker_fee(self, base_currency, quote_currency, amount) -> float:
        pass
    
    def get_taker_fee(self, base_currency, quote_currency, amount) -> float:
        pass
        
    
    def place_order(self, order_type, base_currency, quote_currency, amount, price) -> order.Order:
        pass
    
   
    def cancel_order(self, order) -> bool:
        pass
    
    
    def __str__(self):
        pass
    
    
    
    def _get_ticker_for_currency(self, currency):
        cm = self._get_currency_map()
        if currency in cm:
            return currency[cm]
        
        return currency.default_ticker
    
    def _get_currency_map(self):
        #here's an example mapping
        #exchanges sometimes have their own tickers for things
        # i.e. XBT vs BTC
        #can override those here
        
        return {
            currency.BTC : currency.BTC.default_ticker,
            currency.ETH : currency.ETH.default_ticker,
            currency.LTC : currency.LTC.default_ticker
        }