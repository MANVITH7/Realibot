# 🏠 RealiBot – AI-Powered Real Estate Assistant

RealiBot is a full-stack AI chatbot web application built using Python (Flask) and JavaScript. It helps first-time homebuyers and property investors get real estate insights, such as:
- Median home prices and rent yields (by U.S. state or city)
- Profit/loss and ROI estimates
- Financing, legal, and tax advice
- General real estate Q&A

The AI model is powered by OpenAI’s GPT API, wrapped with custom prompts.

---

## 📁 Project Structure

```
Realibot/
├── backend/
│   └── app.py               # Flask backend
├── public/
│   └── index.html           # Landing page
│   └── chat.html            # Chat UI
├── .gitignore
├── README.md
├── package.json             # Frontend dependencies (optional)
```

---

## ⚙️ Features

- Ask questions about real estate (e.g., prices, taxes, ROI)
- AI-powered responses via OpenAI GPT
- Lightweight frontend (HTML/CSS/JS)
- Backend using Flask API
- Fully deployable to Render or Netlify + Render combo

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/MANVITH7/Realibot.git
cd Realibot
```

### 2. Set Up the Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Your `.env` File

Inside the `backend/` folder, create a `.env` file:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_MODEL=gpt-4
```

> ⚠️ Never commit `.env` to GitHub.

### 4. Run the Flask Server

```bash
python app.py
```

Backend will run at `http://127.0.0.1:5000`

### 5. Open Frontend

Open `public/index.html` directly in your browser or serve using any static server.

---

## 🏗 Deployment

### Deploy Backend (Render)

1. Push the project to GitHub.
2. Go to [Render](https://render.com/)
3. Create a new Web Service:
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
4. Add environment variables:
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL`

### Deploy Frontend (Netlify or GitHub Pages)

Use Netlify:
- Deploy the `public/` folder
- Point to `index.html` as the entry

---

## 🧠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **AI**: OpenAI GPT-4 API
- **Hosting**: Render (backend), Netlify (frontend optional)

---

## 📜 License

This project is open-source and free to use under the MIT License.
