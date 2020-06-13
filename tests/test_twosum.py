import pytest
import src.twosum as twosum


class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(twosum.two_sum(nums=[], target=1) == [])

    def test_one_plus_one_is_two(self):
        assert(twosum.two_sum(nums=[1, 1], target=2) == [0, 1])

    def test_returns_empty_for_one_number_list(self):
        assert(twosum.two_sum(nums=[1], target=1) == [])
