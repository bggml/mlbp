#C:\Python27\python.exe
# -*- coding: UTF-8 -*-
#################################命令接收
import argparse,time
parser = argparse.ArgumentParser()#创建解析器对象ArgumentParser
parser.add_argument('-u','--url',help=u'输入url地址',default='http://bgg8.ml/?id=*&dsa=1')
parser.add_argument('-i',help=u'输入需要多少线程',default=10)
parser.add_argument('-m',help=u'爆破的目录文件 .txt',default='1.txt')
parser.add_argument('-b',help=u'保存文件 扫描目录.txt',default=u'已爆破目录.txt')
parser.add_argument('-c','--code',nargs="+",help=u'状态码默认200 302，多填200 302',default=['200','302'])
args = parser.parse_args()
################################# #处理错误
import requests
try:
	requests.head(args.url,verify=False)
except IOError:
	print u'站出错误或输入url不正确'
	exit()
#################################  进度条 jdt
import sys                      #导入所需模块
def jdt(ii,q=0):
	# for i in range(101):
		i=q*100/ii
		b = u'-'*20
		b = i/5*u'>' + b[i/5:]
		a=u'  [%s]%s%%/100%%(%s)\r' % (b,i,ii)
		sys.stdout.write(a)
		sys.stdout.flush()
#jdt(10,2)
# jdt(总数,进度数)
#################################打开爆破目录的文件     dkwj  
def dkwj():
	try:
		fo=open(u'%s'%(args.m),'r') #打开文件
		ai=fo.read().split('\n')#分割文件内容
		return ai,len(ai)                   #返回分割内容的 列表
		# print ai                  #输出文件
	except IOError:
		print u'你的字典文件不存在,请检查后再尝试'
		quit()
# ml=dkwj()[1]                #文件名调用
# print len(ml)
# print ml
# ml=dkwj(args.m)               #命令调用
#################################    保存http文件     bcwj  
sa=[]
f1=open('%s'%(args.b),'w+') #保存文件
def bcwj():
	for mm in sa:
		f1.write(mm+'\n')          #保存url
	f1.close()
#################################                 判断状态码
def code(url,code):
	for c in xrange(len(args.code)):           #看状态码是否有
		if args.code[c]==code:           #判断网页状态码
			sa.append(url)               #添加字典
			p=args.code[c]+'    '+url+'                   \n'
			p1=p.decode('UTF-8')
			sys.stdout.write(p1)          #输出网站和状态码
			break 
			# sys.stdout.write(args.code[c])
	jdt(mm[1],i+1)         #返回进度条
			                               #退出for
# print len(args.code)
#################################                 发送http请求         http
import requests;            #导入http模块；
def http(url):
	try:
	 	r = requests.head(url,verify=False)      # 发送请求
		# print r.status_code      # 查看返回码
		code(url,str(r.status_code))    #给状态码判断
		# print url,r.status_code
		# return url,r.status_code    # 返回网页状态码和网页地址 
	except IOError:
		print u'被防火墙拦截或已经断网'
		sa.append('xxxxxxxxxxxxxxxxxxx         '+url)
	# q.get()
# y=http('http://www.baidu.com/')
# exit()
# print 232
#################################
import threading
def threa(url):
	t=threading.Thread(target=http,args=[url])
	t.start()# 开始
	# t.join()# 堵塞
################################# 队列
mm=dkwj()
for i in xrange(0,mm[1]):
	while 1:
		if len(threading.enumerate())!=args.i+1:
			if args.url.find('*'):
				url=args.url.replace('*',mm[0][i])
			else:
				url=args.url+mm[0][i]
			threa(url)
			break
		time.sleep(0.1)
time.sleep(1)
print  len(sa)
bcwj()                     #保存网站地址
