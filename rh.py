import heapq
import pyrh
import sys
import time

input_args = sys.argv

rh = pyrh.Robinhood(username=input_args[1], password=input_args[2])
rh.login()

heap = []
stock = input_args[3]
batch_size = int(input_args[4])

while True:
	stock_data = rh.quote_data(stock)
	price = float(stock_data["ask_price"])
	print(price)
	if len(heap) == 0 or heap[0] - price > 0.5:
		# rh.buy
		# buy_data = rh.place_market_buy_order(instrument_URL=stock_data["instrument"],
		#                                      symbol=stock,
		#                                      time_in_force="GFD",
		#                                      quantity=batch_size)
		# print(buy_data)
		heapq.heappush(heap, price)
	elif price - heap[0] > 0.5:
		# rh.sell
		# sell_data = rh.place_market_sell_order(instrument_URL=stock_data["instrument"],
		#                                        symbol=stock,
		#                                        time_in_force="GFD",
		#                                        quantity=batch_size)
		# print(sell_data)
		print("Earned: " + str((price - heap[0]) * batch_size))
		heapq.heappop(heap)
	print(heap)
	time.sleep(30)