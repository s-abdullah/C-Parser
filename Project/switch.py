import interpretter as inter
import ply.yacc as yacc
import ply.lex as lex

# Tokens
reserved = {

    'int': 'INT',
    'char' : 'CHAR',
    'main' : 'MAIN',
    'switch' : 'SWITCH',
    'case' : 'CASE',
    'break' : 'BREAK',
    'default' : 'DEFAULT',
    'cout' : 'COUT',
}


tokens = [
    'STRING',
    'L_CURLY',
    'R_CURLY',
    'L_BRACE',
    'R_BRACE',



    'NUMBER',
    'CHARACTER',

    # 'PL',

    'ASSIGN',
    'COLON',
    'SEMI',
    'NAME',
    'ARITHEMATIC',
    'OP'
    # 'CONST_EXP',

    # 'OPERATOR',
    ] + list(reserved.values());

# t_INT = r'int'
# t_CHAR = r'char'
# t_MAIN = r'main'
# t_STRING = r'\".*\"'

# t_PL = r'\+\+'

t_L_CURLY = r'\{'
t_R_CURLY = r'\}'

t_L_BRACE = r'\('
t_R_BRACE = r'\)'

t_ASSIGN = r'='
# t_NAME = r'[A-Z]+'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9]*'
# t_NAME = r'[^imcscd=()] [a-z | A-Z][a-zA-Z0-9_]*'
# t_NAME = r'^[(?=(int))][a-z]'
t_COLON = r':'
t_SEMI = r';'
#[^(=)][^(char)][^(case)][^(default)[]^(switch)][^(cout)]
# t_TYPE = r'('int' | 'char')'
#
# t_OPERATOR = r'<= | >= | < | > | == | !='
t_ARITHEMATIC = r'\+ | - | \* | \/'
# t_CONST_EXP = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_CHARACTER = r'\'[a-z | A-Z]\''
# t_COUT = r'cout'
t_OP = r'<<'
# t_STRING = r'\"[a-zA-Z0-9]*\"'

# t_SWITCH = r'switch'
# t_CASE = r'case'
# t_BREAK = r'break'
# t_DEFAULT = r'default'


# special cases

def t_STRING(t):
    r'\".*\"'
    t.type = reserved.get(t.value,'STRING');
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME');
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t\v\r"

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0] + "--")
    t.lexer.skip(1)
    print '--------------PROGRAM ENDED----------------'
    exit()




##########     MAIN
def p_program(t):
    '''program : INT MAIN L_BRACE R_BRACE L_CURLY R_CURLY
               | INT MAIN L_BRACE R_BRACE L_CURLY statements R_CURLY'''
    if t[6] == '}':
        t[0] = ['MAIN', 'EMPTY']
    else:
        t[0] = ['MAIN', t[6]]

# def p_statement(t):
#     'statement : INT NAME ASSIGN NUMBER'
#     t[0] = ['DECLARATION', ['TYPE', t[1]],['NAME', t[2]], [ 'NUMBER', t[4]]]



############# STATEMENTS
def p_statements(t):
    '''statements : statement statements'''
    t[0] = [t[1]] + t[2]

def p_statements_empty(t):
    'statements : '
    t[0] = []

def p_statement(t):
    '''statement : expression
                 | function
                 | modifier
                 | case_switch'''
                #  | modifier
    t[0] = t[1]

##### modifier

# def p_modifier(t):
#     '''modifier : NAME ASSIGN NAME ARITHEMATIC NAME
#                 | NAME ASSIGN NAME ARITHEMATIC NAME
#                 | NAME ASSIGN NAME ARITHEMATIC NAME'''
#     t[0]


################# function
def p_function(t):
    'function : COUT more SEMI'
    t[0] = ['COUT'] + t[2]

# def p_more_funct_empty(t):
#     'more : '
#     t[0];
#
def p_more(t):
    '''more : var
            | str'''
    t[0] = t[1]

def p_nomore_func(t):
    'more : '
    t[0]

def p_func_str(t):
    '''str : OP STRING
           | OP STRING OP'''
    t[0] = ['STRING', t[2]]


def p_var(t):
    '''var : OP NAME
           | OP NAME OP '''
    t[0] = ['NAME',t[2]]



################# EXPRESSIONS
def p_expression(t):
    '''expression : INT NAME ASSIGN NUMBER SEMI
                  | CHAR NAME ASSIGN CHARACTER SEMI'''
    t[0] = ['DECLARATION', ['TYPE', t[1]],['NAME', t[2]], [ 'VALUE', t[4]]]


def p_exp_name(t):
    '''expression : INT NAME ASSIGN NAME SEMI
                  | CHAR NAME ASSIGN NAME SEMI'''
    t[0] = ['DECLARATION-N', ['TYPE', t[1]],['NAME', t[2]], [ 'NAME', t[4]]]

def p_expression_m(t):
    '''expression : INT NAME ASSIGN modifier'''
    t[0] = ['DECLARATIONX', ['TYPE', t[1]],['NAME', t[2]], [ 'VALUE', t[4]]]

def p_modifier(t):
    '''modifier : NAME ARITHEMATIC NAME SEMI'''
    t[0] = ['MODIFIER','NAME', t[1],'OPERATOR' , t[2],'NAME', t[3]]

def p_modifier_n(t):
    '''modifier : NAME ARITHEMATIC NUMBER SEMI'''
    t[0] = ['MODIFIER','NAME', t[1],'OPERATOR' , t[2],'NUMBER', t[3]]

# def p_modifier_x(t):
#     '''modifier : NAME SEMI'''
#     t[0] = ['MODIFIER','NAME', t[1]]
####### CASE SWITCH
def p_case_switch(t):
    'case_switch : SWITCH L_BRACE NAME R_BRACE L_CURLY cases R_CURLY'
    t[0] = ['SWITCH', 'NAME', t[3], t[6]]

def p_case_switch_1(t):
    'case_switch : SWITCH L_BRACE CHARACTER R_BRACE L_CURLY cases R_CURLY'
    t[0] = ['SWITCH','CHAR', t[3], t[6]]

def p_case_switch_2(t):
    'case_switch : SWITCH L_BRACE NUMBER R_BRACE L_CURLY cases R_CURLY'
    t[0] = ['SWITCH','INT', t[3], t[6]]


####### cases
def p_cases(t):
    '''cases : case cases'''
    t[0] = [t[1]] + t[2]

def p_cases_empty(t):
    'cases : '
    t[0] = []

###### CASE
def p_case(t):
    '''case : CASE NUMBER COLON statements
            | CASE CHARACTER COLON statements'''
    t[0] = ['CASE', t[2], t[4], 'NO BREAK']

def p_case_break(t):
    '''case : CASE NUMBER COLON statements BREAK SEMI
            | CASE CHARACTER COLON statements BREAK SEMI'''
    t[0] = ['CASE', t[2], t[4], 'BREAK']

# def p_case_empty(t):
#     '''case : CASE NUMBER COLON
#             | CASE CHARACTER COLON'''
#     t[0] = ['CASE', t[2], 'EMPTY', 'NO BREAK']
#
# def p_case_empty_break(t):
#     '''case : CASE NUMBER COLON BREAK SEMI
#             | CASE CHARACTER COLON BREAK SEMI'''
#     t[0] = ['CASE', t[2], 'EMPTY', 'BREAK']


###### DEFAULT CASES
def p_case_default(t):
    '''case : DEFAULT COLON statements'''
    t[0] = ['DEFAULT', t[3], 'NO BREAK']


def p_case_bdefault(t):
    '''case : DEFAULT COLON statements BREAK SEMI'''
    t[0] = ['DEFAULT', t[3], 'BREAK']

# def p_case_default_empty(t):
#     '''case : DEFAULT COLON'''
#     t[0] = ['DEFAULT', 'EMPTY', 'NO BREAK']
#
# def p_case_default_empty_break(t):
#     '''case : DEFAULT COLON BREAK SEMI'''
#     t[0] = ['DEFAULT','EMPTY', 'BREAK']


# def p_default(t):
#     '''default : COLON statement SEMI
#                | COLON'''
#
# def p_expression_identifier(t):
#     'expression : IDENTIFIER'

def p_error(t):
    print ("Code is Incorrect!")
    print t
    print '--------------PROGRAM ENDED----------------'
    exit();
# Build the lexer
def huehue(filename):
    lexer = lex.lex()
    parser = yacc.yacc()

    # s = "{i = 1 \n while i<10 { \n i = i + 1 \n j = j + 1 \n } \n }"
    # print s

    with open (filename, "r") as myfile:
        data=myfile.readlines()

    data = ''.join(data)
    # print data
    # lexer.input(data)
    # while True:
    #         tok = lexer.token()
    #         if not tok: break
    #         print tok
    tree = parser.parse(data, lexer=lexer.input(data))
    # print tree
    print "Code is Correct!"

    # for trees in tree:
    #     print trees
    #     if trees == 'MAIN':
    #         print 'PROGRAM STARTED'


    start = 0

    for x in tree:
        if x == 'MAIN':
            start = 1
            continue;
        if start == 1:

            print '--------------PROGRAM STARTED--------------'
            inter.start_prog(x)
            print '--------------PROGRAM ENDED----------------'
        else:
            print '--------------INVALID PROGRAM--------------'
