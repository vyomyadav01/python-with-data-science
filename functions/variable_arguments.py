#flexible parameter in a function
# *args **kwargs
def mean(*numbers):
    total = 0
    for item in numbers:
        if isinstance(item, (int,float)):
            total += item
    return sum(numbers) / len(numbers)
def report(**marks):
    total_marks = 0
    for k,v in marks.items():
        print(f'{k} got {v} marks')
        total_marks += v
        return total_marks
            
print(report(ram = 90, shyam = 80, hari = 70))
print(mean(1,2,3,4,5,6,7,8,9))
print(12,'a',123,'124',123,12)