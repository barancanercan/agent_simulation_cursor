# 🗣️ Siyasi Tartışma Simülasyonu

Bu proje, yapay zeka ajanları arasında siyasi tartışmaları simüle eden bir uygulamadır. İki farklı siyasi görüşe sahip ajan (Deniz ve Polat), kullanıcı tarafından belirlenen gündem üzerinde tartışır.

## 🚀 Özellikler

- İnteraktif web arayüzü
- Gerçek zamanlı tartışma simülasyonu
- İki farklı siyasi karakterin temsili
- Kullanıcı tarafından belirlenebilen gündem

## 🛠️ Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
cd agent_simulation_cursor
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
- DeepSeek ekibine AI modeli için 