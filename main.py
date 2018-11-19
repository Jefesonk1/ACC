import numpy as np
import openpyxl
import math
import random as rd
def abrirArquivo(filename,min_r,min_c,max_r,max_c,data_type):
	book=openpyxl.load_workbook(filename)
	sheet=book.active
	data2=[]
	row_count=0
	col_count=0
	temp=[]
	for row in sheet.iter_rows(min_row=min_r, min_col=min_c, max_row=max_r, max_col=max_c):
		for cell in row:	
			temp.append(cell.value)
			col_count+=1
		col_count=0
		row_count+=1
		data2.append(temp.copy())
		temp.clear()
	return data2

def calcDist(data,x,y):
	max_c=len(data[0])
	z=0
	for i in range(max_c):
		z+=(data[x][i]-data[y][i])**2
	z=math.sqrt(z)
	return z

def makeGrid(data,index):
	siz=len(data)
	grid=np.full((math.floor(math.sqrt(10*siz)),math.floor(math.sqrt(10*siz))),-1)
	print(rd.randrange(0,22))
	for i in range(siz):
		while True:
			if grid[rd.randrange(0,len(grid)-1)][rd.randrange(0,len(grid)-1)] == -1:
				a=rd.randrange(0,len(grid)-1)
				b=rd.randrange(0,len(grid)-1)
				grid[a][b]=i
				index.append((a,b))
				break
	print (grid)
	return grid
	

def normalize(data):
	lenx=len(data)
	leny=len(data[0])
	z=np.zeros((lenx,leny))
	arrMax=np.zeros(leny)
	arrMin=np.zeros(leny)
	for j in range(leny):
		i_max=np.argmax(data[:,j])
		arrMax[j]=data[i_max][j]

		i_min=np.argmin(data[:,j])
		arrMin[j]=data[i_min][j]
	for i in range(lenx):
		for j in range(leny):
			z[i][j]=(data[i][j]-arrMin[j])/(arrMax[j]-arrMin[j])
	return z

#def sortP()	
	
def ACC(data):
	index=[]#indices que contem dados na matriz
	z=normalize(data)
	grid=makeGrid(z,index)
	agents=np.empty(math.ceil(len(data)*0.1),np.int_)#array de formigas
	
	
	temp=rd.sample(range(len(data)),math.ceil(len(data)*0.1))#gerando 3 numeros aleatorios correspondentes ao indice de dados(qtd)
	for i in range(len(temp)):
		agents[i]=temp[i]
		
	print(index)
	print('\n')
	for i in range(len(agents)):
		print(agents[i])
	print(agents)
		
	
	
	
	
	
def main():
	filename="Dados Para Agrupamento.xlsx"
	a=abrirArquivo(filename,2,1,29,2,"str")
	b=abrirArquivo(filename,2,3,29,6,"float")
	arr=np.asarray(b, dtype=np.float32)
	#print(arr)
	#for i in range(len(a)):
	#	print(a[i])
	#print(calcDist(arr,0,27))
	#makeGrid(arr)
	#z=normalize(arr)
	#grid=makeGrid(z)
	ACC(arr)




if __name__ == '__main__':
	main()