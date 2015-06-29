import os
import sys
import math

# records　是一个评分列表：用户 u　对物品 i 的实际评分 rui　和预测评分　pui　[u,i,rui,pui]
# 加大对预测不准物品的平方项惩罚
def RMSE(records):
	return math.sqrt(sum([(rui - pui) * (rui - pui) for u, i, rui, pui in records])/float(len(records)))


# major components of the gravity recommendation system
# 预测结果取整问题
def MAE(records):
	return sum([abs(rui-pui) for u,i,rui,pui in records]/float(len(records)))

