import random
import numpy as np


def buy_stock(curr_high_price_ele, curr_low_price_ele):
      random_price = float(random.randint(int(curr_low_price_ele), int(curr_high_price_ele)))
            
      print("The price of stock you bought is {}".format(random_price))
      input_volume = int(input("How many volume do you want to buy?\n"))
            
      buy_price = float(random_price)
            # print("The price you buy is {}".format(buy_price))
      buy_volume = input_volume
      # print("The volume you buy is {}".format(buy_volume))
      total_price = np.multiply(float(buy_price), float(buy_volume))
            # print("The total price you buy is {}".format(total_price))
      info = [total_price, random_price, buy_volume]
      return info
            
