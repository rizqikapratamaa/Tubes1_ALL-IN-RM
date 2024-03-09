# Tubes1_ALL-IN-RM

## Implementasi Algoritma Greedy
Pada implementasi program bot kami, kami memutuskan untuk menggunakan pendekatan algoritma greedy berdasarkan object, distance, time, dan tackle karena algoritma ini memiliki beberapa kelebihan yang sesuai dengan kebutuhan dan tujuan dalam permainan. Algoritma greedy merupakan algoritma yang mencari keputusan atau langkah yang paling optimal tanpa bisa kembali ke keadaan sebelumnya. Ada beberapa pendekatan algoritma greedy untuk kasus bot pada game ini, antara lain berdasarkan jarak, berdasarkan bobot diamond, serta gabungan antara jarak dan bobot, atau biasa disebut density. Pada bot ini, diterapkan pendekatan algoritma greedy berbasis density, untuk menghitung density, digunakan bantuan perhitungan jarak menggunakan perhitungan jarak Manhattan. Dengan memperhitungkan semua faktor tersebut, pendekatan algoritma "_**greedy by object, distance, time, dan tackle**_" mampu memberikan strategi yang efisien, adaptif, dan optimal untuk bot dalam mencapai tujuan permainan.

## How to Run
Program permainan Diamonds terdiri atas:

**1. Game engine, yang secara umum berisi:**
- Kode backend permainan, yang berisi logic permainan secara keseluruhan serta API yang disediakan untuk berkomunikasi dengan frontend dan program bot
- Kode frontend permainan, yang berfungsi untuk memvisualisasikan permainan
  
**2. Bot starter pack, yang secara umum berisi:**
- Program untuk memanggil API yang tersedia pada backend
- Program bot logic (bagian ini yang akan kalian implementasikan dengan algoritma greedy untuk bot kelompok kalian)
- Program utama (main) dan utilitas lainnya

Untuk mengimplementasikan algoritma pada bot tersebut, pengguna dapat menggunakan game engine dan membuat bot dari bot starter pack yang telah tersedia pada pranala berikut.

Game engine : 
https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0  
Bot starter pack (menggunakan repository ini): 
(https://github.com/rizqikapratamaa/Tubes1_ALL-IN-RM). 

**Game Engine**

Requirement yang Harus Di-install : 

1. Node.js (https://nodejs.org/en)
2. Docker desktop (https://www.docker.com/products/docker-desktop/)
3. Yarn
   
   ``` npm install --global yarn ```

**Instalasi untuk Game Engine**
1. Download source code (.zip) pada release game engine (https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0).
2. Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal.
3. Masuk ke root directory dari project.
4. Install dependencies menggunakan Yarn.

     ```yarn```

5. Setup default environment variable dengan menjalankan script berikut:

   - Untuk windows

   ```
   ./scripts/copy-env.bat
   ```

   - Untuk Linux /(possibly) macOS

   ```
   chmod +x ./scripts/copy-env.sh
   ./scripts/copy-env.sh
   ```

7. Setup local database dengan menjalankan command:

   ```
   docker compose up -d database
   ```
   Lalu jalankan script berikut:

   - Untuk windows

   ```
   ./scripts/setup-db-prisma.bat
   ```

   -  Untuk Linux /(possibly) macOS

   ```
   chmod +x ./scripts/setup-db-prisma.sh
   ./scripts/setup-db-prisma.sh
   ```
**BUILD**

``` npm run build ```

**Run** 

``` npm run start ```

**Untuk bot starter pack**
Requirement yang Harus Di-install : 

1. Python (https://www.python.org/downloads/)
   
**Instalasi untuk bot**

1. Download source code (.zip) pada source code repository ini (https://github.com/rizqikapratamaa/Tubes1_ALL-IN-RM).
2. Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal.
3. Masuk ke src directory dari project.
4. Install dependencies menggunakan pip.

```pip install -r requirements.txt```

**RUN**
1. Untuk menjalankan satu bot (contoh: manhattan.py):
```
python main.py --logic Manhattan --email=your_email@example.com --name=your_name --password=your_password --team etimo
```
2. Untuk menjalankan beberapa bot sekaligus (contoh: manhattan.py):
- Untuk Windows:
```
./run-bots.bat
```
- Untuk Linux/macOS : 
```
./run-bots.sh
```

## Author
- Rizqika Mulia Pratama (13522126)
- Shabrina Maharani (13522134)
- Auralea Alvinia Syaikha (13522148)
