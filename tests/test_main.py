import pandas as pd

from scripts.main import NewData, Data


def test_initialize_new_data():
    my_date = "2022-10-14"
    my_temp = 37.5

    new_data = NewData(date=my_date, temperature=my_temp)

    assert new_data.date == my_date
    assert new_data.temperature == my_temp

def test_initialize_data():
    my_filename = "../data/test_data.csv"
    my_data = Data(filename=my_filename)

    assert my_data.filename == my_filename

def test_open_file():
    correct_df = pd.DataFrame({"date": ["2022-10-01", "2022-10-02"],
                               "temperature": [36.8, 37.2]})

    my_filename = "../data/test_data.csv"
    my_data = Data(filename=my_filename)

    pd.testing.assert_frame_equal(my_data.open_file(), correct_df)

def test_add_new_data():
    correct_df = pd.DataFrame({"date": ["2022-10-01", "2022-10-02", "2022-10-14"],
                               "temperature": [36.8, 37.2, 37.5]})
    new_data = NewData("2022-10-14", 37.5)
    my_filename = "../data/test_data.csv"

    my_data = Data(filename=my_filename)
    my_data.add_new_data_to_df(new_data)

    pd.testing.assert_frame_equal(my_data.df, correct_df)
