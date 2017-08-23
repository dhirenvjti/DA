import webapp2
from google.appengine.ext.webapp import template

import utils

import StringIO
import openpyxl

class MUHandler(webapp2.RequestHandler):
    def get(self):
        user_email = utils.authenticate_user(self, self.request.url)
        if not user_email:
            return

        page = utils.template("upload.html", "ExcelReader/templates")
        template_values = {
            "upload_label": "Excel File (.xslx): ",
            "accept": ".xlsx"
        }
        self.response.out.write(template.render(page, template_values))

    def post(self):
        user_email = utils.authenticate_user(self, self.request.url)
        if not user_email:
            return

        xslx_file_html = self.request.get('file', '')
        xslx_file = StringIO.StringIO(xslx_file_html)
        wb = openpyxl.load_workbook(filename=xslx_file, read_only=True)
        print wb.get_sheet_names()

    def analyze(self):
        pass
