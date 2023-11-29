from iced_x86 import *


# emojiFile = open('emojis.txt', encoding="utf8")
# disFile = open("disassembled_pairs.txt", "w+", encoding="utf-8")

# codeRIP = 0

# for emoji in emojiFile.readlines():
#     hexString = emoji.split()[0]
#     hexByteArray = bytes.fromhex(hexString)
#     decoder = Decoder(32, hexByteArray)
#     hasBad = False
#     code = ''
#     for instr in decoder:
#         start_index = instr.ip - codeRIP 
#         bytes_str = hexByteArray[start_index:start_index + instr.len].hex().upper()
#         if f'{instr:x}' == '(bad)':
#             hasBad = True
#             break
#         code += f'{bytes_str.lower():16} : {instr:x}\n'

#     if not hasBad:
#         disFile.write(f'\n{emoji}')
#         disFile.write(code)


# Pair of Emojis
# emojiFile = open('emojis.txt', encoding="utf8")
# disFile = open("disassembled_pairs_no_bad.txt", "w+", encoding="utf-8")
# instructions = open('instructions.txt', 'w+', encoding="utf-8")

# codeRIP = 0
# emojis = []

# for emoji in emojiFile.readlines():
#     emojis.append(emoji)

# for i in range(len(emojis)):
#     for j in range(len(emojis)):
#         if i == j:
#             continue
#         hexString = emojis[i].split()[0] + emojis[j].split()[0]
#         hexByteArray = bytes.fromhex(hexString)
#         decoder = Decoder(32, hexByteArray)
#         hasBad = False
#         code = ''
#         instrs = ''
#         for instr in decoder:
#             start_index = instr.ip - codeRIP 
#             bytes_str = hexByteArray[start_index:start_index + instr.len].hex().upper()
#             if f'{instr:x}' == '(bad)':
#                 hasBad = True
#                 break
#             code += f'{bytes_str.lower():16} : {instr:x}\n'
#             instrs += f'{instr:x}\n'

#         if not hasBad:
#             instructions.write(instrs)

#             disFile.write(f'\n{emojis[i]}{emojis[j]}')
#             disFile.write(code)


# Generate Emoji File
import time

emojiFile = open('emojis.txt', encoding="utf8")
streamFile = open("emojistream.bin", "wb")

codeRIP = 0
emojis = []

for emoji in emojiFile.readlines():
    emojis.append(emoji.split())

start = time.time()

for emoji1 in emojis:
    for emoji2 in emojis:
        streamFile.write(bytes(emoji1[1], encoding='utf-8'))
        streamFile.write(bytes(emoji2[1], encoding='utf-8'))

# for emoji1 in emojis:
#     for emoji2 in emojis:
#         for emoji3 in emojis:
#             for emoji4 in emojis:
#                 streamFile.write(bytes(emoji1[1], encoding='utf-8'))
#                 streamFile.write(bytes(emoji2[1], encoding='utf-8'))
#                 streamFile.write(bytes(emoji3[1], encoding='utf-8'))
#                 streamFile.write(bytes(emoji4[1], encoding='utf-8'))

end = time.time()

print("Time Taken:", end - start)




