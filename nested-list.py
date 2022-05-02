if __name__ == '__main__':
    lists = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lists.append([name, score])
        
    sorted_data = sorted(lists, key=lambda x:(x[1],x[0]))
    
    print(sorted_data)