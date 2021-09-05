#'aaa john @hello . comz \na xyz at game dot com sdffsd\n121@2121-121.com\n656-546-45645 565-4645-6456\n656,656 565, 65, '
#[('email', 'john@hello.comz'), ('email', 'xyz@game.com'), ('email', '121@2121-121.com'), ('digit', 6565464564556546456456), ('digit', 65665656565)])
#'aaa joHn\nat\n world dot\t Com \na xyz'
str6 = 'aaa john @hello . comz \na xyz at game dot com sdffsd\n121@2121-121.com\n656-546-45645 565-4645-6456\n656,656 565, 65, '
str1='aaa joHn\nat\n world dot\t Com \na xyz'
str2='aaa joE @ hello . Com \na xyz'
str3='aaa sHin\n@ hello .\t Com \na xyz'
str4 ='aaa 121 at 2121-121 . inf a xyz'
str5 ='aaa joHn\nat\n world dot\t Com \na xyz'

def extractEmailNumbers(str):
    count = str.count('\n')
    strSeg = str.split('\n')
    countAt = strSeg.count('at')
    #print('strSeg: ', strSeg, '\\n', count, 'at',countAt)
    atMail = ''

    if count > 0 and countAt == 0:
        eList=[]
        for item in strSeg:
            indexItem = strSeg.index(item)
         #   print(item, indexItem)
            emailF = ''
            indexSig = item.find('@')
            indexAt = item.find('at')
            if indexSig >=0:
                Aitem = item.split('@')
                #print('aitem: ',Aitem)
                if Aitem[0] != '':
                    aI = Aitem[0].find(' ')
                    #print('ai: ',aI)
                    bAt = Aitem[0][aI+1:].strip().lower()
                    emailF+=bAt+'@'
                    aJ = Aitem[1].replace(' ','')
                    eList.append(emailF+aJ)
                if Aitem[0] == '':
                    aItem = strSeg[indexItem-1].strip().lower().split()
                    #print('aitem2:',aItem)
                    bAt = aItem[1]+'@'+Aitem[1].strip().lower().replace(' ','').replace('\t','')
                    eList.append(bAt)

            if indexAt >0:
                #print(item)
                atItem = item.split('at')
                sI = atItem[0].find(' ')
                bAt = atItem[0][sI+1:].strip().lower()
                emailF+=bAt+'@'
                dItem = atItem[1].split(' ')

                for di in dItem:
                    if di == 'dot':
                        index = dItem.index(di)
                        emailF += dItem[index -1].strip().lower()+'.'+dItem[index+1].strip().lower()
                        #print(emailF)
                eList.append(emailF)
        return eList
    if countAt == 1:
        #print('strSeg')
        for item in strSeg:
            i = strSeg.index(item)
         #   print('item:',item,i)
            if item == 'at':
                preItem = strSeg[i-1].strip().lower()
                #print(preItem)
                index = preItem.find(' ')
                if index > 0:
                    beforeAt = preItem[index+1:]
                    #print(beforeAt+'@')
                    atMail+=beforeAt+'@'
                else:
                    atMail+=preItem
            if item.rfind('dot')>0:
                bDot1 = item.split('dot')
                atMail+=bDot1[0].strip().lower()+'.'+bDot1[1].strip().lower()
        return atMail
    #print('Count: ',count)
    if count == 0:
        #print("Str:",str)
        indexAt = str.split('at')
        #print(indexAt)
        beForeAt = indexAt[0].strip().split(' ')
        length = len(beForeAt)
        beForeAt = beForeAt[length-1]
        #print(length, beForeAt)
        afterAt = indexAt[1].strip().split('.')
        if afterAt[0].strip().find(' ')<0:
            after = afterAt[0].strip()
        if afterAt[1].strip().find(' ')<0:
            #print(afterAt[1])
            a = afterAt[1]
        else:
            a = afterAt[1].strip().split(' ')
            #print(a[0])
        return beForeAt+'@'+after+'.'+a[0]

print(extractEmailNumbers(str1))
print(extractEmailNumbers(str2))
print(extractEmailNumbers(str3))

print(extractEmailNumbers(str4))
print(extractEmailNumbers(str5))
print(extractEmailNumbers(str6))
