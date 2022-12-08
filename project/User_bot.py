import Stock_main

# get a new instance from Stock_main
# create a class called User to get the information from Stock_main
class User(Stock_main.Stock):
      def __init__(self):
            self.stock = Stock_main.Stock()
            len_range = int(self.stock.n)
            for i in range(len_range):
                  print("Round {}".format(i+1))
                  print("Current high price price: {}\nCurrent low price: {}".format(self.stock.high_price_list[i], self.stock.low_price_list[i]))
                  print("Current available volume: {}\n".format(self.stock.volume_list[i]))
                  
                  self.buy_or_pass = input("Do you want to buy the stock? (Y/N)")
                  if self.buy_or_pass == "Y":
                        self.buy = Stock_main.Buy_function(self.stock)
                        self.buy.buy_stock(i)
                        print(self.buy)
                  elif self.buy_or_pass == "N":
                        print("You pass this round")
                  else:
                        print("End of the game, thank you for playing!")
                        break

User()