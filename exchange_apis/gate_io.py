from models import order_book
from models import order
from models import currency
from models import market_stats
from vendor import gate_io_api
import secrets


class GateIOAPI(ExchangeAPI):
    
    _trade_client=None
    _query_client=None
    
    def _get_client(self, for_trade=False):
        apiKey=secrets.GATE_IO_API_KEY
        apiKey=secrets.GATE_IO_SECRET_KEY
        
        if for_trade:
            if not self._trade_client:
                self._trade_client = gate_io_api.GateIO(gate_io_api.API_TRADE_URL, apiKey, secretKey)
            return self._trade_client
        else:
            if not self._query_client:
                self._query_client = gate_io_api.GateIO(gate_io_api.API_QUERY_URL, apiKey, secretKey)
            return self._query_client
    
    
    #returns a list of currency pair tuples with optional stats and order book
    def get_market_list(self) -> list(tuple(currency.Currency, currency.Currency, market_stats.MarketStats)):
        pass

    
    def get_market_stats(self, base_currency, quote_currency) -> market_stats.MarketStats:
        pass
    
    
    def get_order_book(self, base_currency, quote_currency) -> order_book.OrderBook:
        pass

    
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
        return "Gate_io"

    
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