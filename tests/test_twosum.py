import pytest
import src.twosum as twosum


class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(twosum.two_sum(nums=[], target=1) == [])
