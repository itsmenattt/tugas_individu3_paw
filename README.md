# Product Review Analyzer

Aplikasi web full-stack untuk menganalisis review produk dengan AI. Menggunakan Hugging Face untuk sentiment analysis dan Google Gemini untuk ekstraksi key points dari review pelanggan.

## 🚀 Features

- **Sentiment Analysis**: Deteksi sentimen positif, negatif, atau netral menggunakan model Hugging Face
- **Key Points Extraction**: Ekstraksi poin-poin penting dari review menggunakan Google Gemini AI
- **Product Tracking**: Simpan nama produk untuk setiap review
- **Review History**: Lihat riwayat semua review yang telah dianalisis
- **Real-time Analysis**: Analisis instant dengan tampilan hasil yang interaktif
- **Modern UI**: Interface modern dengan React dan Vite

## 📋 Prerequisites

- Python 3.13+
- Node.js 18+
- API Keys:
  - [Hugging Face API Token](https://huggingface.co/settings/tokens)
  - [Google Gemini API Key](https://aistudio.google.com/app/apikey)

## 🛠️ Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd tugas_ai_nadia
```

### 2. Backend Setup

```bash
cd backend

# Buat virtual environment
python -m venv ../env

# Aktifkan virtual environment
# Windows PowerShell:
..\env\Scripts\Activate.ps1
# Windows CMD:
..\env\Scripts\activate.bat

# Install dependencies
pip install --upgrade pip
pip install -e .

# Copy file .env.example dan isi dengan API keys Anda
cp .env.example .env
# Edit backend/.env dengan text editor dan masukkan API keys

# Jalankan migrasi database
alembic -c development.ini upgrade head

# Jalankan server (dari folder backend)
pserve development.ini --reload
```

Backend akan berjalan di http://localhost:6543

### 3. Frontend Setup

Buka terminal baru:

```bash
cd frontend

# Install dependencies
npm install

# Jalankan dev server
npm run dev
```

Frontend akan berjalan di http://localhost:5173

## 🔑 API Keys Setup

### Hugging Face Token
1. Buka https://huggingface.co/settings/tokens
2. Login atau buat akun
3. Klik "New token" → pilih "Read"
4. Copy token dan paste ke `backend/.env`

### Google Gemini API Key
1. Buka https://aistudio.google.com/app/apikey
2. Login dengan Google account
3. Klik "Create API key"
4. Copy key dan paste ke `backend/.env`

## 📁 Project Structure

```
tugas_ai_nadia/
├── backend/                    # Pyramid backend
│   ├── backend/
│   │   ├── __init__.py        # App initialization + .env loader
│   │   ├── routes.py          # API routes
│   │   ├── cors.py            # CORS configuration
│   │   ├── models/
│   │   │   ├── review.py      # ProductReview model
│   │   │   └── meta.py
│   │   ├── services/
│   │   │   ├── sentiment.py  # Hugging Face sentiment analysis
│   │   │   └── keypoints.py  # Gemini key points extraction
│   │   ├── views/
│   │   │   └── default.py     # API endpoints
│   │   └── alembic/
│   │       └── versions/      # Database migrations
│   ├── .env                   # API keys (create this)
│   ├── development.ini        # Pyramid config
│   └── setup.py               # Python dependencies
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── App.jsx            # Main app component
│   │   ├── api.js             # API client
│   │   ├── styles.css         # Styling
│   │   └── components/
│   │       ├── ReviewForm.jsx     # Input form
│   │       ├── ResultsPanel.jsx   # Analysis results
│   │       └── ReviewList.jsx     # Review history
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── env/                        # Python virtual environment
└── README.md
```

## 🎯 Usage

1. Buka http://localhost:5173 di browser
2. Isi **Product name** (contoh: "iPhone 15 Pro")
3. Isi **review** di textarea (contoh: "Amazing phone! Camera is incredible and battery lasts all day. Only downside is the price.")
4. Klik **Analyze Review**
5. Tunggu beberapa detik (API processing)
6. Hasil akan muncul:
   - **Sentiment**: positive/negative/neutral
   - **Score**: confidence level (0-1)
   - **Key points**: bullet points penting dari review
   - **Product**: nama produk yang direview
7. Review tersimpan di panel **Recent Reviews**

## 🔧 Technologies Used

### Backend
- **Pyramid** - Web framework Python
- **SQLAlchemy** - ORM untuk database
- **Alembic** - Database migration tool
- **Hugging Face** - Sentiment analysis model
- **Google Gemini** - AI untuk key points extraction
- **SQLite** - Database (development)
- **Waitress** - WSGI server

### Frontend
- **React 18** - UI library
- **Vite** - Build tool dan dev server
- **Vanilla CSS** - Styling

## 📝 API Endpoints

### `GET /api/health`
Health check endpoint.

**Response:**
```json
{"status": "ok"}
```

### `POST /api/analyze-review`
Analyze a product review.

**Request Body:**
```json
{
  "text": "Review text here",
  "product_name": "Product Name"
}
```

**Response:**
```json
{
  "id": 1,
  "product_name": "Product Name",
  "review_text": "Review text here",
  "sentiment_label": "positive",
  "sentiment_score": 0.95,
  "key_points": ["Point 1", "Point 2", "Point 3"],
  "created_at": "2025-12-14T12:00:00"
}
```

### `GET /api/reviews`
Get all analyzed reviews.

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "product_name": "Product Name",
      "review_text": "Review text",
      "sentiment_label": "positive",
      "sentiment_score": 0.95,
      "key_points": ["Point 1", "Point 2"],
      "created_at": "2025-12-14T12:00:00"
    }
  ]
}
```

## 🐛 Troubleshooting

### Backend tidak bisa start
- Pastikan virtual environment sudah diaktifkan
- Pastikan semua dependencies terinstall: `pip install -e .`
- Cek API keys sudah benar di `backend/.env`

### Frontend error "Failed to fetch"
- Pastikan backend running di port 6543
- Cek CORS settings di `backend/backend/cors.py`
- Verify `VITE_API_BASE_URL` di frontend (default: http://localhost:6543)

### "unable to analyze review"
- Cek API keys valid dan tidak expired
- Lihat error di terminal backend untuk detail
- Pastikan model names benar:
  - Sentiment: `cardiffnlp/twitter-roberta-base-sentiment-latest`
  - Gemini: `gemini-1.5-flash`

## 👥 Authors

Nama : **Nadia Anatashiva**  

NIM  : **123140060**  

Mata Kuliah : **Pengembangan Aplikasi Web - RB**