import chromadb

class MemoryManager:
    def __init__(self):
        # Initialize ChromaDB connection
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("memory")

    def save_memory(self, key, value):
        """Save the memory with a key-value pair."""
        self.collection.add({"key": key, "value": value})

    def search_memory(self, key):
        """Search for memory by key."""
        results = self.collection.query({"key": key})
        return results.get("value", None)

    def utility_function_example(self):
        """An example utility function."""
        pass

# Example usage
if __name__ == "__main__":
    memory_manager = MemoryManager()
    memory_manager.save_memory("example_key", "example_value")
    print(memory_manager.search_memory("example_key"))
