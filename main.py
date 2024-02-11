import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python program.py [arg1] [arg2] ...")
        return

    script_name = sys.argv[0]
    
    arguments = sys.argv[1:]
    
    print("Script Name:", script_name)

    print("Arguments:", arguments)

if __name__ == "__main__":
    main()
