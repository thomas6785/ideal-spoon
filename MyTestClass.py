class MyTestClass:
    """This is a test Python class to see how docs look."""
    
    def __init__(self):
        """Initialiser"""
        print('test')
    
    def _configure(self):
        """Private method to configure self"""
        self.a = 1
    
    def output(self):
        """Output self.a"""
        print(self.a)