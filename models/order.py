
ORDER_TYPE_BUY="BUY"
ORDER_TYPE_SELL="SELL"

#used to quickly grab the opposite order type
OTHER_ORDER_TYPE={
    ORDER_TYPE_BUY : ORDER_TYPE_SELL,
    ORDER_TYPE_SELL : ORDER_TYPE_BUY
}

class Order:

    exchange_name=None
    order_type=None
        
    base_currency=None
    quote_currency=None
    price=None 
    
    initial_quantity=None
    quantity_remaining=None
    
    order_id=None
    opened_timestamp=None

    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def __eq__(self, other):
        if (isinstance(self, other.__class__) 
            and self.order_id 
            and other.order_id):
                
            return self.order_id == other.order_id
        
        return super().__eq(self, other)

    
    def __str__(self):
        #example
        # Bittrex: SELL ETH @ 0.15 BTC
        
        ret = (
            str(self.exchange_name) + ": " + self.order_type + " " + str(self.initial_quantity) + " " + self.base_currency 
            + " @ " + str(self.price) + " " + self.quote_currency
        )
        
        if self.order_id:
            ret += " id: " + str(order_id)
        
        return ret
        