import requesets
from models import exchange_api

class Bittrex(exchange_api.ExchangeAPI):
    
    
    
    def get_maker_fee(self, base_currency, quote_currency):
        pass
    
    def get_taker_fee(self, base_currency, quote_currency):
        pass
    
    
    def get_market_list(self):
        market_configs = self._get_http().get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    
    
    def can_withdraw(self):
        return True
    
    def can_deposit(self):
        return True
    
    
    def is_valid_market(self, base_currency, quote_currency):
        return True
   
    
    def _get_deposit_address(self, ticker):
        self._get_http().post("https://bittrex.com/api/v1.sal1/account/getdepositaddress?apikey=" + config.BITTREX_API_KEY  + "&currency="+ticker)
            
    
    def _withdraw(self, withrawal_address, currency_ticker, quantity):
        
        params={
            "apikey":config.BITTREX_API_KEY,
            "currency":currency_ticker,
            "quantity":str(quantity),
            "address":withrawal_address
        }
        
        self._get_http().post("https://bittrex.com/api/v1.1/account/withdraw", params)
        
    
    
    
    def _cancel_order(self, order):
        self._get_http().post("https://bittrex.com/api/v1.1/market/cancel?apikey=" + config.BITTREX_API_KEY + "&uuid="+order.identifier)
        
    
    def _get_balance_for_ticker(self, ticker):
        temp_balances=self._get_http().get("https://bittrex.com/api/v1.1/account/getbalances?apikey="+config.BITTREX_API_KEY)
        self._balances[ticker]=value
        
        return self._balances[ticker]
           
    
    def get_order_book(self, base_ticker, quote_ticker):
        self._get_http().get("https://bittrex.com/api/v1.1/public/getorderbook?market="+base_ticker+"-"+quote_ticker+"&type=both")
        
    
    def place_order(self, base_currency, quote_currency, order_type, amount, price) -> order.Order:
        
        if order.BUY:
            self._get_http().post("https://bittrex.com/api/v1.1/market/buy?apikey=" + config.BITTREX_API_KEY + "&uuid="+order.identifier)
        elif order.SELL:
            self._get_http().post("https://bittrex.com/api/v1.1/market/sell?apikey=" + config.BITTREX_API_KEY + "&uuid="+order.identifier)
        