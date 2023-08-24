# Blockchain-Mining-Simulation

A simulation of competitive blockchain mining between two miners, Alice and Bob. The project demonstrates proof-of-work based mining competition, block validation, and real-time inter-miner communication using PubNub.

# Description
This project was developed as part of the CSCI 301 course assignment. The main objective is to simulate the race between two miners, Alice and Bob, as they compete to add new blocks to a blockchain. The miners utilize the proof-of-work concept to validate and append blocks. Real-time communication and block announcements between the miners are achieved using the PubNub system.

# Key Components
blockchain.py: Contains the core blockchain logic, defines the Block and Blockchain classes, and manages block creation, appending, and validation.
config.py: Houses the configuration settings for PubNub communication.
alice.py: Simulates Alice's mining activities.
bob.py: Simulates Bob's mining activities.
Execution Instructions
To simulate the mining competition:

# Open two separate terminals.
Ensure you're in the WaiYanZawTin_Assignment3 directory.
In the first terminal, run alice.py.
In the second terminal, run bob.py.
Expected Outcome: Both miners will start their mining operations, competing to append new blocks to the blockchain. The miners will announce found blocks to the shared Channel-Barcelona on PubNub. Upon hearing an announcement, the competing miner will validate and, if valid, add the block to their blockchain before continuing to mine the subsequent block.

# Program Logic
Both miners start with a genesis block. Upon initialization, Alice and Bob compete to append a new block using proof-of-work. They attempt to find a nonce for the new block which satisfies a specific SHA256 condition. Alice begins her nonce search from 0, while Bob starts from 1,000,000,000. If either miner discovers a valid nonce for a new block, they broadcast it using PubNub. After a mining process concludes, miners validate and add any newly discovered blocks before proceeding.

For testing, the project uses a relatively lower difficulty level to expedite block mining and PubNub communication. Sample mined blocks, ranging from the genesis block to block10.txt, are included.