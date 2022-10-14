import pandas as pd


class Data:
    
    def __init__(self, filename):
        self.filename = filename
        self.df = self.open_file()

    def open_file(self):
        data_frame = pd.read_csv(self.filename)
        return data_frame

    def add_new_data_to_df(self, new_data):
        self.df = pd.concat([self.df,
                            new_data.data_to_series()],
                            ignore_index=True)


class NewData:
    
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature

    def data_to_series(self):
        return pd.DataFrame({"date": [self.date],
                             "temperature": [self.temperature]})

    def __repr__(self):
        return f"Temperature on {self.date}: {self.temperature} °C"


if __name__ == "__main__":
    my_date = "2022-10-14"  # input("What is the date? ")
    my_temperature = 37.5  # float(input("What is the temperature? "))
    new_data = NewData(my_date, my_temperature)

    my_filename = "../data/test_data.csv"
    my_data = Data(filename=my_filename)
    my_data.add_new_data_to_df(new_data)
    print(my_data.df)


    