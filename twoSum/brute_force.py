def two_sum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
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
