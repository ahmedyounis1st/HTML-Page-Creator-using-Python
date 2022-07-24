from json.tool import main
from typing import List, overload
import pandas as pd
import numpy as np

from dataclasses import dataclass

@dataclass
class SelectOption:
    value: str = None
    disabled: bool = False
    selected: bool = False

    def __iter__(self):
        return iter((self.value, self.disabled, self.selected))

    def __repr__(self):
        return (f'[{self.value}, {self.disabled}, {self.selected}]')

class HtmlInput:
    serialcnt = 0

    def __init__(self, name,kclass = '', **args):
        self._name = name
        self._kclass = kclass
        self._args = args

    def _evaluate(self):
        res = 'name = "' + self._name + '"' +' class="'+self._kclass+ '"'
        for arg in self._args.items():
             res += ' '+ str(arg[0])+' = "'+str(arg[1])+'"'
        return(res)
        

class Number (HtmlInput):
    def __repr__(self):   
        return ('<input type="number" ' + self._evaluate() +'/>\n')

class Date (HtmlInput):
    def __repr__(self):
        return ('<input type="date" ' + self._evaluate() + '/>\n')

class Button (HtmlInput):
    def __init__(self, name, label, **args):
        super().__init__(name, **args)
        self.label = label
    def __repr__(self):        
        return ('<button ' + self._evaluate() + f'>{self.label}</button>\n')

class Radio (HtmlInput):
    def __init__(self, name, label, checked = False, **args):
        super().__init__(name, **args)
        self.label = label
        self.checked = checked
    def __repr__(self):
        c = ''
        if self.checked == True:
            c = " checked "
        return ('<input type="radio" ' + self._evaluate() + f'{c}>{self.label}')
 
class TextArea (HtmlInput):
    def __init__(self, name, value, **args):
        super().__init__(name, **args)
        self.value = value
        
    def __repr__(self):
        return ('<textarea ' + self._evaluate() + f'>{self.value}</textarea>\n')

class TextBox (HtmlInput):
    def __init__(self, name, value, required = False, **args):
        super().__init__(name, **args)
        self.value = value
        self.required = required

    def __repr__(self):
        r = ''
        if self.required == True:
            r = " required "
        return ('<input type="text" ' + self._evaluate() +f' value = "{self.value}"{r}/>\n')

class CheckBox (HtmlInput):
    def __init__(self, name, label, checked = False, **args):
        super().__init__(name, **args)
        self.label = label
        self.checked = checked

    def __repr__(self):
        c = ''
        if self.checked == True:
            c = " checked "
        return ('<input type="checkbox" ' + self._evaluate() + f'{c}>{self.label}')

class Select (HtmlInput):
    def __init__(self, name, value, multiple = False, **args):
        super().__init__(name, **args)
        self.value = value
        self.multiple = multiple

    def __repr__(self):    
        element = '<select '+ self._evaluate()
        if self.multiple == True:
            element += ' multiple'
        element += '>\n'
        for option in self.value:
             element += f'  <option value="{option.value}"'
             if option.selected == True:
                 element +=' selected'
             if option.disabled == True:
                 element +=' disabled'
             element += f'>{option.value}</option>\n'
        element += '</select>\n'
    
        return str(element)

class STag (HtmlInput):
    
    def __init__(self,tag, name= '', label='', **args):
        self.tag =tag
        self.name = name
        self.label = label
        self.args = args


    def __repr__(self):
        res =f'<{self.tag}'
        if self.name:
            res += f' name="{self.name}"'
        for arg in self.args.items():
            res += f' {str(arg[0])}="{str(arg[1])}"'
      
        if self.label:
            res += f'>{self.label}</{self.tag}>'
        else:
              res += '/>'
        res +=''  
        return  str(res)
        

class DOM:
    def __init__(self):
        self.file_data = '' 
        with  open('test.html', 'w') as file:
            file.write(self.file_data)   

    def __repr__(self):
        return self.file_data
    
    def __iadd__(self, other):
        # with open('test.html', 'r')  as file: 
        #     self.file_data = file.read()
        self.file_data += (str(other)+'\n')
        with  open('test.html', '+a') as file:
            file.write(str(other)+'\n')  
        return self
        
    class HtmlTag :
        def __init__(self, DOM, tag_name, **args): 
            self.file_data = DOM.file_data
            self.tag_name = tag_name
            self.args = args
     

        def __iadd__(self, other):
            self.file_data += (str(other)+'')
            return self           
    
        def __enter__(self):  
            self.file_data =  f'<{self.tag_name}'   
            for arg in self.args.items():
                 self.file_data += f' {str(arg[0])} = "{str(arg[1])}"'
            self.file_data += '>\n'
            with  open('test.html', '+a') as file:
                file.write(self.file_data)       
           
        def __exit__(self, exception_type, exception_value, traceback):
            self.file_data = f'</{self.tag_name}>\n'
            with  open('test.html', '+a') as file:
                file.write(self.file_data)    


    def tag(self, tag_name, **args):
       return self.HtmlTag(self, tag_name, **args)

    class HtmlTable:
        
        def __init__(self, DOM, dim, colwidths, **auxpr):  
            self.dim = dim
            self.colwidths = colwidths
            self.auxpr = auxpr
            self.table = np.full(self.dim, " "*500)
            
        def __enter__(self): 
            res = '<table '
            for arg in self.auxpr.items():
                res += f' {str(arg[0])}="{str(arg[1])}"'
            res += '>\n'
            with  open('test.html', '+a') as file:
                file.write(res)  
            
            return self.table
            
        def search_element(self, item, my_arr):
            first_index = -1
            second_index = -1
            for i,ele in enumerate(my_arr):
                if ele == item :
                    first_index = i
                if first_index != -1 and ele != item:
                    second_index = i-1
                    break
            res = (first_index,second_index)
            return res



        def __exit__(self, exception_type, exception_value, traceback):
            for row in range(self.dim[0]-1):
                res = '<tr>\n'
                colspan = 0
                crnt = ''
                for col in range(self.dim[1]):
                    if self.table[row-1,col] == self.table[row,col]:
                        continue
                        
                    if crnt == self.table[row,col]:
                        colspan += self.colwidths[col]
                    elif colspan == 0 and crnt == '':
                        crnt = self.table[row,col]
                        colspan = self.colwidths[col] 
                    else:
                        if row == 2 and col == 2:
                            res += f'<td colspan="{colspan}" rowspan="2" >\n' + crnt +'</td>\n'
                        else:
                            res += f'<td colspan="{colspan}" rowspan="1" >\n' + crnt +'</td>\n'
                        crnt = self.table[row,col]
                        colspan = self.colwidths[col]
                res += f'<td colspan="{colspan}" rowspan="1" >\n' + crnt +'</td>\n'
                res += '</tr>\n'
                with  open('test.html', '+a') as file:
                    file.write(res)
            res = '</table>'
            with  open('test.html', '+a') as file:
                file.write(res)   


                

    def table(self, dim, colwidths, **auxpr): 
        return (self.HtmlTable(self, dim, colwidths, **auxpr))

    def getvalue(self):
        with  open('test.html', 'r') as file:
            self.file_data = file.read()   
        return self.file_data
   
if __name__ == "__main__":
    print(STag('p', label = 'label',href ='href'))
    print(STag('p', label = 'label'))
    print(STag('meta', charset="UTF-8"))
    print(Number('quantity', value= '5', kclass='style-lf-bo-bgdkred'))
    print(Date('date'))
    print(Button(name='submit-progressreport', id='submit-progressreport', value=1, label='Submit'))
    r = 4
    c = 0
    print(Radio(f'{r}_radio_4', value=f'{r}_{c}', kclass='lf_color', label=f'{r}_{c}_uncheck'))
    print(Radio(f'{r}_radio_2', value=f'{r}_{c}', kclass='lf_color', label=f'{r}_{c}_check', checked=True))
    print(TextArea(f'{r}_{c}', value=f'{r}_{c}', rows=3, cols=4, maxlength=20))
    print(TextBox(f'{r}_{c}', value=f'{r}_{c}', required=True))
    print(CheckBox(f'{r}_{c}', value=f'{r}_{c}', label=f'{r}_{c}_check', checked=True))
    optlist = [ SelectOption(value='pls choose one of the below', disabled=True, selected=True), 
                                    SelectOption(value='Male'), 
                                    SelectOption(value='Female') ]
    r = 1; c = 0
    print(Select(f'{r}_{c}', value=optlist, multiple=True))

    doc = DOM()
    doc += ('<!DOCTYPE html>')
    with doc.tag('html'):
        with doc.tag('body'):
            doc += str(STag('p', label = 'label'))
            with doc.table(dim=(7, 5), colwidths = [2, 2, 4, 2], border='4', kclass='tblbody') as table:
                table

   
    