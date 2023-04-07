import pytest
import os

def test_file_names():
    files = ['books.csv', 'popular_websites.csv', 'products.csv']
    resources_path = 'materials-pandas-iterate-over-rows/resources/'
    for file in files: 
        assert os.path.exists(resources_path + file ) == True

def test_not_empty():
    files = ['books.csv', 'popular_websites.csv', 'products.csv']
    resources_path = 'materials-pandas-iterate-over-rows/resources/'
    for file in files: 
        assert os.stat(resources_path + file).st_size > 0





