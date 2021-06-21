import finnhub


finnhub_client = finnhub.Client(api_key="c2deprqad3i9v1gknf10")

# num_stock = input("how many stocks do you want to track? ")

stock_list = []


def stock_entered():
    stock_prompt = input("Enter in your stock tickers one at a time. When finished type done: ")

    if stock_prompt == "done":
        return False
    else:
        return stock_prompt


i = True

while i:
    stock_list.append(stock_entered())
    i = stock_list[-1]

stock_list.remove(False)

trig_percent = int(input("What percent what you like to trigger a response? "))

stock_bought = []

j = 0

while j < len(stock_list):
    stock_bought.append((finnhub_client.quote(stock_list[j]))["c"])
    j += 1


def price_diff(bought, current):
    if current >= bought + bought*(trig_percent/100) or current <= bought - bought*(trig_percent/100):
        return True
    else:
        return False


is_diff = []

k = 0

while k < len(stock_list):
    is_diff.append(price_diff(stock_bought[k], ((finnhub_client.quote(stock_list[k]))["c"])))
    k += 1

change_dict = {}


l = 0
while l < len(is_diff):
    if is_diff[l]:
        change_dict.update({stock_list[l]: round(((stock_bought[l] - ((finnhub_client.quote(stock_list[l]))["c"]))/stock_bought[l])* 100, 2)})
    l += 1



print(stock_list)
print(stock_bought)
print(is_diff)
print(change_dict)

# print(finnhub_client.quote('AAPL'))



# print(stonk["c"])
