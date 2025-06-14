import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_sensitive_data_exposure(url):
    """Scan for sensitive data exposure"""
    keywords = ["password", "credit card", "ssn", "security number"]
    try:
        response = requests.get(url)
        
        for keyword in keywords:
            if keyword in response.text:
                print(f"Potential sensitive data exposure at: {url}")
                print(f"Keyword found: {keyword}")
                return True
        
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

