class FibCalculator:
    def __init__(self, cache=None):
        if cache is not None:
            self.cache=cache
        else:
            self.cache={}

            
    def fib(self, n):
        if n in self.cache:
            return self.cache[n]
        elif n <= 2:
            return 1
        else:
            ret = self.fib(n-1) + self.fib(n-2)
            self.cache[n] = ret
            return ret

