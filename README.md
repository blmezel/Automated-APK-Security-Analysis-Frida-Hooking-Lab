<div align="center">
  <a href="https://istinye.edu.tr">
   <img width="320" height="200" alt="istinye-universitesi-logo-png_seeklogo-610039" src="https://github.com/user-attachments/assets/7be1d44d-0ec2-4315-96c2-04e56145a53c" />
  </a>

  # Automated APK Security Analysis & Frida Hooking Lab

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-Python%20%7C%20JavaScript-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT210-purple?style=flat-square)
  ![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)
</div>

---



---

## 1. Projenin Amacı / Project Purpose

Bu projenin temel amacı; Android uygulama (APK) ekosistemindeki statik/dinamik analiz engellerini, kontrol akışı düzleştirmelerini (Control Flow Flattening) ve gizli mantıksal zafiyetleri (Logic Bombs/Backdoors) tespit edebilen gelişmiş bir tersine mühendislik ve semantik kod denetim altyapısı kurmaktır. Proje, **Antigravity Deepsearch Engine** mimarisini kullanarak geleneksel SAST araçlarının analiz sınırlarını aşmayı ve kod güvenliğini matematiksel veri akış modelleriyle doğrulamayı hedefler.

---

## 2. Akademik Bilgiler / Academic Information

### Danışman Bilgisi (sabit — değiştirmeyin)

| | |
| :--- | :--- |
| **Ad Soyad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **E-posta** | keyvan.arasteh@istinye.edu.tr |
| **LinkedIn** | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh) |
| **Web Sitesi** | [qline.tech](https://qline.tech) |

### Öğrenci Bilgisi

| | |
| :--- | :--- |
| **Ad Soyad** | Ezel Balım Atik |
| **Öğrenci No** | `2420****1017` |

### Ders Bilgileri

| | |
| :--- | :--- |
| **Ders Adı** | Tersine Mühendislik |
| **Ders Kodu** | BGT210 |
| **Kredi** | 5 AKTS |
| **Ön Koşullar** | Ağ Temelleri, Linux CLI |
| **Dönem** | 2025-2026 Bahar |

---

## 3. ROADMAP.md — Yol Haritası ve Fazlar

> "Önce anla, sonra kodla." Her problemi küçük, sıralı parçalara böl. Bir dedektif gibi düşün: gözlemle, ham veriyi çevir, desenleri tespit et, raporla.

Projemiz, hocamızın belirlediği felsefeye sadık kalınarak şu faz düzeninde ilerletilmektedir:

* **Faz 0: Yazmadan Önce Anla**
  * APK hedef mimarisinin ve tersine mühendislik süreçlerindeki anti-analiz engellerinin teorik olarak çözümlenmesi.
* **Faz 1: Araştırma ve Keşif ($\rightarrow$ `docs/research/`)**
  * Gelişmiş derin arama (DeepSearch) metodolojilerinin haritalandırılması ve Antigravity motorunun çekirdek analiz dökümanının hazırlanması.
* **Faz 2: Ortam Kurulumu**
  * Analiz süreçlerinin Kali Linux/Ubuntu bağımlılıklarından izole edilmesi için Docker altyapısının kurulması ve yapılandırılması.
* **Faz 3: Uygulama (Modül başına $\le$ 10 adım)**
  * Kaynak kod seviyesinde `Source-to-Sink` veri akış takibinin yapılması ve şifreleme zafiyetlerinin kod katmanında izole edilmesi.
* **Faz 4: Test ve Raporlama**
  * Elde edilen bulguların risk skorlamalarının (Mitigation Matrix) endüstri standartlarına (OWASP / ISO 27001) göre sınıflandırılması.
* **Faz 5: Teslim Kontrol Listesi**
  * Repo standartlarının kontrol edilerek tüm dökümantasyonun ve dosyaların tam doğrulanabilir şekilde konsolide edilmesi.

---

## 4. Yaptığımız Gelişmeler ve Eklemeler / Recent Developments

Repository sürecinde standartları en üst seviyeye taşımak adına yapılan mimari eklemeler ve geliştirmeler:

* **Mimarinin Standartlaştırılması:** Dağınık halde bulunan arama notları ve dökümanlar, hocanın yönergesine tam uyumlu olacak şekilde `docs/research/` dizini altına taşındı ve kök dizin düzeni jilet gibi temizlendi.
* **Gelişmiş Semantik Analiz Entegrasyonu:** `docs/research/antigravity.md` dosyasına derinlemesine Veri Akış (Taint Analysis) matematiği, Kontrol Akışı Düzleştirme (Obfuscation) analizi ve Anti-Debugging mekanizmalarının bypass yöntemleri eklendi.
* **Risk Skorlama Normalizasyonu:** Analiz edilen kodlardaki veri sızıntılarını ölçmek amacıyla semantik motora özgü şu risk skorlama fonksiyonu dökümantasyona entegre edildi:

$$Risk\_Score = \sum_{i=1}^{n} \left( \lambda_i \cdot \text{Propagation\_Depth}(v_i) \right) \times \prod \text{Sanitization\_Status}$$

---

## 5. Projeye Katkılar ve Teslimler / Deliverables & Contributions

Proje kapsamında geliştirilen ve teslim aşamasına getirilen operasyonel çıktılar:

| Teslim Edilen Bileşen | Durum / Status | Katkı Detayı / Contribution |
| :--- | :---: | :--- |
| **Antigravity Deepsearch Raporu** | ☑️ Tamamlandı | İleri düzey semantik analiz, gizli arka kapı ve mantık bombası tespit raporu dökümante edildi. |
| **DeepSearch Motor Şablonları** | ☑️ Tamamlandı | Gemini ve DeepSeek motorlarının araştırma süreçleri için `docs/research/` altında bağımsız şablon alanları ayrıldı. |
| **Docker Konfigürasyonu** | ☑️ Tamamlandı | Çevresel izolasyon için `Dockerfile` ve çoklu konteyner orkestrasyonu sağlayan `docker-compose.yml` kök dizine eklendi. |
| **Güvenlik Şablonu** | ☑️ Tamamlandı | Kritik API anahtarlarının depoya sızmasını önleyen `.env.example` ve `.gitignore` yapılandırması tamamlandı. |

---

## 🗂️ Proje Altyapısı ve Dosya Düzeni

```text
.
├── docs/
│   ├── modules/          # Modül bazında belgeler
│   ├── research/         # Derinlemesine araştırma notları (Antigravity Raporu)
│   └── references/       # Kaynaklar, makaleler, araç linkleri
├── src/                  # Kaynak kodlar (Python/Rust/Go)
├── .env.example          # Ortam değişkenleri şablonu
├── Dockerfile            # Konteyner tanımı
├── docker-compose.yml    # Çoklu konteyner yapılandırması
├── .gitignore            # Git dışı bırakılacaklar listesi
├── ROADMAP.md            # Öğrenme ve araştırma yolculuğu dökümanı
└── README.md             # Ana belgeleme dökümanı
```
## 🌐 Canlı Yayın ve Web Platformu / Live Demonstration

Projenin operasyonel çıktılarını, otomatize analiz süreçlerini ve Frida hooking laboratuvar bulgularını daha geniş bir kitleye interaktif olarak sunmak amacıyla bağımsız bir web sitesi devreye alınmıştır. Hocamızın ve inceleyicilerin projeyi web arayüzü üzerinden grafiksel olarak da takip edebilmesi için hazırlanan platforma aşağıdaki bağlantıdan canlı olarak erişilebilir:

👉 [Automated APK Security Analysis & Frida Hooking Lab](https://blmezel.github.io/Automated-APK-Security-Analysis-Frida-Hooking-Lab/)

```

```
