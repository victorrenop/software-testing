import re


class SillyPascal:
    @staticmethod
    def is_valid(identifier: str) -> bool:
        if identifier is not None:
            if len(identifier) >= 1 and len(identifier) <= 6:
                if identifier[0].isalpha():
                    if re.match(r"^[\w]+$", identifier):
                        return True
                    return False
                return False
            return False
        return False
