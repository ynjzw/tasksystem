import os,json

with open('user_study.json','r',encoding='utf8') as fp:
    json_data=json.load(fp)
    arr1=[]
    arr2=[]
    for list in json_data:
        if (list['user_id'] in arr1)==False:
            arr1.append(list['user_id'])

        if (list['course'] in arr2)==False:
            arr2.append(list['course'])


    arr1_num=len(arr1)
    arr2_num=len(arr2)

    print('文件中包含',arr1_num,'名用户，',arr2_num,'门课。')