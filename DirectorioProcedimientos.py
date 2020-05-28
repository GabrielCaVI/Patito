from TablaVariables import TablaVariables
import getopt
import sys
class DirectorioProcedimientos(object):
    def __init__(self):
        self.list = {}
    
    def add_function(self, name, fType, numParams, typeParams, nameParams, numVars, quad):
        if(name not in self.list.keys()):
            self.list[name] = {
                'type': fType,
                'numParams': numParams,
                'typeParams': typeParams,
                'nameParams': nameParams,
                'vars': TablaVariables(),
                'numVars': numVars,
                'quadNum': quad
            }
            #print("added function: " + name)
        else:
            print("function" + name + " already declared")
    
    def search(self, name):
        return name in self.list

    def search_var(self, fName, vName):
        if self.list[fName]['vars'].search(vName) == True:
            return True
        elif self.list['global']['vars'].search(vName):
            return True
        else:
            print("Variable " + str(vName) + " does not exist")
            return False

    def get_function_type(self, fName):
        return self.list[fName]['type']

    def get_var_type(self, fName, vName):
        if self.list[fName]['vars'].search(vName) == True:
            return self.list[fName]['vars'].get_type(vName)
        elif self.list['global']['vars'].search(vName) == True:
            return self.list['global']['vars'].get_type(vName)
        else:
            print("Variable " + str(vName) +" does not exist")
            sys.exit()
    
    def get_var_memory_loc(self, fName, vName):
        if self.list[fName]['vars'].search(vName) == True:
            return self.list[fName]['vars'].get_memory_loc(vName)
        elif self.list['global']['vars'].search(vName) == True:
            return self.list['global']['vars'].get_memory_loc(vName)
        else:
            print("Variable " + str(vName) +" does not exist")
            sys.exit()
    
    def get_parameter_type(self, fName, pos):
        return self.list[fName]['typeParams'][pos]

    def get_numParams(self, fName):
        return self.list[fName]['numParams']

    def get_quad_num(self, fName):
        return self.list[fName]['quadNum']

    def add_var(self, fName, vName, vType, vMemoryLoc):
        if(self.list[fName]['vars'].search(vName) == True):
            print("Variable already exists")
            sys.exit()
        else:
            self.list[fName]['vars'].add_var(vName, vType, vMemoryLoc)
            self.list[fName]['numVars'] = self.list[fName]['numVars'] + 1
    
    def add_param(self, fName, vName, vType):
        self.list[fName]['numParams'] = self.list[fName]['numParams'] + 1
        self.list[fName]['nameParams'].append(vName)
        self.list[fName]['typeParams'].append(vType)
    
    def add_quad_counter(self, fName, quad):
        self.list[fName]['quadNum'] = quad

    def delete_var_table(self, fName):
        self.list[fName]['vars'] = None

    def list_vars(self, name):
        if name in self.list:
            self.list[name]['vars'].print_all_vars()
    
    def add_num_tmp(self, fName, numTmpVars):
        self.list[fName]['numTmp'] = numTmpVars

    def print_proc(self):
        for elem in self.list:
            print(elem, self.list[elem])
        
    def print_out_proc(self):  
        for elem in self.list:
            print(elem, end=' ')
            for l in self.list[elem]:
                print(str(self.list[elem][l]), end=" ")
            print()

# if __name__ == "__main__":
#     print("calando tests...")
#     test = DirectorioProcedimientos()
#     test.add_function('function1', 'void', 2, ['int', 'float'], ['myInt', 'myFloat'], 0)
#     test.add_var('function1', 'x', int, 100)
#     test.add_var('function1', 'y', int, 101)
#     test.add_var('function1', 'z', int, 102)
#     test.add_var('function1', 'b', bool, 103)
#     print(test.search('function1'))
#     test.list_vars('function1')