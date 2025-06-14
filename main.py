import sys

import os
from scanners.XXE_scanner import scan_xxe
from scanners.broken_access_control_scanner import scan_broken_access_control
from scanners.broken_authentication_scanner import scan_broken_authentication
from scanners.insecure_deserialization_scanner import scan_insecure_deserialization
from scanners.insufficient_logging_scanner import scan_insufficient_logging
from scanners.known_vulnerabilities_scanner import scan_known_vulnerabilities
from scanners.security_misconfiguration_scanner import scan_security_misconfiguration
from scanners.senstive_data_exposure_scanner import scan_sensitive_data_exposure
from scanners.sql_injection import scan_sql_injection
from scanners.xss_scanner import scan_xss

def main(url):
    print("This test has been run by Zeydi Meyssa ")

    print("\nChecking for SQL Injection vulnerability...")
    if not scan_sql_injection(url):
        print("No SQL Injection vulnerability found in URL:")

    print("\nChecking for XSS vulnerability...")
    if not scan_xss(url):
        print("No XSS vulnerability found in the forms.")

    print("\nChecking for Broken Authentication...")
    if not scan_broken_authentication(url):
        print("No Broken Authentication detected on the page.")

    print("\nChecking for Sensitive Data Exposure...")
    if not scan_sensitive_data_exposure(url):
        print("No Sensitive Data Exposure detected for the following patterns:")

    print("\nChecking for XXE vulnerability...")
    if not scan_xxe(url):
        print("No XXE vulnerability detected on the page.")

    print("\nChecking for Security Misconfiguration...")
    if not scan_security_misconfiguration(url):
        print("No Security Misconfiguration detected on the page.")

    print("\nChecking for Broken Access Control...")
    if not scan_broken_access_control(url):
        print("No Broken Access Control detected at:")

    print("\nChecking for Insecure Deserialization...")
    if not scan_insecure_deserialization(url):
        print("No Insecure Deserialization detected on the page.")

    print("\nChecking for use of Components with Known Vulnerabilities...")
    if not scan_known_vulnerabilities(url):
        print("No use of Components with Known Vulnerabilities detected on the page.")

    print("\nChecking for Insufficient Logging & Monitoring...")
    if not scan_insufficient_logging(url):
        print("No Insufficient Logging & Monitoring detected on the page.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    main(target_url)

