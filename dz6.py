def powers_of_three():
    power = 0

    while True:
        yield 3 ** power
        power += 1


my_generator = powers_of_three()

for i in range(6):
    print(next(my_generator))