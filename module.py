import requests
import json
import time

class TransactionClient:
    """
    A simple client to send transactions and check status.
    """
    BASE_URL = 'https://mock-node-wgqbnxruha-as.a.run.app'

    def __init__(self, base_url=None):
        """
        Sets up the client with BASE URL.
        """
        if base_url:
            self.BASE_URL = base_url
        print(f"TransactionClient initialized. Using base URL: {self.BASE_URL}")

    def broadcast(self, symbol: str, price: int, timestamp: int):
        """
        Sends a transaction to the server.

        Args:
            symbol (str): The crypto symbol for example 'BTC','SOL','ETH','BNB' etc.
            price (int): The price like 100000
            timestamp (int): When the price was taken
        Returns:
            str: Transaction hash if it works, None if it fails
        """
        data = {
            "symbol": symbol,
            "price": price,
            "timestamp": timestamp
        }
        headers = {'Content-Type': 'application/json'}
        url = f'{self.BASE_URL}/broadcast'

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            
            # Check for a successful HTTP status code
            if response.status_code == 200:
                response_data = response.json()
                print(f"Broadcast successful. tx_hash: {response_data.get('tx_hash')}")
                return response_data.get('tx_hash')
            else:
                print(f"Broadcast failed with status code {response.status_code}: {response.text}")
                return None
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def get_transaction_status(self, tx_hash: str):
        """
        Checks whether a transaction is done or still waiting.

        Args:
            tx_hash (str): The transaction ID from broadcast.

        Returns:
            str: Status -> 'CONFIRMED', 'PENDING', 'FAILED', or 'DNE'
        """
        url = f'{self.BASE_URL}/check/{tx_hash}'
        
        try:
            response = requests.get(url)

            if response.status_code == 200:
                response_data = response.json()
                status = response_data.get('tx_status')
                print(f"Status check for {tx_hash}: {status}")
                return status
            else:
                print(f"Failed to retrieve transaction status with status code {response.status_code}: {response.text}")
                return None
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def monitor_transaction(self, tx_hash: str, poll_interval_sec: int = 5):
        """
        Keeps checking a transaction until it's done (CONFIRMED or FAILED).

        Args:
            tx_hash (str): The transaction ID to watch.
            poll_interval_sec (int): How many seconds to wait between checks.

        Returns:
            str: Final status ('CONFIRMED' or 'FAILED'), or None if error.
        """
        print(f"Monitoring transaction {tx_hash}. Will check every {poll_interval_sec} seconds...")
        while True:
            status = self.get_transaction_status(tx_hash)

            if status == 'CONFIRMED':
                print(f"Transaction {tx_hash} is CONFIRMED.")
                return status
            
            elif status == 'FAILED':
                print(f"Transaction {tx_hash} has FAILED.")
                return status
            
            elif status == 'PENDING':
                print("Status is PENDING. Waiting for next poll...") #try again
                time.sleep(poll_interval_sec)
            
            elif status == 'DNE':
                print(f"Error: Transaction {tx_hash} does not exist (DNE). Stopping monitor.")
                return None
            
            else:
                print("Error retrieving status. Stopping monitor.")
                return None

