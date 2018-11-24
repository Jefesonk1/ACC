import numpy as np
import openpyxl
import math
import random as rd
def abrirArquivo(filename,min_r,min_c,max_r,max_c):
	book=openpyxl.load_workbook(filename)
	sheet=book.active
	data=[]
	temp=[]
	for row in sheet.iter_rows(min_row=min_r, min_col=min_c, max_row=max_r, max_col=max_c):
		for cell in row:	
			temp.append(cell.value)
		data.append(temp.copy())
		temp.clear()
	return data

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
			a=rd.randrange(0,len(grid)-1)
			b=rd.randrange(0,len(grid)-1)
			if grid[a][b] == -1:				
				grid[a][b]=i
				index.append([a,b])
				break
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
	
def moverFormiga(formiga,grid,agents,index):
	possibilidades=[-1,1]	
	x=possibilidades[rd.randrange(0,2)]
	y=possibilidades[rd.randrange(0,2)]
	temp=grid[formiga[0],formiga[1]]
	oldPos=formiga.copy()
	newPos=formiga.copy()
	newPos[0]+=x
	newPos[1]+=y
	newPos=np.mod(newPos, (len(grid),len(grid)))
	'''print('teste')
	print(agents)
	print(oldPos)
	print(newPos)
	print("teste")
	print(formiga)
	print(newPos)'''	
	if grid[newPos[0],newPos[1]]==-1:
		formiga=newPos
		grid[formiga[0],formiga[1]]=temp
		grid[oldPos[0],oldPos[1]]=-1
		index[agents]=[newPos[0],newPos[1]]
		print(grid)
		return formiga
	else:
		moverFormiga(formiga,grid,agents,index)
	return formiga


def densidade():
	pass


def ACC(data):
	index=[]#indices que contem dados na matriz
	z=normalize(data)
	grid=makeGrid(z,index)
	agents=rd.randrange(0,len(index))
	print(agents)
	print(grid)
	print('\n')
	print(index)
	print('\n')
	moverFormiga(index[agents],grid,agents,index)
	print('\n')
	print(index)
	
def main():
	filename="Dados Para Agrupamento.xlsx"
	a=abrirArquivo(filename,2,1,29,2)
	b=abrirArquivo(filename,2,3,29,6)
	arr=np.asarray(b, dtype=np.float32)
	ACC(arr)
	



if __name__ == '__main__':
	main()