import numpy as np
import torch as tc
import time as tm

vec_np_i = np.random.randint(0,100,10000000)
print('Klasa danych np:', type(vec_np_i[0]),"\n")
vec_tc_i = tc.from_numpy(vec_np_i)
print('Klasa danych tc:', type(vec_tc_i[0]),"\n")


b_np_i = tm.time()
np.sum(vec_np_i)
e_np_i = tm.time()
print('Czas np dla int64: ',e_np_i - b_np_i)

b_tc_i = tm.time()
tc.sum(vec_tc_i)
e_tc_i = tm.time()
print('Czas tc dla int64: ',e_tc_i - b_tc_i, "\n")

vec_np_f16 = np.random.rand(10000000).astype(np.float16)
vec_tc_f16 = tc.from_numpy(vec_np_f16)

b_np_f16 = tm.time()
tc.sum(vec_tc_f16)
e_np_f16 = tm.time()
print('Czas np dla float16 : ', e_np_f16 - b_np_f16)

b_tc_f16 = tm.time()
tc.sum(vec_tc_f16)
e_tc_f16 = tm.time()
print('Czas tc dla float16: ', e_tc_f16 - b_tc_f16, "\n")

vec_np_f32 = np.random.rand(10000000).astype(np.float32)
vec_tc_f32 = tc.from_numpy(vec_np_f32)

b_np_f32 = tm.time()
tc.sum(vec_tc_f32)
e_np_f32 = tm.time()
print('Czas np dla float32 : ', e_np_f32 - b_np_f32)

b_tc_f32 = tm.time()
tc.sum(vec_tc_f32)
e_tc_f32 = tm.time()
print('Czas tc dla float32: ', e_tc_f32 - b_tc_f32, "\n")

vec_np_f64 = np.random.rand(10000000).astype(np.float64)
vec_tc_f64 = tc.from_numpy(vec_np_f64)

b_np_f64 = tm.time()
tc.sum(vec_tc_f64)
e_np_f64 = tm.time()
print('Czas np dla float64 : ', e_np_f64 - b_np_f64)

b_tc_f64 = tm.time()
tc.sum(vec_tc_f64)
e_tc_f64 = tm.time()
print('Czas tc dla float64: ', e_tc_f64 - b_tc_f64, "\n")

#czy tc dziedziczy ten sam typ danych?