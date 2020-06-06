
class MissingValueError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MissingValueError, {0} '.format(self.message)
        else:
            return 'MissingValueError has been raised'



class EmptyTreeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'EmptyTreeError, {0} '.format(self.message)
        else:
            return 'EmptyTreeError has been raised'
