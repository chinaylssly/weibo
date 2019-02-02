# -*- coding: utf-8 -*-
 
s="https:\/\/passport.weibo.com\/wbsso\/login?ticket=ST-MjA5Njg2ODk0Nw%3D%3D-1533199834-gz-44B2CB23E3031788CBB230E15E6282B3-1&ssosavestate=1564735834","https:\/\/passport.97973.com\/sso\/crossdomain?action=login&savestate=1564735834","https:\/\/passport.krcom.cn\/sso\/crossdomain?service=krvideo&savestate=1&ticket=ST-MjA5Njg2ODk0Nw%3D%3D-1533199834-gz-5B08D7865C9FB4D28F51FECECBDBF2C0-1&ssosavestate=1564735834"
print 
for i in s:
    print i.replace(r'\/','/')


ss="\u9a8c\u8bc1ticket\u5931\u8d25"

print ss.decode('unicode-escape')