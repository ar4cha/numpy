import numpy as np
print("version numpy:",np.__version__)
first = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
second = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
third = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
four = np.arange(1,16,1)
x = np.concatenate((first,second,third,four))
print(x)

def createArray(x):
  a = np.array([1,2,3])
  b = np.array([(1.5,2,3), (4,5,6)], dtype = float )
  c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)
  print(a)
  print("type in a is: ",type(a))
  print(b)
  print("type in b is: ",type(b))
  print(c)
  print("type in c is: ",type(c))
  print("\n")
  print(a.ndim)
  print(b.ndim)
  print(c.ndim)

def shapeArray(x):
 pipi = x.reshape(4, 15)
 print(pipi)
  
def sliceArray(x):
  pushka = x.reshape(6, 10)
  print("\n")
  gg = pushka[1, 0:11]
  print(gg)
def arrayIO(x):
  pipi = x.reshape(6, 10)
  gg = (pipi[1, 0:11])

  np.save("save", gg)
def arithmetic(x):
  you = np.arange(1, 11, 1)
  lol = (np.multiply(you, 2))
  kek = (np.divide(you, 10))
  ggwp = (np.add(5,you))
  np.save("Results", lol, kek, ggwp)



#main
createArray(x)
shapeArray(x)
sliceArray(x)
arrayIO(x)
arithmetic(x)


