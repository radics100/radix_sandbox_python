import platform
def main():
    messege()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    if False:   #this is a comment
        print('line 3')
    else:
        print('not true')
    if __name__ == '__main__': main()
    

