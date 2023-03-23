# Kreiranje paket

Komanda za kreiranje paketa:
```
catkin_create_pkg hello_world std_msgs rospy
```

Ukoliko je paket kreiran uspšno pojaviće se u wrokspace-u i sadržaće folder pod nazivom **src**, i fajlova **CMakeList.txt** i **package.txt**.

# Kreiranje skripti
Skripte (nodove) potrebno je kreirati u **src** folderu:
```
cd ~/catkin_ws/src/hello_world/src
touch hello_world_publisher.py
touch hello_world_subscriber.py
```

Kako bi omogućili operativnom sistemu da pokrene kreirane skripte potrebno je dati odgovarajuću dozvolu narednim komandama:
```
cd ~/catkin_ws/src/hello_world/src
chmod +x hello_world_publisher.py
chmod +x  hello_world_subscriber.py
```

Sada je moguće izvršiti bildovanje workspace-a komandom:
```
cd ~/catkin_ws
catkin_make
```

Sada je moguce otkucati kod u odgovarajućim skriptama.

# Pokretanje skripti
Kod je moguće pokrenuti na sledeći način:
```
rosrun hello_world hello_world_publisher.py
```
svaku sledeću skriptu je potrbno pokrenuti u zasebnom terminalu:
```
rosrun hello_world hello_world_subscriber.py
```

Napomena: potrebno je pre pokretanja bilo koje skripte pokrenuti ***roscore***.

Ukoliko je sve urađeno kako treba dobiće se sledeći prikaz:

![hello_world_pub_sub](hello_world_pub_sub.png)

# Kreiranje servisa

Za početak neophodno je kreirati folder ***srv** u kome će se nalaziti tip poruke za servis:
```
cd ~/catkin_ws/src/hello_world/
mkdir srv
touch add_value_file.srv
```

U fajl ***add_value_file.srv*** treba upisati sledeće:
```
int64 value
---
bool response
```

Nakon toga potrebno je u fajlu ***package.xml*** odkomentarisati sledeće dve linije:
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

Takođe u fajlu ***CMakeList.txt*** treba napraviti sledeće izmene. U skeciji ***find_package*** treba dodati ***message_generation***:
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
```
Sekciju ***add_service_file*** treba odkomenatrisati i izmenizi zako da ima sledeći izgled:
```
add_service_files(
  FILES
  add_value_file.srv
)
```

I na kraju potrebno je odkomentarisati sekciju ***generate_messages***
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

Sve promene potrebno je izbildovati:
```
cd ~/catkin_ws
catkin_make
```

Kako bi se utvridlo da su sve promene dobro urađene možemo otkucati sledeću komandu u terminalu:
```
rossrv show hello_world/add_value_file
```
pri čemu bi trebalo da se dobije sledeći odgovor:

![hello_world_srv](hell_world_srv.png)

# Kreiranje server strane servisa

Skriptu je potrebno kreirati u ***src*** folderu:
```
cd ~/catkin_ws/hello_world/src
touch hello_world_service.py
chmod +x hello_world_service.py
```

Zatim je može otkucati odgovarajući kod u skripti.

# Pokretanje servisa

Serversku stranu servisa pokrećemo kao i bilo koji drugi nod:
```
rosrun hello_world hello_world_service.py
```

## Pozivanje klijentske strane korz terminal

U novom terminalu možemo otkucati sledeću komandu kako bismo poslali upit ka servisu:
```
rosservice call /add_value_file "value: 115"
```

Na sledećoj slici je prikazno kako izgleda odziv na prosleđen upti:

![hello_world_srv1](hello_world_srv1.png)
