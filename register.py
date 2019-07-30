print('------注册界面----------')

bank = {}
def register():
	username =input('输入用户名：')
	password = input('输入密码：')
	password1 =input('确认密码：')
	if username not in bank:
		if password == password1:
			bank[username]=[password,0]	
	else:
		print('用户已存在！请直接登录！')
