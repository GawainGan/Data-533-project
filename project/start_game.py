from Stock_main import *
from Buy import *
from User import *
U1 = User()
U1.process()
print("\nSummary for the whole procedure: \nuser expense list: {}\nuser price of stock buy list: {}\nuser volume list: {}".format(U1.get_expense_list(), U1.get_price_of_stock_buy_list(), U1.get_volume()))
