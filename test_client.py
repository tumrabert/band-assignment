from module import TransactionClient
import time
# 1. Initialize the client
client = TransactionClient()

# 2. Broadcast a transaction
# Using dummy data for the example [cite: 94-100]
symbol = "BTC"
price = 100000
timestamp = int(time.time())

tx_hash = client.broadcast(symbol, price, timestamp)

# 3. Monitor the transaction only if broadcast was successful
if tx_hash:
    final_status = client.monitor_transaction(tx_hash, poll_interval_sec=3)
    print(f"\nMonitoring complete. Final status for {tx_hash}: {final_status}")
else:
    print("Broadcast failed. Cannot monitor transaction.")
    
print("\n--- Example Finished ---")
