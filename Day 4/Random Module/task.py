import random
import my_module
import time
import datetime

start_time = datetime.datetime.now()

count = 0
while True:
    count += 1
    time.sleep(2)
    random_int = random.randint(1, 10) # randint(a, b) a <= N <= b
    random_number_0_to_1 = random.random() # random() 0.0 <= N < 1.0
    random_number_0_to_1_int = int(random_number_0_to_1 * 10)
    random_float = random.uniform(1, 10) # uniform(a, b) a <= N <= b

    print(f"random_int: {random_int}")
    print(f"random_number_0_to_1: {random_number_0_to_1}")
    print(f"random_number_0_to_1: {random_number_0_to_1_int}")
    print(f"random_float: {random_float}")

    print(f"my_module.my_favorite_number: {my_module.my_favorite_number}")

    glava_ili_pismo = random.randint(1, 10)
    print(f"glava_ili_pismo: {glava_ili_pismo}; {"Glava" if glava_ili_pismo < 5 else "Pismo"}")

    if count > 10:
        break

end_time = datetime.datetime.now()
print(f"start_time: {start_time}")
print(f"end_time: {end_time}")
print(f"sekunde: {(start_time-end_time).total_seconds()}")