# 🗣️ Siyasi Tartışma Simülasyonu

Bu proje, yapay zeka destekli siyasi tartışma simülasyonu uygulamasıdır.

## 🚀 Özellikler

- CHP ve AKP taraftarı seçmenler arasında siyasi tartışma simülasyonu
- Kararsız-küskün seçmen (Miraç) perspektifinden tartışma analizi
- Streamlit tabanlı kullanıcı arayüzü
- Google Gemini API kullanarak yapay zeka destekli yanıtlar
- Konuşma geçmişi özelliği ile önceki tartışmalara erişim
- Yeni konuşma başlatma ve mevcut konuşmayı silme seçenekleri

## 🛠️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/barancanercan/agent_simulation_cursor.git
cd agent_simulation_cursor
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

## 💻 Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run src/app.py
```

2. Sol menüden tartışma gündemini girin
3. "Simülasyonu Başlat" butonuna tıklayın
4. Tartışmayı durdurmak için "Simülasyonu Durdur" butonunu kullanın
5. Yeni bir konuşma başlatmak için "Yeni Konuşma" butonunu kullanın
6. Mevcut konuşmayı silmek için "Konuşmayı Sil" butonunu kullanın
7. Önceki tartışmalara erişmek için sidebar'daki "Konuşma Geçmişi" bölümünü kullanın

## 🌐 Canlı Uygulama

Uygulamayı şu adresten canlı olarak deneyebilirsiniz:
https://siyasitartisma.streamlit.app/

## 📝 Kurallar

1. Her ajan kendi siyasi görüşüne göre cevap verir
2. Konuşma sırası: Deniz -> Polat -> Miraç
3. Miraç, kararsız-küskün seçmen olarak her iki tarafı da değerlendirir
4. Her ajan önceki mesajları dikkate alır

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: X'`)
4. Dalınıza push yapın (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun

## 📄 Lisans

MIT 