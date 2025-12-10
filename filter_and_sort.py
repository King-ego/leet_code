notes_with_duplicates = [
    10,3,5,2,1,4,7,9,6,8,0, 31, 25, 18, 22, 15, 27, 30, 12, 20, 11,3,3,3,
    10,3,5,2,1,4,7,9,6,8,0, 31, 25, 18, 22, 15, 27, 30, 12, 20
]

# Sort List in O(n) time complexity and remove duplicates for item >= 0
def counting_sort_with_remove_duplicates(arr):
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
        if count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1

    return arr[:sorted_index]

if __name__ == "__main__":
    sorted_notes_no_duplicates = counting_sort_with_remove_duplicates(notes_with_duplicates)
    print(f"Sorted notes without duplicates: {sorted_notes_no_duplicates}")