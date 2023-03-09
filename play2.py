def play():
  from memory import magic
  while 1:
    print(f'your magic is {magic}')
    magic=int(input('randome number: '))
    if magic==0:
        return
    with open('memory.py','w') as file:
        file.write(f'magic={magic}')
if __name__=='__main__':
    play()