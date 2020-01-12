from enum import Enum

class TypesEnum(Enum):
    EMAIL = "email"
    PASSWORD = "password"
    STRING = "string"
    STRING_WITH_DIGITS = "string_with_digits"
    STRING_RANDOM = "string_random"
    NUMBER = "number"
    DATE = "date"
    JWT = "jwt"
    UUID = "uuid"
    ID = "id"
    PAYLOAD_JSON = "json"
    PAYLOAD_FORM_DATA = "application/x-www-form-urlencoded"
