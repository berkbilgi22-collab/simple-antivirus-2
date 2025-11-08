python
import os
import hashlib

Örnek kötü amaçlı dosya hash listesi (MD5)
MALWARE_HASHES = {
    "44d88612fea8a8f36de82e1278abb02f",  # örnek kötü amaçlı dosya hash'i
    "098f6bcd4621d373cade4e832627b4f6",
}

def get_file_md5(filepath):
    """Dosyanın MD5 hash'ini hesaplar."""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Dosya okunamadı: {filepath}, Hata: {e}")
        return None

def scan_directory(directory):
    """Klasör içindeki dosyaları tarar ve kötü amaçlı dosyaları raporlar."""
    infected_files = []
    total_files = 0

    for root, _, files in os.walk(directory):
        for filename in files:
            total_files += 1
            filepath = os.path.join(root, filename)
            file_hash = get_file_md5(filepath)
            if file_hash in MALWARE_HASHES:
infected_files.append(filepath)
                print(f"!!! Tehlikeli dosya bulundu: {filepath}")

    print(f"\nToplam taranan dosya sayısı: {total_files}")
    print(f"Bulunan kötü amaçlı dosya sayısı: {len(infected_files)}")

    if not infected_files:
        print("Taranan klasörde tehdit bulunamadı.")
    else:
        print("Kötü amaçlı dosyalar:")
        for f in infected_files:
            print(f" - {f}")

if name == "main":
    target_dir = input("Taranacak klasörün yolunu girin: ")
    if os.path.exists(target_dir):
        scan_directory(target_dir)
    else:
        print("Geçersiz klasör yolu.")
