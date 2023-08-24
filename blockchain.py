import hashlib
import time

class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()
        return self.nonce

class Blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        return genesis_block

    def add_block(self, block):
        if self.is_valid_new_block(block, self.chain[-1]):
            self.chain.append(block)

    def is_valid_new_block(self, new_block, previous_block):
        if previous_block.hash != new_block.previous_hash:
            return False
        if not self.is_valid_hash(new_block):
            return False
        return True
    
    def is_valid_hash(self, block):
        return (block.hash == block.compute_hash())  # Additional validations can be added
