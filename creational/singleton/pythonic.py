class PythonicSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    s1 = PythonicSingleton()
    print(s1.__repr__)
    s2 = PythonicSingleton()
    print(s2.__repr__)
