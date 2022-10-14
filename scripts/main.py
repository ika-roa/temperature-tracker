import pandas as pd


class Data:
    
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        data_frame = pd.read_csv(self.filename)
        return data_frame


class NewData:
    
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature

    def __repr__(self):
        return f"Temperature on {self.date}: {self.temperature} °C"


if __name__ == "__main__":
    # my_date = input("What is the date? ")
    # my_temperature = float(input("What is the temperature? "))
    # new_data = NewData(my_date, my_temperature)
    my_filename = "../data/test_data.csv"
    my_data = Data(filename=my_filename)
    print(my_data.open_file())


    