class InvalidPromotionMethod(Exception):
    def __init__(self,
                 message="Invalid promotion method"
                 ):
        self.message = message
        super().__init__(self.message)


class NodeValueAlreadyExists(Exception):
    def __init__(self,
                 message="Node value already exists"
                 ):
        self.message = message
        super().__init__(self.message)


class ValueInChildNodeRange(Exception):
    def __init__(self,
                 node,
                 message="Value could be inserted in a child node"
                 ):
        self.message = message
        self.node = node
        super().__init__(self.message)
