# 二分查找
def binarySearch(li, item):

    # Search
    print("[*] Binary Search Start")
    timeStart = time.time() # Timer
    n   = 1 # Counter
    low = 0
    high= len(li) - 1
    while low <= high:
        mid   = int((low+high)/2)
        guess = li[mid]
        print("[#"+str(n)+"] Guessing the MID: ", mid)
        if guess == item:
            print("[+] Found! The Number "+str(item)+" at the"+str(mid)+"/"+str(li[-1]))
            timeEnd = time.time()
            timeCost = timeEnd - timeStart
            print("[+] Totally Cost Time: ", timeCost)
            return mid, timeCost
        elif guess > item:
            high = mid - 1
        else:
            low  = mid + 1
        n += 1
    print("[!] Error: Item Not In List!")
    print("[-] Binary Search Stopped.")
    return