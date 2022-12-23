message = '晚上好呀'

encode_message_gbk = message.encode('gbk')
encode_message_utf8 = message.encode('utf-8')

print(encode_message_gbk)
print(encode_message_utf8)

print(encode_message_gbk.decode('gbk'))
# print(encode_message_gbk.decode('utf-8'))
# print(encode_message_utf8.decode('gbk'))
