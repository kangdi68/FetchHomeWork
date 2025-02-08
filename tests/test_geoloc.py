import subprocess
import pytest
from dataSet import GeoInputData

@pytest.mark.parametrize('value', GeoInputData.POSITIVE_INPUT )
def test_place_name_positive(value):
    cmd = ['python3', '../geoloc-util.py', '--locations']
    cmd.extend(value)
    process_check = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process_check.wait()
    data, err = process_check.communicate()
    result = data.decode()
    print(result)
    assert result.find("Error")==-1, f"API error with {result}"

@pytest.mark.parametrize('value', GeoInputData.NEGATIVE_INPUT )
def test_place_name_negative(value):
    cmd = ['python3', '../geoloc-util.py', '--locations']
    cmd.extend(value)
    process_check = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process_check.wait()
    data, err = process_check.communicate()
    result = data.decode()
    print(result)
    assert result.find("Error")==-1, f"API error with {result}"
    assert result.find("Failed")!=-1, f"error with {result}"
