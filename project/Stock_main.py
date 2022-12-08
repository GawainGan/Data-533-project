# class for Stock
# contain the input for number of rounds to paly with
import numpy as np
import random
class Stock:
      # set the parameters as global variables
      
      def __init__(self):
            self.n = input("How many round do you want to play with?")
            print("You are going to play {} round, get ready!".format(self.n))
            self.high_price_list = [random.randint(201, 500) for i in range(int(self.n))]
            self.low_price_list = [random.randint(50, 200) for i in range(int(self.n))]
            self.volume_list = [random.randint(1, 200) for i in range(int(self.n))]

      # when we start the program, it will ask user to input the numbers of round user want to play with, use print
      def get_high_price(self):
            return self.high_price_list
      def get_low_price(self):
            return self.low_price_list
      def get_volume(self):
            return self.volume_list
      
      def __str__(self):
            return f"high price list: {self.high_price_list}\nlow price list: {self.low_price_list}\nvolume list: {self.volume_list}"


class Buy_function():
      def __init__(self, Stock):
            self.high_price_list = Stock.get_high_price()
            self.low_price_list = Stock.get_low_price()
            self.volume_list = Stock.get_volume()
      
      def buy_stock(self, index):
            self.current_high_price = float(self.high_price_list[index])
            self.current_low_price = float(self.low_price_list[index])
            self.random_price = float(random.randint(int(self.current_low_price), int(self.current_high_price)))
            print("Current high price price: {} Current low price: {}".format(self.current_high_price, self.current_low_price))
            
            print("The current price of the stock is {}".format(self.random_price))
            self.input_volume = int(input("How many volume do you want to buy?"))
            
            self.buy_price = float(self.random_price)
            # print("The price you buy is {}".format(self.buy_price))
            self.buy_volume = self.input_volume
            # print("The volume you buy is {}".format(self.buy_volume))
            self.total_price = np.multiply(float(self.buy_price), float(self.buy_volume))
            # print("The total price you buy is {}".format(self.total_price))
            return self.total_price
      
      
      def return_current_high_low_price_n_volume(self):
            return f"Current high price price: {self.current_high_price}\nCurrent low price: {self.current_low_price}\nThe current price of the stock is {self.random_price}\nThe price you buy is {self.buy_price}\nThe volume you buy is {self.buy_volume}\nThe total price you buy is {self.total_price}"
            
      def __str__(self):
            return f"\n------\nTransaction completed!\nbuy price: {self.buy_price}\nbuy volume: {self.buy_volume}\ntotal price: {self.total_price}\n"