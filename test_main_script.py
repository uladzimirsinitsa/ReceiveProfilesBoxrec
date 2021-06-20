import os
import unittest
import requests

from main_script import choice_user_agents
from main_script import cuts_string_containing_url
from main_script import saves_strings
from main_script import connect_via_proxy
from main_script import get_links
from main_script import sort_links
from main_script import write_csv


class TestMainScript(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file_data_urls_1 = open('data/test_data_urls_1.csv', 'w+')
        self.test_list_of_strings = [
            'test string 1\n',
            'test string 2\n',
            'test string 3\n']
        for string in self.test_list_of_strings:
            self.test_file_data_urls_1.write(string)

        self.test_file_data_urls_2 = open('data/test_data_urls_2.csv', 'w+')
        for string in self.test_list_of_strings[1:3]:
            self.test_file_data_urls_2.write(string)
        #self.connect = requests.get()


    def tearDown(self) -> None:
        self.test_file_data_urls_1.close()


    def test_choice_user_agents_1(self):
        """Check actual result equal expected one."""
        self.assertEqual(
            type(choice_user_agents()),
            str,
            msg='Function choice_user_agents() return not a str.')

    def test_choice_user_agents_2(self):
        """Check file exists data/user_agents.txt."""
        self.assertTrue(
            os.path.exists('data/user_agents.txt'),
            msg='The data/user_agents.txt file does not exist.')

    def test_choice_user_agents_3(self):
        """Check user_agents.txt file is not empty."""
        self.assertFalse(os.stat('data/user_agents.txt').st_size == 0)

    def test_cuts_string_containing_url_1(self):
        """Check actual result equal expected one."""
        self.assertEqual(
            type(cuts_string_containing_url(file='data/test_data_urls_1.csv')),
            tuple,
            msg='Function cuts_string_containing_url() return not a tuple.')

    def test_cuts_string_containing_url_2(self):
        """Check file exists data/data_urls.csv."""
        self.assertTrue(
            os.path.exists('data/data_urls.csv'),
            msg='The data/data_urls.csv file does not exist.')

    def test_cuts_string_containing_url_3(self):
        """Check data/data_urls.csv file is not empty."""
        self.assertFalse(
            os.stat('data/data_urls.csv').st_size == 0,
            msg='File data/data_urls.csv is empty.')

    def test_saves_strings_1(self):
        """Check saves_strings() actual result equal expected one."""
        self.assertIsNone(
            saves_strings(self.test_list_of_strings[1:3],
                          file='data/test_data_urls_2.csv'),
            msg='Function saves_strings() return not a None.')

    def test_saves_strings_2(self, file='data/test_data_urls_2.csv'):
        """Check that the recorded data is equal to the transmitted."""
        saves_strings(
            self.test_list_of_strings[1:2],
            file='data/test_data_urls_2.csv'),
        data = [open(file, 'r').readline()]
        self.assertEqual(
            self.test_list_of_strings[1:2],
            data,
            msg='Received and recorded data are not identical.')

    def test_connect_via_proxy_1(self):
        """Check connect."""
        pass
    #  TODO: опросить список прокси на ответ, и сохранить IP и ответ в
    #  TODO: сделать счетчик рабочих IP
    #  TODO: поднять исключения
    #  TODO: запросить API определения IP и сравнить ответ с фактом

    def test_get_links_1(self):
        """"""
    #  TODO: создать тестовый объект и проверить результат
        pass

    def test_sort_links_1(self):
        """"""
    #  TODO: создать тестовый объект и проверить результат
        pass

    def test_write_csv_1(self):
        pass


if __name__ == '__main__':
    unittest.main()
