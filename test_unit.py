import pytest 
from lib.Utils import get_spark_session

@pytest.fixture(scope='session')
def spark():
    return get_spark_session(['LOCAL'])


def test_spark_version(spark):
    print(spark.version)
    assert spark.version == "3.2.4"