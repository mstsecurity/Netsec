# 🕵️ Whomst
Whomst, alan adları ve IP adresleri için hızlı WHOIS sorguları yapmaya yarayan, basit ve hafif bir komut satırı aracıdır.
🚀 Özellikler
Hızlı ve Etkili: Doğrudan WHOIS sunucularına bağlanarak anında sonuçlar verir.

Otomatik Sunucu Tespiti: Alan adı uzantısına (.com, .tr, .co.uk, vb.) veya IP adresine göre doğru WHOIS sunucusunu otomatik olarak bulur.

Yönlendirme Desteği: Yönlendiren WHOIS sunucularını takip ederek en güncel bilgiyi sağlar.

Loglama: Tüm sorgu ve hata süreçlerini hem ekrana hem de whois_log.log dosyasına kaydeder.

Bağımsız Çalışma: Herhangi bir ekstra kütüphane gerektirmez, doğrudan Python ile çalışır.

⚡ Kurulum
Bu araç bir pip paketi değildir ve herhangi bir kurulum gerektirmez. Sadece projeyi klonlayıp dosyayı çalıştırmanız yeterlidir.

Projeyi Klonlayın:

Bash

git clone https://github.com/mstsecurity/whomst.git
Dizin Değiştirin:

Bash

cd whomst
💻 Kullanım
Aracı terminalden çalıştırmak için python komutunu ve ardından dosya adını kullanın.



python whomst <alan_adi_veya_ip>

Bir alan adı sorgulamak için:



python whomst example.com
Bir IP adresi sorgulamak için:

Bash

python whomst 8.8.8.8
💡 Sorunlar & Katkı
Her türlü hata raporu, öneri veya katkı için GitHub'da issue açmaktan çekinmeyin. Katkılarınızı bekliyoruz!

📜 Lisans
Bu proje, MIT Lisansı ile yayınlanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz
