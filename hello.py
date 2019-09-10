import sys

def main():
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'Mundo'
    print('Hola', name)

if __name__ == '__main__':
    main()