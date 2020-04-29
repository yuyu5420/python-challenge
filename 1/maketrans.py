import string
intab = string.ascii_lowercase
outtab = string.ascii_lowercase[2:]+"ab"
map = str.maketrans(intab, outtab)
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(s.translate(map))
s = "map"
print(s.translate(map))