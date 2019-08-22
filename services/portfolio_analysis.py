import sqlite3
import json
import csv
import json
from datetime import datetime, timedelta
#Date, symbol, entry price, position size

def get_cursor():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    return cursor

def get_position_dict():
    cursor = get_cursor()
    command =(
    '''
    SELECT * FROM portfolio
    '''
    )
    cursor.execute(command)
    positions = {}
    for row in cursor:
        date = row[0]
        symbol = row[1]
        entry = row[2]
        position = row[3]
        positions[symbol] = {
        'date':datetime.strptime(date, '%m-%d-%Y'),
        'position':position,
        'entry':entry
        }
    return positions

#0 date
#4 is close
def create_portfolio():
    positions = get_position_dict()
    portfolio = {}
    for symbol in positions.keys():
        access_string = "MII/" + symbol + ".csv"
        with open(access_string, 'r') as csv_file:
            first = True
            stocks_reader = csv.reader(csv_file)
            for row in stocks_reader:
                if first:
                    first = False
                    continue
                if datetime.strptime(row[0], '%Y-%m-%d') >= datetime.strptime('2018-08-20', '%Y-%m-%d'):
                    if row[0] not in portfolio:
                        portfolio[row[0]] = {'profit':0, 'value':0}
                    portfolio[row[0]]['profit'] += ((float(row[4]) - positions[symbol]['entry']) * positions[symbol]['position'])
                    portfolio[row[0]]['value'] += (float(row[4]) * positions[symbol]['position'])
    with open('test.json', 'w+') as port_file:
        json.dump(portfolio, port_file)
    return portfolio

def get_axis():
    dates = []
    value = []
    with open('test.json') as port_file:
        portfolio = json.load(port_file)
    for day in portfolio.keys():
        dates.append(datetime.strptime(day, '%Y-%m-%d'))
        value.append(portfolio[day]['value'])
    return dates, value

def get_starting_cash():
    positions = get_position_dict()
    total = 0
    for key in positions.keys():
        total += positions[key]['position'] * positions[key]['entry']
    return total

def SP_calc():
    starting_cash = get_starting_cash()

def get_pie_graph():
    positions = []
    values = []
    pos_dict = get_position_dict()
    for key in pos_dict:
        positions.append(key)
        values.append(pos_dict[key]['entry'] * pos_dict[key]['position'])
    return positions, values
