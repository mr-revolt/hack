import os, time

local_time = time.localtime()
local_year = local_time.tm_year
local_month = local_time.tm_mon
local_day = local_time.tm_mday
cet = "-"
seq = (str(local_year), str(local_month), str(local_day))
beauti_day = cet.join(seq)

# TODO: 根据日期创建当天的文件夹
# TODO: 复制一个特定模板的文件夹和文件
# TODO: 需要进行Excel的读写和修改
# TODO:
print(range(10))