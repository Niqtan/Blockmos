# This program is for running the blockchain simulation via the flask API

from blockchain import Blockchain
from coin import Coins

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
blockchain = Blockchain()
wallet = Coins()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/vote")
def vote():
    return render_template("vote.html", chain=blockchain.chain)

previous_block = blockchain.chain
no_votes = 0

@app.route("/validate_vote", methods=["POST"])
def validate_vote():
    user_vote = request.form.get("vote")

    if user_vote == "approve":
        blockchain.validate_vote(previous_block)
        no_votes += 1

        miner_id = len(blockchain.chain) + 1
        print(f"{miner_id} approved of the transaction!")
        wallet.reward_miner(miner_address=miner_id)

        return f"{miner_id}'s balance: {wallet.balance}"
    else:
        return redirect(url_for('/'))


@app.route("/add_block", methods=["GET", "POST"])
# Used in order to confirm and add a block
def add_block():
    if request.method == "POST":
        # Look at the last block

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

        tx = {
            "from": request.form.get("from"),
            "to": request.form.get("to"),
            "amount": request.form.get("amount"),
            "purpose": request.form.get("purpose")
        }

        blockchain.add_transaction(tx)
        # Use an api to get the list of transactions? 
        # But how will be able to get a list of transaction?
        # Hash the previous block
        previous_hash = blockchain.hash(previous_block)
        
        # Create a new block
        
        new_block = blockchain.create_block(votes=no_votes, previous_hash=previous_hash)
        print(new_block)

        # Validate the chain

        if blockchain.chain_valid():
            print("Blockchain looks good!")
        else:
            print("Blockchain aint looking so good")

if __name__ == "__main__":
    app.run()