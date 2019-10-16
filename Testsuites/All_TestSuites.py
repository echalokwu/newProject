import sys;
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/echalo/newProject'])

import unittest
from Package1.TestCase1 import TestCase1
from Package2.TestCase2 import TestCase2
from Package2.TestCase3 import TestCase3

# Get all tests from both packages
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestCase3)


testSuite = unittest.TestSuite([tc1, tc2, tc3])
unittest.TextTestRunner().run(testSuite)


