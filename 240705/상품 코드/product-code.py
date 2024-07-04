class Good:
    def __init__(self, name = 'codetree', code = '50'):
        self.name = name
        self.code = code

words = input().split()
good1 = Good()
good2 = Good(words[0], words[1])
print(f'product {good1.code} is {good1.name}')
print(f'product {good2.code} is {good2.name}')