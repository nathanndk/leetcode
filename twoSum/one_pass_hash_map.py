def two_sum(nums, target):
    #Hash map
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

    return None


if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9

    result = two_sum(array, target)
    if result is not None:
        i, j = result
        print(f"Brute-Force → Indeks pasangan: ({i}, {j})")
    else:
        print("Brute-Force → Tidak ditemukan pasangan.")
