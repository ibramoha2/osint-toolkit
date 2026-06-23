#!/usr/bin/env python3
"""
DNS Enumeration Module — ibramoha2/osint-toolkit
Usage: python dns_enum.py -d example.com
"""

import dns.resolver
import argparse
import sys

SUBDOMAINS = ["www", "mail", "ftp", "admin", "vpn", "api", "dev",
              "staging", "test", "portal", "webmail", "ns1", "ns2"]

def resolve(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(r) for r in answers]
    except:
        return []

def enumerate_dns(domain):
    print(f"\n[*] DNS Enumeration: {domain}\n{'='*50}")

    for rtype in ["A", "MX", "NS", "TXT", "AAAA"]:
        results = resolve(domain, rtype)
        if results:
            print(f"[+] {rtype} records:")
            for r in results:
                print(f"    {r}")

    print(f"\n[*] Subdomain bruteforce...")
    found = []
    for sub in SUBDOMAINS:
        target = f"{sub}.{domain}"
        results = resolve(target, "A")
        if results:
            print(f"[+] {target} -> {results[0]}")
            found.append(target)

    print(f"\n[*] Found {len(found)} subdomains")
    return found

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Enumeration Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    args = parser.parse_args()
    enumerate_dns(args.domain)
