#Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames
#it should read the first file and write the contents into the second file (creating it if necessary).
#If the pattern string appears anywhere in the file, it should be replaced with the replacement string.

from __future__ import print_function, division
import os
import re

def sed(pattern, replacement, fin, fout):
    # Open File One
    finMem = open(fin)

    # Write Contents to File Two
    foutMem = open(fout, 'w+')

    # Search and replace string
    for line in finMem:
        if pattern in line:
            print ('pattern found')
            # Don't think it's possible to use list = list.replace()
            # TODO Investigate further
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)

if __name__ == '__main__':
    print (os.getcwd())
    pattern = 'oy'
    replacement = 'it'
    fin = open('/home/ohhlucy/projects/Think-Python-Exercise-14.1/Hello.txt')
    fout = open('/home/ohhlucy/projects/Think-Python-Exercise-14.1/Hello.txt')
    sed(pattern, replacement, fin, fout)


def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()