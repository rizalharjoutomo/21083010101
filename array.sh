#!/bin/bash

# deklarasi array
distroLinux=("twice" "itzy" "blackpink" "omg" "fromis9")

let pilih=$RANDOM%5

echo "saya memilih distro $pilih, ${distroLinux[$pilih]} !"
