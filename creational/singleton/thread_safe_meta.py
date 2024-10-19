import threading

class ThreadSafeSingletonMeta(type):
    _instances = {} # track different types of singleton
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=ThreadSafeSingletonMeta):
    def some_business_logic(self):
        pass
    
if __name__ == "__main__":
    # Simulate multiple threads calling the singleton object

    def get_singleton_instance():
        s = Singleton()
        print(s)
        s.some_business_logic()
    
    threads = []
    for i in range(10):
        t = threading.Thread(target=get_singleton_instance)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
