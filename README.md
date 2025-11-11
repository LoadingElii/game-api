# GameAPI – NFL Prediction Engine

**GameAPI** is a **FastAPI** microservice that generates and serves NFL game predictions.  
It powers the Java-based `FieldVision` backend by providing predictive analytics and live game data.

---

## Overview
GameAPI retrieves live NFL game data using the `nflreadpy` library and provides machine learning-based predictions.  
It’s lightweight, asynchronous, and designed for easy integration with other microservices.

---

## Tech Stack
- **Language:** Python 3.11  
- **Framework:** FastAPI  
- **Cache:** Redis 
- **Data Source:** nflreadpy  
- **Containerization:** Docker  
- **Testing:** PyTest  
- **Logging:** Python `logging` module  

---

## Modules & Endpoints

### Game Router  
**Base URL:** `/games`

| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/currentweek` | Retrieve current week’s NFL games |

**Example Response:**  
```json
[
  {
    "game_id": "2025_07_PIT_CIN",
    "week": 7,
    "season": 2025,
    "home_team": "CIN",
    "away_team": "PIT",
    "home_score": 14,
    "away_score": 21,
    "gameday": "2025-11-14"
  }
]
```

---

### Prediction Router  
**Base URL:** `/predictions`

| Method | Endpoint | Description                                 |
|---------|-----------|---------------------------------------------|
| GET | `/winprobability/{home_team}/{away_team}` | Get win probability for both teams. |

**Example Response:**  
```json
{
  "home_team": "CAR",
  "away_team": "BUF",
  "home_win_probability": 0.45,
  "away_win_probability": 0.55
}
```

---

## Integration with FieldVision
GameAPI is consumed by the **FieldVision** Spring Boot service for prediction and game data.  
Example integration flow:

1. FieldVision calls `/games/currentweek` to fetch current matchups  
2. FieldVision calls `/predictions/winprobability/{home}/{away}` to fetch predictions  
3. FieldVision combines and serves structured responses to the frontend

---

## Setup & Run

### 1. Clone the repo  
```bash
git clone https://github.com/LoadingElii/game-api.git
cd gameapi
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Run the API  
```bash
uvicorn main:app --reload
```

---

## Testing  
```bash
pytest
```

---

## Author  
**Delijhia Brown**  
- [GitHub](https://github.com/LoadingElii)  
- [LinkedIn](https://linkedin.com/in/delijhia-brown)  
- [YouTube](https://youtube.com/@elicancode)

---

## License  
MIT License
