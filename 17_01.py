# Count the number of score combinations.
def cn_nums_for_final_score(final_score, scores):
    nums = []
    for i in range(len(scores)):
        nums.append([1])
        for j in range(1, final_score + 1):
            wo_this_score = 0 if i == 0 else nums[i - 1][j]
            w_this_score = 0 if j - scores[i] < 0 else nums[i][j - scores[i]]
            nums[i].append(wo_this_score + w_this_score)
    return nums[-1][-1]
