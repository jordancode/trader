

class Currency:
    
    def __init__(self, name, default_ticker):
        self._name = name
        self._default_ticker = default_ticker
    
    @property
    def name(self):
        return self._name
    
    @property
    def default_ticker(self):
        return self._default_ticker
    
    def __str__(self):
        return self._name
    

BTC = Currency("Bitcoin", "BTC")
ETH = Currency("Ether", "ETH")
LTC = Currency("Litecoin", "LTC")
XLM = Currency("Stellar Lumens", "XLM")
MOBI = Currency("Mobius", "MOBI")