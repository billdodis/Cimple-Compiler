# Tilemachos Markos Bazakas 3281 cse63281
# Vasileios Ntontis 3300 cse63300
import sys

wordid = 0
programid = 1
ifid = 2
switchcaseid = 3
notid = 4
functionid = 5
inputid = 6
declareid = 7
elseid = 8
forcaseid = 9
andid = 10
procedureid = 11
printid = 12
whileid = 13
incaseid = 14
orid = 15
callid = 16
caseid = 17
returnid = 18
defaultid = 19
inid = 20
inoutid = 21
finalNumbid = 22
plusid = 23
minusid = 24
multiid = 25
divideid = 26
equalsid = 27
lessOrEqualid = 28
notEqualid = 29
lessThanid = 30
moreOrEqualid = 31
moreThanid = 32
assignid = 33
commaid = 34
questionamarkid = 35
rightParenthesisid = 36
leftParenthesisid = 37
Doubleapostrofid = 38
# rightDoubleapostrofid = 39
leftSquareParenthesisid = 40
rightSquareParenthesisid = 41
leftWaveParenthesisid = 42
rightWaveParenthesisid = 43
eofid = 44
beginid = 45
endid = 46

# Scope
class Scope:
    def __init__(self, entitylist, nestingLevel, framelength):
        self.entitylist = entitylist
        self.nestingLevel = nestingLevel
        self.framelength = framelength

    def addentity(self, entity):
	counter = 0
        if entity.gettype() != functionid or entity.gettype() != procedureid:
            for i in range(len(self.entitylist)):
                if self.entitylist[i].type==functionid or self.entitylist[i].type== procedureid:
                    counter = counter +1
            entity.addoffset(len(self.entitylist)*4)
            entity.addoffset(-(counter*4))
            self.framelength = self.framelength + 4
        for i in range(len(self.entitylist)):
            if self.entitylist[i].name == entity.name and self.entitylist[i].type != entity.type:
                print("Error: Two or more entities have the same name but they are of different types.")
                sys.exit()
            if (self.entitylist[i].name == entity.name and self.entitylist[i].type == entity.type) and (self.entitylist[i].type == procedureid or self.entitylist[i].type == functionid):
                print("Error: Two or more entities have the same name and they are both function/procedure.")
                sys.exit()
	self.entitylist.append(entity)

    def getentities(self):
        return self.entitylist

    def changeentityframelength(self, number):
        self.entitylist[-1].framelength = number

    def raisenestinglevel(self):
        self.nestingLevel = self.nestingLevel + 1

    def raiseframelength(self):
        self.framelength = self.framelength + 4

    def getframelength(self):
        return self.framelength    #mporei na thelei +4

# Entity
class Entity:
    #######################################################################
    parmode =''
    framelength = 0
    startquad = -1
    arglist = []
    def __init__(self, type, name, offset):
        self.type = type
        self.name = name
        self.offset = offset
        self.parmode = ''
        self.framelength = 0
        self.arglist = []
	self.startquad = -1

    def gettype(self):
        return self.type

    def getoffset(self):
        return self.offset

    def getparmode(self):
        return self.parmode

    def addoffset(self, numb):
        self.offset = self.offset + numb

# Argument
#class Argument:
#    def __init__(self, parmode, type):
#        self.parmode = parmode
#        self.type = type
#
#    def getparmode(self):
#        return self.parmode
#
#    def gettype(self):
#        return self.type

# lektikos analuths
def lex():
    global lineCounter
    listapo=[] #PROSOXH PAIZEI NA EINIA PROVLHMA STON LEX.
    w = file.read(1)
    while (w == ' ' or w == '\t' or w == '\r'):
        w = file.read(1)
    if w == '\n':
        lineCounter = lineCounter + 1
        return lex()
    elif w.isalpha():
        wordCounter = 1
        word = list(w)
        w = file.read(1)
        while w.isalpha() or w.isdigit():
            wordCounter = wordCounter + 1
            if (wordCounter > 30):
                print("Error: word length surpassed limit of 30, in line:", lineCounter)
                sys.exit()
            word.append(w)
            # print(word)
            w = file.read(1)
        file.seek(file.tell() - 1)
        word = ''.join(word)
        # if len(word)>30:
        # print("Error: max length of word(30) surpassed in line:", lineCounter)
        # sys.exit()
        if (word == 'program'):
            return (programid, word)
        elif (word == 'if'):
            return (ifid, word)
        elif (word == 'switchcase'):
            return (switchcaseid, word)
        elif (word == 'not'):
            return (notid, word)
        elif (word == 'function'):
            return (functionid, word)
        elif (word == 'input'):
            return (inputid, word)
        elif (word == 'declare'):
            return (declareid, word)
        elif (word == 'else'):
            return (elseid, word)
        elif (word == 'forcase'):
            return (forcaseid, word)
        elif (word == 'and'):
            return (andid, word)
        elif (word == 'procedure'):
            return (procedureid, word)
        elif (word == 'print'):
            return (printid, word)
        elif (word == 'while'):
            return (whileid, word)
        elif (word == 'incase'):
            return (incaseid, word)
        elif (word == 'or'):
            return (orid, word)
        elif (word == 'call'):
            return (callid, word)
        elif (word == 'case'):
            return (caseid, word)
        elif (word == 'return'):
            return (returnid, word)
        elif (word == 'default'):
            return (defaultid, word)
        elif (word == 'in'):
            return (inid, word)
        elif (word == 'inout'):
            return (inoutid, word)
        elif (word == 'begin'):
            return (beginid, word)
        elif (word == 'end'):
            return (endid, word)
        else:
            # print(word)
            return (wordid, word)

    elif w.isdigit():
        numb = list(w)
        w = file.read(1)
        while w.isdigit():
            numb.append(w)
            w = file.read(1)
        file.seek(file.tell() - 1)
        numb = ''.join(numb)
        numb = int(numb)
        # print(numb)
        if (numb < -429493345 or numb > 429493345):
            print("Error: invalid range of number, has to be between: -2^32+1 to 2^32-1 in line:", lineCounter)
            sys.exit()
        return (finalNumbid, numb)

    elif (w == '+'):
        return (plusid, w)
    elif (w == '-'):
        return (minusid, w)
    elif (w == '*'):
        return (multiid, w)
    elif (w == '/'):
        s = file.read(1)
        if (s == 'n'):
            lineCounter = lineCounter + 1
            return lex()
        else:
            file.seek(file.tell() - 1)
            return (divideid, w)
    elif (w == '='):
        return (equalsid, w)
    elif (w == '<'):
        doubleEmblemIso = list(w)
        doubleEmblemDiaf = list(w)
        meta = w
        w = file.read(1)
        if (w == '='):
            doubleEmblemIso.append(w)
            doubleEmblemIso = ''.join(doubleEmblemIso)
            return (lessOrEqualid, doubleEmblemIso)
        elif (w == '>'):
            doubleEmblemDiaf.append(w)
            doubleEmblemDiaf = ''.join(doubleEmblemDiaf)
            return (notEqualid, doubleEmblemDiaf)
        else:
            file.seek(file.tell() - 1)
            return (lessThanid, meta)
    elif (w == '>'):
        doubleEmblem = list(w)
        tema = w
        w = file.read(1)
        if (w == '='):
            doubleEmblem.append(w)
            doubleEmblem = ''.join(doubleEmblem)
            return (moreOrEqualid, doubleEmblem)
        else:
            file.seek(file.tell() - 1)
            return (moreThanid, tema)

    elif (w == ':'):  # (DE THEWREITAI LEKTIKH MONADA OPWS < > DEN EINAI SUMBOL THS GLWSSAS)
        listw = list(w)
        w = file.read(1)
        if (w == '='):
            listw.append(w)
            listw = ''.join(listw)
            return (assignid, listw)
        else:
            print("Error: expected '=' after ':' in line:", lineCounter)
            sys.exit()
    elif (w == '#'):
        w = file.read(1)
        while (w != '#'):
            if (not w):
                print("Error, expected '#' to close the comments but found EOF, in line:", lineCounter)
                sys.exit()
            w = file.read(1)
        return lex()

    elif (w == ','):
        return (commaid, w)
    elif (w == ';'):
        return (questionamarkid, w)
    elif (w == ')'):
        return (rightParenthesisid, w)
    elif (w == '('):
        return (leftParenthesisid, w)
    elif (w == '"'):
        w = file.read(1)
        while (w != '"'):
            listapo.append(w)
            w = file.read(1)
        return (Doubleapostrofid, listapo)
    elif (w == '['):
        return (leftSquareParenthesisid, w)
    elif (w == ']'):
        return (rightSquareParenthesisid, w)
    elif (w == '{'):
        return (leftWaveParenthesisid, w)
    elif (w == '}'):
        return (rightWaveParenthesisid, w)
    elif (w == '.'):
        # print(lineCounter)
        return (eofid,"END OF FILE found")
    else:
        print("Error: invalid character:", w, "in line:", lineCounter)
        sys.exit()


def yacc():
    global quadNumb
    global variables
    variables=[]
    quadNumb = 0
    global temp
    temp=-1
    global token0
    global token1
    global lineCounter
    global ccounter
    global quadList
    quadList = []
    global scopeList
    scopeList = []
    global nestingLevel
    nestingLevel = 0
    global listofallscopes
    listofallscopes = []

    # " program " is the starting symbol
    def program():
        global token0
        global token1
        global scopeList
        global nestingLevel
        global listofallscopes
        if (token0 == programid):
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                token0, token1 = lex()
                scope1 = Scope([], 0, 12)
                scopeList.append(scope1)
		listofallscopes.insert(0, scopeList[0])
                block(name)
                genquad('halt', '_', '_', '_')
                genquad('end_block', name, '_', '_')
                return
            else:
                print("Error: program name expected,in line:", lineCounter)
                sys.exit()
        else:
            print("Error: the keyword 'program' was expected,in line:", lineCounter)
            sys.exit()


    # a block with declarations , subprogram and statements
    def block(namee):
        global token0
        global token1
        global quadList
        global listofallscopes
        flag = False
        declarations()
        subprograms()
        genquad('begin_block', namee, '_', '_')
        for i in range(len(listofallscopes)):
            for y in range(len(listofallscopes[i].entitylist)):
                if listofallscopes[i].entitylist[y].name == namee and (listofallscopes[i].entitylist[y].type == functionid or listofallscopes[i].entitylist[y].type == procedureid):
                    listofallscopes[i].entitylist[y].startquad = nextquad()-1
                    flag = True
                    break
            if flag == True:
                break

        statements()
        return

    # declaration of variables , zero or more " declare " allowed
    def declarations():
        global token0
        global token1
        while (token0 == declareid):
            token0, token1 = lex()
            varlist()
            if (token0 == questionamarkid):
                token0, token1 = lex()
                #return
            else:
                print("Error: the keyword ';' was expected after the varlist,in line:", lineCounter)
                sys.exit()
        return

    # a subprogram is a function or a procedure, followed by parameters and block
    def subprogram():
        global token0
        global token1
        global ccounter
        global scopeList
        global nestingLevel
        global listofallscopes
        if (token0 == functionid):
            ccounter=ccounter+1
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                func = Entity(functionid, name, 0)
                scopeList[-1].addentity(func)
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    nestingLevel = nestingLevel+1
                    scope = Scope([], nestingLevel, 12)
                    scopeList.append(scope)
                    formalparlist()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        #genquad('begin_block', name, '_', '_')
                        block(name)
                        framelength = scopeList[-1].getframelength()
                        listofallscopes.append(scopeList[-1])
                        del scopeList[-1]
                        nestingLevel = nestingLevel-1
                        scopeList[-1].changeentityframelength(framelength)
                        genquad('end_block', name, '_', '_')
                    else:
                        print("Error: expected ')' after parameters,in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error: expected '(' after the function,in line:", lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression , expected name for the function,in line:", lineCounter)
                sys.exit()
        elif (token0 == procedureid):
            token0, token1 = lex()
            ccounter=ccounter+1
            if (token0 == wordid):
                name = token1
                proc = Entity(procedureid, name, 0)
                scopeList[-1].addentity(proc)
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    nestingLevel = nestingLevel + 1
                    scope = Scope([], nestingLevel, 12)
                    scopeList.append(scope)
                    formalparlist()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        genquad('begin_block', name, '_', '_')
                        block(name)
                        framelength = scopeList[-1].getframelength()
                        listofallscopes.append(scopeList[-1])
                        del scopeList[-1]
                        nestingLevel = nestingLevel - 1
                        scopeList[-1].changeentityframelength(framelength)
                        genquad('end_block', name, '_', '_')
                    else:
                        print("Error: expected ')' after parameters,in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error: expected '(' after the function,in line:", lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression , expected name for the procedure,in line:", lineCounter)
                sys.exit()
        # else :
        # print("Error: expected 'function' or 'procedure',in line:", lineCounter)
        # sys.exit()
        return

    # zero or more subprograms allowed
    def subprograms():
        global token0
        global token1
        while (token0 == functionid or token0 == procedureid):
            subprogram()
        return

    # a list of variables following the declaration keyword
    def varlist():
        global token0
        global token1
        global variables
        global scopeList
        if (token0 == wordid):
            name = token1
            variables.append(name)
            var = Entity(wordid, name, 12)
            scopeList[-1].addentity(var)
            token0, token1 = lex()
            while (token0 == commaid):
                token0, token1 = lex()
                if (token0 == wordid):
                    name1 = token1
                    var = Entity(wordid, name1, 12)
                    scopeList[-1].addentity(var)
                    token0, token1 = lex()
                    variables.append(name1)
                else:
                    print("Error: a word was expected after the ';' character in line:", lineCounter)
                    sys.exit()
            return

        # list of formal parameters

    def formalparlist():
        global token0
        global token1
        if (token0 == inid or token0 == inoutid):
            formalparitem()
            while (token0 == commaid):
                token0, token1 = lex()
                # print(token1)
                if (token0 == inid or token0 == inoutid):
                    formalparitem()
                else:
                    print("Error: expected 'in' or 'inout' after the comma, in line:", lineCounter)
                    sys.exit()
        return

    # a formal parameter (" in ": by value , " inout " by reference )
    def formalparitem():
        global token0
        global token1
        global scopeList
        if (token0 == inid):
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                inpar = Entity(inid, name, 12)
                inpar.parmode = 'cv'
                scopeList[-1].addentity(inpar)
                wantednum = len(scopeList) -2
                scopeList[wantednum].entitylist[-1].arglist.append('in')
                token0, token1 = lex()
                return
            else:
                print("Error: expected word after 'in' in line:", lineCounter)
                sys.exit()
        elif (token0 == inoutid):
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                inoutpar = Entity(inoutid, name, 12)
                inoutpar.parmode = 'ref'
                scopeList[-1].addentity(inoutpar)
                wantednum = len(scopeList) - 2
                scopeList[wantednum].entitylist[-1].arglist.append('inout')
                token0, token1 = lex()
                return
            else:
                print("Error: expected word after 'inout' in line:", lineCounter)
                sys.exit()
        else:
            print("Error: expected 'in' or 'inout' in line:", lineCounter)
            sys.exit()

    # one or more statements
    def statements():
        global token0
        global token1
        if (token0 == wordid or token0 == ifid or token0 == whileid or token0 == switchcaseid or token0 == forcaseid or token0 == incaseid or token0 == callid or token0 == returnid or token0 == inputid or token0 == printid):
            name = token1
            statement()
            # token0,token1=lex()
            if (token0 == questionamarkid):
                token0, token1 = lex()
            else:
                print("Error: expected ';' after statement, in line:", lineCounter)
                sys.exit()
        elif (token0 == leftWaveParenthesisid):
            token0, token1 = lex()
            if (token0 == wordid or token0 == ifid or token0 == whileid or token0 == switchcaseid or token0 == forcaseid or token0 == incaseid or token0 == callid or token0 == returnid or token0 == inputid or token0 == printid):
                name = token1
                statement()
                while (token0 == questionamarkid):
                    token0, token1 = lex()
                    if (token0 == wordid or token0 == ifid or token0 == whileid or token0 == switchcaseid or token0 == forcaseid or token0 == incaseid or token0 == callid or token0 == returnid or token0 == inputid or token0 == printid):
                        name = token1
                        statement()
                    elif (token0 == rightWaveParenthesisid):
                        token0, token1 = lex()
                        return
                    else:
                        print("Error: expected statement after ';', in line:", lineCounter)
                        sys.exit()
                if (token0 == rightWaveParenthesisid):
                    token0, token1 = lex()
                else:
                    print("Error: expected '}' after statement, in line:", lineCounter)
                    sys.exit()
        else:
            print("Error: expected statement or '{' , in line:", lineCounter)
            sys.exit()
        return

    # one statement
    def statement():
        global token0
        global token1
        global ccounter
        if (token0 == wordid):
            name = token1
            assignStat()
        elif (token0 == ifid):
            ifStat()
        elif (token0 == whileid):
            whileStat()
        elif (token0 == switchcaseid):
            switchcaseStat()
        elif (token0 == forcaseid):
            forcaseStat()
        elif (token0 == incaseid):
            incaseStat()
        elif (token0 == callid):
            ccounter = ccounter + 1
            callStat()
        elif (token0 == returnid):
            returnStat()
        elif (token0 == inputid):
            inputStat()
        elif (token0 == printid):
            printStat()
        return

    # assignment statement
    def assignStat():
        global token0
        global token1
        if (token0 == wordid):
            name = token1
            token0, token1 = lex()
            if (token0 == assignid):
                token0, token1 = lex()
                expa = expression()
                genquad(':=', expa, '_', name)
                return
            else:
                print("Error: After the ID ':=' was expected, in line:", lineCounter)
                sys.exit()
        else:
            print("Error:Invalid expression. A name (ID) was expected, in line:", lineCounter)
            sys.exit()


    # if statement
    def ifStat():
        global token0
        global token1
        if (token0 == ifid):
            token0, token1 = lex()
            if (token0 == leftParenthesisid):
                token0, token1 = lex()
                bee=condition()
                if (token0 == rightParenthesisid):
                    token0, token1 = lex()
                    backpatch(bee[0], nextquad())
                    statements()
                    iflist=makelist(nextquad())
                    genquad('jump', '_', '_', '_')
                    backpatch(bee[1], nextquad())
                    elsepart()
                    backpatch(iflist, nextquad())
                else:
                    print("Error:Invalid expression. ')' was expected in line:", lineCounter)
                    sys.exit()
            else:
                print("Error:Invalid.expression. After 'if' , '(' was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error:Invalid expression. 'if' was expected, in line:", lineCounter)
            sys.exit()
        return

    # else part
    def elsepart():
        global token0
        global token1
        if (token0 == elseid):
            token0, token1 = lex()
            statements()
        return

    # while statement
    def whileStat():
        global token0
        global token1
        if (token0 == whileid):
            token0, token1 = lex()
            if (token0 == leftParenthesisid):
                token0, token1 = lex()
                bquad=nextquad()
                be=condition()
                if (token0 == rightParenthesisid):
                    token0, token1 = lex()
                    backpatch(be[0],nextquad())
                    statements()
                    genquad('jump','_','_',bquad)
                    backpatch(be[1],nextquad())
                else:
                    print("Error:Invalid expression. ')' was expected , in line:", lineCounter)
                    sys.exit()
            else:
                print("Error:Invalid expression. After 'while' , '(' was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error: Invalid expression. 'while' was expected , in line:", lineCounter)
            sys.exit()
        return

    # switch statement
    def switchcaseStat():
        global token0
        global token1
        if (token0 == switchcaseid):
            token0, token1 = lex()
            exitlist=emptyList()
            while (token0 == caseid):
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    cond=condition()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        backpatch(cond[0], nextquad())
                        statements()
                        e=makelist(nextquad())
                        genquad('jump', '_', '_', '_')
                        merged=mergelist(exitlist, e)
                        backpatch(cond[1], nextquad())
                    else:
                        print("Error:Invalid expression. ')' was expected , in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error:Invalid expression. '(' was expected after 'case' , in line:", lineCounter)
                    sys.exit()
            if (token0 == defaultid):
                token0, token1 = lex()
                statements()
                backpatch(exitlist, nextquad())
            else:
                print("Error:Invalid.expression. 'default' was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error:Invalid expression. 'switchcase' was expected , in line:", lineCounter)
            sys.exit()
        return

    # forcase statement
    def forcaseStat():
        global token0
        global token1
        if (token0 == forcaseid):
            token0, token1 = lex()
            p1quad=nextquad()
            while (token0 == caseid):
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    conditio=condition()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        backpatch(conditio[0], nextquad())
                        statements()
                        genquad('jump', '_', '_', p1quad)
                        backpatch(conditio[1], nextquad())
                    else:
                        print("Error:Invalid expression. ')' was expected , in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error:Invalid expression. '(' was expected after 'case' , in line:", lineCounter)
                    sys.exit()
            if (token0 == defaultid):
                token0, token1 = lex()
                statements()
            else:
                print("Error:Invalid.expression. 'default' was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error:Invalid expression. 'forcase' was expected , in line:", lineCounter)
            sys.exit()
        return

    # incase statement
    def incaseStat():
        global token0
        global token1
        global variables
        global scopeList
        if (token0 == incaseid):
            token0, token1 = lex()
            w = newtemp()
            newtempp = Entity(wordid, w, 12)
            scopeList[-1].addentity(newtempp)
            variables.append(w)
            p1quad = nextquad()
            genquad(':= ', 1, '_', w)
            while (token0 == caseid):
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    conditionen=condition()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        backpatch(conditionen[0], nextquad())
                        genquad(':=', 0, '_', w)
                        statements()
                        backpatch(conditionen[1], nextquad())
                    else:
                        print("Error:Invalid expression. ')' was expected , in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error:Invalid expression. '(' was expected after 'case' , in line:", lineCounter)
                    sys.exit()
            genquad('=', w, 0, p1quad)
        else:
            print("Error:Invalid expression. 'incase' was expected , in line:", lineCounter)
            sys.exit()
        return

    # return statement
    def returnStat():
        global token0
        global token1
        if (token0 == returnid):
            token0, token1 = lex()
            if (token0 == leftParenthesisid):
                token0, token1 = lex()
                expansion = expression()
                if (token0 == rightParenthesisid):
                    token0, token1 = lex()
                    genquad('retv', expansion, '_', '_')
                    return
                else:
                    print("Error: Invalid expression. ')' was expected , in line:", lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression. '(' was expected after 'return' , in line:", lineCounter)
                sys.exit()
        else:
            print("Error: Invalid expression. 'return' was expected , in line:", lineCounter)
            sys.exit()

    # call statement
    def callStat():
        global token0
        global token1
        if (token0 == callid):
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                token0, token1 = lex()
                if (token0 == leftParenthesisid):
                    token0, token1 = lex()
                    actualparlist()
                    genquad('call',name,'_','_')
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        return
                    else:
                        print("Error: Invalid expression. ')' was expected , in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error: Invalid expression. '(' was expected after ('call' and a name(ID)) , in line:",
                          lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression. after 'call' a name(ID) was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error: Invalid expression. 'call' was expected , in line:", lineCounter)
            sys.exit()

    # print statement
    def printStat():
        global token0
        global token1
        if (token0 == printid):
            token0, token1 = lex()
            if (token0 == leftParenthesisid):
                token0, token1 = lex()
                expp=expression()
                if (token0 == rightParenthesisid):
                    token0, token1 = lex()
                    genquad('out', expp, '_', '_')
                    return
                else:
                    print("Error: Invalid expression. ')' was expected , in line:", lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression. '(' was expected after 'print' , in line:", lineCounter)
                sys.exit()
        else:
            print("Error: Invalid expression. 'print' was expected , in line:", lineCounter)
            sys.exit()

    # input statement
    def inputStat():
        global token0
        global token1
        if (token0 == inputid):
            token0, token1 = lex()
            if (token0 == leftParenthesisid):
                token0, token1 = lex()
                if (token0 == wordid):
                    name = token1
                    token0, token1 = lex()
                    if (token0 == rightParenthesisid):
                        token0, token1 = lex()
                        genquad('inp', name, '_', '_')
                        return
                    else:
                        print("Error: Invalid expression. ')' was expected , in line:", lineCounter)
                        sys.exit()
                else:
                    print("Error: Invalid expression . After 'input' and '(' a name (ID) was expected, in line:",
                          lineCounter)
                    sys.exit()
            else:
                print("Error: Invalid expression. '(' was expected after 'input' , in line:", lineCounter)
                sys.exit()
        else:
            print("Error: Invalid expression. 'input' was expected , in line:", lineCounter)
            sys.exit()

    # list of actual parameters
    def actualparlist():
        global token0
        global token1
        if (token0 == inid or token0 == inoutid):
            # token0,token1=lex()
            actualparitem()
            while (token0 == commaid):
                token0, token1 = lex()
                actualparitem()
            # if(token0==inid or token0==inoutid):
            # token0,token1=lex()
            # else:
            # print("Error:Invalid expression . Expected 'in' or 'inout' , in line:", lineCounter)
            # sys.exit()
        return

    # an actual parameter (" in ": by value , " inout " by reference )
    def actualparitem():
        global token0
        global token1
        if (token0 == inid):
            token0, token1 = lex()
            aname=expression()
            genquad('par',aname,'CV','_')
            return
        elif (token0 == inoutid):
            token0, token1 = lex()
            if (token0 == wordid):
                name = token1
                token0, token1 = lex()
                genquad('par', name, 'REF', '_')
                return
            else:
                print("Error:Invalid expression. After 'inout' a name(ID) was expected , in line:", lineCounter)
                sys.exit()
        else:
            print("Error:Invalid expression. Expected 'in' or 'inout' , in line:", lineCounter)
            sys.exit()

    # boolean expression
    def condition():
        global token0
        global token1
        btrue=[]
        bfalse=[]
        bolean=boolterm()
        btrue=bolean[0]
        bfalse=bolean[1]
        while (token0 == orid):
            token0, token1 = lex()
            backpatch(bfalse,nextquad())
            bolean2=boolterm()
            btrue=mergelist(btrue,bolean2[0])
            bfalse=bolean2[1]
        return [btrue,bfalse]  # prepei na epistrefei boolean timh

    # term in boolean expression
    def boolterm():
        global token0
        global token1
        qtrue=[]
        qfalse=[]
        bool=boolfactor()
        qtrue=bool[0]
        qfalse=bool[1]
        while (token0 == andid):
            token0, token1 = lex()
            backpatch(qtrue,nextquad())
            bool2=boolfactor()
            qfalse=mergelist(qfalse,bool2[1])
            qtrue=bool2[0]
        return [qtrue,qfalse]

    # factor in boolean expression
    def boolfactor():
        global token0
        global token1
        if (token0 == notid):
            token0, token1 = lex()
            if (token0 == leftSquareParenthesisid):
                token0, token1 = lex()
                b=condition()
                if (token0 == rightSquareParenthesisid):
                    token0, token1 = lex()
                    return [b[1],b[0]]
                else:
                    print("Error:Invalid expression . Expected ']' , in line:", lineCounter)
                    sys.exit()
        elif (token0 == leftSquareParenthesisid):
            token0, token1 = lex()
            a=condition()
            if (token0 == rightSquareParenthesisid):
                #Rtrue=a[0]
                #Rfalse=a[1]
                token0, token1 = lex()
                return [a[0],a[1]]
            else:
                print("Error:Invalid expression . Expected ']' , in line:", lineCounter)
                sys.exit()
        else:
            expa = expression()
            rop = REL_OP()
            expb = expression()
            Rtrue=makelist(nextquad())
            genquad(rop, expa, expb, '_')
            Rfalse = makelist(nextquad())
            genquad("jump",'_','_','_')
            return [Rtrue,Rfalse]

    # arithmetic expression
    def expression():
        global token0
        global token1
        global variables
        global scopeList
        k = optionalSign()
        tok = term()
        while (token0 == plusid or token0 == minusid):
            aop = ADD_OP()
            t = term()
            w = newtemp()
            newtempp = Entity(wordid, w, 12)
            scopeList[-1].addentity(newtempp)
            variables.append(w)
            genquad(aop, tok, t, w)
            tok = w
        return tok

    # term in arithmetic expression
    def term():
        global token0
        global token1
        global variables
        global scopeList
        a = factor()
        while (token0 == multiid or token0 == divideid):
            mop = MUL_OP()
            b = factor()
            w = newtemp()
            newtempp = Entity(wordid, w, 12)
            scopeList[-1].addentity(newtempp)
            variables.append(w)
            genquad(mop, a, b, w)
            a = w
        return a

    # factor in arithmetic expression
    def factor():
        global token0
        global token1
        global variables
        global scopeList
        if (token0 == finalNumbid):
            iteg = INTEGER()
            return iteg
        elif (token0 == leftParenthesisid):
            token0, token1 = lex()
            expa = expression()
            if (token0 == rightParenthesisid):
                token0, token1 = lex()
                return expa
            else:
                print("Error: expected ')' after the parameter, in line:", lineCounter)
                sys.exit()
        elif (token0 == wordid):
            name = token1
            token0, token1 = lex()
            tail = idtail()
            if (tail == 'parameters'):
                newt=newtemp()
                variables.append(newt)
                newtempp = Entity(wordid, newt, 12)
                scopeList[-1].addentity(newtempp)
                genquad('par', newt, 'RET', '_')
                genquad('call', name, '_', '_')
                return newt
            return name
        else:
            print("Error: expected integer or expression or word ID, in line:", lineCounter)
            sys.exit()

    # follows a function of procedure ( parethnesis and parameters )
    def idtail():
        global token0
        global token1
        if (token0 == leftParenthesisid):
            token0, token1 = lex()
            actualparlist()
            if (token0 == rightParenthesisid):
                token0, token1 = lex()
                return 'parameters'
            else:
                print("Error: expected ')' after the parameter, in line:", lineCounter)
                sys.exit()
        return ''

    # sumbols "+" and " -" ( are optional )
    def optionalSign():
        global token0
        global token1
        if (token0 == plusid or token0 == minusid):
            aop = ADD_OP()
            return aop  # tokenextra = add_op return tokenextra.....token1 = add_op return token1
        return ''

    # relational lexer rule
    def REL_OP():
        global token0
        global token1
        if (
                token0 == equalsid or token0 == lessOrEqualid or token0 == moreOrEqualid or token0 == moreThanid or token0 == lessThanid or token0 == notEqualid):
            rel = token1
            token0, token1 = lex()
        else:
            print("Error: expected relational operator after expression, in line:", lineCounter)
            sys.exit()
        return rel

    # arithmetic lexer rule
    def ADD_OP():
        global token0
        global token1
        if (token0 == plusid or token0 == minusid):
            temp = token1
            token0, token1 = lex()
        else:
            print("Error: expected relational operator, in line:", lineCounter)
            sys.exit()
        return temp

    # operations lexer rule
    def MUL_OP():
        global token0
        global token1
        if (token0 == multiid or token0 == divideid):
            temp = token1
            token0, token1 = lex()
        else:
            print("Error: expected '*' or '/' operator, in line:", lineCounter)
            sys.exit()
        return temp

    # integer lexer rule
    def INTEGER():
        global token0
        global token1
        if (token0 == finalNumbid):
            temp = token1
            token0, token1 = lex()
        else:
            print("Error: number expected, in line:", lineCounter)
            sys.exit()
        return temp

    # ID lexer rule
    def ID():
        global token0
        global token1
        if (token0 == wordid):
            temp = token1
            token0, token1 = lex()
        else:
            print("Error: invalid word id, in line:", lineCounter)
            sys.exit()
        return temp

    # number of quad
    def nextquad():
        global quadNumb
        return quadNumb

    # create quad
    def genquad(op, x, y, z):
        global quadList
        global quadNumb
        list = []
        list.append(quadNumb)
        list.append(op)
        list.append(x)
        list.append(y)
        list.append(z)
        # quadList for backpatch
        quadList.append(list)
        quadNumb = quadNumb+1
        return list

    # create and return a temporary variable
    def newtemp():
        global temp
        temp = temp + 1
        return 'T_' + str(temp)

    # make an empty quad list
    def emptyList():
        tempList = ['_', '_', '_', '_']
        return tempList

    # make a list of x
    def makelist(x):
        xlist = [x]
        return xlist

    # merge the two lists in parameters
    def mergelist(list1, list2):
        mergedList = list1.extend(list2)
        return mergedList

    def backpatch(list, z):
        global quadList
        for i in quadList:
            if i[0] in list:
                i[4] = z
        return

    token0, token1 = lex()
    program()



global quadList
global listofallscopes
def writeToSaFile():
    ###################################################################################
    file = open("scopes.txt", "w")
    for i in range(len(listofallscopes)):
        file.write("Scope"+str(i)+"\n")
        for j in range(len(listofallscopes[i].entitylist)):
            file.write("Entity: "+str(j)+" ")
            file.write("Name: "+str(listofallscopes[i].entitylist[j].name)+", "+"Type: "+str(listofallscopes[i].entitylist[j].type)+", "+"StartQuad: "+str(listofallscopes[i].entitylist[j].startquad)+", "+"parMode: "+str(listofallscopes[i].entitylist[j].parmode)+", "+"Framelength: "+str(listofallscopes[i].entitylist[j].framelength)+", "+"Offset: "+str(listofallscopes[i].entitylist[j].offset)+"\n")
            if listofallscopes[i].entitylist[j].type == functionid or listofallscopes[i].entitylist[j].type == procedureid:
                file.write("Arglist: ")
                #for k in range(len(listofallscopes[i].entitylist[j].arglist)):
                file.write(str(listofallscopes[i].entitylist[j].arglist))
                file.write("\n")
	file.write("\n")
    file.close()
def writeToIntFile():
    file=open("quadList.int","w")
    for i in quadList:
        file.write(str(i[0]) + ". (" + str(i[1]) + ", "+ str(i[2]) + ", "+ str(i[3]) + ", "+ str(i[4]) + ")\n")
    file.close
def writeToCFile():
    file=open("quadList.c", "w")
    file.write("#include <stdio.h>\n\n")
    file.write("int main()\n{\n")
    file.write("int: ")
    for i in range(len(variables)):
        file.write(variables[i])
        if(i!=(len(variables)-1)):
            file.write(",")
    file.write(";\n")
    for i in range(len(quadList)):
        quad=quadList[i]
        file.write("L_"+str(quad[0])+":")
        if (quad[1] == 'jump'):
            file.write("goto L_"+str(quad[4])+";")
        if (quad[1]=='=' or quad[1]=='<>' or quad[1]=='<' or quad[1]=='<=' or quad[1]=='>' or quad[1]=='>='):
            if (quad[1] == '='):
                file.write("if("+str(quad[2])+" == "+str(quad[3])+") goto L_"+str(quad[4])+";")
            elif (quad[1] == '<>'):
                file.write("if("+str(quad[2])+" != "+str(quad[3])+") goto L_"+str(quad[4])+";")
            else:
                file.write("if("+str(quad[2])+" "+str(quad[1])+" "+str(quad[3])+") goto L_"+str(quad[4])+";")
        if (quad[1] == ':='):
            file.write(str(quad[4])+"="+str(quad[2])+";")
        if (quad[1]=='*' or quad[1]=='/' or quad[1]=='+' or quad[1]=='-'):
            file.write(str(quad[4])+"="+str(quad[2])+""+str(quad[1])+""+str(quad[3])+";")
        if (quad[1] == 'retv'):
            file.write("return("+str(quad[2])+");")
	if (quad[1] == 'inp'):
	    file.write('scanf("%d",&'+str(quad[2])+');')
	if (quad[1] == 'out'):
	    file.write('printf("%d",'+str(quad[2])+');')
        if (quad[1] == 'halt'):
            file.write("{}")
        if (quad[1]!='halt'):
            file.write(" //("+str(quad[1])+", "+str(quad[2])+", "+str(quad[3])+", "+str(quad[4])+")" )
	file.write("\n")
    file.write("}")
    file.close
# TESTING
file = open(sys.argv[1])
lex()
file.seek(0);
lineCounter = 1
ccounter = 0
yacc()
#print("kalhspera\n")
if (ccounter!=0):
    writeToCFile()
writeToIntFile()
writeToSaFile()