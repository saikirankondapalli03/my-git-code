import unittest
import requests
from my_git import get_user_git_data
from unittest.mock import patch


class TestMyGitData(unittest.TestCase):

    
    def test_get_user_git_data(self):
        with patch('requests.get') as mock_request:
                mock_request.return_value.status_code = 403
                result=get_user_git_data('')
        self.assertEquals(result,'Forbidden')
    
    
    def test_get_user_git_data_my_data(self):
        with patch('requests.get') as mock_request:
                mock_request.return_value.status_code = 201
                result=get_user_git_data('')
        self.assertIsNone(result)
    
    
    def test_get_user_git_data_my_data_1(self):
        with patch('requests.get') as mock_request:
                mock_request.return_value.status_code = 200
                mock_request.return_value.json.return_value  = [{"name":"Algo_Ds_Notes"},{"name":"Angular2SampleProj"}]
                result=get_user_git_data('')
        self.assertEqual(result,[ 'Repository: Algo_Ds_Notes has 2 number of commits','Repository: Angular2SampleProj has 2 number of commits'])
               
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()