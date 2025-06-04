def two_sum(nums, target):
    # 1. Buat list pasangan (nilai, indeks_asli)
    pairs = [(num, i) for i, num in enumerate(nums)]
    # 2. Urutkan berdasarkan nilai
    pairs.sort(key=lambda x: x[0])

    # 3. Inisialisasi dua pointer
    left = 0
    right = len(pairs) - 1

    while left < right:
        val_left, idx_left = pairs[left]
        val_right, idx_right = pairs[right]
        current_sum = val_left + val_right

        if current_sum == target:
            # Kembalikan indeks asli (bisa i < j atau i > j, urutan tidak masalah)
            return (idx_left, idx_right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1

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
