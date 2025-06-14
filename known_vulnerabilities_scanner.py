import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_known_vulnerabilities(url):
    """Scan for use of components with known vulnerabilities"""
    known_vulnerabilities = ["CVE-2021-12345", "CVE-2021-34567"]
    
    try:
        response = requests.get(url)
        
        for vulnerability in known_vulnerabilities:
            if vulnerability in response.text:
                print(f"Use of Components with Known Vulnerabilities detected: {vulnerability}")
                return True
        
       
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False
    
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

