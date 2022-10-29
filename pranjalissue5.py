class SubTestCase(unittest.TestCase):
    def __init__(self, orginal_function):
        self.orginal_function = orginal_function
        
    def wrapper():      
        #decorator code
    
    def __call__(self):
        wrapper()
        cls.setup_subtest()
        cls.teardown_subtest()
