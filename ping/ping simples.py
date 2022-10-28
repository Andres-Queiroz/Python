import os
ip = input("ip ou host a ser verificado: ")
os.system('ping  -c 6 {}'.format(ip))
print("-"*70)
