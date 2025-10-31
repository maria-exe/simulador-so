class SystemClock: 
    def __init__(self):
        self._current_tick = 0

    def tick(self): 
        self._current_tick += 1 

    @property
    def current_time(self):
        return self._current_tick