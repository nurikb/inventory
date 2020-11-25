import os

from django.http import HttpResponse
import xlwt
from pyexcel import source


class Export_xlsMixin():
    column = None
    row_date = None
    row = None

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Admission')

        # Sheet header, first row
        row_num = 0

        date_format = xlwt.XFStyle()
        date_format.num_format_str = 'dd/MM/yyyy'


        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = self.column
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        row_date = self.row_date
        for row in row_date:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], date_format)

        rows = self.row
        row_num = 0
        for row in rows:
            row_num += 1
            for col_num in range(1, len(row)+1):
                ws.write(row_num, col_num, row[col_num-1], font_style)

        wb.save(response)
        return response
