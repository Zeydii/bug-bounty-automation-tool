import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_security_misconfiguration(url):
    """Scan for common security misconfigurations"""
    try:
        response = requests.get(url)
        headers = response.headers
        missing_headers = []
        required_headers = [
            "Content-Security-Policy", 
            "Strict-Transport-Security", 
            "X-Content-Type-Options",
            "X-Frame-Options", 
            "X-XSS-Protection"
        ]
        
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)
        
        if missing_headers:
            print(f"Security Misconfiguration detected: Missing headers - {', '.join(missing_headers)}")
            return True
        
        
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False
    
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

