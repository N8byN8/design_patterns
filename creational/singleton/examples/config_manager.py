import json

class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.config = {}

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def get_setting(self, key):
        return self.config.get(key)
    
if __name__ == "__main__":
    sample_config = {
        "database": 1
    }

    with open ("creational/singleton/examples/sample_config.json", "w") as f:
        json.dump(sample_config, f)

    config1 = ConfigManager()
    config2 = ConfigManager()

    config1.load_config("creational/singleton/examples/sample_config.json")
    print(config1.get_setting("database"))
    print(config2.get_setting("database"))