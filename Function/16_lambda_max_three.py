maximum = lambda first, second, third: first if first >= second and first >= third else second if second >= third else third
print(maximum(14, 27, 19))
