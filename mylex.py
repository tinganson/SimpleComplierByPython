import sys
import ply.lex as lex
reserved = {
   'if' : 'IF',
   'elif' : 'ELIF',
   'else' : 'ELSE',
   'for' : 'FOR',
   'loop' : 'LOOP',

}
tokens=[
        'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS',
        'LPAREN','RPAREN','EXPON','ROOT',
        'EQUAL', 'NOTEQ', 'LARGE', 'SMALL', 'LRGEQ', 'SMLEQ',
        'COLON','SEMICOLON',
]+ list(reserved.values())

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EXPON  = r'\^'
t_ROOT   = r'\*{2}'
t_EQUAL   = r'\=\='
t_NOTEQ   = r'\!\='
t_LARGE   = r'\>'
t_SMALL   = r'\<'
t_LRGEQ   = r'\>\='
t_SMLEQ   = r'\<\='
t_COLON   = r'\:'
t_SEMICOLON   = r'\;'


def t_NAME(t):

    r'[a-zA-Z_][a-zA-Z_0-9]*'

    t.type = reserved.get(t.value,'NAME')    # Check for reserved words

    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore_COMMENT = r'\#.*'
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Give the lexer some input
'''
lexer.input("if (num==3): ck=2;elif ")


# Tokenize

while True:

    tok = lexer.token()

    if not tok: break      # No more input

    print(tok)
'''
