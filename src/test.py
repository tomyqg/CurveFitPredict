from tools import myfunctool


#---------数列拟合并预测-------
print("---------数列拟合预测-------")
#下面是一个拟合斐波那契数列的例子
#斐波那契数列前19个数，并存在缺失值
x=[1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,None,6765]
#拟合斐波那契数列函数
info=myfunctool.find_logical(x,selectmode=2)#selectmode为1时表示使用多项式函数拟合，selectmode=2表示利用整合的函数拟合，selectmode=3表示自动判断二者拟合效果并给出拟合范围内最好的值，默认为3
print("用此公式求得原数列值:",myfunctool.func_general(info,list(range(1,len(info[-1])+1))),"  拟合得分:",info[-3])
#预测该斐波那契数列的之后的3个值 (真实值为:10946,17711,28657)
print("用此公式计算的后3个数列值:",myfunctool.func_general(info,[info[-1][-1]+1,info[-1][-1]+2,info[-1][-1]+3]))
#预测该斐波那契数列中的缺失值 (真实值为:4181)
print("用此公式预测缺失值:",myfunctool.func_general(info,[info[-1][-1]-1]))
print("预测函数公式为:",myfunctool.get_func(info))
# print("拟合的r2分数：",myfunctool.get_model_r2score(info))#r2暂时只能评判不存在缺失值的函数
#显示斐波那契数列拟合函数和真实值对比，展示预测函数x从1到比原数列预测多一个的值
myfunctool.show_func(info,1,len(info[-1])+1)


#---------曲线拟合并预测-------
#随便想一个函数,例如:y=4x^2+3x,并给出任意对应的x和y的值
print("---------曲线拟合预测-------")
x=[0,1,2,3,4]
y=[0, 7, 22, 45, 76]
#曲线拟合
info=myfunctool.auto_func(x,y)
print("原值为:",info[-2])
print("用此公式求得原值:",myfunctool.func_general(info,info[-1]),"  拟合曲线函数得分：",info[-3])
print("x=5时，函数的预测值:",myfunctool.func_general(info,[5]))
print("预测拟合曲线函数为:",myfunctool.get_func(info))
print("r2分数：",myfunctool.get_model_r2score(info))
#显示x=0-6时的预测函数和真实值的对比图
myfunctool.show_func(info,0,6)




