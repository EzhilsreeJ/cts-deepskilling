import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "Task01")
    ),
)

from step41_conftest import *

from step46_screenshot_hook import *