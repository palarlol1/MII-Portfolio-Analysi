import sqlite3
conn = sqlite3.connect('services/portfolio.db')
cursor = conn.cursor()
entryPrices = {
'AAPL':158.42,
'AAXN':24.36,
'AMZN':1365.13,
'BABA':180.16,
'DATA':77.77,
'DIS':105.33,
'DLR':103.65,
'FRC':70.46,
'GOOGL':914.41,
'LIND':9.95,
'LNG':45.61,
'LYV':33.50,
'SHOP':88.44,
'TOWN':33.23,
'ZTS':84.80,
'ALSN':45.90
}

positionSizes = {
          'AAPL':105,
          'AAXN':300,
          'AMZN':8,
          'BABA':95,
          'DATA':268,
          'DIS':311,
          'DLR':331,
          'FRC':415,
          'GOOGL':17,
          'LIND':1201,
          'LNG':393,
          'LYV':655,
          'SHOP':201,
          'TOWN':609,
          'ZTS':407,
          'ALSN':325
        }

symbols = ['AAPL','AAXN','AMZN',
'BABA','DIS','DLR','FRC','GOOGL','LIND','LNG','LYV',
'SHOP','TOWN','ZTS','ALSN']

for symbol in symbols:
    command = (
    '''
    INSERT INTO portfolio VALUES(?, ?, ?, ?)
    '''
    )
    cursor.execute(command, ('1-1-2019', symbol, entryPrices[symbol], positionSizes[symbol]))

conn.commit()