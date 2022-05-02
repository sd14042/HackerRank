if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for count_x in range(x+1):
        for count_y in range(y+1):
            for count_z in range(z+1):
                if not count_x+count_y+count_z == n:
                    list.append([count_x,count_y,count_z])
    print(list)
