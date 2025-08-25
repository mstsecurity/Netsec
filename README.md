## 🕵️ Netsec
Whomst, alan adları ve IP adresleri için hızlı WHOIS sorguları yapmaya yarayan, basit ve hafif bir komut satırı aracıdır.

## 🚀 Özellikler
- **Hızlı ve Etkili**: Doğrudan WHOIS sunucularına bağlanarak anında sonuçlar verir.
- **Otomatik Sunucu** Tespiti: Alan adı uzantısına (.com, .tr, .co.uk, vb.) veya IP adresine göre doğru WHOIS sunucusunu otomatik olarak bulur.
- **Yönlendirme Desteği**: Yönlendiren WHOIS sunucularını takip ederek en güncel bilgiyi sağlar.
- **Loglama: Tüm sorgu** ve hata süreçlerini hem ekrana hem de whois_log.log dosyasına kaydeder.
- **Bağımsız Çalışma**: Herhangi bir ekstra kütüphane gerektirmez, doğrudan Python ile çalışır.

---

## ⚡ Kurulum
- **1.Projeyi Klonlayın**
```bash
git clone https://github.com/mstsecurity/Netsec
```
- **2. Dizin Değiştirin**
```bash
cd Netsec
```
---

## 💻 Kullanım
Aracı terminalden çalıştırmak için python komutunu ve ardından dosya adını kullanın.
```bash-
python Netsec <alan_adi_Veya_ip>
```
- **örnek**
Bir alan adı sorgulamak için
```bash
python Netsec example.com
```
Bir ip adresi sorgulamak için
```bash
python Netsec 8.8.8.8
```

---

## 💡 Sorunlar & Katkı
Her türlü hata raporu, öneri veya katkı için GitHub'da [issue](https://github.com/mstsecurity/whomst/issues) açmaktan çekinmeyin. Katkılarınızı bizim için çok değerli

---

## 📜 Lisans
Bu proje, [MIT](https://opensource.org/licenses/MIT)Lisansı ile yayınlanmıştır. Daha fazla bilgi için [LICENSE](LISENCE) dosyasına bakabilirsiniz.
