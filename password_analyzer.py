#!/usr/bin/env python3
import re
import math
import sys
import argparse
import os

# Entropy calculator
def entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"[!@#$%^&*()_+]", password): charset += 32
    return len(password) * math.log2(charset) if charset else 0

# Basic strength check
def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*()_+]", password): score += 1
    ent = entropy(password)

    if ent > 60:
        return "STRONG"
    elif ent > 40:
        return "MEDIUM"
    else:
        return "WEAK"

# Check against rockyou
def check_leak(password):
    rockyou = "/usr/share/wordlists/rockyou.txt"
    if not os.path.exists(rockyou):
        return "Rockyou not found"
    with open(rockyou, "r", errors="ignore") as f:
        for line in f:
            if password == line.strip():
                return True
    return False

def main():
    parser = argparse.ArgumentParser(
        description="Password Analyzer Tool — Kali Edition (Created by waseem ayamon)"
    )
    parser.add_argument("password", help="Password to analyze", type=str)
    parser.add_argument(
        "--leak", 
        help="Check against rockyou leak database", 
        action="store_true"
    )

    args = parser.parse_args()
    pwd = args.password

    print("\n🔍 Analyzing:", pwd)
    strength = check_strength(pwd)
    print("🔐 Strength:", strength)

    if args.leak:
        leaked = check_leak(pwd)
        print("💥 Leaked?:", "YES" if leaked else "NO")
    print()

if __name__ == "__main__":
    main()
