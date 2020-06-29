from parser import *

def main():
    f = open(sys.argv[1], "r")
    file = f.read()
    if sys.argv[1].endswith(".php"):
        Parser.runCode(file)
    else:
        raise Exception("Voce deveria tentar colocar arquivos do tipo .php!")

if __name__ == "__main__":
    main()