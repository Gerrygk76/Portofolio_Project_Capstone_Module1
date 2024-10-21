**Ringkasan README**

Project ini berfokus pada penggunaan Python dan pembuatan aplikasi CRUD
sederhana yang dirancang untuk memfasilitasi perbandingan berbagai
perangkat berbasis komputer, termasuk laptop dan perangkat genggam
(handheld), berdasarkan spesifikasi teknis dan harga yang tersedia.
Dengan menyediakan informasi yang terstruktur dalam format yang mudah
dipahami, skrip ini dapat digunakan untuk membantu pengguna dalam
membuat keputusan pembelian yang lebih baik atau untuk membandingkan
berbagai perangkat berdasarkan kebutuhan teknis mereka.

Dataset dalam skrip ini terdiri dari beberapa perangkat dari berbagai
merek seperti ASUS, Lenovo, MSI, Valve, dan lainnya. Setiap perangkat
memiliki spesifikasi yang terperinci, seperti:

-   **Tipe Perangkat:** Menunjukkan apakah perangkat tersebut laptop
    atau handheld.

-   **Merek dan Model:** Nama merek dan model perangkat, seperti ASUS
    ROG ZEPHYRUS G14 atau Valve Steam Deck.

-   **Layar (PANEL Hz):** Refresh rate layar dalam Hertz, yang relevan
    bagi mereka yang memprioritaskan tampilan yang *smooth*, terutama
    untuk keperluan gaming.

-   **CPU (Processor):** Jenis prosesor yang digunakan, termasuk CPU
    high-end seperti Intel Core i9 atau AMD Ryzen.

-   **GPU (Kartu Grafis):** Kartu grafis yang digunakan, baik dari
    NVIDIA, AMD, maupun Intel, yang merupakan aspek penting bagi
    pengguna yang membutuhkan kemampuan grafis tinggi.

-   **RAM dan SSD:** Kapasitas memori (RAM) dan penyimpanan (SSD) yang
    sangat penting untuk kinerja perangkat secara keseluruhan.

-   **Harga:** Menampilkan harga masing-masing perangkat, memberikan
    wawasan untuk membandingkan nilai perangkat berdasarkan
    spesifikasinya.

**Fitur Utama:**

1.  **Dataset Terstruktur:** Berisi daftar perangkat yang terorganisir
    dengan baik dalam bentuk dictionary yang mencakup berbagai
    spesifikasi seperti CPU, GPU, RAM, SSD, dan harga.

2.  **Perbandingan Spesifikasi:** Skrip ini sangat berguna untuk mereka
    yang ingin membandingkan berbagai perangkat secara langsung
    berdasarkan kebutuhan spesifik seperti performa gaming, keperluan
    komputasi berat, atau efisiensi energi.

3.  **Pemformatan Tabel dengan Tabulate:** Dengan menggunakan pustaka
    tabulate, informasi disajikan dalam bentuk tabel yang rapi, sehingga
    memudahkan visualisasi dan perbandingan antar perangkat.

4.  **Kemudahan Pengembangan:** Skrip ini mudah diadaptasi untuk
    menambahkan perangkat baru atau memodifikasi spesifikasi yang ada.
    Pengguna juga dapat memodifikasi cara penyajian data agar sesuai
    dengan kebutuhan spesifik mereka.

5.  **Fasilitas atau fitur sederhana beli device :** memungkinkan
    pengguna untuk mengakses device tersedia dan melakukan simulasi
    pembelian berdasarkan list device yang di sajikan serta input atau
    jumlah saldo yang diberikan. Dan secara otomatis melakukan pembaruan
    library device apabila telah di lakukannya transkaksi.

**Persyaratan:**

-   **Python 3.x**: Skrip ini ditulis dalam Python 3.x dan membutuhkan
    versi ini atau yang lebih baru.

-   **Pustaka Tabulate**: Dibutuhkan untuk memformat data menjadi tabel
    yang mudah dibaca. Anda dapat menginstalnya dengan menjalankan
    perintah pip install tabulate.

**Penggunaan:**

1.  **Menambah Perangkat:** Untuk menambahkan perangkat baru, Anda cukup
    memperluas list listDevice dengan menambahkan dictionary baru yang
    berisi spesifikasi perangkat baru.

2.  **Memodifikasi Perangkat:** Anda dapat mengubah spesifikasi
    perangkat yang ada dengan memodifikasi nilai-nilai di dalam
    dictionary yang sesuai.

3.  **Menampilkan Tabel:** Jalankan skrip untuk menampilkan tabel berisi
    informasi perangkat yang diformat rapi.

**Contoh Tabel Output:**

Skrip ini akan menghasilkan output seperti berikut:

![A screenshot of a computer Description automatically
generated](./image1.png){width="6.5in"
height="2.4993055555555554in"}

**Kegunaan:**

-   **Pengguna Umum:** Sangat bermanfaat untuk orang yang ingin
    membandingkan perangkat sebelum membeli, baik untuk keperluan
    gaming, pekerjaan, atau penggunaan sehari-hari.

-   **Teknisi IT:** Membantu teknisi atau profesional IT dalam memilih
    perangkat yang sesuai untuk organisasi mereka berdasarkan anggaran
    dan kebutuhan spesifik.

-   ***Tech savvy researcher*:** Berguna untuk peneliti yang ingin
    mengumpulkan dan menganalisis data teknis perangkat-perangkat
    terbaru di pasar.
