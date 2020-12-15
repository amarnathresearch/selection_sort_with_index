from datetime import datetime
def get_sorted_date_withindex(time_list, time_index_list):
    length = len(time_list)
    for i in range(length-1):
        for j in range(i+1, length):
            if datetime.strptime(time_list[i], "%Y-%m-%d\n%H:%M:%S") > datetime.strptime(time_list[j], "%Y-%m-%d\n%H:%M:%S"):
                tmp_object = time_list[i]
                time_list[i] = time_list[j]
                time_list[j] = tmp_object

                tmp_index = time_index_list[i]
                time_index_list[i] = time_index_list[j]
                time_index_list[j] = tmp_index


time_list = ['2019-11-03\n11:52:33', '2019-11-08\n12:13:22', '2019-11-03\n11:52:33', '2019-02-02\n10:11:06', '2019-10-01\n09:01:11', '2019-02-02\n10:11:06', '2020-09-11\n11:21:01']
time_index_list =  [999, 232, 344, 433, 555, 334, 545]

get_sorted_date_withindex(time_list, time_index_list)

print("time_list", time_list)
print("time_index_list", time_index_list)