# Ghost-Node: Cryptographic Blockchain Core ⛓️

A minimalist, high-integrity private blockchain implemented in Python. This system demonstrates the fundamental principles of decentralized ledgers, including **SHA-256 Hashing**, **Proof-of-Work (PoW)** consensus, and **Immutable Linking**.

## 🧠 Core Architecture
* **Block Structure:** Each block contains an index, timestamp, list of transactions, a proof (nonce), and the cryptographic hash of the previous block.
* **Consensus Mechanism:** Implements a Proof-of-Work algorithm where miners must solve a computational puzzle (finding a hash with 4 leading zeroes) to validate and add new blocks.
* **Immutability:** Because each block's hash depends on the `previous_hash`, altering a single transaction in the past would invalidate all subsequent blocks.



## 🛠️ Technology Stack
* **Language:** Python 3.12 (Standard Library)
* **Hashing:** SHA-256
* **Data Format:** JSON-serialized dictionaries

## 🚀 Usage
1.  **Clone the Repository.**
2.  **Run the Node:**
    ```bash
    python blockchain_core.py
    ```
3.  **Observation:** The system will initialize the "Genesis Block," add simulated transactions, and then begin the mining process to forge a new block.
