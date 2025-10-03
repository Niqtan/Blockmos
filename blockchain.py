# This program creates the blockchain along with validation

#For calculating the hash
import hashlib

import time

class Blockchain:

    # Define the objects of a normal block
    def __init__(self):
        self.chain = []
        # Create the genesis block
        self.create_block(proof_work=1, previous_hash="0")

    # Used to add further blocks
    # Into the chian
    def create_block(self, proof_work, previous_hash):
        block = {
            "proof": proof_work,
            "timestamp": time.time(),
            "previous_hash": previous_hash,
            "index": len(self.chain) + 1,
        }
        block["hash"] = self.hash(block)
        self.chain.append(block)
        return block

    # Used in order to calculate the previous block
    # of the chain
    def calculate_previous_block(self):
        self.chain[-1]

    # The so called
    # proof-of-work (slows down the creation of new blocks)
    # in blockchain systems
    def proof_of_work(self, previous_proof):
        # In order to calculate for the proof-of-work, you need
        # a changing variable (the "nonce") which is needed 
        # for the repeatingly hash block data meets the network's difficulty target
        # TLDR; a puzzle that my computer has to solve to create a valid block
        nonce = 1
        while True:
            guess = f"{previous_proof}{nonce}".encode()

            # Hash that guess
            guess_hash = hashlib.sha256(guess).hexdigest()
            
            if guess_hash[:4] == "0000":
                print(f"Nonce has been found: {nonce}")
                return nonce
            else:
                print("Nonce has not been found yet! You got this lil bro!")
                nonce+=1

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

            current_proof =  current_block['proof']
            previous_proof = previous_block['proof']

            guess = f'{current_proof}{previous_proof}'.encode()

            guess_hash = hashlib.sha256(guess).hexdigest()

            if guess_hash[:4] != "0000":
                return False
            
        return True