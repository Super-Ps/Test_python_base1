#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2018/1/3


class SexOrgans(object):

    def __init__(self,gprs='下面',cloer='黑色',xingzhuang="长方形"):

        self.gprs = gprs
        self.cloer = cloer
        self.xingzhuang = xingzhuang



    def get_attre(self):
        #print(self.name)

        return print(str(self.gprs+self.cloer+self.xingzhuang))

    def get_sex_attrebu(self,man=None,woman=None):
        if man == '1':
            print("男性输入成功！")

            if woman == '2':

                print("女性输入成功！")
            else:
                print("女性必须输入1！")

        else:
            return print("请按套路来！")


# s= SexOrgans("xxx")
# #s.name ='jonny'
# s.get_attre()
# #s.get_sex_attrebu("1","2")





class Sexlove(SexOrgans):

    '''  子类调用父类的方法 super(子类，self).父类方法 '''
    def __init__(self,name,age):

        super(Sexlove,self).__init__(self,name,age)
        self.name = name
        self.age = age
        print("子类实例化对，初始化参数：%s" % self.name,self.age)

    def get_attre(self):

        super(Sexlove, self).get_sex_attrebu()
        print('重写子类方法：%s' % self.name,self.age+self.xingzhuang)



a=SexOrgans()
a.get_attre()

b=Sexlove("JONNY",11)


b.get_attre()
