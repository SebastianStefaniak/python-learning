import numpy as np
scores=np.array([10,12,55,61,91])
#print(scores)
print(type(scores))
scores += 10
#print(scores > 65)

mean=np.mean(scores)
std=np.std(scores)
print(mean)
print(std)
print(scores[:3])
print(scores[scores>75])

data=np.array([
    [10,20,30],
    [30,40,50],
    [70,80,90]
])

#print(data.shape)
print(data[0][2])



temperature=np.array([10,20,30,40,35,21])
print(np.mean(temperature))
print(np.max(temperature))
print(np.min(temperature))
temperature +=2
print(temperature)
print(temperature[temperature>20])
