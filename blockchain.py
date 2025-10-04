# This program creates the blockchain along with validation

#For calculating the hash
import hashlib

import time

class Blockchain:

    # Define the objects of a normal block
    def __init__(self):
        self.transactions = []
        self.chain = []
        # Create the genesis block
        self.create_block(proof_work=1, previous_hash="0")

    # Used to add further blocks
    # Into the chian
    def create_block(self, proof_work, previous_hash):
        block = {
            'proof_work': proof_work,
            'timestamp': time.time(),  
            'transactions': self.transactions, 
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
        self.transactions.append({
            'transaction': transaction,
            'votes': [],
        })
        return True

    # Used for calculating the hash
    # of a block 
    def hash(self, block):
        block_contents = str(block).encode()
        return hashlib.sha256(block_contents).hexdigest()

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

        #Fix it if the previous hash == current hash

        # Check if the proof-of-work is valid

            current_proof =  current_block['proof_work']
            previous_proof = previous_block['proof_work']

            guess = f'{previous_proof}{current_proof}'.encode()

            guess_hash = hashlib.sha256(guess).hexdigest()

            if guess_hash[:4] != "0000":
                print("error 2")
                return False
            
        return True