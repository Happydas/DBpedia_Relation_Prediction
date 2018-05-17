
import matplotlib.pyplot as plt

X, Y = [], []
for line in open('../Results/Main_Capital_Counter_Average.txt', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

plt.plot(X, Y)
plt.xlabel('Number of Vectors.')
plt.ylabel('Accuracy')
plt.title('Accuracy against testing data set.')
fig1=plt.gcf()
plt.show()
plt.draw()
fig1.savefig('../Results/Capital.png')
