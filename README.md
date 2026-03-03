# Brute-force Simulator

This small Python CLI program demonstrates a basic password brute-force attack against a single account, both **without protection** and **with simple rate limiting**.

## Features

- **Hardcoded credentials**: a single target account (`admin` / `P@ssw0rd!`).
- **Common password list**: iterates over several likely passwords.
- **Without protection**:
  - Tries each password and prints every attempt.
  - Reports how many attempts it took to crack the password (if found).
- **With protection (rate limiting)**:
  - After 3 consecutive failed attempts, the "account" is locked for 5 seconds.
  - Continues after the lockout and again reports attempts and success.

## Requirements

- Python 3.7 or newer.

No external dependencies are required.

## Usage

From the `bruteforce` directory, run:

```bash
python3 bruteforce_simulator.py
```

You should see output for:

- The brute-force attack **without protection**.
- The same attack **with rate limiting**.

Compare the behavior to understand why rate limiting and lockout policies are important defenses against brute-force attacks.

