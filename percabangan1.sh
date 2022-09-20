#!/bin/bash

 printf "gunung apa yang kamu suka ?\n"
 printf "ciremai ?\n"
 printf "wilis ?\n"
 printf "kawi ?\n"

 read gunung

 case "$gunung" in
 "ciremai")
 echo "ciremai banyak babinya seru lur!"
 ;;
 "wilis")
 echo "wilis medannya mantap bat"
 ;;
 "kawi")
 echo "kawi kabutnya gaada obat"
 ;;
 *)
 echo "gunung itu kurang tinggi"
 ;;
 esac
