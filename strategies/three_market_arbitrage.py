from models import strategy

class Arbitrage(strategy.Strategy):
    
    @classmethod
    def get_parameters(cls):
        return [
            ("max_trade_amount", float, "Max amount of currency to trade in Bitcoin to mitigate risk."),
            ("min_profit_margin", float, "Minimum ratio of profit to trigger trade."),
            ("exchanges", float, "Only arbitrage on these exchanges. If None, use any exchange"),
            ("markets", float, "Only arbitrage on these markets. If None, use any market"),
        ]
        
    
    def _do_run(self):
        
        # if we haven't purchased any of the desired currency in the desired
        # market within interval ts
        pass
    
    
    def _get_key(self):
        return (
            self.__class__.__name__
        )