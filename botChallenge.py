"""
You are given a list of API calls in the format /project/subproject/method.
You need to calculate and print the number of calls to each node of the API endpoint as a tree.

In this tree, projects, subprojects, and methods should be sorted in the same order as they were given in the input data.
The output tree should consist of several strings. All subprojects fall under their parent project,
and all methods fall under the subproject in which they are included. The string that represents a project starts with --,
while subprojects start with ---- and methods start with ------. After the project, subproject,
or method name, put the number of requests to this module in parentheses.
Take a look at the example for a guide of what this tree should look like.

Example

For

calls = [
        "/project1/subproject1/method1",
        "/project2/subproject1/method1",
        "/project1/subproject1/method1",
        "/project1/subproject2/method1",
        "/project1/subproject1/method2",
        "/project1/subproject2/method1",
        "/project2/subproject1/method1",
        "/project1/subproject2/method1"
]
the output should be

countAPI(calls) = [
        "--project1 (6)",
        "----subproject1 (3)",
        "------method1 (2)",
        "------method2 (1)",
        "----subproject2 (3)",
        "------method1 (3)",
        "--project2 (2)",
        "----subproject1 (2)",
        "------method1 (2)]
"""

class Main():
    def __init__(self):
        self.dicc = {}

    def add(self, ruta):
        tokens = ruta[1:].split('/')

        def f(dicc, tokenList):
                if len(tokenList) == 1:
                    dicc[tokenList[0]] = None
                    return
                elif dicc.has_key(tokenList[0]):
                    f(dicc[tokenList[0]], tokenList[1:])
                else:
                    dicc[tokenList[0]] = {}
                    f(dicc[tokenList[0]], tokenList[1:])

                return dicc #cambia dic tras bambalinas
        f(self.dicc,tokens)

    def printing(self):
        def console(dicc,i):
            if dicc != None:
                for k, v in dicc.iteritems():
                    print i*'-'+k
                    #print k
                    console(dicc[k],i+2)

        console(self.dicc,2)

"""def someName(calls):    
    Api = Main()
    for path in calls:
        Api.add(path)
    Api.printing()

someName([
        "/project1/subproject1/method1",
        "/project2/subproject1/method1",
        "/project1/subproject1/method1",
        "/project1/subproject2/method1",
        "/project1/subproject1/method2",
        "/project1/subproject2/method1",
        "/project2/subproject1/method1",
        "/project1/subproject2/method1"])"""


#Right and Easy Solution
def countAPI(calls):
    lista = list()
    lista_count = {}
    for path in calls:
        tokens = path[1:].split('/')
        aux = ''
        for toke in tokens:
            aux = aux + '/' + toke
            if aux in lista:
                lista_count[aux] += 1
            else:
                lista.append(aux)
                lista_count[aux] = 1

    lista1 = []
    for elemento in lista:
        tokens = elemento[1:].split('/')
        if len(tokens) == 1:
            lista1.append(tokens[0])
            
    lista2 = list(lista1)
    index = 0
    aux = []
    for p in lista1:
        aux = []
        for elemento in lista:
            tokens = elemento[1:].split('/')
            if len(tokens) == 2 and p == tokens[0]:
                aux.append(tokens[1])
        lista2[index] = aux
        index += 1
            
    lista3 = [j for i in lista2 for j in i]
    index = 0
    aux = []
    for i in range(len(lista1)):
        for s in lista2[i]:
            aux = []
            for elemento in lista:
                tokens = elemento[1:].split('/')
                
                if len(tokens) == 3 and lista1[i] == tokens[0] and s == tokens[1]:
                    #print lista1[i], s
                    aux.append(tokens[2])

        #print aux
            lista3[index] = aux
            index += 1


    index=0
    final_list = []
    #print lista_count
    for i in range(len(lista1)):
        final_list.append('--'+lista1[i]+' ('+str(lista_count['/'+lista1[i]])+')')
        for j in lista2[i]:
            final_list.append('----'+j+' ('+str(lista_count['/'+lista1[i]+'/'+j])+')')
            for k in lista3[index]:
                final_list.append('------'+k+' ('+str(lista_count['/'+lista1[i]+'/'+j+'/'+k])+')')
            index +=1
        

    #print lista1, lista2, lista3
    
            
    return final_list





a = countAPI([
"/project/subproject1/methods", 
 "/project/subproject1/method", 
 "/project/subproject2/method", 
 "/project/subproject3/method", 
 "/project/subproject2/method", 
 "/project/subproject4/method", 
 "/project/subproject2/method", 
 "/project/subproject4/method2", 
 "/project/subproject4/method1", 
 "/project/subproject1/methods", 
 "/project/subproject4/method1", 
 "/project/subproject2/method", 
 "/project/subproject4/method", 
 "/project/subproject2/method", 
 "/project/subproject1/methods"])
