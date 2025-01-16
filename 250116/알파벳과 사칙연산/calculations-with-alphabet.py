expression = input()
alphabet = []
for i in range(0, len(expression), 2):
    if expression[i] not in alphabet:
        alphabet.append(expression[i])

def calculate(numbers):
    mapping = {alphabet[i]: numbers[i] for i in range(len(numbers))}
    result = mapping.get(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            result += mapping.get(expression[i + 1])
        elif expression[i] == '-':
            result -= mapping.get(expression[i + 1])
        elif expression[i] == '*':
            result *= mapping.get(expression[i + 1])
    return result

max_result = 0
def simulation(numbers):
    global max_result
    if len(numbers) == len(alphabet):
        value = calculate(numbers)
        max_result = max(max_result, value)
        return 
    for i in range(1, 5):
        numbers.append(i)  
        simulation(numbers) 
        numbers.pop()

simulation([])
print(max_result)