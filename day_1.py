import requests
import json
import urllib.request


## TRYING TO GET DATA FROM WEBSITE ###############
# # data = requests.get('https://adventofcode.com/2022/day/1/input')
# # print(data)

# # with urllib.request.urlopen('https://adventofcode.com/2022/day/1/', params = {'login':username, 'password':password}) as response:
# #     html = response.read()
# #     print(html)


# # create a password manager
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# # Add the username and password.
# # If we knew the realm, we could use it instead of None.
# top_level_url = 'https://adventofcode.com/2022/'
# password_mgr.add_password(None, top_level_url, username, password)

# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# # create "opener" (OpenerDirector instance)
# opener = urllib.request.build_opener(handler)

# # # use the opener to fetch a URL
# # opener.open('https://adventofcode.com/2022/day/1')

# # Install the opener.
# # Now all calls to urllib.request.urlopen use our opener.
# urllib.request.install_opener(opener)

# with opener.open('https://adventofcode.com/2022/day/1/input') as response:
#     html = response.read()
#     print(html)

def evaluateMax(lst):
    largest_sum = 0
    summed_val = 0
    for i in range(len(lst)):
        if lst[i] != '':
            summed_val += int(lst[i]) 
        if lst[i] == '':
            if summed_val > largest_sum:
                largest_sum = summed_val
                summed_val = 0
            else:
                summed_val = 0
    return largest_sum




def topThree(lst):
    largest_sum = 0
    summed_val = 0
    cal_list = []
    for i in range(len(lst)):
        if lst[i] != '':
            summed_val += int(lst[i]) 
        if lst[i] == '':
            cal_list.append(summed_val)
            summed_val = 0
    cal_list = sorted(cal_list)
    return cal_list[-1] + cal_list[-2] +cal_list[-3]
     


with open('data.txt', "r") as myfile:
    data = myfile.read().splitlines(True)
    print(data)
    # largest_sum = topThree(data)
    # print(largest_sum)
    