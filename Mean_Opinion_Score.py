
scores_before_quantization = [3, 4, 4, 3, 5] 
scores_after_quantization = [4, 4, 5, 4, 5]
def calculate_mos(scores):
    return sum(scores) / len(scores)

mos_before = calculate_mos(scores_before_quantization)
mos_after = calculate_mos(scores_after_quantization)

print(f"Mean Opinion Score Before Quantization: {mos_before:.1f}")
print(f"Mean Opinion Score After Quantization: {mos_after:.1f}")
