import moment

x = moment.now()
y = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
print(x)
print(y)