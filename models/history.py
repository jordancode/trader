import redis 
import config



class TradeHistory(RedisHistory):
    
    def __init__(self, trade_key):
        series_key=self.__class__.__name__+":"+trade_key
        super().__init__(series_key)
    
    

class StrategyRunHistory(RedisHistory):
    
    def __init__(self, strategy):
        series_key=self.__class__.__name__+":"+strategy.get_unique_key()
        super().__init__(series_key)
    
    def record_run(self):
        self.save_event( 1 )
    
    def get_last_run_time(self):
        last_value,last_score = RedisFactory.get().zrange(self._series_key, "inf", "-inf", withscores=1, limit=1)
        
        return last_score
    
        
class BalanceHistory(RedisHistory):
    def __init__(self, currency):
        series_key=self.__class__.__name__+":"+currency.default_ticker
        super().__init__(series_key)
    


class RedisHistory:
    
    def __init__(self, series_key):
        self._series_key=series_key
    
    def save_event(self, value):
        now_ts=self._datetime_to_unix(datetime.datetime.now())
        RedisFactory.get().zadd(self._series_key, now_ts, str(value)+":"+str(now_ts))
    
    def _datetime_to_unix(self, dt):
        return int(time.mktime(dt.timetuple()))
    
    def _unix_to_datetime(self, ts_seconds):
        return datetime.datetime.fromtimestamp(int(ts_seconds))
        
