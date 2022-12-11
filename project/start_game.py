from Stock_main import *
from User import *

Stock1 = Stock()
U1 = User(Stock1)
U1.process()
# player_1_status = [U1.get_expense_list(), U1.get_price_of_stock_buy_list(), U1.get_volume()]
#player_1_stock = [U1.get_high_price(), U1.get_low_price()]  - needs adding these methods in User object
print("\nSummary for the whole procedure: \nuser expense list: {}\nuser price of stock buy list: {}\nuser volume list: {}".format(U1.get_expense_list(), U1.get_price_of_stock_buy_list(), U1.get_volume()))