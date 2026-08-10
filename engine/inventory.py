from .base_memory import BaseMemory


class Inventory(BaseMemory):
    FILE = "inventory.md"


inventory = Inventory()