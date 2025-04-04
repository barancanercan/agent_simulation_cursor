# Tartışma Simülasyonu - Kurallar ve Yapılandırma

## 🎯 Amaç
Bu proje, lokal bilgisayar üzerinde çalışan basit ancak işlevsel bir UI/UX'e sahip bir tartışma simülasyonu sunmayı hedeflemektedir. Kullanıcı tarafından verilen bir **gündem özeti** doğrultusunda, iki yapay zeka ajanı karşılıklı siyasi argümanlarını sunarak interaktif bir tartışma ortamı oluşturur.

## 🧠 Teknoloji ve Altyapı

- **Programlama Dili:** Python  
- **LLM Framework:** Langchain (gerektiğinde)  
- **Dil Modeli:** `deepseek-ai/DeepSeek-R1`  
- **UI/UX:** Yerel arayüz (örneğin Streamlit, Gradio veya Tkinter gibi)

## 🧩 Mimari Yapı

1. Kullanıcı, UI aracılığıyla bir **gündem özeti** yazar.
2. "Simülasyonu Başlat" butonuna tıkladığında simülasyon tetiklenir.
3. İki farklı yapay zeka ajanı, belirli roller çerçevesinde gündemi tartışır.
4. Diyalog, kullanıcı manuel olarak durdurana kadar döngüsel biçimde devam eder.

## 🧑‍🤝‍🧑 Ajan Tanımları

### 🟥 Ajan 1: Deniz
- **Konum:** Ankara / Çankaya  
- **Parti:** CHP  
- **Karakter:** Aydın, kültürlü, entelektüel  
- **Görev:** Gündem özeti doğrultusunda CHP’yi savunur. Karşısındaki kişiyi ikna etmeye çalışır. İlk yorumu yapan kişidir.  
- **Rol:** İlk konuşmayı yapar ve gündemi analiz eder.

### 🟦 Ajan 2: Polat
- **Konum:** Konya / Merkez  
- **Parti:** AKP  
- **Karakter:** Muhafazakar, taşralı, halkçı  
- **Görev:** CHP’li ajanın söylemlerine karşı çıkar, AKP’yi savunur, karşı argümanlar sunar.

## 🔄 Konuşma Döngüsü

1. Deniz (CHP ajanı) gündemi okur ve ilk yorumunu yapar.
2. Polat (AKP ajanı) yanıt verir, CHP söylemlerini çürütmeye çalışır.
3. Bu diyalog sırası döngüsel olarak kullanıcı durdurana kadar devam eder.

## 🚀 Kullanım Notları
- Kullanıcı istediği zaman simülasyonu durdurabilir.
- UI üzerinde geçmiş konuşmalar gösterilebilir.
- Gelişmiş özellikler için argüman puanlama, taraf değiştirme, özetleme gibi eklentiler entegre edilebilir.

---

Bu belge `rules.md` olarak Cursor'a eklenebilir. Uygulamanın mantığını, teknolojisini ve konuşma protokolünü net bir şekilde açıklar.

