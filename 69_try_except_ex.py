def count_words(file_name):
    """Counts the number of words in a given file."""
    try:
        with open(file_name) as file:
            file = file.read()
    except FileNotFoundError:
        print('File does not exists.')
    else:
        print(f"There are {len(file.split())} words in {file_name}")


file_names = (input('Enter file name/s : '))
file_names = file_names.split()
for filename in file_names:
    print(f'Given file is {filename}')
    count_words(filename)
