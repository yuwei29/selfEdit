from memory import magic
def play(magic):
    print(f'your magic is {magic}')
    magic=int(input('randome number: '))
    if magic==0:
        return
    with open('memory.py','w') as file:
        file.write(f'magic={magic}')
play(magic)