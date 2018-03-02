import history

class Strategy():
    
    @classmethod
    def get_parameters(cls):
        #returns a mapping of parameter name to type
        #this is used to generate 
        return {
            #( param_name, param_type, param_description )
            #i.e.
            #( "market", market.Market, "The market to make trades on"
        }
        
    def __init__(self, **kwargs):
        #copy arbitrary params the the object
        parameters=self.get_parameters()
        for p in parameters:
            param_name=p[0]
            for param_name, value in kwargs.items():
                setattr(self, param_name, value)
            
    
    def run(self):
        self._do_run()
        self._save_last_run_ts()
        
    def _do_run(self):
        #override
        pass
    
    def get_unique_key(self):
        #this needs to id this strategy by it's class and parameters
        #override
        
        return None
    
    def get_markets(self):
        #override
        return []
    
    def get_exchanges(self):
        #override
        return []
    
    
    def _save_last_run_ts(self):
        history.StrategyRunHistory(self).record_run()
            
            
    
    def _get_last_run_ts(self):
        return history.StrategyRunHistory(self).get_last_run_time()
    
    
    def __str__(self):
        return self.__class__.__name__
    