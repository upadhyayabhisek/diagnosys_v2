#mediai

A health analysis platform designed for the Nepal context, featuring a Nuxt 3 frontend and a Flask AI backend.

---

## Project Structure

- **nuxt-app**: Frontend built with Nuxt 3 and Tailwind CSS.
- **python-backend**: Flask API for symptom analysis and disease prediction.

---

## Getting Started

### Frontend

```bash
cd nuxt-app
npm install
npm run dev
```

### Backend

```bash
cd python-backend
pip install -r requirements.txt
python app.py
```

---

## Testing

The project uses **pytest** for backend validation. The CI pipeline automatically runs these tests on every push to the main branch.

**Run tests locally:**

```bash
cd python-backend
pytest
```

---

## Features

- **Symptom Prediction**: AI-driven analysis of user symptoms.
- **Bilingual Support**: Functional in both English and Nepali.
- **Nepal Emergency Integration**: Quick access to local services like 102 (Ambulance) and 100 (Police).

---

## API Endpoints

**POST /analyze**
Analyzes symptoms and returns potential matches with a confidence score.

```json
{
  "message": "High fever and headache",
  "lang": "en"
}
```

---

## Disclaimer

diagnosys is an informational tool and does not provide medical diagnoses. For emergencies in Nepal, dial 102 or 100 immediately.
