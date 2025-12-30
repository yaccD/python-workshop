import sys
import base64

print(f"Scrip name:{sys.argv[0]}")

print(sys.argv[0:2])

if len(sys.argv)>2:
    print("Arguments passed:")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"  Arguments{i+1}:{arg}")
    
    f_name = sys.argv[1]
    outf_name = sys.argv[2]
else:
    print("No Arguments passed.")
    f_name = input("image file name?")
    outf_name=inpurt("base64 file name?")

f=open(f_name,'rb')

ls_f=base64.b64encode(f.read())

f.close()

out_file=open(outf_name,'w',encoding='utf-8')
try:
    out_file.write(f"{ls_f}")
finally:
    out_file.close()


print(ls_f[:100],'......')

