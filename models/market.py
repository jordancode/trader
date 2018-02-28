import datetime

class Market:
    
    def __init__(self, exchange_api, base_currency, quote_currency):
        self._exchange_api = exchange_api
        self._base_currency = base_currency
        self._quote_currency = quote_currency

    
    _market_stats_update_ts=None
    _market_stats=None
    
    _order_book_update_ts=None
    _order_book=None
    
    
    @property
    def base_currency(self):
        return self._base_currency
    
    @property
    def quote_currency(self):
        return self._quote_currency
        
    
    def get_base_currency_balance(self):
        return self._exchange_api.get_balance(self._base_currency)
    
    def get_quote_currency_balance(self):
        return self._exchange_api.get_balance(self._quote_currency)
    
    
    
    def get_open_orders(self):
        return self._exchange.get_open_orders(self._base_currency, self._quote_currency)
    
    
    def update(self):
        #asks it's exchange to fetch it's data
        market_stats=self._exchange_api.get_market_stats(self._base_currency, self._quote_currency)
        self.set_market_stats(market_stats)
    
    def set_market_stats(self, market_stats):
        self._market_stats=market_stats
        self._market_stats_update_ts=datetime.datetime.now()
    
    def get_market_stats(self):
        if not self._market_stats:
            self.update()
        
        return self._market_stats    
    
    def update_order_book(self):
        order_book = self._exchange_api.get_order_book(self._base_currency, self._quote_currency)
        self.set_order_book(order_book)
    
    
    def set_order_book(self, order_book):
        self._order_book_update_ts=datetime.datetime.now()
        self._order_book=order_book
    
    def get_order_book(self):
        if not self._order_book:
            self.update_order_book()
        return self._order_book
    
    def buy(self, amount, price):
        return self._place_order(order.BUY, amount, price)
    
    def sell(self, amount, price):
        return self._place_order(order.SELL, amount, price)
    
    def _place_order(self, order_type, amount, price):
        if self.can_place_order(order_type, amount, price):
            return self._exchange_api.place_order(order_type, self._base_currency, self._quote_currency, amount, price)
        
        return False
    
    
    def buy_market(self, amount):
        return self._place_market_order(order.BUY, amount)
    
    def sell_market(self, amount):
        return self._place_market_order(order.SELL, amount)
    
    def cancel_order(self, order):
        self._exchange_api.cancel_order(order)
    
    
    def _place_market_order(self, order_type, amount):
        order_book = self.get_order_book()
        
        matching_orders = order_book.get_matching_orders(order_type, amount)
        
        created_orders=[]
        for order in matching_orders:
            created_orders.append(
                self._place_order(order_type, order.amount, order.price)
            )
        
        return created_orders
        
    
    def can_place_order(self, order_type, amount, price):
        
        if order_type == order_type.BUY:
            self.get_quote_currency_balance() > ( amount * price ) + self.get_fee(order_type, amount, price)
        
    def _get_fee(self, order_type, amount, price):
        is_taker=self._is_order_taker(order_type, amount, price)
        
        if is_taker:
            return self._exchange_api.get_taker_fee(self._base_currency, self._quote_currency, amount)
        else:
            return self._exchange_api.get_maker_fee(self._base_currency, self._quote_currency, amount)
    
    def _is_order_taker(order_type, amount, price):
        order_book=self.get_order_book() 
        matching_orders=order_book.get_matching_orders(order_type, amount, price)
        if len(matching_orders):
            return True
        
        return False
    
    
    def __str__(self):
        return str(self._exchange) + ":" + str(self._base_currency)  + "-" + str(self._quote_currency)
        
    
    