import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Create the Genesis Block (The first block in the chain)
        self.new_block(previous_hash="00000000000000000000000000000000", proof=100)

    def new_block(self, proof, previous_hash=None):
        """Creates a new Block and adds it to the chain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Adds a new transaction to the list of transactions."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Creates a SHA-256 hash of a Block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains 4 leading zeroes
         - p is the previous proof, and p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?"""
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# --- EXECUTION ---
if __name__ == "__main__":
    ghost_chain = Blockchain()
    print("--- ⛓️ GHOST-NODE: BLOCKCHAIN INITIALIZED ---")
    
    # Simulate Transactions
    print("[*] Adding Transactions...")
    ghost_chain.new_transaction(sender="Samael", recipient="Architect", amount="500 TITAN")
    ghost_chain.new_transaction(sender="Forge", recipient="Inquisitor", amount="10 TITAN")

    # Start Mining
    print("[*] Starting Miner... (Solving Proof of Work)")
    last_proof = ghost_chain.last_block['proof']
    proof = ghost_chain.proof_of_work(last_proof)

    # Forge the new block
    previous_hash = ghost_chain.hash(ghost_chain.last_block)
    block = ghost_chain.new_block(proof, previous_hash)

    print(f"\n[+] BLOCK FORGED: #{block['index']}")
    print(f"    Hash: {previous_hash}")
    print(f"    Proof: {block['proof']}")
    print("-" * 50)
    print("CURRENT CHAIN LEDGER:")
    print(json.dumps(ghost_chain.chain, indent=4))
