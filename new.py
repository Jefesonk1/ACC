import numpy as np
import openpyxl
import math
import random as rd

def extractFromFile(filename,min_r,min_c,max_r,max_c):
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
		z+=((data[x][i]-data[y][i])**2)
	z=math.sqrt(z)
	#print(z)
	return z

def makeGrid(data):
	index=[]
	siz=len(data)
	grid=np.full((math.floor(math.sqrt(10*siz)),math.floor(math.sqrt(10*siz))),-1)
	#print(rd.randrange(0,22))
	for i in range(siz):
		while True:
			a=rd.randrange(0,len(grid)-1)
			b=rd.randrange(0,len(grid)-1)
			if grid[a][b] == -1:				
				grid[a][b]=i
				index.append([a,b])
				break
	return grid,index

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




def move(ant,grid,index,indexPos):
	possibilities=[-1,0,1]
	oldData=grid[ant[0],ant[1]]
	oldPos=ant.copy()
	c_ant=ant.copy()
	while True:	
		x=possibilities[rd.randrange(0,3)]
		y=possibilities[rd.randrange(0,3)]
		c_ant[0]+=x
		c_ant[1]+=y
		c_ant=np.mod(c_ant, (len(grid),len(grid)))
		if grid[c_ant[0],c_ant[1]]==-1:
			grid[c_ant[0],c_ant[1]]=oldData
			grid[oldPos[0],oldPos[1]]=-1
			index[indexPos]=[c_ant[0],c_ant[1]]
			return c_ant






def getNeighborhood(data,grid,x,y,s,alpha):
	'''print('inicio{}'.format(grid[x][y]))
	print('x{}'.format(x))
	print('y{}'.format(y))'''
	s=math.floor((s-1)/2)
	y_s = y - s
	x_s = x - s
	total = 0.0
	for i in range((s*2)+1):
		xi = (x_s + i) % len(grid)
		for j in range((s*2)+1):
			if j != x and i != y:
				yj = (y_s + j) % len(grid)
				o = grid[xi][yj]
				if o is not None and  o !=-1 and grid[x,y]!=o:
					'''print('\n')
					print('valor coordenada passada{}'.format(grid[x,y]))
					print('valor coordenada achada{}'.format(grid[xi,yj]))
					print('\n')'''
					dist=calcDist(data,grid[x,y],grid[xi,yj])/alpha
					total+=(1-dist)
	if (1/(s**2))*total>0:
		return (1/(s**2))*total
	else:
		return 0


def pPick(data,grid,x,y,s,kp,alpha):
	prob=np.random.sample()
	if prob < (kp/(kp+getNeighborhood(data,grid,x,y,s,alpha)))**2:
		return True
	return False

def pDrop(data,grid,x,y,s,kd,alpha):
	prob=np.random.sample()
	if prob < ((getNeighborhood(data,grid,x,y,s,alpha))/(kd+(getNeighborhood(data,grid,x,y,s,alpha))))**2:
		return True
	return False


def ACC(data,kp,kd,alpha,s,its):
	contador=0
	index=[]#indices que contem dados na matriz
	z=normalize(data)
	grid,index=makeGrid(z)
	print(grid)
	print('\n')
	print(index)

	indexPos=rd.randrange(0,len(index))
	ant=index[indexPos]


	while True:
		ant=move(ant,grid,index,indexPos)
		drop=pDrop(z,grid,ant[0],ant[1],s,kd,alpha)
		#print(drop)
		if drop:
			pick=False
			while not pick:
				indexPos=rd.randrange(0,len(index))
				ant=index[indexPos]
				if pPick(z,grid,ant[0],ant[1],s,kp,alpha):
					pick=True
		contador+=1			
		if contador>=its:
			break
	print('\n')
	print(grid)
	print('\n')
	print(index)
	return grid
		#print('\n')	

def main():
	filename="Dados Para Agrupamento.xlsx"
	a=extractFromFile(filename,2,1,29,2)
	b=extractFromFile(filename,2,3,29,6)
	arr=np.asarray(b, dtype=np.float32)
	kp=0.8	
	kd=0.3
	alpha=0.5
	s=3
	its=500
	jog=ACC(arr,kp,kd,alpha,s,its)
	for i in range(len(jog)):
		for j in range(len(jog)):
			pass
	for i in range(len(a)):
		print('{} {}     {}'.format(i,a[i][1], a[i][0]))


if __name__ == '__main__':
	main()	