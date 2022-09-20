echo "Masukkan nilai a= "
read a
echo "Masukkan nilai b= "
read b

if [ $a -eq $b ]
then
echo "$a sama dengan $b"
elif [ $a -gt $b ]
then
echo "$a lebih dari $b"
elif [ $a -lt $b ]
then
echo "$a kurang dari $b"
else
echo "Tidak ada kondisi yang memenuhi"
fi
