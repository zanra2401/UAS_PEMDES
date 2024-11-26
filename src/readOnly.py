from PyQt6.QtWidgets import QStyledItemDelegate

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column() in (0, 3, 6): 
            return None
        return super().createEditor(parent, option, index)