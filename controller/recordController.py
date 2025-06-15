#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-06-15

from model.Record import Record
from view.recordView import recordView
from util.fileIO import fileIO
import uuid

class recordController:
    def reloadData(self):
        self.records = CSVReader(self.filename)
        self.view.message("Data Reloaded")

    