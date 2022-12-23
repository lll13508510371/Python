import queue

# 队列是基于线程安全的
q = queue.Queue(maxsize=10)

# 往队列里面存放数据
for i in range(1, 11):
    q.put(f'包子 {i}')

# q.put(f'包子 11')
# q.put_nowait(f'包子 11')
print(q, q.qsize())
for i in range(1, 11):
    item = q.get()
    print(item)
# item = q.get()
item = q.get_nowait()
"""
    .put            往队列里面放数据, 如果队列里面的数据满了,就等队列有空间的时候再放进去
    .put_nowait     如果满了,不等待,直接报错
    .get            从队列里面获取数据,没有数据默认进行等待
    .get_nowait     如果没有数据了就直接报错
"""
