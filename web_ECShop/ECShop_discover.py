import unittest

# discover = unittest.defaultTestLoader.discover(start_dir=".\".pattern="web*.py")
discover = unittest.defaultTestLoader.discover(start_dir='./',pattern='web*.py')
runner = unittest.TextTestRunner()
runner.run(discover)