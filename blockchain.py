# This program creates the blockchain along with validation

#For calculating the hash
import hashlib

import time

class Blockchain:

    # Define the objects of a normal block
    def __init__(self):
        self.pending_transactions = []
        self.chain = []
        # Create the genesis block
        self.create_block(votes=0, previous_hash="0")

    # Used to add further blocks
    # Into the chian
    def create_block(self, votes, previous_hash):
        block = {
            'timestamp': time.time(),  
            'votes': votes,
            'data': self.pending_transactions, 
            'previous_hash': previous_hash,
            'index': len(self.chain) + 1,
        }
        self.chain.append(block)
        return block

    # The so called
    # proof-of-work (slows down the creation of new blocks)
    # in blockchain systems
    # However, the proof-of-work
    # will be the contribution that the miner puts in
    # in order to validate a transaction
    def add_transaction(self, transaction):
        self.pending_transactions.append(
            transaction
        )

    # Used for calculating the hash
    # of a block 
    def hash(self, block):
        block_contents = str(block).encode()
        return hashlib.sha256(block_contents).hexdigest()
    
    def validate_vote(self, block):
        nonce = 1
        block_data = str(block)
        while True:
            guess = f"{block_data}{nonce}".encode()

            # Hash that guess
            guess_hash = hashlib.sha256(guess).hexdigest()
            
            if guess_hash[:4] == "0000":
                print(f"Nonce has been found: {nonce}")
                return nonce
            else:
                print("Nonce has not been found yet! You got this lil bro!")
                nonce+=1

            
    # Used for validating the contents
    # of the blockchain 
    # if it meets the right conditions
    def chain_valid(self):
        # Check if the previous_hash is the same as the hash of the current block

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block['previous_hash'] != self.hash(previous_block):
                print("Chain is broken... mayday! mayday!")
                return False
            
        return True