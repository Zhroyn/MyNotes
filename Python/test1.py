# 导入python资源包
from random import random
 
# 用户体验模块 
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
 
# 获得A和B的能力值与场次模块 
def getIntputs():
    a = eval(input("请输入A的能力值(0-1)："))
    b = eval(input("请输入B的能力值(0-1)："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n
 
# 模拟n局比赛模块 
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB
 
# 判断比赛结束条件 
def gameOver(a, b):
    return a == 15 or b == 15
 
# 模拟n次单局比赛=模拟n局比赛 
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB
 
# 打印结果模块 
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))
 
 
def main():
    printIntro()    
    probA, probB, n = getIntputs()                # 获得用户A、B能力值与比赛场次N
    winsA, winsB = simNGames(n, probA, probB)     # 获得A与B的场次
    printSummary(winsA, winsB)                    # 返回A与B的结果
 
 
main()