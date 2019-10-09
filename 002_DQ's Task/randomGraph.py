#coding=utf-8

import numpy as np
import random
from random import shuffle

def randomGraph(v_nums,e_nums):
	mat=np.zeros((v_nums,v_nums))  #生成全0矩阵
	'''给上三角（没有对角线）随机置1，在(V×V-V)/2个可能的边中一共置e_nums次'''
	random_list=[]
	for i in range((v_nums*v_nums-v_nums)//2):
		random_list.append(0)
	print(random_list)
	for i in range(e_nums):
		random_list[i]=1
	print(random_list)
	shuffle(random_list)
	print(random_list)
	
	
	for i in range(v_nums):
		for j in range(v_nums):
			if i>=j:
				print("对角线以下 "+str(i)+" "+str(j)+" 排除")
				continue
			else:
				print(i,j)
				mat[i][j]=random_list[-1]
				random_list.pop(-1)               #把随机数列表里的种子种到矩阵的上三角里面
				
			
	#把上三角复制给下三角。组成对称矩阵
	mat+=mat.T-np.diag(mat.diagonal())
	
	print("*****")
	print(mat)
	print("****")
	#验证是不是对称矩阵
	print(mat.T==mat)
	
	return mat
	
	
	


if __name__=="__main__":
	randomGraph(5,10)
