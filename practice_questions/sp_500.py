fname = 'SP500.txt'
with open(fname, 'r') as f:
    lines = f.readlines()
    closing_prices = []
    long_term_interest = []
    for lin in lines[1:]:
        date = lin.strip().split(',')[0].split('/')
        
        # assign date values
        # Todo: Date values needs improvement
        for i in range(len(date)):
            
        
            #print(date[i])
            if i == 0:
                month = int(date[0])
            elif i == 2:
                
                year = int(date[2])
        # print("month: ", month)
        # print("year: ", year)
        # if (month >= 6 and year >= 2016) and  (year <= 2017 and month <=5):
        if (month >= 6 and year == 2016) or (year == 2017 and month <= 5):
           
            row = lin.split(',')
            closing_prices.append(row[1])
            long_term_interest.append(row[5])
        
    # print(month)
    # print(year)
    # print('closing_prices: ', closing_prices)
    # print('long_term_interest: ', long_term_interest)
    sum_cp = 0  
    for num in closing_prices:
        sum_cp += float(num)
    mean_SP = sum_cp / len(closing_prices)
    print(mean_SP)
    max_interest = float(max(long_term_interest))
    print(float(max_interest))
    
    
    
        
        