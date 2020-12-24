"""
Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để lấy companyname.
"""

# import re
# emailAddress = input()
# pat = "(\W+)@((\W+\.)+(com))"
# re2 = re.match(pat, emailAddress)
# print(re2.group(2))
# Bài Python 59, Code by Quantrimang.com
import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2, emailAddress)
print (r2.group(2))
