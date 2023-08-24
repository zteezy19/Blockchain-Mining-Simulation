from blockchain import Block, Blockchain
from config import pubnub  
import threading


TARGET = 2**236

def mine_new_block_from(bob_chain):
    transactions = {"alice": -1, "bob": 1}
    previous_hash = bob_chain.chain[-1].hash
    new_block = Block(transactions, previous_hash)
    new_block.nonce = 1000000000  # Bob starts from 1,000,000,000

    while True:
        new_hash = new_block.compute_hash()
        int_hash = int(new_hash, 16)  # Convert hex to integer
        
        if int_hash < TARGET:
            break  # Found a valid nonce
        
        new_block.nonce += 1
        
    return new_block

def announce_new_block(block):
    data = {
        "new_block": {
            "transactions": block.transactions,
            "previous_hash": block.previous_hash,
            "nonce": block.nonce,
            "hash": block.hash
        }
    }
    pubnub.publish().channel("Channel-Barcelona").message(data).sync()

def mine_forever():
    bob_chain = Blockchain()
    while True:
        new_block = mine_new_block_from(bob_chain)
        announce_new_block(new_block)
        bob_chain.add_block(new_block)

if __name__ == '__main__':
    mining_thread = threading.Thread(target=mine_forever)
    mining_thread.start()
