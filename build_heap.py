# python3




def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    s = len(data)
    for i in range((s//2)-1, -1, -1):
        minIndex = i
        while True:
            leftChild = 2*minIndex+1
            if leftChild < s and data[leftChild] < data[minIndex]:
                minIndex = leftChild

            rightChild = 2*minIndex+2
            if rightChild < s and data[rightChild] < data[minIndex]:
                minIndex = rightChild
            if i != minIndex:
                data[i] , data[minIndex] = data[minIndex], data[i]
                swaps.append((i, minIndex))
                minIndex = i
            else:
                break
    return swaps

def main():
    
    inputType = input("F or I")

    if inputType == 'F':
        fileName = input("File Name?")
        if "./test/" not in fileName:
            fileName = "test/" + fileName
        with open(fileName, 'r')as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    elif inputType == 'I':
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
