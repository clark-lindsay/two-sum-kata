import pytest
import src.hello as hello


class TestHello:
    def test_it_prints(self):
        assert(hello.hello() == 'hello, world!')
