import res= '我的电子邮件tom@gmail.com。 将什么发送到jerry123@163.com或者3123432@qq.com.若遇特殊情况打电话给182123445678.'
print(re.findall(r'[A-Za-z0-9]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+',s))
print(re.findall(r'1\d{11}',s))
