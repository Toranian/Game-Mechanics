def trace(x, y, target_x, target_y):

    get_x = True
    get_y = True

    while True:

        if get_x:

            if x == target_x:
                get_x = False

            if x > target_x:
                x -= 1
            if x < target_x:
                x += 1

        if get_y:

            if y == target_y:
                get_y = False

            if y > target_y:
                y -= 1
            if y < target_y:
                y += 1

        print(x, y, target_x, target_y)

        if not get_x and not get_y:
            print(x, y, target_x, target_y)
            return x, y

trace(10, 10, 100, 100)
