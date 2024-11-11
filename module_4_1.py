from fake_math import divide as f_0
from true_math import divide as f_inf

result_0_1 = f_0 (22, 5)
result_0_2 = f_0 (22, 0)
result_inf_1 = f_inf (14, 7)
result_inf_2 = f_inf (14, 0)
print(result_0_1)
print(result_0_2)
print(result_inf_1)
print(result_inf_2)