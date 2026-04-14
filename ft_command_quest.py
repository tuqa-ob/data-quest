import sys
print("=== Command Quest ===")
program_name: str = sys.argv[0]
args = sys.argv[1:]
print(f"Program name: {program_name}")
if len(args) == 0:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(args)}")
    for element in range(len(args)):
        print(f"Argument {element + 1}: {args[element]}")
print(f"Total arguments: {len(sys.argv)}")
