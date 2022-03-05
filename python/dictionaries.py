# key/value pair
employees = {"chef": "Ann", "ceo": "Jin"}

print(employees["ceo"])

employees["waiter"] = "Mike"  # inserting new key/value pair to a dictionary

print(employees)

employees["chef"] = "Jose"  # update key/value pair

print(employees)

stock_prices = {"GOOGL": [200, 210, 220], "GME": [20, 100, 300]}
history = stock_prices["GOOGL"]
print(f"First day price is: {history[0]}")

mydict = {"outer": {"inner": 100}}
print(mydict["outer"]["inner"])

mydict2 = {'key1': 100, 'key2': 200, 'key3': 400}
print(mydict2.keys())   # return just keys
print(mydict2.values())  # return just values
print(mydict2.items())  # return a list of tuples
