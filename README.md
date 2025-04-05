# 🗣️ Siyasi Tartışma Simülasyonu

Bu proje, yapay zeka destekli siyasi tartışma simülasyonu uygulamasıdır.

## 🚀 Özellikler

- CHP ve AKP taraftarı seçmenler arasında siyasi tartışma simülasyonu
- Kararsız-küskün seçmen (Miraç) perspektifinden tartışma analizi
- Streamlit tabanlı kullanıcı arayüzü
- Google Gemini API kullanarak yapay zeka destekli yanıtlar

## 🛠️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/barancanercan/agent_simulation_cursor.git
cd siyasi-tartisma-simulasyonu
```

2. Sanal ortam oluşturun ve aktive edin:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# veya
.venv\Scripts\activate  # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

## 🎮 Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run src/app.py
```

2. Web tarayıcınızda `http://localhost:8501` adresine gidin
3. Sidebar'dan tartışma gündemini girin
4. "Simülasyonu Başlat" butonuna tıklayın
5. Tartışmayı izleyin ve istediğiniz zaman durdurun

## 🧩 Proje Yapısı

```
.
├── README.md
├── requirements.txt
├── rules/
│   └── rules.md
├── src/
│   ├── app.py
│   └── agents.py
├── templates/
└── static/
```

## 🤝 Katkıda Bulunma

1. Bu repo'yu fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## 🙏 Teşekkürler

- Streamlit ekibine harika framework için
- Gemini ekibine AI modeli için

## Canlı Uygulama

Uygulamayı şu adresten canlı olarak deneyebilirsiniz:
https://siyasitartisma.streamlit.app/ 