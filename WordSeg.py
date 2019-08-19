import time
import re #正則表達式

while True:
        try:
                Fileman = input("輸入檔案名稱(含副檔名.txt)：")
                Filead = open(Fileman, 'r')
                Filead = Filead.read()
                break
        except:
                print("指定的檔案找不到... 再試一次 !")

#單字詞, 以正則表達式清資料, 目前取11904-65400, 不包含\n(沒有符號的標題?)
Arr1=[]
Arr1 = re.findall(r"[⺀-ｸ]|\n",Filead)

click = time.time() #計時開始

def dida():
        return round(time.time() - click,1)

print("處理單字詞：", dida())

'''
for i in range(len(Arr)):
        #12288全形空格\u3000、10為換行符號\n、<126排除數字與字母等半形符號、>40917排除無法顯示的漢字
        if Arr[i] == "\u3000" or Arr[i] == "\n" or ord(Arr[i])<11904 or ord(Arr[i])>65400:
                continue
        else:
                Arr1.append(Arr[i])
'''

#正切
Arr2= [];Arr3= [];Arr4= []
for i in range(len(Arr1)):
        Arr2.append("".join(Arr1[i:i+2]))
        Arr3.append("".join(Arr1[i:i+3]))
        Arr4.append("".join(Arr1[i:i+4]))

print("切二至四字：", dida())

#計次矩陣、拿掉符號
No1=[];No2=[];No3=[];No4=[]
try:
        for i in range(len(Arr1)):
                if ord(Arr1[i]) >= 19968 and ord(Arr1[i]) <= 40869:
                        No1.append(Arr1.count(Arr1[i]))
                        if ord(Arr2[i][len(Arr2[i])-1:len(Arr2[i])]) >= 19968 and ord(Arr2[i][len(Arr2[i])-1:len(Arr2[i])]) <= 40869:
                                No2.append(Arr2.count(Arr2[i]))
                                if ord(Arr3[i][len(Arr3[i])-1:len(Arr3[i])]) >= 19968 and  ord(Arr3[i][len(Arr3[i])-1:len(Arr3[i])]) <= 40869:
                                        No3.append(Arr3.count(Arr3[i]))
                                        if ord(Arr4[i][len(Arr4[i])-1:len(Arr4[i])]) >= 19968 and  ord(Arr4[i][len(Arr4[i])-1:len(Arr4[i])]) <= 40869:
                                                No4.append(Arr4.count(Arr4[i]))
                                        else:
                                                No4.append(0)
                                else:
                                        No3.append(0)
                                        No4.append(0)
                        else:
                                No2.append(0)
                                No3.append(0)
                                No4.append(0)
                else:
                        No1.append(len(Arr1))
                        No2.append(0)
                        No3.append(0)
                        No4.append(0)
except Exception as e:
        print("Arr矩陣長度1-4:",len(Arr1),len(Arr2),len(Arr3),len(Arr4)) 
        print(e)
#not 同時判斷None、跟空集合[]

print("各矩陣計次：", dida())
#頻次理論(包含i的考量)，順序有差, 相同時取最後
Nm=[];Dm=[];Comprises=[];Freq=[];Ng={};k=0
try:
        for i in range(len(Arr1)):
                if k > 1:
                        k -= 1
                else:
                        if No1[i] == len(Arr1) or No1[i] == 1:
                                Ng = {No1[i]:100}
                        else:
                                if No2[i] > 1 and True:
                                        Ng.update({No2[i]:200,No2[i-1]:210})
                                        if No3[i] > 1 and True:
                                                Ng.update({No3[i]:300,No3[i-1]:310,No3[i-2]:320})
                                                if No4[i] > 1 and True:
                                                        Ng.update({No4[i]:400,No4[i-1]:410,No4[i-2]:420,No4[i-3]:430})
                                else:
                                        Ng = {No1[i]:100}
                        Nm.append(int((Ng.get(max(Ng))/100)%10)) #詞數編號
                        Dm.append(i - int(Ng.get(max(Ng))/10%10)+int(Ng.get(max(Ng))%10)) #位置編號
                        k = int((Ng.get(max(Ng))/100)%10)
                        Ng = {}
                #Comprises.append(eval('Arr'+str(Nm[i])+'['+str(Dm[i])+']')+'_'+str(Nm[i])+'_'+str(Dm[i]))
                #Freq.append(eval('No'+str(Nm[i])+'['+str(Dm[i])+']'))
except Exception as e:
        print("No矩陣長度1-4:",len(No1),len(No2),len(No3),len(No4))
        print(e)

print("選取字詞數：", dida())

#頻次理論(排除i的考量)

#刪除重複的
Nn={};Resulist=[]
Nn = dict(zip(Dm,Nm))
for i in Nn.keys():
        Resulist.append(eval('Arr'+str(Nn[i])+'['+str(i)+']'))       
#print(Comprises)

print("刪除重複詞：", dida())

'''垂直輸出字串'''
Standing = open("cut_"+Fileman, "w")
Standing.writelines("\n".join(Resulist))
Standing.close()
''''''
print("產出資料檔:", dida())
