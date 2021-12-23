from datetime import datetime

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"time tracker:{diff.total_seconds()}")
