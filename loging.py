print("------登录界面------")

Bank = {}

def log_ing():
	while True:
		count = 1		
		username = input("请输入用户名:")
		passwd = input("请输入密码:")
		passwd2 = int(input("请再次输入密码:"))



		if 6>len(username)>0 and isinstance(passwd,int):
			if passwd2 == passwd:		
				bank[username] = passwd
				print("登陆成功!")
				break
		
			else:
				print("用户密码输入错误!")
				conut+=1
				if count >3:
				print("密码输入错误3次,卡被锁定,请拿着身份证到柜台办理!")

		else:
			print("用户或者密码输入有误!")

log_ing()








