import plotly


class NewData:
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature


if __name__ == "__main__":
    date = input("What is the date? ")
    temperature = float(input("What is the temperature? "))
    new_data = NewData(date, temperature)
    print(new_data)