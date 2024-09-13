import numpy as np
import matplotlib.pyplot as plt
array = np.arange(1,17).reshape(4,4)
print("Original 2D Array:\n", array)

reshaped_array=array.reshape(2, 8)
print("\nReshaped Array (2*8):\n", reshaped_array)

flattened_array=array.flatten()
print("\nFlattened Array:\n", flattened_array)

sliced_array = array[1:3, 1:3]
print("\nSliced arrya(2*2):\n", sliced_array)


search_result = np.where(array>10)
print("\nIndices of elements greater than 10:\n", search_result)

sorted_array = np.sort(flattened_array)
print("\nSorted Flattened Array:\n", sorted_array)


split_arrays = np.array_split(array,2)
print("\nSplit Arrays")
for i, split_array in enumerate(split_arrays, start=1):
    print("Array {i}:\n{split_array}")
x = np.array([[1],[2],[3]])
y = np.array([10,20,30])


broadcasted_result = x+y
print("\n Broadcasted Result(x+y):\n", broadcasted_result)

t =np.linspace(0, 2*np.pi, 100)
sin_wave = np.sin(t)

plt.plot(t, sin_wave)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
