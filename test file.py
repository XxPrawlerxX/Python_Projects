

prices= {"apple": 10, "orange":20, "thing":12}
cart={"apple":8, "orange":9}
total_cost = 0
for key, value in cart.items():
    total_cost += value * prices[key]

print(total_cost)




word = "banana"

letter_count= {}

for i in word:
    if i in letter_count:
        letter_count[i] += 1

    else:
        letter_count[i] = 1

print(letter_count)




num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
try:
    x = int(num1) / int(num2)
except ZeroDivisionError:
    print("Cannot divide by zero")
    x = None
except Exception as e:
    print("Error occured")
    x = None
finally:
    print(x)
    

