import re
import os
import sys

from simpleindent import indent
from simpletag import DOM, Button, Number, Radio, CheckBox, Select, SelectOption, Date, TextBox, TextArea, STag
from yatheading import headmeta, styling


if __name__ == '__main__':
    #----------------------------
    # HTML set up
    #
    doc = DOM()
    doc += ('<!DOCTYPE html>')
    
    #----------------------------
    # HTML rendering
    #
    with doc.tag('html'):
        with doc.tag('head'):
            headmeta(doc)
        with doc.tag('style'):
            #doc.text('body { background-image: url("static/images/ironman.jpeg"); background-repeat: no-repeat; background-attachment: fixed; background-size: cover; }')
            styling(doc)
            doc += ('.tblbody { background-image: url("static/images/ironman.jpeg"); background-repeat: no-repeat; background-attachment: fixed; background-size: cover; }')

        with doc.tag('body'):
            with doc.tag('div', id='tooplate_content', width='100%', kclass='scale-base') as div:
                doc += STag('p', label='The is a sample output .... ')

                with doc.tag('form', id='form-progressreport', name='form-progressreport', action="/progressreport", method="post"):
                    rows, cols = 7, 4
                    with doc.table(dim=(rows, cols), colwidths = [2, 2, 4, 2], border='4', kclass='tblbody') as table:
                        r = 0
                        for c in range(cols):
                            table[r, c] = Number(f'{r}_{c}', value=f'{r}_{c}', kclass='style-lf-bo-bgdkred')

                        optlist = [ SelectOption(value='pls choose one of the below', disabled=True, selected=True), 
                                    SelectOption(value='Male'), 
                                    SelectOption(value='Female') ]
                        r = 1; c = 0
                        table[r, c:c+3] = Select(f'{r}_{c}', value=optlist, multiple=True)

                        r = 1; c = 3
                        table[r, c] = CheckBox(f'{r}_{c}', value=f'{r}_{c}', label=f'{r}_{c}_check', checked=True)
                        r = 2; c = 0
                        table[r:r+2, c:c+2] = CheckBox(f'{r}_{c}', value=f'{r}_{c}', label=f'{r}_{c}_uncheck')
                        r = 2; c = 2
                        table[r, c] = Date(f'{r}_{c}')
                        r = 2; c = 3
                        table[r, c] = TextBox(f'{r}_{c}', value=f'{r}_{c}', required=True)
                        r = 3; c = 2
                        table[r, c:c+2] = TextArea(f'{r}_{c}', value=f'{r}_{c}', rows=3, cols=4, maxlength=20)

                        r = 4
                        c = 0
                        table[r, c] = Radio(f'{r}_radio_2', value=f'{r}_{c}', kclass='lf_color', label=f'{r}_{c}_uncheck')
                        c = 1
                        table[r, c] = Radio(f'{r}_radio_2', value=f'{r}_{c}', kclass='lf_color', label=f'{r}_{c}_check', checked=True)
                        for c in range(2, 4):
                            table[r, c] = Radio(f'{r}_radio_4', value=f'{r}_{c}', kclass='lf_color', label=f'{r}_{c}_uncheck')

                        table[5, 1:3] = 'this is a very long string ..... what the hack .....'
                        table[5, 0] = ''

                        r = 6
                        c = 0
                        #table[r, c] = Button(name='submit-progressreport', id='submit-progressreport', value=1, label='Submit')
                    doc += Button(name='submit-progressreport', id='submit-progressreport', value=1, label='Submit', kclass ="style-lf-bo-bgdkred style-base-fz")
                    with doc.tag('p'):
                        doc += '<br>'
                        doc += 'This is normal text - <span style="font-weight:bold;">and this is bold text</span>'
                    doc += STag('p', label='story is .... ')
                    with doc.tag('i'):
                        doc += 'Feedback to ' + STag('a', label='Visit W3Schools', href="https://www.w3schools.com")



    #----------------------------
    # HTML output
    #
    output = doc.getvalue()
    print(indent(output)) 

