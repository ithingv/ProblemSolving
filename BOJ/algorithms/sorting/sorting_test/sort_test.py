from unittest import TestCase, main

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from sorting.insertion_sort import insertion_sort

class SortTestCase(TestCase):
    def test_to_insertion_sort(self):
        # python .\sort_test.py SortTestCase.test_to_insertion_sort
        print("삽입정렬 테스트 중....")
        arr = [5,4,3,2,1]
        self.assertEqual([1,2,3,4,5], insertion_sort(arr))


if __name__ == "__main__":
    main()