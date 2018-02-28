
class OrderBook:
    
    
    def __init__(self, market, order_list):
        self._market=market
        self._order_list=order_list
    
    def get_spread(self):
        high_buy=self.get_highest_buy_order()
        low_sell=self.get_lowest_sell_order()
        if high_buy and low_sell:
            return low_sell - high_buy
        
        return None
    
    def add_order(self, order):
        self._order_list.append(order)
        
    def remove_order(self, order):
        #match by reference or order_id (overloaded in order.Order)
        self._order_list=[o for o in self._order_list if o != order]
    
    def get_highest_buy_order(self):
        buy_orders=self.get_buy_orders()
        if len(buy_orders):
            return buy_orders[0]
        return None
    
    def get_lowest_sell_order(self):
        sell_orders=self.get_sell_orders()
        if len(sell_orders):
            return sell_orders[0]
        return None
    
    def get_matching_orders(self, order_type_to_match, amount_to_match, limit_price=None):
        #todo, add price logic
        matching_orders=self.get_orders_for_type(order.OTHER_ORDER_TYPE(order_type_to_match))
        
        ret=[]
        total_matched=0
        for mo in matching_orders:
            if total_matched < amount_to_match:
                ret.append(mo)
                total_matched+=mo.amount
            else:
                break
        
        return ret
            
    
    def get_buy_orders(self):
        return self.get_orders_for_type(order.BUY)
    
    def get_sell_orders(self):
        return self.get_orders_for_type(order.SELL)
    
    def get_average_price_for_order_list(self, order_list):
        
        weighted_price=0
        total_amount=0
        
        for order in order_list:
            total_amount+=order.amount
            weighted_price=(order.price*order.amount)
        
        if total_amount:
            return (weighted_price/total_amount)
        
        return None #no average if no amount
            
    
    #return sorted list of orders
    def get_orders_for_type(self, order_type):
        ret = [order for order in self._order_list if order.order_type == order_type]
        ret.sort(key=lambda o: o.price, reverse=(order_type == order.ORDER_TYPE_BUY))
        
        return ret
            
    
    
    
    
    
    