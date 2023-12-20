#!/bin/bash

set -euo pipefail

# $1: architecture
# $2: out file
gen_instructions () {
    tmpfile1=$(mktemp /tmp/z.XXXXXX)
    objdump -b binary -D -m "$1" build/diss.bin | grep  $':\t' | cut -f 2-      \
        | grep -v $'   \t[(. ]' | sort -t$'\t' -k2,2 -k3,3                       \
        > "${tmpfile1}"
    tmpfile="${tmpfile1}"
    mv "${tmpfile}" "$2"
}

gen_instructions i386:x86-64 "build/instr64.txt" 0
gen_instructions i386 "build/instr32.txt" 0

