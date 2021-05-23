$ pip install allure-pytest
$ py.test --alluredir=%allure_result_folder% ./tests
$ allure serve %allure_result_folder%
$ pytest -v
$ pytest runfile