import requests
from requests.exceptions import ConnectionError, HTTPError
def scan_broken_authentication(url):
    """Scan for broken authentication vulnerabilities"""
    login_attempts = [
        {"username": "admin", "password": "admin"},
        {"username": "admin", "password": "password"},
        {"username": "admin", "password": "123456"},
    ]
    try:
    	for attempt in login_attempts:
           response = requests.post(url, data=attempt)
           if "Welcome" in response.text or "Dashboard" in response.text:
             print(f"Broken Authentication detected at {url} with credentials {attempt}")
             return True
           return False
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False
  
