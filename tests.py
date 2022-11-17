import unittest
from domains import regions, global_south
from tools import build_cf_axes

class TestCordex(unittest.TestCase):
    """ 
    Test cordex domains
    """
    def setUp(self):
        self.domains = {k[1]:v[0] for k,v in regions.items()}
        for k,v in global_south.items():
            self.domains[k]=v[0]

    def test_domains(self):
        """ Test each domain"""
        for r,d in self.domains.items():
            print(f'\n\n****\nChecking {r}\n****\n')
            cf_domain = build_cf_axes(d)
        

if __name__=="__main__":
    unittest.main()