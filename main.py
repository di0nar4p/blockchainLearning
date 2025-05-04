import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.now(), 'Genesis Block', '0')

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Exemplo de uso
blockchain = Blockchain()

reg = {
    'Data': 'https://bitcoin.org/files/bitcoin-paper/bitcoin_pt_br.pdf'
}


reg2 = {
    'Data': 'https://bitcoin.org/files/bitcoin-paper/bitcoin_pt_br.pdf'
}

reg3 = {
    'Data': 'https://bitcoin.org/files/bitcoin-paper/bitcoin_pt_br.pdf'
}

blockchain.add_block(Block(1, datetime.now(), reg, blockchain.chain[-1].hash))
blockchain.add_block(Block(2, datetime.now(), reg2, blockchain.chain[-1].hash))
blockchain.add_block(Block(3, datetime.now(), reg3, blockchain.chain[-1].hash))


def print_blockchain(chain):
    for block in chain:
        print(f'Block: {block.index}')
        print(f'Timestamp: {block.timestamp}')
        print(f'Data: {block.data}')
        print(f'Hash: {block.hash}')
        print(f'Previous Hash: {block.previous_hash}')
        print(20*'------')




print(print_blockchain(blockchain.chain))


