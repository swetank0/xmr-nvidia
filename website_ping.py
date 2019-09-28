import os,time
while True :
    os.system("hping3 -c 1 www.google.com -S -V -p 443 ") # 80
    time.sleep(2) #
    os.system("hping3 -c 1 www.google.com -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.facebook.com -S -V -p 443 ") # 80
    time.sleep(2) #
    os.system("hping3 -c 1 www.facebook.com -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.twitter.com -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.twitter.com -S -V -p 443 ") # 80
    time.sleep(2) #
    os.system("hping3 -c 1 www.instagram.com -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.python.com -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.linux.org -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.kaggle.com -S -V -p 443 ") # 443
    time.sleep(1)
    os.system("hping3 -c 1 www.tensorflow.org -S -V -p 443 ") # 443
    time.sleep(1)
    os.system("hping3 -c 1 pandas.pydata.org -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 scikit-learn.org -S -V -p 443 ") # 443
    time.sleep(2) #
    os.system("hping3 -c 1 www.scipy.org -S -V -p 443 ") # 443 
    time.sleep(1)
