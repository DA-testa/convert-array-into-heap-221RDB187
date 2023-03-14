# python3




def build_heap(data):
    swaps = []
    s = len(data)
    for i in range((s//2)-1, -1, -1):
        j = i
        while True:
            l = 2*j+1
            if l < s and data[l] < data[j]:
                j = l

            r = 2*j+2
            if r < s and data[r] < data[j]:
                j = r

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
            data=list(map(int,f.readline().split()))

    elif 'I' in inputType:
        n = int(input())
        data = list(map(int, input().split()))

    else:
        print("Input error")

    assert len(data) == n
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
