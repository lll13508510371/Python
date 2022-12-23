# 没有锁
def add(a):
    a += 1


import dis

dis.dis(add)

"""
  3           0 LOAD_FAST                0 (a)      # 锁定 a 的值
              2 LOAD_CONST               1 (1)      # 锁定常量
              4 INPLACE_ADD                         # 执行加法运行
              6 STORE_FAST               0 (a)      # 存储运算的结果
              8 LOAD_CONST               0 (None)   # 加载常量
             10 RETURN_VALUE                        # 返回运算的结果
"""

value = add(a=5)
