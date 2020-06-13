import pytest
import src.twosum as twosum


class TestTwoSum:
    def test_it_returns_empty_for_empty_list(self):
        assert(twosum.two_sum(nums=[], target=1) == [])

    def test_one_plus_one_is_two(self):
        assert(twosum.two_sum(nums=[1, 1], target=2) == [0, 1])

    def test_returns_empty_for_one_number_list(self):
        assert(twosum.two_sum(nums=[1], target=1) == [])

    def test_list_of_unique_positive_numbers(self):
        assert(twosum.two_sum(nums=[1, 2, 3, 4, 5], target=9) == [3, 4])

    def test_must_return_unique_indices(self):
        assert(twosum.two_sum(nums=[3, 3, 3, 3], target=6) != [0, 0])
        assert(twosum.two_sum(nums=[3, 3, 3, 3], target=6) == [0, 1])
