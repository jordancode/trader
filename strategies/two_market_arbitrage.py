from models import strategy
from models import market

class Two_Market_Arbitrage(strategy.Strategy):
    
    @classmethod
    def get_parameters(cls):
        return [
            ("max_trade_amount", float, "Max amount of currency to trade in Bitcoin to mitigate risk."),
            ("min_profit_margin", float, "Minimum ratio of profit to trigger trade."),
            ("markets", list(market.Market), "Market pair to arbitrage"),
        ]
        
    
    def _do_run(self):
        pass
        
        
        
        
        
    def get_arbitrage_opportunities(self):
        m1 = self.markets[0]
        m2 = self.markets[1]
        
        if m1.
    
    
    
    def _get_key(self):
        return (
            self.__class__.__name__
        )