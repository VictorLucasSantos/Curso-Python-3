import multiprocessing

results = []


def calc_square(numbers):
    global results
    print("calculate square numbers")
    for number in numbers:
        print("square: {} ".format(number * number))
        results.append(number * number)
        print("Square result: {} ".format(results))


def calc_cube(numbers):
    global results
    print("calculate cube of numbers")
    for number in numbers:
        print("cube: {} ".format(number * number * number))
        results.append(number * number * number)
        print("Cube result: {} ".format(results))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done")
