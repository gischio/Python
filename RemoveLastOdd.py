# Iterating over lists
  
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in range(len(numbers)):
        if numbers[num] % 2 == 1:
            has_odd = True
            last_odd = num
     
    if has_odd:
        numbers.pop(last_odd)
        

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()