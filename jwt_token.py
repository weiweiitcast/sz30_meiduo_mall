

import json,base64
import hmac,hashlib

# 模拟jwt签发流程

# 头信息
header = {
  'typ': 'JWT',
  'alg': 'HS256' # 哈希运算(散列运算,不可逆)
}
header = json.dumps(header) # string
header = base64.b64encode(header.encode())
print("header: ", header)

# 载荷信息
payload = {
  "sub": "1234567890",
  "name": "John Doe",
  "admin": True,
  "age": 20
}
payload = json.dumps(payload) # string
payload = base64.b64encode(payload.encode())
print("payload: ", payload)

# 生成签名
msg = header + b'.' + payload
SECRET_KEY = b'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='

hash_obj = hmac.new(SECRET_KEY, msg=msg, digestmod=hashlib.sha256)
signature = hash_obj.hexdigest()
print("signature: ", signature)

# 模拟后台签发好token值发送给浏览器
JWT_TOKEN = header.decode() + '.' + payload.decode() + '.' + signature
print("JWT_TOKEN: ", JWT_TOKEN)



# 模拟jwt校验流程

# 模拟未篡改
jwt_token_from_browser = JWT_TOKEN
# 模拟被篡改
# jwt_token_from_browser = "fewfewfewf" + JWT_TOKEN

# 1、提取header、payload、signature
header = jwt_token_from_browser.split('.')[0]
payload = jwt_token_from_browser.split('.')[1]
signature = jwt_token_from_browser.split('.')[2]

# 2、校验是否篡改（对信息重复哈希，对比签名是否一致）
msg = header + '.' + payload
new_signature = hmac.new(SECRET_KEY, msg.encode(), digestmod=hashlib.sha256).hexdigest()

# if new_signature == signature:
if hmac.compare_digest(new_signature, signature):
    print("数据完整！")

    payload = base64.b64decode(payload) # b"{'name':'weiwei'}"
    payload = json.loads(payload.decode()) # {'name':'weiwei'}
    print(payload)

else:
    print("数据被篡改了")
















