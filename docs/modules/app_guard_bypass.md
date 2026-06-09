# Uygulama Guard Dedektörü ve Atlatma Stratejileri (Bypass Guide)

## 1. Root Tespiti (Root Detection)
* **Tespit Mekanizması:** Uygulama `/system/xbin/su`, `/sbin/su` yollarını veya `Superuser.apk` paketini arar.
* **Atlatma Stratejisi:** Frida kullanılarak `java.io.File.exists()` metodu kancalanır (hook). Uygulama bu dosyaları sorguladığında zorla `false` değeri döndürülür. 
* **Referans:** `src/root_bypass.js`

## 2. Emülatör Tespiti (Emulator Detection)
* **Tespit Mekanizması:** `android.os.Build` özelliklerini (örn: MODEL="Emulator", HARDWARE="goldfish") veya QEMU sürücülerini kontrol eder.
* **Atlatma Stratejisi:** Frida ile `android.os.Build.getString()` fonksiyonu manipüle edilerek fiziksel bir cihazın (örn: Samsung Galaxy S23) `build.prop` verileri taklit edilir.

## 3. SSL Certificate Pinning
* **Tespit Mekanizması:** Ağ trafiğinin Burp Suite/ZAP gibi araçlarla dinlenmesini (MITM) engellemek için sunucu sertifikasını uygulamanın içine gömer.
* **Atlatma Stratejisi:** JavaScript payload'u ile çalışma zamanında `com.android.org.conscrypt.TrustManagerImpl` sınıfına sızılarak tüm untrusted (güvenilmeyen) sertifikalar zorla kabul ettirilir.
* **Referans:** `src/ssl_pinning_bypass.js`

## 4. Anti-Debugging
* **Tespit Mekanizması:** `android.os.Debug.isDebuggerConnected()` metodunu çağırır veya Linux çekirdeğindeki `/proc/self/status` dosyasından `TracerPid` değerini okur.
* **Atlatma Stratejisi:** APKTool ile statik analiz yapılarak `AndroidManifest.xml` içerisine `android:debuggable="true"` bayrağı eklenir (bkz. Orkestrasyon Lab) veya `TracerPid` değeri hafızada "0" olarak yamalanır.
