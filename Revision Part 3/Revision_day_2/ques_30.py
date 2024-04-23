
# 30. stocks.csv contains stock price, earnings per share and book value. You are writing a stock market 
# application that will process this file and create a new file with financial metrics such as pe ratio and
# price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value

# Your input format (stocks.csv) is,

# Company Name	Price	Earnings Per Share	Book Value
# Reliance	    1467	    66	                s
# Tata Steel	391	        89	                572

# Output.csv should look like this,

# Company Name	PE Ratio	PB Ratio
# Reliance	      22.23	    2.25
# Tata Steel	      4.39	    0.68

with open('Revision_day_2//stocks.csv','r') as file:
    with open('Output.csv','w') as write_file:
        write_file.write('Company Name,PE Ratio,PB Ratio\n')
        next(file)
        for stock in file:
            values = stock.split(',')
            comp_name = values[0]
            price = float(values[1])
            eps = float(values[2])
            book = float(values[3])
            PE_Ratio = round(price/eps, 2)
            PB_Ratio = round(price/book, 2)
            write_file.write(f'{comp_name},{PE_Ratio},{PB_Ratio}\n')


