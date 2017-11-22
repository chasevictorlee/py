#原码转换为真值
def trueform2truevalue(trueform):
    sign = '+'
    dec = 0
    exp = 0
    if trueform[0] == '1':
        sign = '-'
    for i in trueform[-1:0:-1]:
        dec += eval(i)*2**exp
        exp += 1
        
    return sign + str(dec)


#补码转换为真值的第一种方法
#教材上的方法
def complement2truevalue1(complement):
    #补码00000000的真值是+0或-0
    count = 0
    for i in complement:
        if i != '0':
            break    
        count += 1
    if count == len(complement):
        return '+0 or -0'

    #正数的补码和原码一样   
    if complement[0] == '0':
        return trueform2truevalue(complement)
    
    #10000000特殊处理
    count = 1
    for i in complement[1:]:
        if i != '0':
            break
        count += 1
    if count == len(complement):
        return '-' + str(2**(count-1))
    
    #处理剩余补码：将包括符号位在内的所有位取反再加一，得到绝对值，最后开头加上负号
    #这样可以处理类似10000000的补码
    anti = '1'
    for i in complement[1:]:
        if i == '0':
            anti += '1'
        else:
            anti += '0'
            
    return str(int(trueform2truevalue(anti)) - 1)


#补码转换为真值的第二种方法
#教材上的方法改进
def complement2truevalue2(complement):
    #补码00000000的真值是+0或-0
    count = 0
    for i in complement:
        count += 1
        if i != '0':
            break    
    if count == len(complement):
        return '+0 or -0'

    #正数的补码和原码一样   
    if complement[0] == '0':
        return trueform2truevalue(complement)
    
    #负数处理：将包括符号位在内的所有位取反再加一，得到绝对值，最后开头加上负号
    #这样可以处理类似10000000的补码
    anti = ''
    for i in complement:
        if i == '0':
            anti += '1'
        else:
            anti += '0'
            
    return '-' + str(int(trueform2truevalue(anti)) + 1)


#补码转换为真值的第三种方法
#根据cs:app给出的补码定义
def complement2truevalue3(complement):
    dec = 0
    exp = 0

    #除最高位的剩余位权值是2**exp
    for i in complement[-1:0:-1]:
        dec += eval(i)*2**exp
        exp += 1

    #最高位的权值是-2**exp
    dec += -2**exp*eval(complement[0])
    
    #纯粹是将int型转换为str型
    if dec == 0:
        return '+0 or -0' 
    elif dec > 0:
        return '+' + str(dec)
    else:
        return str(dec)


#补码转换为真值的第四种方法
#根据数字逻辑给出的求补码方法
#补码本质
def complement2truevalue4(complement):
    #补码00000000的真值是+0或-0
    count = 0
    for i in complement:
        count += 1
        if i != '0':
            break    
    if count == len(complement):
        return '+0 or -0'

    #正数的补码和原码一样   
    if complement[0] == '0':
        return trueform2truevalue(complement)
    
    #补码1000 0000的真值等于无符号数100000000减去无符号数10000000的差的负数
    #补码1000 0001的真值等于无符号数100000000减去无符号数10000001的差的负数
    #etc
    return '-' + str((2**len(complement)-int(trueform2truevalue('0'+complement))))
    

#真值转换为原码
def truevalue2trueform(truevalue, length):
    #判断真值是否超过范围
    #原码表示的范围是[-(2**(length-1)-1), 2**(length-1)-1]
    num = eval(truevalue[1:]) #真值的绝对值
    if num > 2**(length-1)-1:
        return 'Overflow'
    
    #最高值为符号位
    #正数符号位是0，负数符号位是1
    if truevalue[0] == '+':
        sign = '0'
    else:
        sign = '1'

    #将真值的绝对值转换为二进制无符号数
    trueform = ''
    trueform += str(num%2)
    q = num // 2    
    while q != 0:
        trueform += str(q%2)
        q //= 2
    trueform = trueform[::-1]
    
    #补全0
    while len(trueform) != length-1:
        trueform = '0' + trueform
    
    #最后在二进制无符号数前面加上符号位，返回二进制有符号数，即原码
    return sign + trueform


#真值转换为补码
#教材上的方法
def truevalue2complement1(truevalue, length):
    #正数和+0的原码和补码相同
    if truevalue[0] == '+':
        return truevalue2trueform(truevalue, length)
                
    num = eval(truevalue[1:]) #真值的绝对值
    
    #补码表示的范围是[-(2**(length-1)), 2**(length-1)-1]
    if num > 2**(length-1):
        return 'Overflow'
    
    #-128的补码是10000000
    if num == 2**(length-1):
        return '1' + '0'*(length-1)
    
    #-0的补码是00000000
    if num == 0:
        return '0'*length
    
    #得原码
    trueform = truevalue2trueform(truevalue, length)
    
    #除符号位的剩余位取反，得反码
    ones_complement = '1'
    for i in trueform[1:]:
        if i == '0':
            ones_complement += '1'
        else:
            ones_complement += '0'

    #加1，得补码
    addone = truevalue2trueform('+'+str(int(trueform2truevalue('0'+ones_complement))+1),length+1)[1:]
       
    return addone


#真值转换为补码的第二种方法
#教材上的方法改进
def truevalue2complement2(truevalue, length):
    #正数和+0的原码和补码相同
    if truevalue[0] == '+':
        return truevalue2trueform(truevalue, length)
                
    num = eval(truevalue[1:]) #真值的绝对值
    
    #补码表示的范围是[-(2**(length-1)), 2**(length-1)-1]
    if num > 2**(length-1):
        return 'Overflow'
    
    #求负数对应的无符号数，相当于其相反数有符号数
    anti_truevalue = '+' + str(num)
    
    #得原码
    trueform = truevalue2trueform(anti_truevalue, length+2)
    
    #将包括符号位在内的所有位取反
    #这样可以处理-128和-0的补码
    anti_trueform = '00'
    for i in trueform[2:]:
        if i == '0':
            anti_trueform += '1'
        else:
            anti_trueform += '0'

    #加1，得补码
    addone = truevalue2trueform('+'+str(int(trueform2truevalue(anti_trueform))+1),length+2)[2:]
       
    return addone


#真值转换为补码的第三种方法
#补码本质
def truevalue2complement3(truevalue, length):
    #正数和+0的原码和补码相同
    if truevalue[0] == '+':
        return truevalue2trueform(truevalue, length)
                
    num = eval(truevalue[1:]) #真值的绝对值
     
    #-0的补码是00000000
    if num == 0:
        return '0'*length
    
    #补码表示的范围是[-(2**(length-1)), 2**(length-1)-1]
    if num > 2**(length-1):
        return 'Overflow'
    
    #-128的补码是其相反数的补数无符号数256-128=128的二进制表示
    #-127的补码是其相反数的补数无符号数256-127=129的二进制表示
    #etc
    
    #求补数
    complement_truevalue = '+' + str(2**length-num)
    
    trueform = truevalue2trueform(complement_truevalue, length+1)
    
    return trueform[1:]



s = ['01101110', '10001101', '01011001', '11001110']
for i in s:
    print(trueform2truevalue(i))
    print(complement2truevalue1(i))
    print(complement2truevalue2(i))
    print(complement2truevalue3(i))
    print(complement2truevalue4(i))
    
print('='*20)

s = ["+23", "+43", "-40", "-63"]
for i in s:
    print(truevalue2trueform(i, 8))
    print(truevalue2complement1(i, 8)) 
    print(truevalue2complement2(i, 8))
    print(truevalue2complement3(i, 8))
    
print('='*20)

s = ['00001110', '11111111', '10000000', '10000001']
for i in s:
    print(trueform2truevalue(i))
    print(complement2truevalue1(i))
    print(complement2truevalue2(i))
    print(complement2truevalue3(i))
    print(complement2truevalue4(i))

print('='*20)

s = ['00000000', '10000000']
for i in s:
    print(trueform2truevalue(i))
    print(complement2truevalue1(i))
    print(complement2truevalue2(i))
    print(complement2truevalue3(i))
    print(complement2truevalue4(i))
    
print('='*20)

s = ["+0", "-0", "-128"]
for i in s:
    print(truevalue2trueform(i, 8))
    print(truevalue2complement1(i, 8)) 
    print(truevalue2complement2(i, 8))
    print(truevalue2complement3(i, 8))
