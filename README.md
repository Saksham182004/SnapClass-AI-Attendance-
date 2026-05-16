# SnapClass — AI-Powered Classroom Attendance

SnapClass automates classroom attendance using face recognition and voice identification. Teachers scan classroom photos or record audio; the AI marks who is present. Students register once with their face and voice, then get detected automatically every class.

**Live Demo → [snapattend.streamlit.app](https://snapattend.streamlit.app)**

---

## How It Works

### Teacher Flow
1. Create a subject and share the join code (or QR) with students
2. Upload classroom photos **or** record classroom audio
3. Hit **Run Face Analysis** / **Analyse Audio** — AI marks attendance instantly
4. View session-wise attendance records from the dashboard

### Student Flow
1. Register a face profile (3+ photos) and voice profile
2. Join subjects via teacher-shared code or QR scan
3. Get marked present automatically — no action needed in class

---

## AI Pipelines

### Face Recognition
- **Detector:** dlib HOG-based frontal face detector
- **Landmarks:** 68-point shape predictor for face alignment
- **Embeddings:** 128-dimensional face descriptors via `dlib.face_recognition_model_v1`
- **Classifier:** Linear SVM (`sklearn.SVC`, balanced class weights) trained on all enrolled student embeddings
- **Validation:** Euclidean distance threshold ≤ 0.6 — predictions above threshold are rejected to avoid false matches
- **Caching:** dlib models and trained SVM cached via `st.cache_resource`; SVM cache is selectively cleared and retrained whenever a new student enrolls

### Voice Identification
- **Encoder:** `resemblyzer.VoiceEncoder` producing 256-dimensional speaker embeddings
- **Matching:** Cosine similarity (`np.dot`) with a threshold of 0.65
- **Bulk Processing:** `librosa.effects.split(top_db=30)` segments classroom audio into individual utterances; segments under 0.5s are filtered out; each segment is matched independently against all enrolled voice profiles

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend / App | Streamlit |
| Database | Supabase (PostgreSQL) |
| Face Recognition | dlib, face_recognition_models, scikit-learn |
| Voice Recognition | resemblyzer, librosa |
| Auth | bcrypt |
| QR Codes | segno |
| Data Processing | pandas, numpy, Pillow |

---

## Project Structure

```
app.py                          # Entry point, session routing
src/
  screens/
    home_screen.py              # Landing page
    teacher_screen.py           # Teacher dashboard (tabs: attendance, subjects, records)
    student_screen.py           # Student dashboard (face login, enrollment, history)
  pipelines/
    face_pipeline.py            # dlib + SVM face recognition
    voice_pipeline.py           # resemblyzer + librosa voice identification
  components/
    subject_card.py             # Subject card UI component
    dialog_create_subject.py    # Create subject dialog
    dialog_share_subject.py     # QR + link share dialog
    dialog_add_photo.py         # Face profile registration
    dialog_enroll.py            # Manual subject enrollment
    dialog_auto_enroll.py       # Auto-enroll via join-code URL param
    dialog_attendance_results.py # Results + confirm/save attendance
    dialog_voice_attendance.py  # Voice attendance recording + analysis
  database/
    config.py                   # Supabase client init
    db.py                       # All database queries
  ui/
    base_layout.py              # Global CSS, fonts, background
```

---

## Local Setup

**Prerequisites:** Python 3.10+, a Supabase project

```bash
git clone https://github.com/your-username/SnapClass-AI-Attendance
cd SnapClass-AI-Attendance
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

```bash
streamlit run app.py
```

---

## Database Schema

| Table | Key Columns |
|---|---|
| `teachers` | `teacher_id`, `username`, `password` (bcrypt), `name` |
| `students` | `student_id`, `name`, `face_embedding`, `voice_embedding` |
| `subjects` | `subject_id`, `subject_code`, `name`, `section`, `teacher_id` |
| `subject_students` | `student_id`, `subject_id` |
| `attendance_logs` | `student_id`, `subject_id`, `timestamps`, `is_present` |

---

## Features at a Glance

- Multi-photo scanning — queue N classroom photos, detect all faces across all images in one pass
- Voice attendance — record classroom audio once, identify multiple students from a single recording
- QR code join links — students scan to auto-enroll into a subject
- Session-wise attendance records — grouped by timestamp, aggregated with present/total counts
- Face-ID student login — no passwords for students, face is the credential
