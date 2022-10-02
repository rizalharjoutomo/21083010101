#!/bin/bash
echo "masukkan bilangan = "
read bilangan

until [ ! $bilangan -gt 0 ]
do

echo $bilangan
bilangan=$((bilangan-2))
done


