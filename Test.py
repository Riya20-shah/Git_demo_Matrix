class MyClass:
    def __init__(self):
        # Constructor method
        self.value = 0

    def increment(self, amount):
        """
        Increment the value by the given amount.
        
        :param amount: The amount to increment the value by.
        """
        self.value += amount

    def get_value(self):
        """
        Get the current value.
        
        :return: The current value.
        """
        return self.value