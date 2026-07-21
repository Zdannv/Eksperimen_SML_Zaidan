# Eksperimen_SML_Zaidan

Repository eksperimen untuk submission Dicoding Membangun Sistem Machine Learning.

## Struktur

```
Eksperimen_SML_Zaidan/
├── raw_dataset/
├── preprocessing/
│   ├── Eksperimen_Zaidan.ipynb
│   ├── automate_Zaidan.py
│   └── processed_wine.csv
├── requirements.txt
└── README.md
```

## Menjalankan Notebook

1. Install dependency

```bash
pip install -r requirements.txt
```

2. Jalankan notebook `preprocessing/Eksperimen_Zaidan.ipynb`.

## Menjalankan Preprocessing Otomatis

```bash
cd preprocessing
python automate_Zaidan.py
```

Hasil preprocessing akan disimpan sebagai `processed_wine.csv`.
