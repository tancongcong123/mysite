#-*- coding:utf-8 -*-
#运行脚本 输入操作类型 add=0, del=1, modify=2, quit=3
#0 添加用户 需输入用户名 电话
#1 删除用户 需输入用户名 判断是否存在
#2 修改用户 需输入用户名 电话 判断是否存在 存在即修改
#3 退出脚本
import pickle as p
import sys

class WrongInputException(Exception):
	"""docstring for ClassName"""
	def __init__(self, errorinfo):
		super(WrongInputException, self).__init__()
		self.errorinfo = errorinfo
	def __str__(self):
		return self.errorinfo
		
class Members(object):
	"""docstring for Members"""
	def __init__(self, name, phone):
		super(Members, self).__init__()
		self.name = name
		self.phone = phone

	def getMember(self):
		return ("%s's phone is %s" % (self.name, self.phone))

members = {}

def addMember(name, phone):
	global members
	members[name] = Members(name, phone)
	saveMember()
	operate()

def delMember(name):
	global members
	if name in members:
		del members[name]
		saveMember()
	else:
		print("%s is not exist" % name)	
	operate()

def modifyMember(name, phone):
	global members
	if name in members:
		addMember(name, phone)
	else:
		print("%s is not exist" % name)	
	operate()

def saveMember():
	global members
	f = open('membersfile','wb')
	p.dump(members, f)
	f.close()

def readMember():
	global members
	f = open('membersfile','rb')
	members = p.load(f)	
	f.close()
	for key in members:
		print('key==',key)
		print(members[key].getMember())

def operate():
	readMember()
	try:
		op = input('enter operation type(add=0, del=1, modify=2, quit=3)->')
		if op=='0':
			inputName = input('enter name->')
			if inputName is None:
				inputName = input('enter name->')

			inputPhone = input('enter phone->')
			if inputName is None:
				inputPhone = input('enter phone->')
			else:
				addMember(inputName, inputPhone)
		elif op=='1':
			inputName = input('enter delete name->')
			if inputName is None:
				inputName = input('enter delete name->')
			delMember(inputName)
		elif op=='2':
			inputName = input('enter mofidy name->')
			if inputName is None:
				inputName = input('enter mofidy name->')

			inputPhone = input('enter mofidy phone->')
			if inputName is None:
				inputPhone = input('enter mofidy phone->')
			else:
				modifyMember(inputName, inputPhone)	
		elif op=='3':
			quit		
		else:
			raise WrongInputException('WrongInputException:enter operation type(add=0, del=1, modify=2, quit=3)')						
	except WrongInputException as e:
		print(e)
		operate()
	else:
		pass
	finally:
		pass

operate()

	



