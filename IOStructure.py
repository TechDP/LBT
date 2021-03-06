#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

class IOStruct(object):
    """
    外设模块的IO结构
    """

    def __init__(self):
        super().__init__()
        self.IOStruct_Remap = "Remap_1"
        self.IOStruct_Mode = "InputPullUp"
        self.IOStruct_Pin = "Pin_0"
        self.IOStruct_Group = "GPIOA"
 
    def SetIOStructRemap(self, Remap):
        if int(Remap[-1]) >= 0 and int(Remap[-1]) <= 3:
            self.IOStruct_Remap = Remap
        else:
            pass
            # TODO:抛出异常


    def GetIOStructRemap(self):
        return self.IOStruct_Remap

    def SetIOStructMode(self, Mode):
        self.IOStruct_Mode = Mode

    def GetIOStructMode(self):
        return self.IOStruct_Mode

    def SetIOStructPin(self, Pin):
        self.IOStruct_Pin = Pin

    def GetIOStructPin(self):
        return self.IOStruct_Pin

    def SetIOStructGroup(self, Group):
        self.IOStruct_Group = Group

    def GetIOStructGroup(self):
        return self.IOStruct_Group

    def GetIOStructData(self):
        self.IOStructData = {
            "IOGroup": self.IOStruct_Group, 
            "IOUsage": self.IOStruct_Mode, 
            "IOPin": self.IOStruct_Pin, 
            "IORemap": self.IOStruct_Remap
            }
        return self.IOStructData
        

if __name__ == "__main__":
    print(IOStruct.__doc__)
    test = IOStruct()
    test.SetIOStructRemap("Remap_0")
    test.SetIOStructGroup("GPIOA")
    test.SetIOStructMode("RX")
    test.SetIOStructPin("Pin_0")
    print(test.GetIOStructData())
    test.SetIOStructPin("Pin_1")
    test.SetIOStructMode("Tx")
    print(test.GetIOStructData())
    # print(IOStruct.__dict__)
    # # 可以随便增加类中的变量？？？
    # IOStruct.age = 1
    # print(IOStruct.age)
    # print(IOStruct.__dict__)
