#!/usr/bin/env python3
"""
Google Dorks Generator — ibramoha2/osint-toolkit
Generates OSINT dorks for a target domain.
Usage: python dork_gen.py -t example.com
"""

import argparse

def generate_dorks(target):
    dorks = [
        f'site:{target}',
        f'site:{target} filetype:pdf',
        f'site:{target} filetype:xls OR filetype:xlsx',
        f'site:{target} intitle:"index of"',
        f'site:{target} inurl:admin',
        f'site:{target} inurl:login',
        f'site:{target} inurl:wp-admin',
        f'site:{target} inurl:config',
        f'site:{target} "password" OR "passwd" filetype:txt',
        f'site:{target} inurl:.git',
        f'site:{target} inurl:.env',
        f'"{target}" site:pastebin.com',
        f'"{target}" site:github.com',
        f'"{target}" email OR contact',
        f'link:{target}',
    ]
    return dorks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Dorks Generator")
    parser.add_argument("-t", "--target", required=True, help="Target domain")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()

    dorks = generate_dorks(args.target)
    print(f"\n[*] Google Dorks for: {args.target}\n{'='*50}")
    for d in dorks:
        print(d)

    if args.output:
        with open(args.output, "w") as f:
            f.write("\n".join(dorks))
        print(f"\n[+] Saved to {args.output}")
