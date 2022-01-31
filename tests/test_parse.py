import os.path
from datetime import datetime
from .context import hwinfo_grapher as grapher


def test_parse_csv():
    json = grapher.parse_csv(os.path.join(
        os.path.dirname(__file__), 'data.csv'))
    assert len(json) == 10
    assert list(json[0].keys()) == ['Date', 'Time',
                                    'Virtual Memory Committed [MB]']


def test_extract_values():
    json = [
        {'Date': '30.1.2022', 'Time': '9:13:6.931',
            'Virtual Memory Committed [MB]': '8413'},
        {'Date': '30.1.2022', 'Time': '9:13:8.979',
            'Virtual Memory Committed [MB]': '8406'},
        {'Date': '30.1.2022', 'Time': '9:13:11.025',
            'Virtual Memory Committed [MB]': '8395'},
        {'Date': '30.1.2022', 'Time': '9:13:13.071',
            'Virtual Memory Committed [MB]': '8400'},
        {'Date': '30.1.2022', 'Time': '9:13:15.123',
            'Virtual Memory Committed [MB]': '8395'},
        {'Date': '30.1.2022', 'Time': '9:13:17.175',
            'Virtual Memory Committed [MB]': '8394'},
        {'Date': '30.1.2022', 'Time': '9:13:19.230',
            'Virtual Memory Committed [MB]': '8387'},
        {'Date': '30.1.2022', 'Time': '9:13:21.954',
            'Virtual Memory Committed [MB]': '8391'},
        {'Date': '30.1.2022', 'Time': '9:13:24.001',
            'Virtual Memory Committed [MB]': '8386'},
        {'Date': '30.1.2022', 'Time': '9:13:26.047',
            'Virtual Memory Committed [MB]': '8391'}
    ]

    dates = grapher.extract_values(json, 'Date')
    assert len(dates) == 10
    assert all([date == '30.1.2022' for date in dates])

    times = grapher.extract_values(json, 'Time')
    assert times == ['9:13:6.931', '9:13:8.979', '9:13:11.025', '9:13:13.071', '9:13:15.123',
                     '9:13:17.175', '9:13:19.230', '9:13:21.954', '9:13:24.001', '9:13:26.047']

    memory = grapher.extract_values(json, 'Virtual Memory Committed [MB]')
    assert memory == ['8413', '8406', '8395', '8400', '8395',
                      '8394', '8387', '8391', '8386', '8391']


def test_to_numbers():
    memory = ['8413', '8406', '8395', '8400', '8395',
              '8394', '8387', '8391', '8386', '8391']
    assert grapher.to_numbers(memory) == [
        8413, 8406, 8395, 8400, 8395, 8394, 8387, 8391, 8386, 8391]


def test_to_datetimes():
    dates = ['30.1.2022', '30.1.2022', '30.1.2022', '30.1.2022', '30.1.2022',
             '30.1.2022', '30.1.2022', '30.1.2022', '30.1.2022', '30.1.2022']
    times = ['9:13:6.931', '9:13:8.979', '9:13:11.025', '9:13:13.071', '9:13:15.123',
             '9:13:17.175', '9:13:19.230', '9:13:21.954', '9:13:24.001', '9:13:26.047']
    datetimes = grapher.to_datetimes(dates, times)
    assert len(datetimes) == 10
    assert all([type(dt) == datetime for dt in datetimes])
    assert all([dt.date().year == 2022 for dt in datetimes])
    assert all([dt.date().month == 1 for dt in datetimes])
    assert all([dt.date().day == 30 for dt in datetimes])
    assert all([dt.time().hour == 9 for dt in datetimes])
    assert all([dt.time().minute == 13 for dt in datetimes])


def test_find_units():
    keys = ['CPU [°C]', 'System [°C]', 'GPU Temperature [°C]']
    units = grapher.find_units(keys)
    assert len(units) == 1
    assert '[°C]' in units
    keys = ['CPU [°C]', 'System [°C]', 'GPU Temperature [°C]',
            'GPU Power [W]', 'GPU Fan1 [%]', 'GPU Fan2 [%]']
    units = grapher.find_units(keys)
    assert len(units) == 3
    assert '[°C]' in units
    assert '[W]' in units
    assert '[%]' in units
