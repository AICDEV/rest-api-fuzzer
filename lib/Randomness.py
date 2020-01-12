import random
import string
import jwt
import datetime
from datetime import datetime, timedelta, date

def getRandomMail():
    randomMail =  getRandomString(getRandomNumber()) + '@' + getRandomString(getRandomNumber()) + '.' + getRandomDomain()
    return randomMail


def getRandomDomain():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(random.choice([2,3])))

def getRandomString(length):
    return  ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def getRandomStringWithDigits(length):
    return  ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

def getRandomPassword(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))

def getRandomFakeID():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(24))

def getRandomNumber():
    return random.choice(range(1,100))

def getRandomRole():
        return random.choice(['admin','user','member','editor','guest','anonymous'])

def getRandomFakeUUID():
    return f"{getRandomStringWithDigits(8)}-{getRandomStringWithDigits(4)}-{getRandomStringWithDigits(4)}-{getRandomStringWithDigits(4)}-{getRandomStringWithDigits(12)}"

def getRandomDate():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day

def getRandomJWT():
    return "Bearer "+jwt.encode({
    '_id': getRandomFakeID(),
    'email': getRandomMail(),
    'role': getRandomRole(),
    'iat': datetime.utcnow(),
    'exp': datetime.now() + timedelta(hours=1)
    }, getRandomPassword(getRandomNumber()), algorithm='HS256').decode('utf-8')
