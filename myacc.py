import ply.yacc as yacc
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import math
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


b = nx.DiGraph()
b.clear()

# Get the token map from the lexer. This is required.


precedence = (
    ('nonassoc','EQUALS'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','EXPON','ROOT'),
    ('if', 'IF'), ('left', 'ELSE') ,
    )

names = {}

def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]
    plt.clf()
    plt.cla()
    b.clear()
    b.add_node('assign')
    b.add_nodes_from(['name','=','exp'])
    b.add_edges_from([('assign','name'),('assign','='),('assign','exp')])
    b.add_node(p[1])
    b.add_node(p[3])
    b.add_edge('name',p[1])
    b.add_edge('exp',p[3])
    plt.title('assign')
    pos = graphviz_layout(b, prog='dot')
    nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
    plt.show()
    plt.close() # 关闭图 0
def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_statement_if(p):
    '''statement : IF LPAREN comparison RPAREN COLON NAME EQUALS expression SEMICOLON
                 | IF LPAREN comparison RPAREN COLON NAME EQUALS expression SEMICOLON ELSE COLON NAME EQUALS expression SEMICOLON'''
    if p[3]:
        names[p[6]] = p[8]
        if p[12] is not None:
            plt.clf()
            plt.cla()
            b.clear()
            b.add_node('stmt')
            b.add_nodes_from(['if','comp','stmt1','else','stmt2'])
            b.add_edges_from([('stmt','if'),('stmt','comp'),('stmt','stmt1'),('stmt','else'),('stmt','stmt2')])
            b.add_node(p[3])
            b.add_edge('comp',p[3])
            b.add_nodes_from(['name1','equel1','exp1'])
            b.add_edges_from([('stmt1','name1'),('stmt1','equel1'),('stmt1','exp1')])
            b.add_nodes_from(['name2','equel2','exp2'])
            b.add_edges_from([('stmt2','name2'),('stmt2','equel2'),('stmt2','exp2')])
            b.add_node(p[6])
            b.add_node(p[8])
            b.add_edge('name1',p[6])
            b.add_edge('exp1',p[8])
            b.add_node(p[12])
            b.add_node(p[14])
            b.add_edge('name2',p[12])
            b.add_edge('exp2',p[14])
            plt.title("if-else-statement")
            pos = graphviz_layout(b, prog='dot')
            nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
            plt.show()
            plt.clf()
            plt.cla()
        else:
            plt.clf()
            plt.cla()
            b.clear()
            b.add_node('stmt')
            b.add_nodes_from(['if','comp','stmt1'])
            b.add_edges_from([('stmt','if'),('stmt','comp'),('stmt','stmt1')])
            b.add_node(p[3])
            b.add_edge('comp',p[3])
            b.add_nodes_from(['name1','equel1','exp1'])
            b.add_edges_from([('stmt1','name1'),('stmt1','equel1'),('stmt1','exp1')])
            b.add_node(p[6])
            b.add_node(p[8])
            b.add_edge('name1',p[6])
            b.add_edge('exp1',p[8])
            plt.title("ifstatement")
            pos = graphviz_layout(b, prog='dot')
            nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
            plt.show()
            plt.clf()
            plt.cla()
    else:
        try:
            if p[12] is not None:
                names[p[12]] = p[14]
                plt.clf()
                plt.cla()
                b.clear()
                b.add_node('stmt')
                b.add_nodes_from(['if','comp','stmt1','else','stmt2'])
                b.add_edges_from([('stmt','if'),('stmt','comp'),('stmt','stmt1'),('stmt','else'),('stmt','stmt2')])
                b.add_node(p[3])
                b.add_edge('comp',p[3])
                b.add_nodes_from(['name1','equel1','exp1'])
                b.add_edges_from([('stmt1','name1'),('stmt1','equel1'),('stmt1','exp1')])
                b.add_nodes_from(['name2','equel2','exp2'])
                b.add_edges_from([('stmt2','name2'),('stmt2','equel2'),('stmt2','exp2')])
                b.add_node(p[6])
                b.add_node(p[8])
                b.add_edge('name1',p[6])
                b.add_edge('exp1',p[8])
                b.add_node(p[12])
                b.add_node(p[14])
                b.add_edge('name2',p[12])
                b.add_edge('exp2',p[14])
                plt.title("if-else-statement")
                nx.nx_agraph.write_dot(b,'test.dot')
                pos = graphviz_layout(b, prog='dot')
                nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
                plt.show()
                plt.clf()
                plt.cla()
        except:
            pass


def p_statement_for(p):
    '''statement : FOR statement LOOP NUMBER COLON NAME EQUALS expression PLUS expression SEMICOLON
                 | FOR statement LOOP NUMBER COLON NAME EQUALS expression MINUS expression SEMICOLON
                 | FOR statement LOOP NUMBER COLON NAME EQUALS expression TIMES expression SEMICOLON
                 | FOR statement LOOP NUMBER COLON NAME EQUALS expression DIVIDE expression SEMICOLON
                 | FOR statement LOOP NUMBER COLON NAME EQUALS expression EXPON expression SEMICOLON
                 | FOR statement LOOP NUMBER COLON NAME EQUALS expression ROOT expression SEMICOLON '''
    plt.clf()
    plt.cla()
    b.clear()
    b.add_node('stmt')
    b.add_nodes_from(['for','stmt1','loop','time','stmt2'])
    b.add_edges_from([('stmt','for'),('stmt','stmt1'),('stmt','loop'),('stmt','time'),('stmt','stmt2')])
    b.add_node(p[6])
    b.add_node(p[4])
    b.add_edge('stmt1',p[6])
    b.add_edge('time',p[4])
    b.add_node('=')
    b.add_edge('stmt2',p[6])
    b.add_edge('stmt2','=')
    if p[9]=='+':
        b.add_node('+stmt')
        b.add_edge('stmt2','+stmt')
        b.add_node('t1')
        b.add_edge('+stmt','t1')
    elif p[9]=='-':
        b.add_node('-stmt')
        b.add_edge('stmt2','-stmt')
        b.add_node('t1')
        b.add_edge('-stmt','t1')
    elif p[9]=='*':
        b.add_node('*stmt')
        b.add_edge('stmt2','*stmt')
        b.add_node('t1')
        b.add_edge('*stmt','t1')
    elif p[9]=='/':
        b.add_node('/stmt')
        b.add_edge('stmt2','/stmt')
        b.add_node('t1')
        b.add_edge('/stmt','t1')
    elif p[9]=='^':
        b.add_node('^stmt')
        b.add_edge('stmt2','^stmt')
        b.add_node('t1')
        b.add_edge('^stmt','t1')
    elif p[9]=='**':
        b.add_node('**stmt')
        b.add_edge('stmt2','**stmt')
        b.add_node('t1')
        b.add_edge('**stmt','t1')
    plt.title("forstatement")
    pos = graphviz_layout(b, prog='dot')
    nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
    plt.show()
    plt.clf()
    plt.cla()
    if p[4]>0:

        for names[p[2]] in range(1,p[4]+1):
            names[p[2]]=names[p[2]]+1
            p[8]=int(names[p[2]])
            if p[9]=='+':
                if(names[p[2]]<=1):
                    p[0]=p[8]+p[10]
                else:
                    p[0]=names[p[6]]+p[10]
                    names[p[6]]=p[0]
            elif p[9]=='-':
                if(names[p[2]]<=1):
                    p[0]=p[8]-p[10]
                else:
                    p[0]=names[p[6]]-p[10]
                    names[p[6]]=p[0]
            elif p[9]=='*':
                if(names[p[2]]<=1):
                    p[0]=p[8]*p[10]
                else:
                    p[0]=names[p[6]]*p[10]
                    names[p[6]]=p[0]
            elif p[9]=='/':
                if(names[p[2]]<=1):
                    p[0]=p[8]/p[10]
                else:
                    p[0]=names[p[6]]/p[10]
                    names[p[6]]=p[0]
            elif p[9]=='^':
                if(names[p[2]]<=1):
                    p[0]=math.pow(p[8] , p[10])
                else:
                    p[0]=math.pow(names[p[6]],p[10])
                    names[p[6]]=p[0]
            elif p[9]=='**':
                if(names[p[2]]<=1):
                    p[0]=math.pow(p[8] , 1/p[10])
                else:
                    p[0]=math.pow(names[p[6]],1/p[10])
                    names[p[6]]=p[0]

def p_comparison_binop(p):
    '''comparison : expression EQUAL expression
                  | expression NOTEQ expression
                  | expression LARGE expression
                  | expression SMALL expression
                  | expression LRGEQ expression
                  | expression SMLEQ expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPON expression
                  | expression ROOT expression '''
    if p[2] == '+'  :
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = math.pow(p[1] , p[3])
    elif p[2] == '**':
        p[0] = math.pow(p[1] , 1 / p[3])


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()
lexer = lex.lex()

while True:
    try:
        s = input('calc > ')

        lexer.input(s)
        while True:
           tok = lexer.token()
           if not tok:
              break
           print(tok)

    except EOFError:
        break
    if not s:
        continue
    def find_top_prio(lst):
        top_prio = 1
        count_ops = 0
        for i in range(len(lst)-1):
            if lst[i]=='*'and lst[i+1]=='*':
                lst[i]='**'
                lst.pop(i+1)
        for ops in lst:
            if ops in prio_dict:
                    count_ops += 1
                    if prio_dict[ops] > 1:
                        top_prio = prio_dict[ops]
        return top_prio, count_ops
    ip_str = s
    ip_lst = list(map(str, ip_str))
    prio_dict = {'-': 1, '+': 2, '*': 3, '/': 4, '^': 5,'**': 6,}
    op_lst = []
    op_lst.append(['op', 'arg1', 'arg2', 'result'])
    top_prio, count_ops = find_top_prio(ip_lst)
    ip = ip_lst
    i, res = 0, 0
    while i in range(len(ip)):
        if ip[i] in prio_dict:
            op = ip[i]
            if (prio_dict[op] >= top_prio) and (ip[i+1] =='*'):
                res += 1
                op_lst.append(['**', ip[i-1],ip[i+2] , 't'+str(res)])
                ip[i] = 't'+str(res)
                ip.pop(i-1)
                ip.pop(i)
                ip.pop(i)
                i = 0
                top_prio, count_ops = find_top_prio(ip)
            elif (prio_dict[op] >= top_prio):
                res += 1
                op_lst.append([op, ip[i-1], ip[i+1], 't'+str(res)])
                ip[i] = 't'+str(res)
                ip.pop(i-1)
                ip.pop(i)
                i = 0
                top_prio, count_ops = find_top_prio(ip)
            if len(ip) == 1:
                op_lst.append(['=', ip[i], ' ', 'a'])

        i += 1
    i = 1
    while i in range(1,len(op_lst)):
        print(op_lst[i])
        i+=1
    b.clear()

    for i in range(1,len(op_lst)):
        if op_lst[i][2]==' ':
            break
        else:
            b.add_node(op_lst[i][1])
            b.add_node(op_lst[i][2])
            b.add_node(op_lst[i][3])
            b.add_edges_from([(op_lst[i][3],op_lst[i][1]),(op_lst[i][3],op_lst[i][2])])
    if len(op_lst)>1:
        plt.title("calcustatement")
        pos = graphviz_layout(b, prog='dot')
        nx.draw(b,pos, with_labels=True, arrows=True, node_size=600)
        plt.show()
        plt.clf()
        plt.cla()
    parser.parse(s)
