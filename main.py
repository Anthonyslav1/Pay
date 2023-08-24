import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the blockhash."""
        return hashlib.sha256((
            str(self.index) + str(self.timestamp) + str(self.transactions) + self.previous_hash
        ).encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block = Block(0, datetime.datetime.now(), [], "")
        self.chain.append(self.genesis_block)

    def view_all_blocks(self):
        """Returns all blocks in the chain."""
      
        return self.chain

    def mine(self):
        """Simulates mining using a PoW."""
        # A nonce that makes the block hash start with 0000
        for nonce in range(1000000):
            block = Block(len(self.chain), datetime.datetime.now(), [], self.chain[-1].hash)
            block.hash = block.calculate_hash()
            if block.hash.startswith("0000"):
                self.chain.append(block)
                return block


def main():
    blockchain = Blockchain()
    
    blockchain.mine()
    blockchain.mine()
    blockchain.mine()
    blockchain.mine()
    block = blockchain.mine()
    print("Current Block", block)
    print("This is the genesis block", blockchain.genesis_block)
    print("Current hash is ", block.hash)
    print("previous hash is ", block.previous_hash)
    print("All Blocks", blockchain.chain)
if __name__ == "__main__":
    main()
