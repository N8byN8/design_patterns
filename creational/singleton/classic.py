class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    s1 = ClassicSingleton.get_instance()
    print(s1)
    s2 = ClassicSingleton.get_instance()
    print(s2)