#!/usr/bin/python
import re
import string
import scanner
import symbolTable
import sys
import shlex
import Token

symbol_table = []
comments = []
not_tokens = []

def parseFile(fileName):
    with open(fileName, 'r') as source_file:
        line_number = 1
        for line in source_file:
            lexeme_number = 1
            if scanner.isComment(line):
                comments.append(line)
                continue
            words = parseWords(line)
            for word in words:
                t = (scanner.getToken(word))
                if t is not None:
                    symbol_table.append(t)
                    lexeme_number += 1
                else:
                    not_tokens.append(word)
            line_number += 1

def printTokens():
    print "Tokens: < Type, Lexeme >"
    for entry in symbol_table:
        print(entry)

def printComments():
    print "Comments, denoted by a line starting with '//'"
    for entry in comments:
        print(entry)

def printNotTokens():
    print "Invalid input:"
    for entry in not_tokens:
        print(entry)

def parseWords(line):
    line = line.replace("\n", "")
    line = line.replace("\t", " ")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    words = shlex.shlex(line)
    words.wordchars += '.'
    words.wordchars += '-'
    return words

if __name__ == "__main__":
    parseFile(sys.argv[1])
    printTokens()
    printComments()
    printNotTokens()
