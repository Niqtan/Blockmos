# This program is for running the blockchain simulation via the flask API

from blockchain import Blockchain

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "skibidi toilet"

@app.route("/new_transaction", methods=["GET", "POST"])
def new_transaction():
    ...

@app.route
def vote():
    ...

@app.route("/add_block")
# Used in order to confirm and add a block
def add_block():
    blockchain = Blockchain()

    while True:
        # Look at the last block

        previous_block = blockchain.chain[-1]
        previous_proof = previous_block['proof_work']
        

        """
        
        Here's the question: 
        how will we make people mine?
        -  The most basic thing is to let miners guess the nonce
        
        However, for this sytem, we want to be able to allow people
        to audit or vote whether if the transaction is valid, thus 
        promoting democracy

        So instead of traditional proof-of-work:
            Users validate by reviewing transactions
            Once a block has enoguh validations/votes, its considered confirmed

        Thus, once the block has been approved, then the system will reward
        coins to those miners.
        
        """
        # Use an api to get the list of transactions? 
        # But how will be able to get a list of transaction?

        # What if we actually give input of the transactions?
        # In order to do that, I guess it would be great to learn forms with flask
        blockchain.transactions = ...
        
        # Genarate a valid proof-of-work
        proof = blockchain.proof_of_work(previous_proof)
        
        # Hash the previous block
        previous_hash = blockchain.hash(previous_block)
        # Create a new block
        
        new_block = blockchain.create_block(proof_work=proof, previous_hash=previous_hash)
        print(new_block)

        # Validate the chain

        if blockchain.chain_valid():
            print("Blockchain looks good!")
        else:
            print("Blockchain aint looking so good")

if __name__ == "__main__":
    app.run()