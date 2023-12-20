#!/usr/bin/env python3

from iced_x86 import *

codeRIP = 0

emojiFile = open('emojis.txt', encoding="utf8")
emojis = []

for emoji in emojiFile.readlines():
    emojis.append(emoji.split())


def gen_pairs_bin():
    streamFile = open("generated/emojistream.bin", "wb")
    for emoji1 in emojis:
        for emoji2 in emojis:
            streamFile.write(bytes(emoji1[1], encoding='utf-8'))
            streamFile.write(bytes(emoji2[1], encoding='utf-8'))


def diss_emojis():
    disFile = open("generated/diss_emojis.txt", "w+", encoding="utf-8")
    for emoji in emojis:
        hexString = emoji[0]
        hexByteArray = bytes.fromhex(hexString)
        decoder = Decoder(32, hexByteArray)
        hasBad = False
        code = ''
        for instr in decoder:
            start_index = instr.ip - codeRIP 
            bytes_str = hexByteArray[start_index:start_index + instr.len].hex().upper()
            if f'{instr:x}' == '(bad)':
                hasBad = True
                break
            code += f'{bytes_str.lower():16} : {instr:x}\n'

        if not hasBad:
            disFile.write(f'\n{emoji[0], emoji[1]}\n')
            disFile.write(code)


def diss_emoji_pairs():
    disFile = open("generated/diss_emoji_pairs.txt", "w+", encoding="utf-8")
    for i in range(len(emojis)):
        for j in range(len(emojis)):
            if i == j:
                continue
            hexString = emojis[i][0] + emojis[j][0]
            hexByteArray = bytes.fromhex(hexString)
            decoder = Decoder(32, hexByteArray)
            hasBad = False
            code = ''
            instrs = ''
            for instr in decoder:
                start_index = instr.ip - codeRIP 
                bytes_str = hexByteArray[start_index:start_index + instr.len].hex().upper()
                if f'{instr:x}' == '(bad)':
                    hasBad = True
                    break
                code += f'{bytes_str.lower():16} : {instr:x}\n'
                instrs += f'{instr:x}\n'

            if not hasBad:
                # instructions.write(instrs)
                disFile.write(f'\n{emojis[i]}\n{emojis[j]}\n')
                disFile.write(code)


# gen_pairs_bin()
diss_emojis()
diss_emoji_pairs()