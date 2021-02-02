while True:
    try:
        n = int(input())
        library = []
        for i in range(n):
            library.append(input())
        library.sort()
        for v in library:
            print(v)
    except EOFError:
        break

