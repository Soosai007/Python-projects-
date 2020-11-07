import xlsxwriter
import datetime
workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 30)
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
worksheet.write('A2',now.strftime("%Y-%m-%d %H:%M:%S"))
workbook.close()
