"An ATM Dispenser that dispenses denominations of notes"
import sys
from atm_dispenser_chain import ATMDispenserChain

ATM = ATMDispenserChain()
AMOUNT = int(input("Enter amount to withdrawal : "))
if AMOUNT < 10 or AMOUNT % 10 != 0:
    print("Amount should be positive and in multiple of 10s.")
    sys.exit()
# process the request
ATM.chain1.handle(AMOUNT)
print("Now go spoil yourself")
