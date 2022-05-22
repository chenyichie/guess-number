from random import randint
from time import sleep
from pickle import load, dump


def load_pickle(file):
    with open(file, 'rb') as load_file:
        if not load_file == '':
            return load(load_file)


def guess():
    num = randint(1, 100)
    steps = 0
    min_num = 1
    max_num = 100
    while True:
        guess_num = 0
        while guess_num < min_num or guess_num > max_num:
            guess_num = int(input(f'guess a number between {min_num} and {max_num}'))
        steps += 1
        if guess_num == num:
            print(f'you guessed right, you use {steps} steps to guess right.')
            break
        elif guess_num > num:
            print('Try lower')
            max_num = guess_num
        else:
            print('Try bigger')
            min_num = guess_num
    return steps


def average(list_for_average):
    if type(list_for_average) = 'list':
        try:
            return round(sum(list_for_average) / len(list_for_average))
        except ValueError:
            print('no any data')

def main():
    step: list = []
    data = load_pickle('data.pkl')
    times = int(input("How many times to guess a number?"))
    if not times == 0:
        for x in range(0, times):
            steps = guess()
            step.append(steps)
            data.append(steps)
    if not times == 0:
        print(f'This is your all use steps: {step} ,and average is {average(step)}')
        with open('data.pkl', 'wb') as load_data:
            dump(data, load_data)
    else:
        print('No data')
    print('Enter "data" to read the data,enter"exit" to exit,enter"data average" to get average of data')
    while True:
        input_now = input()
        match input_now:
            case 'data':
                print(f'history data:{data})
            case 'data average':
                print(f'average of data is {average(data)}')
            case 'exit':
                exit(0)
            case _:
                pass
        sleep(0.001)


if __name__ == "__main__":
    main()
