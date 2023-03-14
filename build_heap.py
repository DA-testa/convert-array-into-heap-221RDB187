# python3

def Sift(data, i , swaps):
    n = len(data)
    minIndex = i
    leftChild = 2*i+1
    if leftChild < n and data[leftChild] < data[minIndex]:
        minIndex = leftChild

    rightChild = 2*i+2
    if rightChild < n and data[rightChild] < data[minIndex]:
        minIndex = rightChild
    if i != minIndex:
        data[i] , data[minIndex] = data[minIndex], data[i]
        swaps.append(i, minIndex)
        minIndex = i



def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2-1, -1, -1):
        Sift(data, i, swaps)
    return swaps

def main():
    
    inputType = input("F or I")

    if inputType == 'F':
        fileName = input("File Name?")
        if "test/" not in fileName:
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
