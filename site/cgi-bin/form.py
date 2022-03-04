import cgi, sys
form = cgi.FieldStorage()         # извлечь данные из формы
print("Content­type: text/html")  # плюс пустая строка

html1 = """
<TITLE>таблица с анкетой</TITLE>
<META charset='utf-8'>
<LINK rel='stylesheet' href='../main.css' />
<H1 class='formResultsHeading' >Анкета пользователя</H1>
<table class='table' border =2> <tr>  <td>Имя поля</td><td>Значение</td>  </tr>
"""

# печать заголовка таблицы
print (html1)


ll = ['Имя','Любимый язык программирования', 'Инструмент параллелизма']

data = ['','','','','']; i=0
for field in (['username', 'userFavoriteLanguage', 'userLastInstrument' ]):
    if not field in form:
        data[i] = '(unknown)'
    else:

        if not isinstance(form[field], list):
            data[i] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[i] = ', '.join(values)
    i+=1

for i in range(5):
   print ('<tr><td> %s </td> <td> %s </td></tr>'% (ll[i], data[i]))

print (' </table>')
