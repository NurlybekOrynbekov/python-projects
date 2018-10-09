#! python3
# tableView.py - Форматирует переданный список, и выводит его в табличном виде

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    widht = []
    for row in list:
        maxWidth = 0
        for col in row:
            maxWidth = max(maxWidth, len(col))
        widht.append(maxWidth)
        
    for y in range(len(list[0])):
        text = ''
        for x in range(len(list)):
            text = text + list[x][y].rjust(widht[x]) + ' '
        print(text)
        
printTable(tableData)