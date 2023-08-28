import pandas
import random
class Dict():

    def __init__(self):

        self.df = pandas.DataFrame()

        self.dict = dict()

    def change(self, file):
        self.df = pandas.read_excel(file)
        self.dict = self.df.to_dict(orient='records')
        return self.dict

    def choice(self, dict): # dict는 리턴한 self.dict
        pass



