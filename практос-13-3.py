import math
def calculator():
    symbol=('*',"-","+",'/','sqrt','1','2','3','4','5','6','7','8','9','0','(',')')
    print(symbol)
    f=open("log.txt",'r+')
    task=input("Введите выражение: ")

    for i in task:
        if i not in symbol:
            f.write("ERROR")
            raise print("ERROR")

    f.close()
    result=0

    for i in task:
        if i == '*':
            a=task[task.index(i)+1:]
            b=task[:task.index(i)]
            result=int(a)*int(b)
            print(task,'=',result)
        elif i =='/':
            a=task[task.index(i)+1:]
            b=task[:task.index(i)]
            result=int(b)/int(a)
            print(task,'=',result)
        elif i =='+':
            a=task[task.index(i)+1:]                
            b=task[:task.index(i)]
            result=int(a)+int(b)
            print(task,'=',result)
        elif i =='-':
            a=task[task.index(i)+1:]
            b=task[:task.index(i)]
            result=int(b)-int(a)
            print(task,'=',result)
        elif 'sqrt' in task:
            i=task.find('(')
            b=task.find(')')
            a=int(task[i+1:b])
            result=math.sqrt(a)
            print(task,'=',result)
            break
    testEnd=input("Желаете продолжить ? (x/n): ")
    if testEnd=="x":
        calculator()
    else:
        print("До свидания!")
calculator()