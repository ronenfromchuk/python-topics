
class SomethingWentWrongException(Exception):
    def __init__(self, inner, message="something went wrong in the kitchen"):
        self.message = message
        self.inner = inner
        super().__init__(self.message)

    def __str__(self):
        return f'SomethingWentWrongException: {self.message}'