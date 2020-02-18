import unittest
import requests
from my-git import get_user_git_data

class TestMyGitData(unittest.TestCase):

    def test_get_user_git_data(self):
        self.assertIsNone(get_user_git_data(''))

    def test_get_user_git_data_invalid_data(self):
        self.assertIsNotNone(get_user_git_data('12'))

    def test_get_user_git_data_my_data(self):
        result=get_user_git_data('saikirankondapalli03')
        self.assertEqual(result
            , [
                'Repository: Algo_Ds_Notes has 30 number of commits',
                'Repository: Angular2SampleProj has 1 number of commits',
                'Repository: AngularJs has 5 number of commits',
                'Repository: gedcom_Agile has 30 number of commits',
                'Repository: HW09 has 2 number of commits',
                'Repository: Node-Angular2Example has 3 number of commits',
                'Repository: PlanPackRepeat has 30 number of commits',
                'Repository: planpackrepeat-backend has 30 number of commits',
                'Repository: pythonmath has 9 number of commits',
                'Repository: spring-boot has 30 number of commits',
                'Repository: spring-boot-quartz-demo has 6 number of commits',
                'Repository: SSW-567 has 10 number of commits'
            ])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()