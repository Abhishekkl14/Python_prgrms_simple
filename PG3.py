marks = [100, 30, 100]
sum = sum(marks)
print(sum)
average = sum/len(marks)
print(average)
if average>90:
    print("A")
elif average>60:
    print("B")
else:
    print("C")
