def fnidMinMax(arr):
    sorted_arr = sorted(arr)
    return [sorted_arr[0], sorted_arr[-1]]

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = fnidMinMax(arr)

    print(f"min: {result[0]}, max: {result[1]}")