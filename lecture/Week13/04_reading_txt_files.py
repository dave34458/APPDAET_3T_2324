from pathlib import Path

my_text_file = open(f"{Path.cwd()}/hello.txt")
my_text_file_contents = my_text_file.read()

print(my_text_file_contents)