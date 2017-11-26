import string
rot11 = string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","LMNOPQRSTUVWXYZABCDEFGHIJKlmnopqrstuvwyxzabcdefghijk")
print string.translate("Ctktg vxkt je", rot11)
