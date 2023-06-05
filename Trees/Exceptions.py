class MaxChildrenReached(Exception):
    def __init__(self,
                 message="Max children reached"
                 ):
        self.message = message
        super().__init__(self.message)


class LeftNodeAlreadySet(Exception):
    def __init__(self,
                 message="Left node already set"
                 ):
        self.message = message
        super().__init__(self.message)


class RightNodeAlreadySet(Exception):
    def __init__(self,
                 message="Right node already set"
                 ):
        self.message = message
        super().__init__(self.message)
