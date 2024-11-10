# # format 用法
# year ="龙"
# name ="房老师"
# message ="""
# 金{0}贺岁,欢乐祥瑞。
# 金{0}敲门,五福临门。
# 给{1}及家人拜年啦！
# 新春快乐，{0}年大吉！
# """.format(year,name)
# print(message)

# # second practice
# def calculate_bmi(weight, height):
#     bmi = weight/(height**2)
#     if bmi <= 18.5:
#         print('您的BMI分类为:偏瘦')
#     elif 18.5< bmi <= 25:
#         print('您的BMI分类为:正常')
#     elif 25 < bmi <=30:
#         print('您的BMI分类为:偏胖')
#     else:
#         print('您的BMI分类为:肥胖')
#
# weight,height = list(map(float,input().split()))
# calculate_bmi(weight,height)

#import json
# class CuteCat:
#     # 定义猫咪的属性
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     # 定义猫咪的speak方法
#     def speak(self):
#         print(f"我的名字叫{self.name}，我会喵喵叫！")
#
#     # 定义猫咪的hunt方法
#     def hunt(self):
#         print(f"我抓过{self.age}只老鼠！")
#
# # 类实例化为对象
# cat1 = CuteCat(name="小白", age=1, color="白色")
# cat1.speak()
# cat1.hunt()
#
# cat2 = CuteCat(name="大黄", age=2, color="黄色")
# cat2.speak()
# cat2.hunt()

# class pratice three
# class Student:
#     def __init__(self,name,stuid,chinese=0,math=0,english=0):
#         self.name = name
#         self.stuid = stuid
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#     def setgrade(self,chinese=0,math=0,english=0):
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#     def outgrade(self):
#         print(f"""{self.name}的成绩是:
#                 语文:{self.chinese}
#                 数学:{self.math}
#                 英语:{self.english} """)
# stu1 = Student('小明','2023312620')
# print(stu1)
# stu1.setgrade(119,129,137)
# stu1.outgrade()

#streamlit 入门
import streamlit as st
from streamlit import text_area

#添加一个标题
st.title('吴佳沅的个人空间')

#添加水平分割线
st.divider()
#添加一些文本,可以使用markdown,###表示三级标题
st.write('### 高中:深圳中学')
st.write('学校图片')

# 添加一个图片
image_file = 'shenzhong.jpg'
st.image(image_file,caption='shenzhen middle school')

#Markdown格式，***表示加粗和斜体
st.write('很好的学校')

#添加组件

#文本输入
name = st.text_input("请输入你的名字:")
if name:
    st.write(f"你好，{name}!")
password = st.text_input("请输入你的密码:",type='password')

#数字输入
age = st.number_input("请输入你的年龄:", min_value=0, max_value=120, step=1)
#长文本输入
text_area = st.text_area("请输入一段你的简介： ")
st.divider()
checked = st.checkbox("我同意以上条款")
if checked:
    st.write("感谢支持！")
# 按钮
if st.button("提交"):
    st.write("感谢提交")
