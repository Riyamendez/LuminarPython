import re
f=open("/TEST_1/test1", "r")
f1=open("/TEST_1/EmailList", "w")
mailid=[]
for lines in f:
    employee = lines.rstrip("\n").split(",")
    email=employee[3]
    mailid.append(email)


for data in mailid:
    pattern='[a-zA-z]\w.*[_]*\w*[.]*@[a-z]*[.][a-z]{3}'
    match=re.fullmatch(pattern,data)

    if(match!=None):
        f1.write(data+"\n")
    else:
        print(mailid)
