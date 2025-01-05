if __name__ == '__main__':
    data = input()

    sol = set()

    for i in range(len(data)):
        for j in range(i,len(data)):
            sol.add(data[i:j+1])

    print(len(sol))