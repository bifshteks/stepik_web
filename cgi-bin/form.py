#!/usr/bin/env python3
import cgi
import html
import datelist

def get_pather(month):
	month = month.lower()
	if month.endswith('ь') or  month.endswith('й'):
		month = month[:-1] + 'я'
		return month
	else:
		month = month + 'а'
		return month
	
form = cgi.FieldStorage()

month = form.getvalue('Month', '')
day_from = int(form.getvalue('Day_from', 1))
day_to = int(form.getvalue('Day_to', 1))

day_to = day_from if day_to < day_from else day_to
month = html.escape(month)
#day_from = html.escape(day)
#day_to = html.escape(day)
days_range = tuple([day_from,day_to])

day_days = days_range[0] if days_range[0] == days_range[1] else\
					'{} - {}'.format(days_range[0], days_range[1])

datelist = datelist.main(day_from, day_to, month)					

print('Content-type: text/html\n')
print('''<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="windows-1251">
            <title>Обработка данных форм</title>
			<style>
				body{
					background-image: url("http://weblabfon.com/_ld/2/244_wood05.jpg");
					background-repeat: repeat;
					color: white;
					font-family: cursive;
					text-shadow: black 2px 2px 7px,
							black 2px 2px 7px,
							black 2px 2px 7px;
				}

				.header{
                                        width: 70%;
                                        heigth: 100px;
				}

				.head-text{
					width: 50%;
					height: 100px;
					font-size: 60px;
				}
				
				td{
					width: 100px;
					padding-bottom: 5px;
					border-bottom: 2px solid white;
					
				}
				
				td{
					margin-bottom: 5px;
				}
				
				.first{
					padding-top: 30px;
				}
				
				<!--input{
					border-radius: 3px;
					background-color: #5e81a8;
					color: white;
					border: 0px;
					padding: 4px;
					box-shadow: 0 0 10px black;
					margin-top: 20px;
				}-->
				.btn{
					border-radius: 8px;
					background-color: black;-->
					color: white;
					border: 0px;
					padding: 4px;
					box-shadow: 0 0 10px white;
			</style>
        </head>
        <body>''')
print('<div class="header"><span class="head-text">Расписание на {} {}:</span></div>'.format(day_days, get_pather(month)))
print('')
test_empty = 0
for day in datelist:
	if len(day) == 1:
		test_empty += 1

if test_empty == len(datelist):
	print('Занятий нет <br/><sub style="font-size: 8px">или программа хуево работает</sub>')
else:
	print('<table>')
	print('		<tr>')
	print('			<th class="1">День недели</td>')
	print('			<th class="2">Время</td>')
	print('			<th class="3">Предмет</td>')
	print('		</tr>')
	#print('test == ' + str(datelist))
	for day in datelist:
		for subj in day[:-1]:
			if subj == day[0]:
				print(' <tr>')
				print(' 	<td class="1 first">{}</td>'.format(day[-1]))
				print(' 	<td class="2 first">{}</td>'.format(subj[0]))
				print(' 	<td class="3 first">{}</td>'.format(subj[1]))
				print(' </tr>')
			
			else:
				print(' <tr>')
				print(' 	<td class="1">{}</td>'.format(''))
				print(' 	<td class="2">{}</td>'.format(subj[0]))
				print(' 	<td class="3">{}</td>'.format(subj[1]))
				print(' </tr>')

	print('</table>')

print('<form action="../index.html">')
print('<input type="submit" value="Вернуться на главную" class="btn">')
print('</form>')

print('''</body>
        </html>''')