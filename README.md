# 🚴‍♂️ Bike Sharing Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda harian dan per jam.  
Aplikasi ini menampilkan tren pengguna berdasarkan **waktu, cuaca, dan suhu udara**, serta memungkinkan pengguna memfilter data berdasarkan tanggal.

---

## 📋 Fitur Utama
- Filter tanggal interaktif menggunakan sidebar.
- Visualisasi tren jumlah pengguna per jam.
- Statistik ringkas:
  - Total jumlah pengguna.
  - Suhu udara rata-rata (°C).
  - Cuaca dominan.
- Konversi suhu otomatis ke satuan Celsius (nilai × 41).
- Mapping cuaca otomatis:
  - 1 → Clear  
  - 2 → Mist  
  - 3 → Light Rain  
  - 4 → Heavy Rain  

---
## ⚙️ Setup Environment - Anaconda

```bash
conda create --name dashboard python=3.10
conda activate dashboard
pip install -r requirements.txt 
```

---
## ⚙️ Setup Environment - Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## ⚙️ Setup Environment - Anaconda
```bash
streamlit run dashboard.py
```

