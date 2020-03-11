def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count_pos = 0
    sum_neg = 0
    for i in arr:
        if i > 0:
            count_pos +=1
        elif i < 0:
            sum_neg += i
    return [count_pos, sum_neg]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print (count_positives_sum_negatives(nums))
