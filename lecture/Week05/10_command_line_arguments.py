import sys

number_of_arguments = len(sys.argv)
print(f"Total arguments passed: {number_of_arguments}")

print(f"Type of sys.argv: {type(sys.argv)}")
print(f"First argument of sys.argv is {sys.argv[0]}")
print(f"Last argument of sys.argv is {sys.argv[-1]}")