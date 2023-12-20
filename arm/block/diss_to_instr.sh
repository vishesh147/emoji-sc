#!/bin/bash

#
# (c) 2022-2022 Hadrien Barral
# SPDX-License-Identifier: Apache-2.0
#

set -euo pipefail

# $1: architecture
# $2: out file
# $3: remove floating-point
gen_instr () {
    tmpfile1=$(mktemp /tmp/z.XXXXXX)
    arm-none-eabi-objdump -b binary -D -m "$1" ../../emojistream.bin | grep  $':\t' | cut -f 2- \
        | grep -v $'<UNDEFINED>' | grep -v $'Address' | sort -t$'\t' -k2,2 -k3,3 \
        | sed -E 's/([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2}) \t/\4\3\2\1        /' \
        > "${tmpfile1}"
    if [ "$3" == "1" ]; then
        tmpfile=$(mktemp /tmp/z.XXXXXX)
        < "${tmpfile1}" \
            grep -v "flq" | grep -v "fld" | grep -v "flw"  | grep -v "fsd" | grep -v "fsw" \
            > "${tmpfile}"
    else
        tmpfile="${tmpfile1}"
    fi
    mv "${tmpfile}" "$2"
}

gen_instr arm "build/instr32.txt" 0
gen_instr arm "build/instr16.txt" 0