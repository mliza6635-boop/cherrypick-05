#!/usr/bin/env python3
"""
Simple Python Configuration Checker
BUG: This does not yet check whether APP_ENV is set.
"""
import os


def main():
    print("Checking configuration...")
    # TODO: check whether APP_ENV exists and exit(1) if missing
    app_env = os.environ.get("APP_ENV")
    print("Configuration OK")


if __name__ == "__main__":
    main()
