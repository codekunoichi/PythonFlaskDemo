import unittest
from datetime import datetime
from data_access import save, find_last_10, count_records


class TestDataAccess(unittest.TestCase):

    def test_save_typing_score(self):
        count = count_records()
        print(count)
        #{"timestamp":"2020-10-01T19:00:00","value":0.1},
        save(0.25, '2020-10-29T19:30:30')
        new_count = count_records()
        self.assertTrue(count + 1 == new_count)

    def test_find_last_10(self):
        result = find_last_10()
        self.assertTrue(10 == len(result))


if __name__ == "__main__":
    unittest.main()
