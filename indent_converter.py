import getopt
import sys
import random


def usage():
    print("Indent Converter: a small script used to reformat other python scripts"
          + " converting tabs into four spaces or mix four spaces and tab indentation.")
    print("\n")
    print("Syntax format: ")
    print('<command> [file name] <options>')
    print('\n')
    print('Commands:')
    print("-h       --help		prints usage information")
    print('-m       --mix       mixes tab and four spaces indentation')
    print('-r       --repair    reformat the script converting tabs into four spaces.')
    print('Options:')
    print('-o       --output	sets the argument as the new name for the reformatted file')
    print('\n')
    print('Author: https://www.github.com/FIRE-IN-THE-CODE')


def mixer(file_target, new_file_name):
    original_code = []
    new_code = []

    open_target_file = open(file_target, 'r')
    for code_line in open_target_file.readlines():
        original_code.append(code_line)
    open_target_file.close()

    # Count indents, remove them, and modify each code line
    for line in original_code:
        processing_code = ''
        indent = ''
        tab_count = 0
        space_count = 0
        space_counter = 0
        indent_condition = False

        for char in line:
            if indent_condition:
                processing_code += char
                continue
            elif char == ' ':
                space_counter += 1
            elif char == '\t':
                tab_count += 1
            else:
                processing_code += char
                indent_condition = True
        space_count += int(space_counter / 4)

        while space_count != 0 or tab_count != 0:
            chance = random.randrange(1, 101)
            if 0 < chance < 50:
                indent += '    '
            elif 50 < chance < 102:
                indent += '\t'
            if space_count != 0:
                space_count -= 1
            elif tab_count != 0:
                tab_count -= 1
        code_to_add = indent + processing_code
        new_code.append(code_to_add)

    if new_file_name == '':
        result_file_name = new_file_name + '_new.py'
        result_file = open(result_file_name, 'w')
        for line in new_code:
            result_file.write(line)
        result_file.close()
    else:
        result_file_name = new_file_name
        result_file = open(result_file_name, 'w')
        for line in new_code:
            result_file.write(line)
        result_file.close()
    print('Indents of the file "%s" has been mixed to the file "%s".' % (file_target, result_file_name))


def fixer(file_target, new_file_name):
    original_code_lines = []
    new_code_lines = []

    file = open(file_target)
    for line in file.readlines():
        original_code_lines.append(line)
    file.close()

    # Count indents, remove them, and modify each code line
    for line in original_code_lines:
        processing_code = ''
        indent = ''
        tab_count = 0
        space_count = 0
        space_counter = 0
        indent_condition = False

        for char in line:
            if indent_condition:
                processing_code += char
                continue
            elif char == '\t':
                tab_count += 1
            elif char == ' ':
                space_counter += 1
            else:
                processing_code += char
                indent_condition = True
        space_count += int(space_counter/4)

        while tab_count != 0 or space_count != 0:
            if tab_count != 0:
                indent += '    '
                tab_count -= 1
            elif space_count != 0:
                indent += '    '
                space_count -= 1
        code_to_add = indent + processing_code
        new_code_lines.append(code_to_add)

    if new_file_name == '':
        result_file_name = file_target + '_new.py'
        result_file = open(result_file_name, 'w')
        for line in new_code_lines:
            result_file.write(line)
        result_file.close()
    else:
        result_file_name = new_file_name
        result_file = open(result_file_name, 'w')
        for line in new_code_lines:
            result_file.write(line)
        result_file.close()
    print('Indents of the file "%s" has been fixed to a file called "%s".' % (file_target, result_file_name))


def main():
    targeted_file = ''
    result_file = ''
    mixer_state = False
    fixer_state = False

    opts, args = getopt.getopt(sys.argv[1:], 'ho:m:r:', ['help', 'output=', 'mix=', 'repair='])

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-o', '--output'):
            result_file = a
        elif o in ('-m', '--mix'):
            targeted_file = a
            mixer_state = True
        elif o in ('-r', '--repair'):
            targeted_file = a
            fixer_state = True

    if fixer_state:
        fixer(targeted_file, result_file)
    elif mixer_state:
        mixer(targeted_file, result_file)


if __name__ == '__main__':
    main()
