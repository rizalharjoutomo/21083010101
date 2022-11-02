#!/bin/bash

{
   echo "Masukan Panjang"
   read panjang
   echo "Masukan Lebar"
   read lebar
   let luaspersegi=$panjang*$lebar
   echo "Luas persegi :
$luaspersegi"

}
