import numpy as np
#import matplotlib.pyplot as plt
from hello import module_portfilio
import json
# Trường hợp n = 2 thì corr khi nhập vào không cần cho vào mảng vd corr12 = 0.3

# mean = [20, 22, 24]
# stdev = [4, 5, 4]
# corr = [0.3, 0.3, -0.1]
# w = np.arange(-0.5, 1.51, 0.01)

# trả về một tuple() các array mean12, mean13, mean23


def listMeanAndStdev(mean, stdev, corr, wFrom, wTo):
    n = len(mean)
    w = np.round((np.arange(wFrom, wTo, 0.01)), 2).tolist()
    ar_mean = module_portfilio.portfolio(
        n, mean, stdev, corr, w).compution_mean()
    ar_stdev = module_portfilio.portfolio(
        n, mean, stdev, corr, w).compution_stdev()
    minimum_std, mean_mini_std = module_portfilio.portfolio(n, mean, stdev, corr, w).minimum_risk()
    std_f, mean_f = module_portfilio.portfolio(n, mean, stdev, corr, w).frontier_eff()
    M = module_portfilio.portfolio(n, mean, stdev, corr, w).point_M()
    std_cml, mean_cml = module_portfilio.portfolio(n, mean, stdev, corr, w).CML()
    dataTitle = ['W']
    dataTitle.append('std_f')
    dataTitle.append('mean_f')
    dataTitle.append('M')
    dataTitle.append('std_cml')
    dataTitle.append('mean_cml')
    dataTitle.append('minimum_std')
    dataTitle.append('mean_mini_std')
 
    for i in range(1, n):  
        for j in range(i+1, n+1):
            dataTitle.append('mean' + str(i) + str(j))
            dataTitle.append('stdev' + str(i) + str(j))
 
    rows = []
    rows.extend([w,std_f, mean_f, M, std_cml.tolist(), mean_cml, [minimum_std], [mean_mini_std.tolist()]])

     
    """
    for i in range(len(ar_mean)): 
        rowsMeanStd.extend([ar_mean[i]])
        rowsMeanStd.extend([ar_stdev[i]])  
        
    rows.extend([rowsMeanStd])
    """
    rowTest = []
    for r in range(len(ar_mean[0])): 
        row = [w[r], ]  
        for i in range(len(ar_mean)): 
            row.append(ar_mean[i][r])
            row.append(ar_stdev[i][r])  
        #rows.append(row)
        rowTest.append(row)


    rows.extend([rowTest])
     

    
    rows = [dataTitle] + rows
    return rows


def formatDataJson(data):
    jsonData = json.loads(json.dumps(data))
    return jsonData
