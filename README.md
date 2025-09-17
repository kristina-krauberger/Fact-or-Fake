# Fact or Fake Wiki-Game 🎮  

**Hackathon Project – Awarded *Best Game***  

A text-based multiplayer game where players distinguish between real and fake Wikipedia articles. Test your knowledge and sharpen your ability to detect fake news!  

---

## 📖 Description  
The *Fact or Fake* Wiki-Game is an educational and entertaining project developed during a 3-day hackathon.  
Players are presented with two statements – one true (*Fact*), one false (*Fake*) – and must identify the fake article.  

---

## ✨ Features  
- **Multiplayer mode**: Up to 5 players can compete against each other  
- **Difficulty levels**: Easy, Medium, Hard  
- **Real-time Wikipedia data**: Facts are pulled live from Wikipedia via API  
- **Colorful console interface** for an engaging experience  
- **Scoring system**: Track your progress and compare results  

---

## 🛠️ Requirements  
- Python 3.6 or higher  
- Installed Python packages: `wikipedia`, `beautifulsoup4`, `requests`  

---

## 🚀 Installation  

Clone the repository:  
```bash
git clone https://github.com/kristina-krauberger/fact-or-fake.git
cd fact-or-fake
```

Create a virtual environment (optional but recommended):  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies:  
```bash
pip install wikipedia beautifulsoup4 requests
```

Start the game:  
```bash
python main.py
```

---

## 🎲 Game Rules  
- **Players**: 1–5  
- **Gameplay**:  
  - Each round presents two statements  
  - One is *Fact*, the other is *Fake*  
  - Players must identify the fake statement  
- **Scoring**:  
  - Correct = 1 point  
  - Incorrect = turn passes to next player  
- **Game End**: After 2 rounds, the winner is declared  

---

## 📂 Project Structure  

```
fact-or-fake/
│
├── main.py                 # Main program & game logic
├── controller/
│   └── question_generator.py   # Generates questions & article pairs
├── view/
│   └── game_gui.py             # Console UI
└── README.md
```

---

## 👥 Team & My Role  
This project was developed during a 3-day hackathon by a diverse 7-person team.  
The original repository was created and maintained by [Martin (Mk97x)](https://github.com/Mk97x). 

My contributions included:  
- **Project coordination**: structured meetings & time planning
- **Coded input functionality**: implemented player input handling to support game interaction  
- **Team communication & collaboration**: ensured smooth interaction across different skill levels  

---

## 🏆 Outcome  
- Awarded **Best Game** of the hackathon – recognized not only for the idea and coding, but especially for **outstanding teamwork and collaboration**.  
