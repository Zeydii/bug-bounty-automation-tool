import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_insecure_deserialization(url):
    """Scan for insecure deserialization vulnerabilities"""
    try:
        payload = '{"name":"test"}'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 500 and "unserializable" in response.text.lower():
            print(f"Insecure Deserialization vulnerability detected at: {url}")
            return True
        
        
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False
    
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

