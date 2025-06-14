import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_insufficient_logging(url):
    """Scan for insufficient logging and monitoring"""
    try:
        response = requests.get(url)
        if "log" not in response.text.lower():
            
            return False
        
        print("Insufficient Logging & Monitoring detected on the page.")
        return True
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False
    
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

