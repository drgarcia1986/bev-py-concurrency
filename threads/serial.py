from time import sleep

counter = 0


def update_counter(count, delay):
    global counter
    for _ in range(count):
        current_counter = counter
        sleep(delay)
        counter = current_counter + 1


if __name__ == "__main__":
    print('start serial')

    update_counter(5, 0.5)
    update_counter(3, 1)
    update_counter(10, 0.2)

    print('Final value is ', counter)
