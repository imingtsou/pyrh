import pyrh
import time
import sys

input_args = sys.argv

rh = pyrh.Robinhood(username=input_args[1], password=input_args[2])
rh.login()

stack = []
stock = input_args[3]
batch_size = input_args[4]

while True:
	stock_data = rh.quote_data(stock)
	price = float(stock_data["ask_price"])
	print(price)
	if len(stack) == 0 or stack[-1] - price > 0.5:
		# rh.buy
		# buy_data = rh.place_market_buy_order(instrument_URL=stock_data["instrument"],
		#                                      symbol=stock,
		#                                      time_in_force="GFD",
		#                                      quantity=batch_size)
		# print(buy_data)
		stack.append(price)
	elif price - stack[-1] > 0.5:
		# rh.sell
		# sell_data = rh.place_market_sell_order(instrument_URL=stock_data["instrument"],
		#                                        symbol=stock,
		#                                        time_in_force="GFD",
		#                                        quantity=batch_size)
		# print(sell_data)
		print("Earned: " + str((price - stack[-1]) * batch_size))
		stack.pop()
	print(stack)
	time.sleep(30)