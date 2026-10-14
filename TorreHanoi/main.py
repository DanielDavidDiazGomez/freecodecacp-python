def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]

    def snapshot():
        return ' '.join(str(rod) for rod in rods)

    states = [snapshot()]

    def move(disks, source, target, auxiliary):
        if disks == 0:
            return
        move(disks - 1, source, auxiliary, target)
        rods[target].append(rods[source].pop())
        states.append(snapshot())
        move(disks - 1, auxiliary, target, source)

    move(n, 0, 2, 1)
    return '\n'.join(states)
