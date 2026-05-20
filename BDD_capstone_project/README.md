# Ixigo Behave BDD Capstone Project

This project automates Ixigo hotel booking scenarios with Selenium, Behave BDD, and Allure reporting.

## Setup

```powershell
pip install -r requirements.txt
```

## Run Tests

```powershell
behave
```

To clean old reports, run Behave, and generate the Allure report:

```powershell
python runtests.py
```

## Manual OTP

Login automation enters the mobile number and clicks Continue. When the OTP screen appears, enter the OTP manually within the configured wait time.

The wait time is controlled in:

```text
config/config.ini
```

## Useful Tags

```powershell
behave --tags=@login
behave --tags=@hotel
behave --tags=@e2e
behave --tags=@negative
```

