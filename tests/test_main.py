from scripts.main import NewData


def test_initialize_new_data():
    my_date = "2022-10-14"
    my_temp = 37.5

    new_data = NewData(date=my_date, temperature=my_temp)

    assert new_data.date == my_date
    assert new_data.temperature == my_temp
