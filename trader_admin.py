
#endpoints


class TraderAdmin():
    
    def add_strategy_config( strategy_class_name, **kwargs ):
        
        strategy_class=self._get_strategy_class_for_name( strategy_class_name )
        params=strategy_class.get_parameters()
        strategy=strategy_class(params)
        
        StrategyConfigs().delete(strategy_unique_key)
        
        return JSONResponse({"success" : True})
        
    
    def delete_strategy_config( strategy_unique_key ):
        StrategyConfigs().delete(strategy_unique_key)
        return JSONResponse({"success" : True})
    
    def get_current_strategies():
        strategy_list=StrategyConfigs().get_all()
        return JSONResponse({"strategy_list" : strategy_list})
    
    def get_exchange_list(self):
        return JSONResponse({"exchange_list" :config.EXCHANGES})
    
    def get_history_stats( history_type, start_ts, end_ts ):
        pass

    

    def __call__(self, environ, start_response):
        #route to correct method with configs
        pass
    


app = TraderAdmin()