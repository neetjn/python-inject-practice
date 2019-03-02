class Database:
    """Some theoretical database provider."""
    data = {}

    def get(self, key: str):
        return self.data.get(key)

    def save(self, key: str, value: all):
        self.data.setdefault(key, value)
