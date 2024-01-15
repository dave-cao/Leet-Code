class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # group the position and speed together
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # sort the cars based on position
        cars.sort(key=lambda a: a[0])

        # intialize stack
        stack = []

        # go through the cars list backwards
        for i in range(len(cars) - 1, -1, -1):
            # grab our time needed to reach the finish line
            time = (target - cars[i][0]) / cars[i][1]

            # if there is nothing in our stack, then append (first car)
            # if a behind car takes longer to get to the finish line,
            # then it can't be a part of the fleet of the first position car
            # if all the cars are faster than the first car,
            # then the first car will be the deciding factor, and create a
            # single fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


def main():
    sol = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    sol.carFleet(target, position, speed)
    pass


if __name__ == '__main__':
    main()
