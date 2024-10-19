import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    s1 = ThreadSafeSingleton()
    print(id(s1))
    s2 = ThreadSafeSingleton()
    print(id(s2))
