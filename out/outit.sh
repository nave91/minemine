Proj=$1
Title="573:"$Proj":Naveen Kumar Lekkalapudi"
echo $Title
a2ps --center-title="$Title" -qr2gC -o ~/git/minemine/out/$Proj.ps ~/git/minemine/src/*
ps2pdf ~/git/minemine/out/$Proj.ps
