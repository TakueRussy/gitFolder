try:
    file=open('.gitignore','w')
    print('Created')
    file.write('*.pdf')
    file.close()
except:
    print('Error')