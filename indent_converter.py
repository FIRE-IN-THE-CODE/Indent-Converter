import getopt
import sys
import random


def usage():
    print("Indent Converter: a small script used to reformat other python scripts"
          + " converting tabs into 4 spaces or vice versa.")
    print("\n")
    print("Syntax format: ")
    print('<command> [file name] [options]')
    print('\n')
    print('Commands:')
    print("-h	--help		prints usage information")
    print('-m   --mix       mixes the indents into tabs and spaces')
    print('-r   --repair    fixes the script to make all indents into 4 spaces.')
    print('Options:')
    print('-o	--output	gives a new name to the new converted file')
    print('\n')
    print('Author: www.github.com/FIRE-IN-THE-CODE')


def mixer(file_target, new_file_name):
    original_code = []
    new_code = []

    open_target_file = open(file_target, 'r')
    for code_line in open_target_file.readlines():
        original_code.append(code_line)
    open_target_file.close()

    for line in original_code:
        processing_code = ''
        indent = ''
        code_to_add = indent + processing_code
        tab_count = 0
        space_count = 0
        space_counter = 0

        # Remove spaces and tabs and count the number of indents
        for byte in line:
            if byte == ' ':
                space_counter += 1
                del byte
            elif byte == '\t':
                tab_count += 1
                del byte[0]
            else:
                pass
            try:
                processing_code += byte
            except NameError:                           # May be NameError or localVariable referenced something
                pass
        space_count += space_counter/4

        # Modify the indents and add the new code line
        while space_count != 0:
            chance = random.randrange(1, 101)
            if 0 < chance < 50:
                indent += ' '
            elif 50 < chance < 102:
                indent += '\t'
            space_count -= 1
        new_code.append(code_to_add)

    # Create the file and add the code
    print('Value of the new_code list: ', new_code)         # Debugging
    if new_file_name == '':
        result_file = open(file_target + '_new.py', 'w')
        for line in new_code:
            result_file.write(line)
        result_file.close()
    else:
        result_file = open(new_file_name, 'w')
        for line in new_code:
            result_file.write(line)
        result_file.close()


def fixer(file_name, new_file_name):
    original_code_lines = []
    new_code_lines = []

    file = open('test.py')                                          # Debugging
    for line in file.readlines():
        original_code_lines.append(line)
    file.close()

    for line in original_code_lines:
        code_line = ''
        for character in line:
            if character == '\t':
                code_line = '    '
            else:
                new_code_lines += line


def main():
    target_file = 'test.py'         # Debugging
    result_file = ''
    opts, args = getopt.getopt(sys.argv[1:], 'hmo:', ['help', 'mix', 'repair=', 'output='])  # Took out output settings

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-o', '--output'):
            result_file = a
        elif o in ('-m', '--mix'):
            print('Result_file value: ', result_file)       # Debugging
            mixer(target_file, result_file)
        elif o in ('-r', '--repair'):
            target_file = a
            fixer(target_file, result_file)


if __name__ == '__main__':
    main()
