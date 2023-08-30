# BankingOperationsSystem-201015
## Project Overview:
This banking operations system is created using OOPs Concepts in Python. 
The scope of the Online Banking System project includes the following
functionalities:
- Account management (Create Account, Deposit Amount, Withdraw
Amount).
- Fund transfers between accounts.
- Balance Inquiry.

## Class Diagram: 
<img width="338" alt="image" src="https://github.com/RASHI2505/BankingOperationsSystem-201015/assets/64950686/4f3de333-e57c-410b-bad8-40d7abc96fd8">

+---------------------+     +-----------------------------------+
|      BankAccount    |     |         Bank                      |
+---------------------+     +-----------------------------------+
| - account_number    |     | - accounts: list                  |
| - account_holder    |     |                                   |
| - balance           |     | + create_savings_account()        |
|                     |     | + create_current_account()        |
| + deposit(amount)   |     | + get_account_by_number()         |
| + withdraw(amount)  |     | + fund_transfer()                 |
| + get_balance()     |     | + get_all_customers()             |
| + get_details()     |     |                                   |
+---------------------+     +-----------------------------------+
       ^    ^                              ^
       |    |                              |
       |    |                              |
+----------------+              +---------------------+
| SavingsAccount |              |   CurrentAccount    |
+----------------+              +---------------------+
| -interest_rate |              | - overdraft_limit   |
| +add_interest()|              | + withdraw(amount)  |
+----------------+              +---------------------+

