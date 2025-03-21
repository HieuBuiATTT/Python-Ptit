def find_min_subarray(arr):
    min_sum = float('inf')  
    current_sum = 0
    start = end = temp_start = 0
    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum < min_sum:
            min_sum = current_sum
            start = temp_start
            end = i
        if current_sum > 0:
            current_sum = 0
            temp_start = i + 1
    return min_sum, arr[start:end+1]

numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

min_sum, subarray = find_min_subarray(numbers)
print("Tổng nhỏ nhất của dãy con là:", min_sum)
print("Dãy con nhỏ nhất là:", subarray)
