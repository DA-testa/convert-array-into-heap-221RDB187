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
        Sift(data, minIndex, swaps)


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2-1, -1, -1):
        Sift(data, i, swaps)
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
