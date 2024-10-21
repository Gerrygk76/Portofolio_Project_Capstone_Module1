from tabulate import tabulate

listDevice=[
{'SKU' : 0, 'BRAND' : 'ASUS', 'TYPE' : 'HANDHELD', 'MODEL': 'ROG ALLY X', 'PANEL(Hz)' : 120, 'CPU' : 'Z1 Extreme', 'GPU' : 'AMD Radeon 780M', 'RAM' : '24 GB', 'SSD' : '1 TB', 'PRICE $' : 700},
{'SKU' : 1, 'BRAND' : 'ASUS', 'TYPE' : 'LAPTOP', 'MODEL':'ROG ZEPHYRUS G14', 'PANEL(Hz)' : 144, 'CPU' : 'AMD Ryzen 7 8845HS', 'GPU' : 'RTX 4060 M', 'RAM' : '32 GB', 'SSD' : '2 TB', 'PRICE $' : 1700},
{'SKU' : 2, 'BRAND' : 'Valve', 'TYPE' : 'HANDHELD', 'MODEL': 'Steam Deck OLED', 'PANEL(Hz)' : 90, 'CPU' : 'Custom AMD APU 6 nm', 'GPU' : 'RDNA 2', 'RAM' : '16 GB', 'SSD' : '1 TB', 'PRICE $' : 649},
{'SKU' : 3, 'BRAND' : 'LENOVO', 'TYPE' : 'LAPTOP', 'MODEL':'ThinkPad X1 Carbon', 'PANEL(Hz)' : 60, 'CPU' : 'Intel Core i7-1260P', 'GPU' : 'Intel Iris Xe', 'RAM' : '16 GB', 'SSD' : '1 TB', 'PRICE $' : 1100},
{'SKU' : 4, 'BRAND' : 'LENOVO', 'TYPE' : 'LAPTOP', 'MODEL': 'Legion 5', 'PANEL(Hz)' : 240, 'CPU' : 'AMD Ryzen 9 8895HS', 'GPU' : 'RTX 4070 M', 'RAM' : '32 GB', 'SSD' : '2 TB', 'PRICE $' : 2200},
{'SKU' : 5, 'BRAND' : 'HP', 'TYPE' : 'LAPTOP', 'MODEL':'Omen 6', 'PANEL(Hz)' : 165, 'CPU' : 'AMD Ryzen 9 7940HS', 'GPU' : 'RTX 4060 M', 'RAM' : '32 GB', 'SSD' : '1 TB', 'PRICE $' : 1200},
{'SKU' : 6, 'BRAND' : 'LENOVO', 'TYPE' : 'HANDHELD', 'MODEL':'Legion Go', 'PANEL(Hz)' : 144, 'CPU' : 'AMD Ryzen 7 7840U', 'GPU' : 'AMD Radeon 780M', 'RAM' : '16 GB', 'SSD' : '1 TB', 'PRICE $' : 800},
{'SKU' : 7, 'BRAND' : 'GPD', 'TYPE' : 'HANDHELD', 'MODEL': 'Win Max 2', 'PANEL(Hz)' : 144, 'CPU' : 'AMD Ryzen 7 8840U', 'GPU' : 'AMD Radeon 780M', 'RAM' : '64 GB', 'SSD' : '4 TB', 'PRICE $' : 1500},
{'SKU' : 8, 'BRAND' : 'MSI', 'TYPE' : 'HANDHELD', 'MODEL':'Claw 7', 'PANEL(Hz)' : 120, 'CPU' : 'Intel Core Ultra 7', 'GPU' : 'Intel Arc Graphic', 'RAM' : '16 GB', 'SSD' : '1 TB', 'PRICE $' : 700},
{'SKU' : 9, 'BRAND' : 'MSI', 'TYPE' : 'LAPTOP', 'MODEL': 'TITAN 18 HX', 'PANEL(Hz)' : 120, 'CPU' : 'Intel Core i9 14900HX', 'GPU' : 'RTX 4090 M', 'RAM' : '128 GB', 'SSD' : '4 TB', 'PRICE $' : 4800}]

#====================================== isi saldo - extra feature =============================
# Saldo awal -  extra feature
saldo = 0.0

def isiSaldo():
    global saldo
    while True:
        try:
            inputSaldo = float(input("\nMasukkan jumlah uang yang Anda miliki: $"))
            if inputSaldo < 0:
                print("Jumlah uang tidak bisa negatif. Silakan coba lagi.")
            else:
                saldo += inputSaldo
                print(f"Saldo uang Anda sekarang: ${saldo:}")
                break  
        except ValueError:
            print("Input tidak valid, silakan masukkan angka untuk jumlah uang.")

def beli_device():   # ======== function beli device ===============
    global saldo
    while True:
        try:
            # menampilkan device yang tersedia
            print("\n=== devices yang tersedia ===")
            for device in listDevice:
                print(f"SKU: {device['SKU']}, Model: {device['MODEL']}, Price: ${device['PRICE $']}")

            # pembelian dengan acuan SKU
            sku_untuk_beli = int(input("\nMasukkan SKU device yang ingin Anda beli (atau -1 untuk keluar): "))
            
            if sku_untuk_beli == -1:
                print("Keluar dari pembelian.")
                return  
            
            device_untuk_dibeli = next((device for device in listDevice if device['SKU'] == sku_untuk_beli), None)
            
            if device_untuk_dibeli:
                # check saldo mencukupi atau tidak
                if saldo < device_untuk_dibeli['PRICE $']:
                    print(f"\nUang Anda tidak cukup untuk membeli {device_untuk_dibeli['MODEL']} yang harganya ${device_untuk_dibeli['PRICE $']}.")
                    continue

                # konfirmasi pembelian
                konfirmasi = input(f"Anda akan membeli {device_untuk_dibeli['MODEL']} seharga ${device_untuk_dibeli['PRICE $']}. Apakah Anda yakin? (yes/no): ").strip().lower()
                
                if konfirmasi == 'yes':
                    saldo -= device_untuk_dibeli['PRICE $']
                    print(f"Pembelian {device_untuk_dibeli['MODEL']} berhasil! Terima kasih.")
                    print(f"Saldo uang Anda sekarang: ${saldo:}")
                    listDevice.remove(device_untuk_dibeli)  
                else:
                    print("Pembelian dibatalkan.")
            else:
                print("SKU tidak ditemukan, silakan coba lagi.")
        
        except ValueError:
            print("Input tidak valid, silakan masukkan angka untuk SKU.")


#====================================================================================================


#=========================================== Read function  ==========================================

def showList(): 
    while True:
        opsi= input(''' 
              1. Menampilkan rekomendasi device gaming
              2. Cari berdasarkan popular search (brand, type dan SKU)
              3. kembali ke menu utama
              4. sudah siap belanja ? masuk kesini !
                                          
                masukan opsi pilihan 1~4: ''')
                
        print()
        
        if opsi == '1':
            print(f'opsi yang anda pilih adalah {opsi} yaitu List Device Gaming \n')
            display_devices()          
            
        elif opsi == '2':
            filter_utama()
        elif opsi == '3':
            print(f'opsi yang anda pilih {opsi} yaitu kembali ke menu utama')
            menu_utama()
        elif opsi == '4':
            isiSaldo()
            beli_device()

        else:
            print('Input harus angka 1 ~ 4')


def display_devices(): # menampilkan list devices
    table = tabulate(listDevice, headers='keys', tablefmt="fancy_grid")
    print(table)


#======================================== input password - extra feature ==================================================


def password_admin():
    password = "masuk"  
    user_input = input("Masukkan password untuk melanjutkan : ")
    return user_input == password

    
#====================================== start function pencarian - extra feature filter ===================================

def filter_devices_by_sku(sku):
    for device in listDevice:
        if device['SKU'] == sku:
            return [device] 
    return []

def filter_devices_by_brand(brand):
    return [device for device in listDevice if device['BRAND'].lower() == brand.lower()]

def filter_devices_by_type(device_type):
    return [device for device in listDevice if device['TYPE'].lower() == device_type.lower()]

def filter_utama():
    print(''' Pencarian berdasarkan:
            1. SKU
            2. Brand
            3. Type
          ''')
    
    pilihan = input("Silakan input pilihan (1 ~ 3): ")
    
    if pilihan == '1':
        sku = int(input("input nilai SKU yang ingin di cari: "))
        filtered_devices = filter_devices_by_sku(sku)
    elif pilihan == '2':
        brand = input("input brand atau pabrikan yang ingin ada cari: ")
        filtered_devices = filter_devices_by_brand(brand)
    elif pilihan == '3':
        device_type = input("menampilkan pencarian berdasarkan type laptop atau handheld: ")
        filtered_devices = filter_devices_by_type(device_type)
    else:
        print("opsi yang anda input tidak tersedia, input menu 1 ~ 3")
        return

    if filtered_devices:
        print("Hasil Pencarian:")
        print(tabulate(filtered_devices, headers='keys', tablefmt='fancy_grid'))
    else:
        print("Tidak ditemukan device dengan informasi yang anda input.")

#=================================== akhir function pencarian ==================================


#===================================== feature create - add data =========================
def cariIndex(dataBaru): 
    for i in range(len(listDevice)):
        if listDevice[i]['SKU'] == dataBaru:
            return i
    return -1

def tambahPart(): 
    while True:
        opsi = input(''' 
        === Anda berada di menu input device baru ===        
            
              1. Input device baru
              2. Kembali ke menu utama 
                
              Masukkan opsi Anda: ''')

        if opsi == '2':
            menu_utama()
            return  

        if opsi == '1':
            display_devices()

            # Handle SKU input saat error checking
            while True:
                try:
                    tambah_sku = int(input('Lihat tabel di atas untuk referensi SKU yang telah ada, dan masukkan SKU baru: '))
                    sku_tambah = cariIndex(tambah_sku)
                    break  # Exit loop saat input invalid
                except ValueError:
                    print('Input tidak valid, silakan masukkan angka untuk SKU.')

            if sku_tambah != -1:
                print('SKU yang akan di input sudah ada!')
                continue
            
            
            brand = input("Silakan input nama Brand: ").strip().upper()
            tipe = input("Silakan input nama tipe: ").strip().upper()
            model = input("Silakan input model: ")
            panel = input("Silakan input refresh rate panel: ")
            cpu = input("Silakan input jenis CPU: ").strip().upper()
            gpu = input("Silakan input jenis GPU: ").strip().upper()
            ram = input("Silakan input size RAM: ").strip().upper()
            ssd = input("Silakan input size SSD: ").strip().upper()
            
            
            while True:
                try:
                    price = int(input("Silakan input MSR PRICE: "))
                    break  
                except ValueError:
                    print('Input tidak valid, silakan masukkan angka untuk harga.')

            new_device = {
                'SKU': tambah_sku,
                'BRAND': brand,
                'TYPE': tipe,
                'MODEL': model,
                'PANEL(Hz)': panel,
                'CPU': cpu,
                'GPU': gpu,
                'RAM': ram,
                'SSD': ssd,
                'PRICE $': price
            }
    
            konfirmasi = input(f"Apakah Anda ingin menambahkan device ini? {new_device} (yes/no): ").strip().lower()
            print()
            
            if konfirmasi == 'yes':
                print(f"Device baru berhasil ditambahkan!")
                print(f"Device baru telah ditambahkan sebagai berikut: {new_device}")
                listDevice.append(new_device)
            else:
                print("Device tidak ditambahkan.")
                menu_utama()
                return  

#================================================================================================
      
# ========================================= menu delete =========================================
def Menu_delete(): 
    while True:
        opsi= input(''' 
            ---selamat datang di menu delete--- 
            ----- anda masuk sebagai admin ----
                    
              1. delete item di list devices
              2. kembali ke menu utama
                              
                masukan opsi pilihan 1~2: ''')
                
        print()
        
        if opsi == '1':
            print(f'opsi yang anda pilih adalah {opsi} yaitu delete list devices')
            print()            
            display_devices
            delete_device()

        elif opsi == '2':
            menu_utama()
            
        else:
            print('masukan input numerik 1 ~ 2: ')


def delete_device():
    while True:
        try:
            sku_delete = int(input('Delete device SKU (input SKU yang tertera): '))
            device_to_delete = next((device for device in listDevice if device['SKU'] == sku_delete), None)
            
            if device_to_delete:
                konfirmasi = input(f"Apakah Anda yakin menghapus? {device_to_delete} (yes/no): ").strip().lower()
                
                if konfirmasi == 'yes':
                    listDevice.remove(device_to_delete)
                    print(f"Device dengan SKU {sku_delete} telah dihapus.")
                    print()
                    display_devices() 
                    print()
                    Menu_delete()
                elif konfirmasi == 'no':
                    print("Device tidak dihapus.")
                else:
                    print("Input tidak valid, silakan jawab 'yes' atau 'no'.")
            else:
                print('SKU yang di input tidak tersedia.')
        
        except ValueError:
            print("Input tidak valid, harap masukkan angka untuk SKU.")


    # =========================== update device ================================   


def update_device(sku, **kwargs):
    for device in listDevice:
        if device['SKU'] == sku:
            for key, value in kwargs.items():
                if key in device:
                    device[key] = value
            return device
    return None


def select_and_update_device():
    # show listdevice yang ada
    print("list device saat ini:")
    print(tabulate(listDevice, headers="keys", tablefmt="fancy_grid"))

    # Input SKU
    
    sku = int(input("masukan sku yang ingin anda edit: "))
    device = next((d for d in listDevice if d['SKU'] == sku), None)
    
    if device:
        print(f"\nDevice yang dipilih: {device}")

        # konfirmasi sebelum update
        konfirmasi = input("anda ingin mengubah device ini? (yes/no): ").strip().lower()
        print()
        if konfirmasi != 'yes':
            print(f"(\tidak jadi melakukan edit untuk {konfirmasi} .")
            return
        
        brand = input(f" BRAND (device saat ini {device['BRAND']}, masukan nilai baru: ): ").strip().upper()
        type_ = input(f" TYPE (device saat ini {device['TYPE']}, masukan nilai baru: ): ").strip().upper()
        model = input(f" MODEL (device saat ini {device['MODEL']}, masukan nilai baru: ): ")
        panel_hz = input(f" PANEL(Hz) (device saat ini {device['PANEL(Hz)']}, masukan nilai baru: ): ")
        cpu = input(f" CPU (device saat ini {device['CPU']}, masukan nilai baru: ): ").strip().upper()
        gpu = input(f" GPU (device saat ini {device['GPU']}, masukan nilai baru: ): ").strip().upper()
        ram = input(f" RAM (device saat ini {device['RAM']}, masukan nilai baru: ): ").strip().upper()
        ssd = input(f" SSD (device saat ini {device['SSD']}, masukan nilai baru: ): ").strip().upper()
        price = input(f" PRICE $ (device saat ini {device['PRICE $']}, masukan nilai baru: ): ")

        # 
        updated_device_info = {
            'SKU': sku,
            'BRAND': brand if brand else device['BRAND'],
            'TYPE': type_ if type_ else device['TYPE'],
            'MODEL': model if model else device['MODEL'],
            'PANEL(Hz)': panel_hz if panel_hz else device['PANEL(Hz)'],
            'CPU': cpu if cpu else device['CPU'],
            'GPU': gpu if gpu else device['GPU'],
            'RAM': ram if ram else device['RAM'],
            'SSD': ssd if ssd else device['SSD'],
            'PRICE $': price if price else device['PRICE $']
        }

        # menampilkan update device
        print("\ninformasi edit device:")
        print(tabulate([updated_device_info], headers="keys", tablefmt="fancy_grid"))
        
        # langkah konfirmasi untuk melakukan perubahan
        confirm = input("apa anda yakin untuk mengubah data? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("\nsukses mengubah data listdevice.")
            update_device(sku, **{key: value for key, value in updated_device_info.items() if key != 'SKU'})
        else:
            print("\ntidak diberlakukan perubahan.")
    else:
        print(f"\nDevice dengan SKU {sku} tidak ditemukan.")


    # ============================== akhir update device =================================    
         
def menu_utama():
    while True:
        menu= input('''
    -------------- Selamat datang di GerryPlaymore ------------
    ------ Wujudkan momen gaming terbaikmu sekarang juga!------ \n
            List Menu:
        1. Menampilkan Rekomendasi dari GerryPlaymore
        2. Menambahkan pengajuan device (*)
        3. Pembaharuan device (*)
        4. Hapus item device dalam list device (*) 
        5. Exit program
                    
        (* = password required)
        Masukan angka menu yang ingin dijalankan (1~5) : ''')

        if menu == '1': #read menu 
            print()
            showList() #display all data

        elif menu == '2': #create menu
            print()
            if password_admin():
                tambahPart() #add data
            else:
                print("Password salah. Kembali ke menu utama.")
            
                                     
        elif menu == '3': #update menu untuk devices
            print()
            if password_admin():
                select_and_update_device() #edit
            else:
                print("Password salah. Kembali ke menu utama.")
            
            
        elif menu == '4': # delete menu untu devices
            print()
            if password_admin():
                Menu_delete() #edit
            else:
                print("Password salah. Kembali ke menu utama.")
            Menu_delete()
            
        elif menu == '5':
            break

        else:
            print()
            print('opsi yang ada masukan tidak tersedia')
            print('\n \t nilai yang ada masukan harus 1 ~ 5')
            menu_utama()
            
        
menu_utama()




    
