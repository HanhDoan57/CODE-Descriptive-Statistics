from code_6 import *
import random

def test_describe_country():
    country_code = ['mex','arg','col','usa','pol','chn']
    result = get_describe_country(random.choice(country_code))
    assert list(result.keys()) == ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
def test_groupby_year_country():
    country_code = ['mex','arg','usa','pol','chn']
    count_number = 23
    result = get_country_groupby_year(random.choice(country_code))
    assert list(result.count())[0] == count_number 