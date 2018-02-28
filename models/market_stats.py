
class MarketStats:
    
    high=None
    low=None
    last=None
    quote_volume=None
    base_volume=None
    last_day_change=None
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)