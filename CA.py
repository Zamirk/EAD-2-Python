
BANK_ACCOUNT_1 = [100, 200, -50]

def DebitBankAccount(amountInserted, account):
    if (amountInserted > 0):
        account.append(amountInserted)
        return account
    else:
        print('Cannot insert less than 0')
    return account

def CreditBankAccount(amountWithdrawn, account):
    if (amountWithdrawn < 0):
        print('Cannot withdraw less than 0')
        return account
    else:
        if (sum(account)-amountWithdrawn < 0):
            print('Cannot withdrawn, not enough funds')
            return account
        else:
            account.append(-amountWithdrawn)
            return account
        return account


def CalculateTotal(account):
    return sum(account)

print('My account: {}'.format(BANK_ACCOUNT_1))
print('Inserting 10')
BANK_ACCOUNT_1 = DebitBankAccount(10, BANK_ACCOUNT_1)
print('My account: {}'.format(BANK_ACCOUNT_1))
print('Inserting  -10')
BANK_ACCOUNT_1 = DebitBankAccount(-10, BANK_ACCOUNT_1)

print('Withdrawing  10')
BANK_ACCOUNT_1 = CreditBankAccount(10, BANK_ACCOUNT_1)
print('Withdrawing  -10')
BANK_ACCOUNT_1 = CreditBankAccount(-10, BANK_ACCOUNT_1)
print('Withdrawing  1000')
BANK_ACCOUNT_1 = CreditBankAccount(10000, BANK_ACCOUNT_1)




from enum import Enum
class Currency(Enum):
        CANADIANDOLLARS = 1
        BRITISHPOUNDS = 2
        USDOLLARS = 3


def ConvertEuros(Currency, data):
    EURO_TO_DOLLARS = 1.09
    EURO_TO_BPOUNDS = .84
    EURO_TO_CDOLLARS = 1.5

    newValue = 0

    if (Currency == Currency.CANADIANDOLLARS):
        print('Converting Euro to Canadian dollars')
        newValue = data * EURO_TO_CDOLLARS
    elif (Currency == Currency.BRITISHPOUNDS):
        print('Converting Euro to British pounds')
        newValue = data * EURO_TO_BPOUNDS
    elif (Currency == Currency.USDOLLARS):
        print('Converting Euro to US dollars')
        newValue = data * EURO_TO_DOLLARS

    return newValue

print(ConvertEuros(Currency.CANADIANDOLLARS, 10))
print(ConvertEuros(Currency.USDOLLARS, 10))
print(ConvertEuros(Currency.BRITISHPOUNDS, 10))

def ConvertToEuros(Currency, amount):
    DOLLARS_TO_EURO = 0.92
    BPOUNDS_TO_EURO = 1.18
    CDOLLARS_TO_EURO = .67

    newValue = 0

    if (Currency == Currency.CANADIANDOLLARS):
        print('Converting Canadian dollars to Euro ')
        newValue = amount * CDOLLARS_TO_EURO
    elif (Currency == Currency.BRITISHPOUNDS):
        print('Converting British pounds to Euro ')
        newValue = amount * BPOUNDS_TO_EURO
    elif (Currency == Currency.USDOLLARS):
        print('Converting US Dollar to Euro ')
        newValue = amount * DOLLARS_TO_EURO

    return newValue

print(ConvertToEuros(Currency.CANADIANDOLLARS, 10))
print(ConvertToEuros(Currency.USDOLLARS, 10))
print(ConvertToEuros(Currency.BRITISHPOUNDS, 10))

