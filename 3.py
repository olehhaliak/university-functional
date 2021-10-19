def f(x):
    return 0.01 * x ** 3 - 0.25 * x ** 2 + x


def gen():
    x = 0
    while x < 50:
        x = x + 1
        yield round(f(x), 4)


gen = gen()
arr = []
for i in range(50):
    arr.append(next(gen))


def find_extremum():
    if len(arr) >= 2:
        if arr[0] < arr[1]:
            print(f"Local min at {arr[0]}")
        elif arr[0] > arr[1]:
            print(f"Local max at {arr[0]}")

    if len(arr) >= 3:
        prev = None
        next = None
        for i in range(1, len(arr) - 1, 1):
            prev = arr[i - 1]
            next = arr[i + 1]
            current = arr[i]
            if current < prev and current < next:
                print(f"Local min at {arr[i]}");
            elif current > prev and current > next:
                print(f"Local max at {arr[i]}");

    if len(arr) >= 2:
        if arr[len(arr) - 2] < arr[len(arr) - 1]:
            print(f"Local max at {arr[len(arr) - 1]}")
        elif arr[len(arr) - 2] > arr[len(arr) - 1]:
            print(f"Local min at {arr[len(arr) - 1]}")


find_extremum()