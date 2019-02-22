#!/usr/bin/python
# -*- coding: UTF-8 -*-

class IOStruct:
    """
    外设模块的IO结构
    """

    def __init__(self, Remap, Mode, Pin, Group):
        IOStruct.__IOStruct_Remap = Remap
        IOStruct.__IOStruct_Mode = Mode
        IOStruct.__IOStruct_Pin = Pin
        IOStruct.__IOStruct_Group = Group
 
    def SetIOStructRemap(self, Remap):
        if Remap >= 0 and Remap <= 3:
            IOStruct.__IOStruct_Remap = Remap
        else:
            pass
            # TODO:抛出异常


    def GetIOStructRemap(self):
        return IOStruct.__IOStruct_Remap

    def SetIOStructMode(self, Mode):
        IOStruct.__IOStruct_Mode = Mode

    def GetIOStructMode(self):
        return IOStruct.__IOStruct_Mode

    def SetIOStructPin(self, Pin):
        IOStruct.__IOStruct_Pin = Pin

    def GetIOStructPin(self):
        return IOStruct.__IOStruct_Pin

    def SetIOStructGroup(self, Group):
        IOStruct.__IOStruct_Group = Group

    def GetIOStructGroup(self):
        return IOStruct.__IOStruct_Group

    def GetStruct(self):
        return IOStruct.__IOStruct_Remap, IOStruct.__IOStruct_Mode, IOStruct.__IOStruct_Pin, IOStruct.__IOStruct_Group

def test():
    print(IOStruct.__doc__)
    test = IOStruct(1, "OutPut", 2, "A")
    print(test.GetStruct())
    test.SetIOStructRemap(3)
    print(test.GetStruct())
    # print(IOStruct.__dict__)
    # # 可以随便增加类中的变量？？？
    # IOStruct.age = 1
    # print(IOStruct.age)
    # print(IOStruct.__dict__)

