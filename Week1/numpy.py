import numpy as np

# initialising an array in numpy, basic syntax: np.array(HereGoesAList)
a = np.array([1,2,3]) 
# initialising an multidimensional array in numpy
# also while defining an array, we can define the type of data we wanna store, suppose if there are not long interegers we can store them as int16 so they consumer less storage
b = np.array([[1,2,3],[4,5,6]], dtype='int16')
print(f"a = {a}\nb = {b}\n")

#Dimensions:
print(f"dimensions of a = {a.ndim}") #ndim = number of dimensions for a i.e 1
print(f"dimensions of b = {b.ndim}") #tells the number of dimesions for b i.e 2
print()

#Shape: tells about the row and columns for the array, (row,column)
print(f"Shape of a; a.shape = {a.shape}") #here output would be (3,); i.e 3 row 1 column, 1 not explicitly mentioned
print(f"Shape of b; b.shape = {b.shape}") #here output = (3,2); 3 row, 2 column
print()

#Getting type of data of the array
print(f"data type of a: a.dtype = {a.dtype}") #here output would be what type of data, does a store, by default int are stored as int64
print(f"data type of b: b.dtype = {b.dtype}") #here we changed the data type, so they are stored as int16
print()

#Sizes in numpy arrays: size of array and size of items
#Size of item 
print(f"size of a item in a; a.itemsize= {a.itemsize}") #8 byte since we are storing int as int64, 
print(f"data type of b: b.itemsize = {b.itemsize}") #2 byte, int store as int16, 
        #doubt learn how did int64->8 and how int16->2 ?
#Size of an array (.size) gives the number of items in the array
print(f"size of array, a: a.size = {a.size}") #output 3 as there are 3 items
print(f"size of array, b: b.size = {b.size}") #output 6 as there are 6 items
# for total size of array i.e total storage taken by the array
print(f"Total size of array, a: a.size * a.itemsize = {a.size * a.itemsize}") #output, 3 * 8 = 24
print(f"Another way of finding the total number of bytes in array is, a.nbytes = {a.nbytes}") #n.bytes = number of bytes
print()



c = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])
print(f"c = {c}")
#Getting a specific element from a array, say 13, so c[row, column]
print(f"Accessing c[1,5] = {c[1,5]}")

#Getting a row, similar to string, c[row, :]
print(f"c 1st Row, c[0, :] = {c[0, :]}")

#Getting a column
print(f"c 1st cloumn, c[:,0] = {c[:,0]}")

#Getting fancy with this accessing elements, [startIndex(inclusive), endIndex(exclusive), stepSize]
print(f"c[0, 1:6:2] = {c[0, 1:6:2]}")
print(f"c[0, 1:-1:2] = {c[0, 1:-1:2]}")
print()

#Changing elements in arrays
#Changing one 1st column to 5, c[row,cloumn] = newValue
c[:,0] = 5
print(f"after c[:0:] = 5; c = \n{c}")

#3-d Example
d = np.array([ [[1,2],[3,4]], [[5,6], [7,8]] ]) #here d is an 3d array of dimensions, 2x2x2, so basically the number in the end of the dimensions, speficies the number of numbers inside the bracket there are going to be written in an array, here there are 2, so 1,2 and 3,4 like these, there are going to be 2 elements finally inside the array
#another representation of d, but simple 
d1 = np.array([
    [
        [1,2],[3,4]
    ], 
    [
        [5,6],[7,8]
    ]
])
print(f"d = \n{d}\n")

#Getting specific elements in 3-d, (work outside in) [row, column, element]
print(f"d[0,1,1] = {d[0,1,1]}")

#Replacing  
#replacing the 2nd row in each block
d[:,1,:] = [[9,9],[8,8]]
print(f"d = \n{d}\n")



#Intialising Different types of arrays
# All 0s matrix
print()
np.zeros((2,3)) #here inside the brackets write the dimension of the array you want. 
print(f"Initialising All 0s Matrix:\nnp.zeroes((2,3), dtype = 'int32'), inside the () there goes dimensions of the matrix you want, you can also specify the datatype you want\n{np.zeros((2,3))}")
#All 1s matrix
np.ones((2,3))
print(f"Matrix having all 1s: np.ones((2,3), dtype = 'int32') \n{np.ones((2,3), dtype='int32')}")
#AnyOther number matrix
print(f"\nCreating a matrix of anyother number\nnp.full((dimensions), number, datatype);\nExample: np.full((2,2), 99, dtype = 'int32'):\n{np.full((2,2), 99, dtype = 'int32')}")
print()

#Creating an array with similar dimersion to one created before but with a new number 
print("Initialing array with similar dimensions to one created before but with a new number")
print(np.full(c.shape, 4)) #syntax: np.full(arrayNameofCopyingDimensions, number)
#or
print()
print(np.full_like(c, 4)) #when using full like, you don't need to use c.shape, syntax: np.full_like(arrayNameofCopyingDimensions, number)
print()

#Initialing an Matrix of random numbers
print('Initialing an Matrix of random numbers')
print(np.random.rand(4,2)) #Keep in mind when we pass in dimension here we don't write an extra ()
print()
#For making an random matrix of same dimernsion of a matrix as created one before we use
print(np.random.random_sample(c.shape)) #here we pass in, arrayName.shape
#for making a matrix using random integer value 
print("Matrix with random int")
print(np.random.randint(4,8, size = (3,3))) #syntax: np.random.randint(startInt(inclusive), endInt(exclusive), size = (dimensions)) 
#Making an identity matrix
print(f"Making an Identity matrix:\n{np.identity(3)}")
print()

#Repeating an array
print(f"Repeating an array")
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis = 0) # syntax np.repeat(arrayYouWannaRepeat, numberofTimetoRepeat, axis(no idea what itis))
print(r1)
print()



#Solving a question
print("Solving a question")
s = np.ones((5,5))
#replace 2->4 row from column 2->4 with 0
s[1:4, 1:4] = 0
#replace the center element = 9
s[2,2] = 9
#final matrix
print(s)
print()


#Copying arrays
a = np.array([1,2,3])
b = a.copy() #We can't do, b = a, as that just makes copy the pointers and making changes in b will also make changes in a.



#Mathematics on matrices
a = np.array([1,2,3,4]) ; b = np.array([5,6,7,8])
#we can do, 
#a + 2; a-2; a+=2; a*2; a/2; a**2; a+b 
#Taking sin of all values
print(f"sin of a = {np.sin(a)}") # similar goes for cos


print()
#Linear Algebra
#Multiplying Matrics
print("Multiplying Matrics")
m1 = np.ones((2,3))
print(f"m1 = \n{m1}")
m2 = np.full((3,2), 2)
print(f"m2 = \n{m2}")
print(f"{np.matmul(m1, m2)}")
print()

#Finding Determinant
m3 = np.identity(3)
print(f"determinant of m3 = {np.linalg.det(m3)}")
#can find more stuff just search on google
print()

#Statistics
stats = np.array([[1,2,3], [4,5,6]])
print(f"stats: \n{stats}") 
#finding the min and value of an array
print(f"min value in array stats is: {np.min(stats)}")  #you can also specify axis in this, but idk what that means so search on that. 
print(f"max value in array stats is: {np.max(stats)}") 

#sum all the elements in the matrix
print(f"sum of all elements in stats: {np.sum(stats)}") #axis yaha bhi hota hai ek parameter search on that. 
print()

#Reorganising Arrays; matrixNametobeChanged.reshpe((newDimensions))
print("Reshaping the arrays")
before = np.array([[1,2,3,4], [5,6,7,8]]) #2x4 shape matrix, no of elements = 8
after = before.reshape((4,2)) #matrixNametobeChanged.reshpe((newDimensions)), just keep in mind the dimensions should be such that the number of elements remain the same.
print(f"Before:\n{before}\nAfter:\n{after}")
print()

#Vertically Stacking Arrays; np.vstack([v1,v2,v1,v2])
print("Vertically stacking arrays")
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(f"v1 = {v1}\nv2 = {v2}\nVertically Stacking them:\n{np.vstack([v1,v2,v1,v2])}") #Obviously the number of columns need to be same

#Horizontally Stacking arrays; np.hstack([h1,h2,h1])
print("Hrz stacking arrays")
h1 = np.ones((2,4))
h2 = np.full((2,5), 4)
print(f"h1 = {h1}\nh2 = {h2}\nHorizontally Stacking:\n{np.hstack([h1,h2,h1])}") #number of rows should be same
print()



# Miscle 
#Load from data file, np.genfromtxt('nameofthefile.txt', delimiter = 'symbol that sperates the data')
filedata = np.genfromtxt('data.txt', delimiter=',')
#to change the datatype of the file
filedata = filedata.astype('int32') #.astype Create a copy of the data in the given type, syntax: fileArray.astype('nameoftype')
print(f"array from the text file is:\n{filedata}")
print()

#Boolean Masking and Advance indexing 
print("Printing where the elements of filedata are gretor than 50") #Boolean Masking
print(filedata > 50) #prints where in all elements from the list the number is gretor than 50.
#Now we can index on the basis of boolean masking, by using this list from filedata > 50. 
print()
print("Elements greator than 50 in filedata are: ")
print(filedata[filedata > 50]) #True jaha jaha hoga woh values print ho jaa yegi, in form of a list
#Advance Indexing: we can also index on the basis of a list 
print()
a = np.array([11,22,33,44,55,66])
print("Printing number of arrays using list indexing:") #syntax: arrayName[[arrayof indexs]]
print(a[[0,1,2]])
print()

#Doubt wala
print("Doubt wala")
print(np.any(filedata > 50, axis = 0)) #idk what the axis does
print(np.all(filedata > 50, axis = 0)) #idk what the axis does
print()

#More on Boolena Indexing
print("Number greator than 50 but less than 100")
print((filedata > 50) & (filedata < 100))
print()
print("Number not greator than 50 but less than 100") # here '~' is a not sign
print(~((filedata > 50) & (filedata < 100)))

#Points to remember:
#Improve advance indexing concept, the indexing which involves list, didn't understand that much. 
#link to kaggle notebook of numpy: 
# https://www.kaggle.com/code/orhansertkaya/numpy-tutorial-for-beginners/notebook

# print(f"*"*20"end" )# how to write *****end***** using format string?