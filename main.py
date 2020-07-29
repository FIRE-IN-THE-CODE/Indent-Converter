import getopt
import sys
import random


def usage():
    print("Tab Converter: a small script used to reformat other python scripts"
          + " converting tabs into 4 spaces or vice versa.")
    print("\n")
    print("Note: it is recommended to backup any important scripts before "
          + " using this program in case anything unexpected happens.")
    print("Options: ")
    print('Syntax: [-f (name of the file)] [-m or -r] [-o if desired]')
    print("-f	--file		select the script to convert")
    print("-h	--help		prints usage information")
    print('-m   --mix       mixes the indents into tabs and spaces')
    print("-o	--output	gives the name to the new converted file")
    print('-r   --repair    fixes the script to make all indents into 4 spaces.')


'''
def main():
    opts, args = getopt.getopt(sys.argv[1:], 'f:ho:', ['file=', 'help', 'output='])

    for o, a in opts:
        if o in ('-f', '--file'):
            target_script = a
        elif o in ('-h', '--help'):
            usage()
        elif o in ('-o', '--output'):
            result_file = a
'''


def mixer():
    code_lines = []
    new_code = []

    file_target = open('test.py', 'r')     # Temporarily has the value 'test1.py' for debugging
    for line in file_target.readlines():
        code_lines.append(line)
    file_target.close()

    for item in code_lines:
        original_code_line = []
        new_code_line = ''
        for letter in item:
            original_code_line.append(letter)
        print('Value of tmp_list: ', original_code_line)  # Debugging only
        try:
            chance = random.randrange(1, 101)
            if original_code_line[0] == ' ' and original_code_line[1] == ' ' \
                    and original_code_line[2] == ' ' and original_code_line[3] == ' ':
                if 0 < chance < 50:
                    original_code_line[0] = ' '
                elif 50 < chance < 101:
                    original_code_line[0] = '\t'
                print('The value of tmp_list 1: ', original_code_line)      # Debugging
                for i in original_code_line: new_code_line = new_code_line + i
                new_code.append(new_code_line)
                del original_code_line, new_code_line
            elif original_code_line[0] == '\t':
                if 0 < chance < 50:
                    original_code_line[0] = '    '
                elif 50 < chance < 101:
                    original_code_line[0] = '\t'
                print('The value of tmp_list 2: ', original_code_line)        # Debugging
                for i in original_code_line: new_code_line += i
                new_code.append(new_code_line)
                del original_code_line, new_code_line
            else:
                new_code.append(item)
        except IndexError:
            pass

        print('Value of the new_code list: ', new_code)         # Debugging

    result_file = open('test.py', 'w')   # Should be file name
    for line in new_code:
        result_file.write(line)
    result_file.close()


def fixer():
    original_code_lines = []
    new_code_lines = []

    file = open('test.py')      # Debugging
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


if __name__ == '__main__':
    mixer()
