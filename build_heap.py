# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    s = len(data)
    for i in range((s//2)-1, -1, -1):
        minIndex = i
        leftChild = 2*minIndex+1
        rightChild = 2*minIndex+2
        while True:
            if leftChild < s and data[leftChild] < data[minIndex]:
                minIndex = leftChild
 
            if rightChild < s and data[rightChild] < data[minIndex]:
                minIndex = rightChild

            if i != minIndex:
                data[i] , data[minIndex] = data[minIndex], data[i]
                swaps.append((i, minIndex))
                i = minIndex
                leftChild = 2*i+1
                rightChild = 2*i+2
            else:
                break
    if len(swaps)>4*len(data):
        raise Exception("Greater than 4n")

    return swaps

def main():
    
    inputType = input("F or I")

    if 'F' in inputType:
        fileName = input("File Name?")
        tests = './tests/'
        file = tests + fileName
        with open(file, 'r')as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    elif 'I' in inputType:
        n = int(input())
        data = list(map(int, input().split()))

    else :
        print("Input error")

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, minIndex in swaps:
        print(i, minIndex)


if __name__ == "__main__":
    main()
