import datetime
import sys

def fill_arr(test):
    lines = []
    with open(test) as f:
        lines = f.readlines()
    return lines

def append_id(arr):
    id_list_log = []
    sub_arr = []
    temp = 0

    for i in range(len(arr)):
        curent_string = arr[i]

        find_time = curent_string.find("2021-03-16")
        i_of_ID = arr[i].find("\"LogonId: ");

        hour = int(curent_string[find_time + 11: find_time + 13])
        min = int(curent_string[find_time + 14: find_time + 16])


        sub_arr = arr[i]
        if(i_of_ID > 0):
            if(arr[i].find("Successful logon") > 0):
                print("LOG ON-----------------")
                print(sub_arr[i_of_ID+10:i_of_ID+18])
                print(hour, ":", min)
                print("-----------------------")

            if(arr[i].find("An account was logged off") > 0):
                print("LOG OFF----------------")
                print(sub_arr[i_of_ID+10:i_of_ID+18])
                print(hour, ":", min)
                print("-----------------------")

    return id_list_log

def main():
    # 0X372091
    if(len(sys.argv) < 2):
        print("USAGE python3 main.py ip")
        exit()

    ip = str(sys.argv[1])
    txt = fill_arr("test.txt")
    new_arr = []
    logon_arr = []
    logout_arr = []

    for i in range(len(txt)):
        if(txt[i].find(ip) > 0):
            new_arr.append(txt[i])

    logon_arr = append_id(new_arr)

main()
