import sys
if 'test' in sys.argv:
  from test_settings import *
else:
  from site_settings import *