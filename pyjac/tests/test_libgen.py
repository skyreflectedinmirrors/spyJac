# Python 2 compatibility
from __future__ import print_function
from __future__ import division

import sys

from pyjac.libgen import libgen  # noqa


class TestLibgen(object):
    """
    """
    def test_imported(self):
        """Ensure libgen module imported.
        """
        assert 'pyjac.libgen.libgen' in sys.modules
