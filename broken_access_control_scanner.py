import requests
from urllib.parse import urljoin
from requests.exceptions import ConnectionError, HTTPError

def scan_broken_access_control(url):
    """Scan for broken access control vulnerabilities"""
    sensitive_urls = [
        "/admin", "/admin/login", "/user/profile", "/settings"
    ]
    try:
        for sensitive_url in sensitive_urls:
            target_url = urljoin(url, sensitive_url)
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"Broken Access Control detected at: {target_url}")
                return True
        
        print("No Broken Access Control detected at:")
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False
    
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

