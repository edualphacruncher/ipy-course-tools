import unittest

import ipy_course_tools


class VersionTestCase(unittest.TestCase):
    """ Version tests """

    def test_version(self):
        """ check ipy_course_tools exposes a version attribute """
        self.assertTrue(hasattr(ipy_course_tools, "__version__"))
        self.assertIsInstance(ipy_course_tools.__version__, str)


if __name__ == "__main__":
    unittest.main()
