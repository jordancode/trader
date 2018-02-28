from models import strategy
from models import history
from models import exchange

class CrashBot(strategy.Strategy):
    
    @classmethod
    def get_parameters(cls):
        return [
            ("exchange", exchange.Exchange, "Exchange to use for trading"),
            ("base_currency", currency.Currency, "Currency to accumulate"),
            ("quote_currency", currency.Currency, "Currency to buy it with"),
            ("amount", float, "How much currency (in base_currency units) to accumulate on crash."),
            ("down_tolerance", float, "How much (in percent) of a fall are we looking for"),
            ("up_tolerance", float, "How much (in percent) of a raise are we looking for"),
            ("interval_secs", int, "Number of seconds before") 
        ]
    
        
    
    def _do_run(self):
        
        # if we haven't purchased any of the desired currency in the desired
        # market within interval ts
        market=self._get_market()
        
        last_trade_ts = history.TradeHistory().get_last( market )
        
        if datetime.datetime.now() - last_trade_ts > self.interval:
            market.buy_market(self.amount)
    
    def _get_market(self):
        return self.exchange.get_market(self.base_currency, self.quote_currency)
    
    def get_exchanges(self):
        return [self.exchange]
    
    def get_markets(self):
        return [self._get_market()]
        
    
    def _get_key(self):
        return (
            self.__class__.__name__ + "_" + 
            str(self.exchange) + "_"  +
            str(self.base_currency) + "-" + 
            str(self.quote_currency) + "_" +
            str(self.amount) + "_" + 
            str(self.interval)
        )