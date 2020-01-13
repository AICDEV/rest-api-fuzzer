from lib import Randomness, Types


def parse_uri(uri):

    for type_s in Types.TypesEnum:
        if type_s.value in uri:
            uri = uri.replace(f"%{type_s.value}",str( _get_random_for_type(type_s.value)))

    return uri

def _get_random_for_type(method):
    random_type = method.lower()

    if random_type == Types.TypesEnum.EMAIL.value:
        return Randomness.getRandomMail()

    elif random_type == Types.TypesEnum.PASSWORD.value:
        return Randomness.getRandomPassword(Randomness.getRandomNumber())

    elif random_type == Types.TypesEnum.STRING.value:
        return Randomness.getRandomString(Randomness.getRandomNumber())

    elif random_type == Types.TypesEnum.STRING_WITH_DIGITS.value:
        return Randomness.getRandomStringWithDigits(Randomness.getRandomNumber())

    elif random_type == Types.TypesEnum.STRING_RANDOM.value:
        return Randomness.getRandomPassword(Randomness.getRandomNumber())

    elif random_type == Types.TypesEnum.NUMBER.value:
        return Randomness.getRandomNumber()

    elif random_type == Types.TypesEnum.DATE.value:
        return Randomness.getRandomDate()

    elif random_type == Types.TypesEnum.JWT.value:
        return Randomness.getRandomJWT()

    elif random_type == Types.TypesEnum.UUID.value:
        return Randomness.getRandomFakeUUID()

    elif random_type == Types.TypesEnum.ID.value:
        return Randomness.getRandomFakeID()

    else:
        print(f"unsupported {method}")
