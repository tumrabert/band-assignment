# Band Software Engineer Assignment Solutions

Hi! This is my submission for the Band software engineer assignment.

## Folder structure

```
📁 Assignment Files
├── main_q1.py         # Problem 1 solution (Boss Baby)
├── main_q2.py         # Problem 2 solution (Superman)  
├── module.py          # Problem 3 solution (Transaction Client)
├── test_client.py     # Example of how to use Problem 3
├── requirements.txt   # What you need to install
└── readme.md          # This file you're reading
```

## Getting Started

First, install what you need:
```bash
pip install requests
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Problem 1: Boss Baby's Revenge 👶

### How to run it
```bash
python main_q1.py
```

This will run all my tests automatically. You can also use it like this:
```python
from main_q1 import Boss
print(Boss("SRSSRRR"))  # Should print "Good boy"
```

### Test cases I added
- All the examples from the problem
- Edge cases like single characters
- Really big inputs to test performance
- Boss starting with revenge (should be "Bad boy")

## Problem 2: Superman's Chicken Rescue 🐔

### How to run it
```bash
python main_q2.py
```

Or import it:
```python
from main_q2 import Superman
result = Superman(5, 5, [2, 5, 10, 12, 15])  # Returns 2
```

### Test cases I added
- Examples from the problem statement
- Edge cases like zero chickens or zero roof length
- Large inputs to make sure it's fast enough
- Chickens at the same position

## Problem 3: Transaction Client 💰

### What it does
This is a Python class that can:
1. Send transactions to a server
2. Check if a transaction is done
3. Keep checking until it's finished (confirmed or failed)

### My design
I made a `TransactionClient` class with three main methods:
- `broadcast()` - sends a transaction
- `get_transaction_status()` - checks status once
- `monitor_transaction()` - keeps checking until done

### How to use it

#### Quick test:
```bash
python test_client.py
```

#### If you want to test you own code:
```python
from module import TransactionClient
import time

# Make a client
client = TransactionClient()

# Send a transaction
tx_hash = client.broadcast("BTC", 100000, int(time.time()))

# Watch it until it's done
if tx_hash:
    status = client.monitor_transaction(tx_hash)
    print(f"Final result: {status}")
```

### How I handle different statuses
- **PENDING**: Keep waiting and check again later
- **CONFIRMED**: Success! Stop monitoring
- **FAILED**: Failed! Stop monitoring  
- **DNE**: Transaction doesn't exist, something went wrong
- **Network errors**: Stop trying if the connection fails
