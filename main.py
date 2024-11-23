import unittest
import time
import os
from common.BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
ENVIRON = 'Online'  # 'Online' -> 线上环境， 'Offline' -> 测试环境

if __name__ == '__main__':
    run_pattern = 'all'  # all 全量测试用例执行 /  smoking 冒烟测试执行  /  指定执行文件
    if run_pattern == 'all':
        pattern = 'test_*.py'
    elif run_pattern == 'smoking':
        pattern = 'test_major*.py'
    else:
        pattern = run_pattern + '.py'
    suite = unittest.TestLoader().discover('./testCase', pattern=pattern)

    result = BeautifulReport(suite)
    result.report(filename="report.html", description='测试报告', report_dir='./')


