file_name = open('amazon.txt','r+')
output = open("newfile.txt", "r+")
def get_monthly_averages(data_list):
    num = 1
    product = 0
    sum1 = 0
    monthly_averages_list = []
    a = ()
    for i in range(1, len(data_list)-2):
        check = data_list[num][0][0:-3]
        if data_list[i][0][0:-3] == check:            
            product = product + (int(data_list[i][5])*(float((data_list[i][6])))) 
            sum1 = sum1 + int(data_list[i][5])
        else:
            average = product / sum1
            a = a + (float("%.2f"%average),)
            a =  a + (check,)
            monthly_averages_list.append(a)
            a = ()
            product = 0
            sum1 = 0
            product = product + (int(data_list[i][5])*(float((data_list[i][6]))))            
            sum1 = sum1 + int(data_list[i][5])
            num = i
    return monthly_averages_list
def print_info(monthly_averages_list, filename):
    monthly_averages_list.sort()
    output.writelines('Amazon Stock from Jan 1, 2008 to Oct. 28, 2014'+'\n')
    output.writelines('Six Worst Months:'+'\n')
    output.writelines('Month   Average'+'\n')
    for i in range(6):
        output.writelines('%s %s'%(monthly_averages_list[i][1] , monthly_averages_list[i][0])+'\n')
    output.writelines('\n')
    output.writelines('Six Best Months:'+'\n')
    output.writelines('Month   Average'+'\n')
    for i in range(len(monthly_averages_list)-6, len(monthly_averages_list)):
        output.writelines('%s %s'%(monthly_averages_list[i][1], monthly_averages_list[i][0])+'\n')    
def get_data_list(file_name):
    data_list = []
    for line in file_name:
        data_list.append(line.split(','))
    return data_list
data_list = get_data_list(file_name)
monthly_averages_list = get_monthly_averages(data_list)
print_info(monthly_averages_list, file_name)