## Implimenting a hash map to store and retrive customer balances.

class Account:
    "This represents a customer account record."
    
    def __init__(self, account_number: str, name: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __repr__(self) -> str:
        # Formats output as: Account(NX-002, Bob, $450)
        formatted_balance = (
            f"{int(self.balance):,}"
            if self.balance.is_integer()
            else f"{self.balance:,.2f}"
        )
        return f"Account({self.account_number}, {self.name}, ${formatted_balance})"
    
class CustomHashMap:
    "Storing customer accounts indexed by alphanumeric account numbers and it uses Separate Chaining (nested lists) for collision resolution."

    def __init__(self, capacity: int = 1009):
        self.capacity = capacity
        # Initialize array of buckets (Separate Chaining)
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash_function(self, account_number: str) -> int:
        "Computes a bucket index from an account number string.Polynomial rolling hash with prime multiplier 31."
        hash_value = 0
        prime_multiplier = 31

        for char in account_number:
            hash_value = (hash_value * prime_multiplier + ord(char)) % self.capacity

        return hash_value
    
    def insert(self, account: Account) -> None:
        "Inserts or updates an account in average O(1) time."
        index = self._hash_function(account.account_number)
        bucket = self.buckets[index]

        for i, existing_account in enumerate(bucket):
            if existing_account.account_number == account.account_number:
                bucket[i] = account  # Update existing
                return

        bucket.append(account)  # Insert new record

    def lookup(self, account_number: str):
        "Retrieves account or returns None if not found in average O(1) time."
        index = self._hash_function(account_number)
        bucket = self.buckets[index]

        for account in bucket:
            if account.account_number == account_number:
                return account

        return None

    def delete(self, account_number: str) -> bool:
        "Removes account from registry. Returns True if deleted, False otherwise."
        index = self._hash_function(account_number)
        bucket = self.buckets[index]

        for i, account in enumerate(bucket):
            if account.account_number == account_number:
                del bucket[i]
                return True

        return False
    
# TYPE SCRIPT: The above code defines a simple hash map implementation for storing and retrieving customer account records.
# It uses separate chaining to handle collisions, allowing multiple accounts to be stored in the same bucket.
# The `Account` class represents individual customer accounts, while the `CustomHashMap` class provides methods for inserting, looking up, and deleting accounts based on their account numbers.

if __name__ == "__main__":
    print("-Initializing Custom Hash Map-")
    registry = CustomHashMap(capacity=10)

    # 1. Inserting test accounts.
    account1 = Account("NX-001", "Alice",  1200)
    account2 = Account("NX-002", "Bob",  450)
    account3 = Account("NX-003", "Carol",  8900)
    
    #2. Insert accounts into the registry
    registry.insert(account1)
    registry.insert(account2)
    registry.insert(account3)
    print("Inserted: Alice, Bob, Carol\n")

    # 3. Lookup NX-002 "Bob's account"
    result_lookup_1 = registry.lookup("NX-002")
    print(f"Lookup NX-002  -->  {result_lookup_1}")

    # 4. Delete NX-001 "Alice's account"
    result_delete = registry.delete("NX-001")
    print(f"Delete NX-001  -->  {result_delete}")

    # 5. Lookup NX-001 "Alice's account" after deletion
    result_lookup_2 = registry.lookup("NX-001")
    print(f"Lookup NX-001  -->  {result_lookup_2}")