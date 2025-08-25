import socket
import logging
import sys

WHOIS_SERVERS = {
    "com": "whois.verisign-grs.com",
    "net": "whois.verisign-grs.com",
    "org": "whois.pir.org",
    "info": "whois.afilias.net",
    "tr": "whois.nic.tr",
    "co.uk": "whois.nic.uk",
    "de": "whois.denic.de",
    "fr": "whois.nic.fr",
    "it": "whois.nic.it",
    "jp": "whois.jprs.jp",
    "ru": "whois.tcinet.ru",
    "eu": "whois.eu",
    "asia": "whois.nic.asia",
    "biz": "whois.biz",
    "ca": "whois.cira.ca",
    "cz": "whois.nic.cz",
    "pl": "whois.dns.pl",
    "ip": "whois.arin.net",
    "pro": "whois.registry.pro"
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("whois_log.log"),
        logging.StreamHandler()
    ]
)

def get_whois_server(domain_or_ip):
    # IP adresi kontrolü
    if domain_or_ip.replace('.', '').isdigit():
        logging.info("sorgu bir ip adresi olduğu için varsayılan ip whois sunucusu seçildi.")
        return WHOIS_SERVERS.get("ip")

    try:
        domain_parts = domain_or_ip.split('.')
        if len(domain_parts) > 1:
            two_part_tld = f"{domain_parts[-2]}.{domain_parts[-1]}"
            if two_part_tld in WHOIS_SERVERS:
                return WHOIS_SERVERS.get(two_part_tld)
            
            single_part_tld = domain_parts[-1]
            return WHOIS_SERVERS.get(single_part_tld)
        return None
    except IndexError:
        return None

def whois_query(server, query_string):
    port = 43
    try:
        logging.info(f"'{server}:{port}' adresine bağlanılıyor.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            s.send(f"{query_string}\r\n".encode())

            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
            
            logging.info(f"whois sunucusundan yanıt alındı.")
            return response.decode("utf-8", errors="ignore")
    except Exception as e:
        logging.error(f"sorgu sırasında bir hata oluştu: {e}")
        return None

def get_whois_info(domain_or_ip):
    query_target = domain_or_ip.replace("www.", "").replace("http://", "").replace("https://", "")
    server = get_whois_server(query_target)
    
    if not server:
        logging.error(f"'{query_target}' için uygun whois sunucusu bulunamadı.")
        return f"hata: desteklenmeyen alan adı veya ip adresi."

    logging.info(f"'{query_target}' whois sorgusu '{server}' üzerinden başlatılıyor.")
    
    response = whois_query(server, query_target)

    if not response:
        return "sorgu başarısız oldu veya sunucuya erişilemedi."

    lines = response.splitlines()
    for line in lines:
        if line.lower().startswith(("whois server:", "referralserver:")):
            new_server = line.split(":", 1)[1].strip()
            if new_server and new_server != server:
                logging.info(f"yönlendirme sunucusu bulundu: '{new_server}'. yeni sorgu başlatılıyor.")
                response = whois_query(new_server, query_target)
                break
    
    return response

def main():
    if len(sys.argv) < 2:
        print("Kullanım: whomst <alan_adi_veya_ip>")
        sys.exit(1)

    domain_or_ip = sys.argv[1]
    whois_result = get_whois_info(domain_or_ip)
    print(f"\n--- {domain_or_ip} için WHOIS Bilgisi ---\n")
    print(whois_result)

if __name__ == "__main__":
    main()
