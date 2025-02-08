import pytest

class GeoInputData:
    POSITIVE_INPUT = [
        pytest.param(['Bellevue, WA'], id='name_correct'),
        pytest.param(['98006'], id='zip_correct'),
        pytest.param(['Bellevue, WA', '98006', 'Seattle, WA', '98005'], id='mulitple_mix')
    ]

    NEGATIVE_INPUT =  [
        pytest.param(['Bellevue'], id='only city'),
        pytest.param(['980063'], id='incorrect_zip_correct'),
        pytest.param(['WA'], id='only state code')
    ]