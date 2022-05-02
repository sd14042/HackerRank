if __name__ == '__main__':
    lists = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lists.append([name, score])
        
    sorted_data = sorted(lists, key=lambda x:(x[1],x[0]))
    
    for index,data in enumerate(sorted_data):
        if index == 0:
            max_score = data[1]
            continue
            
        if max_score == data[1]:
            continue
        elif max_score < data[1]:
            if not 'second_max_score' in locals():
                second_max_score = data[1]
            
            if second_max_score < data[1]:
                break
            else:
                print(data[0])

            