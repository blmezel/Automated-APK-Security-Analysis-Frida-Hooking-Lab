# Automated APK Security Analysis & Frida Hooking Lab

## 📌 Proje Hakkında
Bu proje, **İstinye Üniversitesi Bilgisayar Teknolojileri Bölümü Bilişim Güvenliği Teknolojisi** programı bünyesinde yer alan **Tersine Mühendislik** dersi final çalışması olarak geliştirilmektedir. 

Projenin ana amacı; Android uygulamalarının (`.apk`) güvenlik mimarisini tersine mühendislik metodolojileriyle analiz etmek, statik analiz süreçlerini otomatize eden bir araç geliştirmek ve uygulama içi güvenlik mekanizmalarını (Root Algılama, Biometrik Doğrulama, SSL Pinning vb.) çalışma zamanında (runtime) manipüle edecek dinamik hooking scriptleri kurgulamaktır.

Analizler ve testler, eğitim amaçlı geliştirilmiş açık kaynaklı zafiyetli laboratuvar uygulamaları (Örn: *InsecureBankv2*, *DIVA Android*) üzerinde gerçekleştirilecektir.

---

## 👥 Proje Ekibi & Akademik Bilgiler
* **Üniversite:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi (Önlisans)
* **Ders:** Tersine Mühendislik (Reverse Engineering)
* **Dönem:** Bahar 2026
* **Proje Danışmanı:** Keyvan Arasteh
* **Geliştirici:** Ezel Balım Atik ([@blmezel](https://github.com/blmezel))

---

## 🎯 Projenin Temel Hedefleri & Beklenen Teslimatlar
Proje, hocamızın belirlediği **APK & Uygulama Analizi** ile **Dinamik Araçlar & Hooking** modüllerindeki tüm isterleri karşılayacak şekilde 3 ana fazdan oluşmaktadır:

### 1. Statik Analiz Otomasyon Aracı (Python - `src/static_analyzer/`)
* **JADX-CLI Entegrasyonu:** Hedef APK dosyasını otomatik olarak decompile eden Python motoru.
* **Manifest & İzin Analizcisi:** `AndroidManifest.xml` dosyasını otomatik ayrıştırarak (parsing) kritik ve tehlikeli izinleri (SMS, Kamera, Depolama vb.) listeleyen otomasyon.
* **Hardcoded Secret Scanner:** Kaynak kodlar içerisinde unutulmuş olabilecek API anahtarlarını, şifreleme tuzlarını (salt), AWS/Firebase credential bilgilerini regex pattern'leri ile otomatik tespit eden modül.

### 2. Tersine Mühendislik & Zafiyet Raporu (`docs/report/`)
* Decompile edilen laboratuvar uygulamasının kaynak kod bloklarının incelenmesi.
* Güvensiz veri depolama (SharedPreferences, SQLite veri tabanı sızıntıları) alanlarının tespiti.
* Logcat mekanizmasına sızan hassas verilerin analizi ve raporlanması.

### 3. Dinamik Hooking & Enstrümantasyon Modülü (Frida & JS - `src/frida_scripts/`)
* **Root Detection Bypass:** Uygulamanın cihazdaki root yetkilerini kontrol eden fonksiyonlarını (`isRooted()`, `checkRootMethod()` vb.) runtime'da yakalayarak manipüle eden JavaScript scriptleri.
* **Authentication & Login Bypass:** Mantıksal if-else kontrollerini veya server-side dönen response değerlerini havada değiştirerek giriş ekranlarını aşma senaryoları.
* **SSL Pinning Bypass (Opsiyonel/Gelişmiş):** Uygulamanın ağ trafiğini izole laboratuvarda (`mitmproxy` veya *Burp Suite*) inceleyebilmek adına SSL sabitleme mekanizmalarını devre dışı bırakan Frida scripti.

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar
* **Programlama Dilleri:** Python 3.x (Otomasyon aracı için), JavaScript (Frida scriptleri için)
* **Tersine Mühendislik Araçları:** JADX-CLI, Frida Framework, ADB (Android Debug Bridge)
* **Analiz Ortamı:** Kali Linux / Ubuntu Linux (İzole Laboratuvar)

---

## 🗺️ Proje Yol Haritası & Milestones (Commit Planı)

Proje geliştirme süreci boyunca GitHub üzerinde düzenli, anlamlı ve açıklayıcı commit'lerle ilerlenecektir. Ana kilometre taşlarımız şu şekildedir:

* [ ] **Milestone 1:** Repository yapısının kurulması ve `README.md` dokümantasyonu (Başlangıç).
* [ ] **Milestone 2:** Python tabanlı `JADX-CLI` otomasyon scriptinin kodlanması ve Manifest Parser modülünün eklenmesi.
* [ ] **Milestone 3:** Regex tabanlı Hardcoded API Key/Secret tarayıcı motorunun Python aracına entegre edilmesi.
* [ ] **Milestone 4:** Hedef test APK'sının statik analize tabi tutulması ve kaynak kod açıklarının raporlanması.
* [ ] **Milestone 5:** Root algılama mekanizmasını bypass edecek ilk Frida scriptinin (`root_bypass.js`) yazılması ve test edilmesi.
* [ ] **Milestone 6:** Giriş ve yetkilendirme (Auth) mekanizmalarını manipüle edecek Frida scriptinin (`auth_bypass.js`) yazılması.
* [ ] **Milestone 7:** Tüm testlerin izole laboratuvarda tamamlanarak nihai final projesi raporunun (`Final_Report.pdf`) hazırlanması.

---
⚠️ *Yasal Uyarı: Bu proje tamamen eğitim amaçlı ve İstinye Üniversitesi bünyesindeki Tersine Mühendislik dersi laboratuvar çalışmaları için geliştirilmiştir. Zararlı faaliyetler veya izinsiz sızma testleri amacıyla kullanılamaz.*
