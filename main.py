import marshal, base64
print('PYO\nPython Obfuscator\n\n')
tfile = 'template.py' if input("Put a try/except statement?\nThis can stop code leaking if an error happens in the compiler script (very rare unless the user is on the wrong python version)\nThis will also stop any errors in your pogram from being reported to the user\nNote that someone with basic python knowledge CAN get around this, but it wouldn't leak them the source code\n\nRecommended setting: No\n\nType T for yes, N for no: ").lower() == 't' else 'tempnoerror.py'
print('\n\n')
try:
    with open("input.py", 'r') as f:
        content = f.read()
        f.close()
    print("[1/5] Got content")
    with open(tfile, 'r') as f:
        temp = f.read()
        f.close()
        del f
    print("[2/5] Got template")
    cc = compile(content, "__PYO__obfuscated", 'exec')
    print("[3/5] Compiled code to binary")
    #exec(marshal.loads(base64.b85decode(base64.b85encode(marshal.dumps(cc)).decode('utf-8'))))
    with open("output.py", 'w') as f:
        res = temp.replace("__PYO__386x45152", base64.b85encode(marshal.dumps(cc)).decode('utf-8'))
        print("[4/5] Marshalled code object, encoded to base85, added to template")
        f.write("import base64 as b;exec(b.b64decode(\'__PYO__43170087\'))".replace("__PYO__43170087", base64.b64encode(res.encode('utf-8')).decode('utf-8')))
        print("[5/5] Encoded to base64, wrote to file")
        f.close()
except:
    print("\n\n[PYO] Failed to compile. Make sure your input code is valid")
else:
    print("\n\n[PYO] Compile finished. Result in output.py")