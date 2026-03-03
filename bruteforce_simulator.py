#!/usr/bin/env python3

"""
Brute-force simulator for a single account.

Demonstrates:
- A naive brute-force attack without any protection.
- The same attack with simple rate limiting (account lockout).
"""

import time
from typing import List, Tuple


TARGET_USERNAME = "admin"
TARGET_PASSWORD = "P@ssw0rd!"

# A small list of common / guessable passwords to simulate an attack.
COMMON_PASSWORDS: List[str] = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "P@ssw0rd!",
]


def simulate_without_protection(
    username: str, password: str, guesses: List[str]
) -> Tuple[int, bool]:
    """
    Simulate a naive brute-force attack with no protection.

    Returns a tuple of:
    - attempts: number of tries made
    - success: True if password was found, False otherwise
    """
    print("=== Brute-force WITHOUT protection ===")
    attempts = 0

    for guess in guesses:
        attempts += 1
        print(f"[Attempt {attempts}] Trying username='{username}', password='{guess}'")

        if guess == password:
            print("-> Password cracked!")
            return attempts, True

    print("-> Attack failed. Password not found in list.")
    return attempts, False


def simulate_with_rate_limiting(
    username: str,
    password: str,
    guesses: List[str],
    max_attempts_before_lock: int = 3,
    lockout_seconds: int = 5,
) -> Tuple[int, bool]:
    """
    Simulate brute-force with simple rate limiting.

    After `max_attempts_before_lock` consecutive failures, the account is
    locked for `lockout_seconds` seconds.
    """
    print("\n=== Brute-force WITH protection (rate limiting) ===")
    attempts = 0
    consecutive_failures = 0

    for guess in guesses:
        attempts += 1
        print(f"[Attempt {attempts}] Trying username='{username}', password='{guess}'")

        if guess == password:
            print("-> Password cracked!")
            return attempts, True

        consecutive_failures += 1

        if consecutive_failures >= max_attempts_before_lock:
            print(
                f"-> Too many failed attempts. "
                f"Account locked for {lockout_seconds} seconds."
            )
            time.sleep(lockout_seconds)
            consecutive_failures = 0

    print("-> Attack failed. Password not found in list.")
    return attempts, False


def main() -> None:
    """Entry point for the CLI program."""
    print("Brute-force Simulator")
    print("---------------------")
    print(f"Target account: username='{TARGET_USERNAME}'")

    # Simulation 1: without any protection.
    attempts, success = simulate_without_protection(
        TARGET_USERNAME, TARGET_PASSWORD, COMMON_PASSWORDS
    )
    print(f"\nResult (without protection): attempts={attempts}, success={success}")

    # Simulation 2: with rate limiting / account lockout.
    attempts_protected, success_protected = simulate_with_rate_limiting(
        TARGET_USERNAME, TARGET_PASSWORD, COMMON_PASSWORDS
    )
    print(
        f"\nResult (with protection): attempts={attempts_protected}, "
        f"success={success_protected}"
    )


if __name__ == "__main__":
    main()

