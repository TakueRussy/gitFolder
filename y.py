try:
    file=open('.gitignore','w')
    print('Created')
    file.write('*.txt')
    file.close()
except:
    print('Error')
