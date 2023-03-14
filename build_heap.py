# python3




def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    s = len(data)
    for i in range((s//2)-1, -1, -1):
        j = i
        while True:
            leftChild = 2*j+1
            if leftChild < s and data[leftChild] < data[j]:
                j = leftChild

            rightChild = 2*j+2
            if rightChild < s and data[rightChild] < data[j]:
                j = rightChild

            if i != j:
                data[i] , data[j] = data[j], data[i]
                swaps.append((i, j))
                i = j
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
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
