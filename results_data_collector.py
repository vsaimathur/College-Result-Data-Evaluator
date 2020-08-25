            #CODE TO RETRIVE ALL CLASSMATES RESULTS FROM VCE SITE

from selenium import webdriver
import time
import pandas as pd
browser = webdriver.Edge("msedgedriver.exe")
#time.sleep(10)
browser.get("https://sis.vce.ac.in/Results_BE_05022020/")
browser.set_page_load_timeout(10)
l_sgpa = []
l_cgpa = []
l_name = []
a1 = ["1602-18-735-00"+str(i) for i in range(1,10)]
a2 = ["1602-18-735-0"+str(i) for i in range(10,62)]
a3 = ["1602-18-735-30"+str(i) for i in range(1,10)]
a4 = ["1602-18-735-3"+str(i) for i in range(11,13)]     
a1.extend(a2)
a1.extend(a3)
a1.extend(a4)
for i in a1:
    browser.find_element_by_id("txtHTNO").clear()
    browser.find_element_by_id("txtHTNO").send_keys(i)
    browser.find_element_by_id("btnResults").click()
    browser.set_page_load_timeout(10) # wait for page to load for 10sec...
#    time.sleep(3)
    flag = False
    try:
        
        name = browser.find_element_by_id("lblStudName").text # name
        l_name.append(name+'\n')
    except:
        l_name.append("Discontinued...")
    try:
        result_sgpa = browser.find_element_by_id("lblSGPa").text # SGPA
    except:
        l_sgpa.append("not found")# not found(SGPA)...
        flag = True
    try:
        result_cgpa = browser.find_element_by_id("lblCGPA").text # CGPA
    except:
        l_cgpa.append("not found")# not found(CGPA)...
        flag = True
    if(not flag):
        try:
            l_sgpa.append(str(result_sgpa.split()[-1])+'\n') # found(SGPA).
        except:
            l_sgpa.append("failed") # failed(SGPA).
        try:
            l_cgpa.append(str(result_cgpa.split()[-1])+'\n') # found(CGPA).
        except:
            l_cgpa.append("failed") # failed(CGPA).
    else:
        pass
#    time.sleep(1)
    print(name, result_sgpa, result_cgpa)
browser.quit()
print(l_sgpa,len(l_sgpa))
print(l_cgpa,len(l_cgpa))
print(l_name,len(l_name))
dict_results = {"Name" : l_name, "Roll Number" : a1 , "SGPA" : l_sgpa, "CGPA" : l_cgpa}
results_data = pd.DataFrame(dict_results)
results_data.to_csv("results.csv")

