#!/usr/bin/env python3
"""
Simple Python Configuration Checker
BUG: This does not yet check whether APP_ENV is set.
"""
import os


def main():
    print("Checking configuration...")
    app_env = os.environ.get("APP_ENV")
    if not app_env:
        print("Error: APP_ENV is not set")
        exit(1)
    print("Configuration OK")

if __name__ == "__main__":
    main()
