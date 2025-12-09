notes = [10,2,3,5,2,1,4,7,9,6,8,0]

# Sort List in O(n) time complexity
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    print(f"Initial count array: {count}")

    for num in arr:
        count[num] += 1

    print(f"Count array after counting elements: {count}")

    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1
    return arr

if __name__ == "__main__":
    sorted_notes = counting_sort(notes)
    print("Sorted notes:", sorted_notes)