import Stock_main
from Buy import *
class User(Stock_main.Stock):
      def __init__(self):
            self.stock = Stock_main.Stock()
            # self.buy = Buy()
            self.len_range = int(self.stock.n)
            # self.b_p = ''
            self.expense = []
            self.price_of_stock_buy = []
            self.volume_list = []
            self.total_price_of_stock_by_each_process = 0
            self.total_stock_price_list = []
            
            
            
      def process(self):
            for i in range(self.len_range):
                  curr_high_price_ele = self.stock.high_price_list[i]
                  curr_low_price_ele = self.stock.low_price_list[i]
                  curr_volume_ele = self.stock.volume_list[i]
                  print('----------Round{}----------'.format(i+1))
                  print("The high price of stock is {}".format(curr_high_price_ele))
                  print("The low price of stock is {}".format(curr_low_price_ele))
                  print("The volume of stock is {}".format(curr_volume_ele))
                  
                  self.buy_or_pass = input("Do you want to buy the stock? (Y/N)\n")
                  if self.buy_or_pass == "Y" or 'y':
                        print("\n---Buying---")
                        price = buy_stock(curr_high_price_ele, curr_low_price_ele)
                        # print(price)
                        expense = float(price[0])
                        stock_price = float(price[1])
                        volume = float(price[2])
                        self.total_price_of_stock_by_each_process = stock_price*volume
                        
                        print("The volume you buy is {}".format(volume))
                        print("The stock price you buy is {}\n".format(self.total_price_of_stock_by_each_process))
                        self.price_of_stock_buy.append(stock_price)
                        self.expense.append(expense)
                        self.volume_list.append(volume)
                        self.total_stock_price_list.append(self.total_price_of_stock_by_each_process)
                        
                  elif self.buy_or_pass == "N" or 'n':
                        self.expense.append(0)
                        self.price_of_stock_buy.append(0)
                        self.volume_list.append(0)
                        print("\nYou pass this round")
                  else:
                        # print("----------\nCalculating your total expense......")
                        self.expense.append(0)
                        self.price_of_stock_buy.append(0)
                        self.volume_list.append(0)
                        break
                  
            print("\n----------Calculating your total expense......")
            print("The total price of the stock you bought is {}".format(sum(self.total_stock_price_list)))
            # print("The total expense you have is {}".format(sum(self.expense)))
            print("End of the game")

      def get_expense_list(self):
            return self.expense

      def get_price_of_stock_buy_list(self):
            return self.price_of_stock_buy
      
      def get_volume(self):
            return self.volume_list