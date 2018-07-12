import math
# 本章主要介绍math模块中三角函数的应用，一般用于曲线绘制、沿弧线移动和旋转等操作

# 弧度和角度互相转换的公式分别是
math.degrees()
math.radians()

# 计算绕着一个圆的圆周的任意点的x坐标，使用余弦函数
X = math.cos(math.radians(90))
"{:.2f}".format(X)  # 格式化为2位小数
# 计算绕着一个圆的圆周的任意点的y坐标，使用正弦函数
Y = math.sin(math.radians(90))
# 综合起来，围绕圆的圆周上的任意一个点的坐标是
X = math.cos(math.radians(90)) * radius
Y = math.sin(math.radians(90)) * radius