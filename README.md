# RTR105
***Datormācības kursa eletroniskā kladē***

***(06.09.2018)***

Mācības saites: 1. https.//edx2.etf.rtu.lv/portal (Sakai) - mācība procēsa parvaldīšana 2. github.com - kodus saglābašana 

Terminal > caur GUI (var iett internetā no dekstopā)
         > Ctrl + Alt + T (var ieet internetā caur kodus)

Datormācība sastāva iekļauti šādi posmi: cietvielas objekts (dzelzis) > kodols > OS > aplikācijas (fizikālie lielumi)
Aplikācijas veidojas ar shell valodas palīdzību. 

Katrai komandai ir savs īpašs kods, kuru var uzzināt ar tādu shēmu: burts (-is) 1. TAB > 2. komandas saraksts 
Ja gribāt attīrīt eksrānu, tad vajadzīgī nospiež (Ctrl+L)
```
uname (-a) - man uname (kods ar kuru var uzzināt detalizēto informāciju par programmu)
komanda (-a) atslēga 
whoami (ka es esmu, informācija par tevi)
pwd (tekošais darba katalogs)
/zwx//rwx/ - x (fails) - saimnieks grupa (pasaule) neredzemes vajadzīgi likt dškumpunktu
ls - ls (visu dekt. det.fails)
```

***(12.09.2018)***

Ctrl + Shift + T - var veidot papildus tabulas
*stradajot sistēmā, mēs esam failu sistēmā
*failu sistēmā var parvietoties > cd + mape (cd.Music)
cd/home/user - atgriezties atpakaļ
```
man + ls - ? - konandu apraksts 
d - mapē 
cd ~/
cd - atgriezties mājās 
rmnir - dzēst
mndir - izveidot mapi 
rm -r ManaMape-
echo - attēlot tekstu 
echo -e ' Teksts\ncits teksts"
cdf > pardaudīt faila satura, kātekstu 
cp - kopēt 
mv - pārvietot 
rm*...*.txt - dzēst 
```
***(19.09.2018)***

(skripts) - fails ar komandu sarakstu 

Skripts
(fails)
mkdir Mape
cd Mape
mdkir MapeMapee = izdarīt vairāk failus

Jaunas konandas:
cat - pārskatīt sarakstu 
nano mana_skripts (veidojam mape)
echo $PATH - (komandam saraksts)
PATH = (piešķiršanas operācija (zīme)
rwx - 111(7) rwx - 110(6) rwx =100 (4)

Ar skriptu var izveidot mape
instrukcijas 0/1  > OS
fails > instruksijas cilvēkam saprotāmā gadījumā > interpretarors > OS (bash/sh)
./mans_skripts.sh (relitātīvais)
~/mans_skripts.sh (mājas apgabals)

Darbības:
Terminal > Firefox > github READ.ME >/< nano (nebūs atkarīgi no tīkla)
git clone https://github.com/vika1999/RTR105
./git-upload (tagad un šeit)
Python skripti > Python interpritators > OS
               = python >/<; ipython > idle + "interpritators">/<
```
vars () - (objekta nosaukums, apraksts, pilns saraksts)
objekts..doc.. (jebkura dokumenta - īss apraksts)
print > python 3... print ()
exit() - iziet
type() = vesela tipa skaitļi
ipython (V+TAB) - var izmantot tikai to, kas ir definets.
```
Cilvēks - burts (simboli _ _ _ _ ) /  Dators 0/1
          skaiļi > 0,1,2,3,4      / 0101110101 > interpritācija + atbilstoša tabulā ASCII (www.ecowin.org/ascii.htm)
                 > 1,5,6,7       
Skaītīšanas sistēmas > dec, bin, hek un oct.

***(26.09.2018)***

1.mans_mainiigais=input (saglabāt skaitļa dokumentu)
file-newfile ("Untitle") - skripta vārds interpritators = python (GUI - idle)
failā (caur nano; caur idle)
Ctrl + S (saglabāt) + F3 
Programmas intalēšana (komanda) - sudo apt-get intal ipyhon;idle.

***(03.10.2018)***
```
Nodarbības nosaukums:
- dgr_20181003a.py
- history_20181003a.txt
```
***(10.10.2018)***
```
Nodarbības nosaukums:
- dgr_20181010_py
- test_20181010_1.py
```

***(24.10.2018)***
```
- history_20181024.txt
- dgr_20181024.py
 ```
***(31.10.2018)***
```
- dgr_20181031.py
- teksts-short.txt
- teksts.txt
- sin_caur_summu_ver1.py		
- sin_caur_summu_ver2.py
- sin_caur_summu_ver3.py
- test_sin_caur_summu_ver1.py
- test_sin_caur_summu_ver2.py
- test_sin_caur_summu_ver3.py
```
***(07.11.2018)***
```
- sin_caur_summuver4.py
- sin_caur_summu_ver5.py
- sin_caur_summu_end.py
- test_sin_caur_summu_ver4.py
- test_sin_caur_summuver5.py
_ test_sin_caur_summu_end.py
```
***(14.11.2018)***
```
16. nodarbība (zīmešana)
Sakai -> Lessons -> Class 15
Darba gaita 2.-5.
17. nodarbība
Sakai -> Lessons -> Class 15
Darba gaita 5.-12.
Visu saglabābāt repozitārijā
```
***(20.11.2018)***
```
Katru reizi rēķināt funkcijas vēŗtību 
Funkcijas vērtību var arī saglabāt (masīvā) un pēct tam izmantot 
f(x)
      |___________
      |_______    |     f(x3)
      |____   |   |     f(x2)
      |____|__|___|____ f(x1) 
                        (x)
 
 
 
              __
 f'(x) = lim |f(x+~x)-f(x)
             |------------- - forward difference
             |      ~x
             |f(x+~x)-f(x-~x)
             |------------- - central difference *sin'(x) = cos(x)*
             |      2~x
             |f(x)-f(x-~x)
             |------------- - backward difference *sin"(x) = cos'(x) = -sin(x)*
             |      ~x
              __
```
***(05.12.2018)***
```
T = 84(10) = MSB - 0|101|0100(2) - LSB                                                   XOR
                        |                                                          X(1)| X(2) | Y
                        |  ^                                                        0  |  0   | 0
                        |(XOR)                                                      0  |  1   | 1
                        |                                                           1  |  0   | 1
    5(10)  = 0000|0101(2)                                                           1  |  1   | 0
                 |
           ______|______ = 2^0 + 2^4 + 2^6 = 1 + 16 + 64 + 81(10)
             0101 0001
       
"Iekļūst savā studenta darba apgabalā ..."
  ssh_-X_x181REB100@213.175.92.22
```
***(19.11.2018)***
```
Funkcijas:
sudo apt-get update
sudo apt-get install jupyter
Windows OS -> Anaconda <- jupyter
```

   
    
             
