# DeepSeek DeepSearch Araştırma Sonuçları
Automated APK Security Analysis Lab — Frida Hooking & Reporting
This lab guides you through building an automated dynamic analysis pipeline for Android applications. You will learn to combine Frida’s instrumentation with Python scripting to hook sensitive APIs, capture runtime behaviour, and generate a basic security report — all with minimal manual effort.
1. Objectives
By the end of this lab you will:

Statically inspect an APK to identify interesting classes/methods.

Dynamically instrument Android apps with Frida using Python bindings.

Automate hooking of:

Cryptographic operations

Network calls (HTTP/HTTPS)

File I/O

Intent handling

WebView interactions

Collect runtime logs and parse them for security findings.

Export a machine-readable (JSON) and human-readable report.

2. Prerequisites
Install the following on your host machine (Linux/macOS/Windows):

Tool	Purpose
Python 3.8+	Automation scripting
Frida tools	Dynamic instrumentation (pip install frida-tools)
Android SDK Platform Tools	adb communication
Apktool / aapt	APK metadata extraction
JADX (optional)	Static decompilation
An Android device/emulator	Rooted recommended; at least frida-server running
Emulator / Device Setup
Create an Android Virtual Device (AVD) with API 28+ and root access (or use a rooted physical device).

adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &
https://github.com/dineshshetty/Android-InsecureBankv2

Install it on the emulator:
adb install InsecureBankv2.apk
4. Quick Static Analysis
Before hooking, let’s quickly identify what to monitor. Use jadx-gui or apktool:
# Extract package name and main activity
aapt dump badging InsecureBankv2.apk | grep package
Output:
package: name='com.android.insecurebankv2' versionCode='1' versionName='1.0' ...
Open the APK in JADX and note interesting classes like:

com.android.insecurebankv2.CryptoClass

com.android.insecurebankv2.DoLogin

com.android.insecurebankv2.ViewStatement

com.android.insecurebankv2.PostLogin

These will be our primary targets for hooking.

5. Building the Automated Hooking Script
We’ll use Python + Frida to spawn the app, load a bundle of JavaScript hooks, capture console messages, and parse results.

5.1 The Frida JavaScript Payload
Create a file hooks.js that contains our reusable instrumentation:
// hooks.js – Collection of security-relevant hooks

Java.perform(function() {
    // --- Crypto ---
    var Cipher = Java.use("javax.crypto.Cipher");
    Cipher.getInstance.overload('java.lang.String').implementation = function(transformation) {
        send({type: "crypto", action: "Cipher.getInstance", details: transformation});
        return this.getInstance(transformation);
    };

    Cipher.doFinal.overload('[B').implementation = function(input) {
        send({type: "crypto", action: "Cipher.doFinal", details: "Data encrypted/decrypted"});
        return this.doFinal(input);
    };

    // --- HTTP/HTTPS ---
    var URL = Java.use("java.net.URL");
    URL.openConnection.overload().implementation = function() {
        var conn = this.openConnection();
        send({type: "network", action: "URL.openConnection", details: this.toString()});
        return conn;
    };

    // OkHttp (if present)
    try {
        var OkHttpClient = Java.use("okhttp3.OkHttpClient");
        OkHttpClient.newCall.implementation = function(request) {
            send({type: "network", action: "OkHttp.newCall", details: request.url().toString()});
            return this.newCall(request);
        };
    } catch(e) {}

    // --- File I/O ---
    var FileOutputStream = Java.use("java.io.FileOutputStream");
    FileOutputStream.$init.overload('java.io.File').implementation = function(file) {
        send({type: "file", action: "FileOutputStream.open", details: file.getPath()});
        return this.$init(file);
    };

    var FileInputStream = Java.use("java.io.FileInputStream");
    FileInputStream.$init.overload('java.io.File').implementation = function(file) {
        send({type: "file", action: "FileInputStream.open", details: file.getPath()});
        return this.$init(file);
    };

    // --- Intents ---
    var Activity = Java.use("android.app.Activity");
    Activity.startActivity.overload('android.content.Intent').implementation = function(intent) {
        send({type: "intent", action: "startActivity", details: intent.getAction() + " -> " + intent.getData()});
        return this.startActivity(intent);
    };

    // --- WebView ---
    var WebView = Java.use("android.webkit.WebView");
    WebView.loadUrl.overload('java.lang.String').implementation = function(url) {
        send({type: "webview", action: "loadUrl", details: url});
        return this.loadUrl(url);
    };

    // --- SQLite (optional) ---
    var SQLiteDatabase = Java.use("android.database.sqlite.SQLiteDatabase");
    SQLiteDatabase.execSQL.overload('java.lang.String').implementation = function(sql) {
        send({type: "database", action: "execSQL", details: sql});
        return this.execSQL(sql);
    };
});
5.2 Python Automation Script
Create auto_frida.py:
import frida
import sys
import json
import time
from datetime import datetime

# ---------- Report Generator ----------
class SecurityReport:
    def __init__(self, package_name):
        self.package = package_name
        self.events = []
        self.start_time = datetime.now()

    def add_event(self, event):
        event["timestamp"] = datetime.now().isoformat()
        self.events.append(event)

    def export_json(self, filename="report.json"):
        with open(filename, "w") as f:
            json.dump({
                "package": self.package,
                "analysis_start": self.start_time.isoformat(),
                "total_events": len(self.events),
                "events": self.events
            }, f, indent=2)
        print(f"[*] JSON report saved: {filename}")

    def print_summary(self):
        print(f"\n=== Security Analysis Summary for {self.package} ===")
        categories = {}
        for e in self.events:
            cat = e.get("type", "unknown")
            categories[cat] = categories.get(cat, 0) + 1
        for cat, count in categories.items():
            print(f"  {cat}: {count} events")
        print("=" * 40)

# ---------- Frida Automation ----------
def on_message(message, data):
    if message["type"] == "send":
        payload = message["payload"]
        report.add_event(payload)
        print(f"[EVENT] {payload['type']}/{payload['action']}: {payload['details']}")
    elif message["type"] == "error":
        print(f"[ERROR] {message['stack']}")

def load_hooks(script_file):
    with open(script_file, "r") as f:
        return f.read()

def main(apk_package, activity=None):
    global report
    report = SecurityReport(apk_package)

    device = frida.get_usb_device()
    print(f"[*] Connected to device: {device.name}")

    # Spawn the app
    pid = device.spawn([apk_package])
    print(f"[*] Spawned {apk_package} with PID {pid}")
    session = device.attach(pid)

    # Load hook script
    js_code = load_hooks("hooks.js")
    script = session.create_script(js_code)
    script.on("message", on_message)
    script.load()
    print("[*] Hooks loaded")

    # Resume the app
    device.resume(pid)
    print("[*] App resumed – interact with the app now. Press Ctrl+C to stop.")

    try:
        # Keep running, possibly set a timeout
        time.sleep(60)  # 60 seconds of monitoring; adjust as needed
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
    
    # Cleanup
    session.detach()
    report.export_json()
    report.print_summary()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python auto_frida.py <package_name>")
        sys.exit(1)
    package = sys.argv[1]
    main(package)
    5.3 Running the Lab
python auto_frida.py com.android.insecurebankv2
Interact with the app on the emulator: login (credentials dinesh / Dinesh@123$), transfer money, view statement.
The script will capture every hook trigger and build a JSON report.

6. Interpreting the Report
The report.json will contain entries like:
{
  "type": "crypto",
  "action": "Cipher.getInstance",
  "details": "AES/CBC/PKCS5Padding",
  "timestamp": "2026-06-10T12:34:56"
}
You can automatically flag insecure practices:

Hardcoded crypto transforms – if details is a weak algorithm like DES.

HTTP (not HTTPS) URLs – network events with http:// scheme.

Sensitive file paths – e.g., writing to /data/data/.../shared_prefs with plain text credentials.

WebView loading untrusted URLs – possible WebView vulnerabilities.

SQL injection prone queries – raw SQL strings containing concatenated user input.

7. Extending the Lab
Bypass SSL Pinning
Add to hooks.js:
var SSLContext = Java.use("javax.net.ssl.SSLContext");
var TrustManager = Java.use("javax.net.ssl.X509TrustManager");
// Implement a custom trust manager that accepts all certificates...
Root Detection Bypass
Hook common root checks like Runtime.exec("su") or Build.TAGS to always return "release-keys".

Automated Input (Monkey / UI Fuzzing)
Use adb shell monkey or Frida’s UiAutomator support to automatically navigate the app and trigger more code paths.

8. Conclusion
You have built a reusable automated APK security analysis lab using Frida. The Python-Frida combo allows you to:

Rapidly instrument any Android application without modifying its APK.

Collect runtime evidence of insecure coding patterns.

Generate actionable security reports automatically.

This framework can be integrated into CI/CD pipelines, malware analysis labs, or bug bounty workflows. The full source code is modular – you can easily swap in new hooks for specific libraries or custom API monitoring.


Download the matching frida-server binary from Frida releases.

Push and start the server:
