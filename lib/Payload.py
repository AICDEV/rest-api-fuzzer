from lib import Randomness, Types

class PayloadBuilder():
    def __init__(self, job):
        if 'fields' in job:
            self.fields = job['fields']
        else:
            self.fields = []

        if 'headers' in job:
            self.headers = job['headers']
        else:
            self.headers = []

    def get_payload(self):
        payload = {}

        for field in self.fields:
            if field['type'].lower() not in self._get_allowed_types():
                raise Exception('type not supported.')

            payload[field['name']] = self._get_random_for_type(field['type'])
        
        return payload

    def get_headers(self):
        build_headers = {}

        for header in self.headers:
            if 'value' in header:
                build_headers[header['name']] = header['value']
                
            else:
                if header['type'].lower() not in self._get_allowed_types():
                    raise Exception('type not supported.')

                build_headers[header['name']] = self._get_random_for_type(header['type'])

        return build_headers

    def _get_random_for_type(self, method):
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

        
    def _get_allowed_types(self):
        return [item.value for item in Types.TypesEnum]
