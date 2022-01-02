
class OutOfSalmonException(Exception):
    def __init__(self, order_name, message="No more salmon. order will not take place"):
        self.message = message
        self.order_name = order_name
        super().__init__(self.message)

    def __str__(self):
        return f'OutOfSalmonException: {self.message}'