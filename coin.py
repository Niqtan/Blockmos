# This program distributes the coins to the user
class Coins:
    
    def __init__(self):
        self.balance = []

    # Reward the miner
    # when they contribute to validating
    # the financial transaction
    def reward_miner(self, miner_address):
        amount = 0
        transaction = {
            'from': 'System',
            'to': miner_address,
            
            # Block reward = block subsidy (3.125 as per 2024 consensus) + 1 (as fixed total transactional fees)
            'amount': amount + 4.125
        }
        
        self.balance.append(transaction['amount'])

