#coding=utf-8
from randomGraph import randomGraph
from drawGraph import drawGraph

def run():
	v_nums=int(input("点数 "))
	e_nums=int(input("边数 "))
	max_e=v_nums*(v_nums)/2
	if e_nums>max_e:
		print("超出最大边数")
		exit()
	G=randomGraph(v_nums,e_nums)  #生成邻接矩阵
	drawGraph(G,v_nums,e_nums)     #画图
	#simulatedAnnealing(G,v_nums,e_nums)  #求最小覆盖	

if __name__=="__main__":
	run()
