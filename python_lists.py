if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for i in range(N):
        string = input().split()
        if string[0] == 'insert':
            list.insert(int(string[1]), int(string[2]))
        elif string[0] == 'print':
            print(list)
        elif string[0] == 'remove':
            list.remove(int(string[1]))
        elif string[0] == 'append':
            list.append(int(string[1]))
        elif string[0] == 'sort':
            list = sorted(list)
        elif string[0] == 'pop':
            list.pop(-1)
        elif string[0] == 'reverse':
            list.reverse()
