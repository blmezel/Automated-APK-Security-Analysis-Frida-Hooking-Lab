<div align="center">
  <img width="320" height="320" alt="istinye-universitesi-logo-png_seeklogo-610039" src="https://github.com/user-attachments/assets/da681d83-2f61-4daf-be78-c01abe656e88" />

# 🛡️ Automated APK Security Analysis & Frida Hooking Lab

  ![Static Analysis](https://img.shields.io/badge/Security-Static_Analysis-red)
  ![Frida Instrumentation](https://img.shields.io/badge/Frida-Runtime_Hooking-blue)
  ![Automation](https://img.shields.io/badge/Automation-Python_CLI-green)
  ![Course Code](https://img.shields.io/badge/Ders_Kodu-BGT210-yellow)
  ![Instructor](https://img.shields.io/badge/E%C4%9Fitmen-Keyvan_Arasteh-purple)

  <br>

  🚀 **İstinye Üniversitesi - BGT210: Tersine Mühendislik Dersi Final Projesi**
</div>

---

## 📑 İçindekiler (TOC)
1. [Proje ve Öğrenci Bilgileri](#-proje-ve-öğrenci-bilgileri)
2. [Projenin Amacı](#-projenin-amacı)
3. [Dizin Yapısı ve Derin Araştırma Klasörü](#-dizin-yapısı-ve-derin-araştırma-klasörü)
4. [Planlanan Analiz Aşamaları](#-planlanan-analiz-aşamaları)
5. [🛠️ Kullanılacak Teknolojiler](#️-kullanılacak-teknolojiler)
6. [📅 Haftalık Çalışma Planı](#-haftalık-çalışma-planı)
7. [🏗️ Gelişmiş Sistem Mimarisi ve Otomasyon](#️-gelişmiş-sistem-mimarisi-ve-otomasyon)
8. [📌 Beklenen Çıktılar](#-beklenen-çıktılar)
9. [🔐 Sonuç ve Yasal Uyarı](#-sonuç-ve-yasal-uyarı)

---

## 📋 Proje ve Öğrenci Bilgileri

| Kriter                   | Detay                                                      |
| :----------------------- | :--------------------------------------------------------- |
| **Öğrenci Adı Soyadı**   | Ezel Balım Atik                                             |
| **Üniversite & Bölüm**   | İstinye Üniversitesi - Bilişim Güvenliği Teknolojisi       |
| **Ders Kodu & Adı**      | **BGT210 - Tersine Mühendislik (Reverse Engineering)**     |
| **Eğitmen & Danışman**   | Keyvan Arasteh                                             |
| **Analiz Edilecek Altyapı**| Açık Kaynak Zafiyetli Laboratuvar APK'ları (*InsecureBankv2*, *DIVA*) |
| **Seçilen Senaryo**      | **Automated Static Analysis & Dynamic Runtime Hooking**     |

---

## 🎯 Projenin Amacı

Bu projenin amacı, Android uygulamalarının (`.apk`) güvenlik mimarisini tersine mühendislik metodolojileriyle hem statik hem de dinamik olarak analiz etmektir. 

Proje kapsamında, statik analiz süreçlerini hızlandıracak Python tabanlı bir otomasyon motoru geliştirilecek ve uygulama içi kritik güvenlik mekanizmaları çalışma zamanında (runtime) Frida enstrümantasyon aracıyla manipüle edilecektir. Özellikle aşağıdaki güvenlik katmanları mercek altına alınacaktır:

* Root Detection (Kök Dizin Kontrolü) Mekanizmaları
* Hardcoded Secrets & API Keys (Kaynak Koda Gömülü Hassas Veriler)
* Android Kimlik Doğrulama (Authentication) ve Mantıksal İzin Matrisleri
* SSL Pinning (Sertifika Sabitleme) Engelleri

---

## 📁 Dizin Yapısı ve Derin Araştırma Klasörü

Hocamızın direktifleri doğrultusunda, projede gerçekleştirilen derin akademik araştırmalar, teorik altyapı bilgileri ve analiz sonuç raporları için bağımsız bir alan ayrılmıştır. Projenin ana dosya hiyerarşisi şu şekildedir:

```text
├── research/                  # 🔍 Derin Araştırma Bilgileri ve Analiz Sonuçları Klasörü
│   ├── theoretical_bg.md      # Android güvenlik mimarisi ve Frida çalışma teorisi araştırması
│   └── analysis_results.md    # APK analizlerinden elde edilen derin teknik bulgular ve sonuçlar
├── src/
│   ├── static_analyzer/       # Python tabanlı otomatik statik analiz aracı kodları
│   └── frida_scripts/         # Runtime manipülasyonu için yazılan JavaScript (Frida) kodları
├── docs/
│   └── report/                # Görseller ve nihai proje teslim rapor dosyaları
└── README.md                  # Ana proje dökümantasyonu

---

## 🔍 Planlanan Analiz Aşamaları

### 1️⃣ JADX-CLI ile Otomatik Decompile Motoru
* `JADX-CLI` araç seti Python scriptimize bir wrapper olarak entegre edilecek.
* Hedef APK dosyası verildiğinde, kaynak kodun otomatik olarak decompile edilmesi ve temiz bir dizine çıkartılması sağlanacaktır.

🔴 **Araştırma Sorusu:** Büyük ölçekli APK dosyalarında manuel decompile süreçlerinin yarattığı zaman kaybı ve insan hatası otomasyon ile nasıl minimize edilir?

---

### 2️⃣ Manifest Güvenlik Analizcisi (Parsing)
* `AndroidManifest.xml` dosyası otomatik ayrıştırma (parsing) işlemine tabi tutulacak.
* Uygulamanın talep ettiği kritik ve tehlikeli izinler (SMS okuma, Rehber, Kamera vb.) ile dışa açılmış (`exported=true`) güvensiz bileşenler tespit edilecektir.

🔴 **Araştırma Sorusu:** Gereksiz veya kötü niyetli izinlerin varlığı, uygulamanın atak yüzeyini nasıl genişletir?

---

### 3️⃣ Hardcoded Secret Scanner (Statik Kod Denetimi)
* Decompile edilen Java/Smali kaynak kodları üzerinde regex (düzenli ifade) pattern'leri çalıştırılacaktır.
* Kod blokları arasında unutulmuş şifreleme anahtarları, AWS/Firebase API key'leri ve hardcoded credential bulguları taranacaktır.

🔴 **Araştırma Sorusu:** Kaynak koda gömülen statik anahtarlar, APK'yı decompile eden bir saldırgan tarafından nasıl ele geçirilebilir?

---

### 4️⃣ Dinamik Root Detection & Auth Bypass (Frida Hooking)
* Hedef uygulamanın root kontrol fonksiyonları (`isRooted()`, `checkRootMethod()`) kaynak kod üzerinden tespit edilecek.
* Yazılacak özel JavaScript enjeksiyon scriptleri ile Frida üzerinden bu fonksiyonların return değerleri runtime'da değiştirilerek (Hooking) root engeli aşılacaktır. Aynı mantık mantıksal if-else giriş (login) ekranları için de uygulanacaktır.

🔴 **Araştırma Sorusu:** Uygulama kodunun cihaz üzerinde değiştirilmeden bellekte manipüle edilmesi, geleneksel istemci tarafı güvenlik önlemlerini nasıl işlevsiz bırakır?

---

## 🛠️ Kullanılacak Teknolojiler
* **Python 3.x:** Otomasyon Motoru
* **JavaScript:** Frida Hooking Scriptleri
* **JADX-CLI:** Decompiler Altyapısı
* **Frida Framework & ADB:** Android Debug Bridge
* **Linux:** Kali / Ubuntu Linux Laboratuvar Ortamı

---

## 📅 Haftalık Çalışma Planı

| Gün | Aşama     | Yapılacak İş                                               |
| :-- | :-------- | :--------------------------------------------------------- |
| **1** | Altyapı   | Repository yapısının kurulması, `research/` alanı aktivasyonu|
| **2** | Otomasyon | Manifest Parser ve İzin Analizcisi modülünün kodlanması    |
| **3** | Tarayıcı  | Regex tabanlı Hardcoded API Key/Secret motorunun yazılması |
| **4** | Analiz    | Hedef laboratuvar APK'sının statik analizi ve kod denetimi |
| **5** | Dinamik   | Root tespiti engelini aşacak Frida scriptinin yazılması    |
| **6** | Bypass    | Kimlik doğrulama katmanı için Frida Hooking testleri        |
| **7** | Rapor     | Derin araştırma verilerinin `research/` altına işlenmesi     |

---

## 🏗️ Gelişmiş Sistem Mimarisi ve Otomasyon

Bu proje, sadece basit bir manuel analiz çalışması olmayıp düzenli ve modüler bir yazılım mimarisi ve siber güvenlik otomasyon disiplini ile kurgulanmıştır:

* **📁 src/static_analyzer/:** APK dosyalarını girdi olarak alan, otomatik ayrıştıran ve bulguları terminale raporlayan ana Python otomasyon aracının yer aldığı dizindir.
* **⚙️ src/frida_scripts/:** Uygulamanın bellek alanına çalışma zamanında enjekte edilecek, tamamen projeye özgü geliştirilmiş `root_bypass.js` ve `auth_bypass.js` gibi dinamik enstrümantasyon kodlarını barındırır.
* **🔍 research/:** Hocamızın isteği doğrultusunda ayrılan, tersine mühendislik süreçlerindeki akademik araştırma bulgularını ve derin analiz sonuçlarını içeren merkez klasördür.
* **🔐 Güvenli Çevre Yönetimi:** Analiz esnasında üretilebilecek hassas loglar ve test ortamı parametreleri repoda gizli tutulacak, şablon yapılar üzerinden modüler ilerlenecektir.

---

## 📌 Beklenen Çıktılar
* Python tabanlı otomatik APK statik analiz aracı
* Güvenlik açıkları ve Manifest risk değerlendirme raporu
* Root Detection ve Auth mekanizmalarını kıran Frida script kütüphanesi
* `research/` klasöründe barındırılan derin araştırma dökümanları ve analiz sonuçları

---

## 🧠 Projenin Katkısı
Bu proje sayesinde:
* Gerçek dünya siber güvenlik senaryoları izole laboratuvarda simüle edilecek,
* Android işletim sisteminin mimari zafiyetleri ve uygulama koruma yöntemleri anlaşılacak,
* Statik ve dinamik tersine mühendislik pratikleri otomasyon kodlarıyla birleştirilerek profesyonel bir çıktı üretilecektir.

---

## 🔐 Sonuç ve Yasal Uyarı
Bu çalışma; kurulum, otomasyon, statik analiz ve dinamik test süreçlerini kapsayan ileri düzey bir tersine mühendislik incelemesi olarak kurgulanmıştır. Projenin tüm kodları ve derin araştırma çıktıları bu repository üzerinde hocamız Keyvan Arasteh'e davet gönderilerek teslim edilecektir.

⚠️ **YASAL UYARI:** *Bu projede yer alan tüm araçlar, scriptler ve dökümanlar tamamen eğitim amaçlı ve İstinye Üniversitesi Tersine Mühendislik dersi laboratuvar çalışmaları için geliştirilmiştir. Yetkisiz sistemler veya üçüncü parti uygulamalar üzerinde gerçekleştirilecek izinsiz test faaliyetleri için kesinlikle kullanılamaz; tüm sorumluluk uygulayıcıya aittir.*

---

## 👨‍🏫 Eğitmen Bilgisi
**Instructor:** Keyvan Arasteh
