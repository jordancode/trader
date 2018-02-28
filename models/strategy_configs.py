
class StrategyConfigs:
        
    
    def delete(self, unique_key):
        RedisFactory.get().hdel("strategies",unique_key)
        RedisFactory.get().delete("strategy_params_"+unique_key)
    
    def save(self, strategy):
        
        params=stragegy.get_params()
        unique_key=strategy.get_unique_key()
        
        RedisFactory.get().hset("strategies", unique_key, strategy.__class__.__name__)
        
        param_strings=" ".join( [  k+" "+str(v) for k, v in params ] )
        
        RedisFactory.get().hmset("strategy_params_"+unique_key, param_strings)
    
    
    def get_list(self):
        
        strategy_classes=RedisFactory.get().hgetall("strategies")
        
        for unique_key, strategy_class_name in strategy_classes.items():    
            
            params=RedisFactory.get().hget("strategy_params_"+unique_key)
            cls_=self.get_strategy_class_for_name(strategy_class_name)
            
            strategy = cls_(**params)
            ret.append( strategy )
            
        return strategy_classes
        
    
    
    def get_strategy_class_for_name(self,strategy_class_name):
        cls_=strategy_class_name
        
        class_name = module_name.split(".")[-1]
        class_name = string.capwords(class_name,"_").replace("_","")

        module = importlib.import_module("strategies." + module_name)
        class_ = getattr(module, class_name)
        
        return class_
        
        
        