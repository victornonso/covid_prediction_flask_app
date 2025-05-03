**COVID-19 Risk Predictor App**
An interactive Flask‑based web service that predicts the likelihood of a user having COVID‑19 based on demographic information and self‑reported symptoms. Built with Python,Flask scikit‑learn, and Flask, this app combines data science and healthcare insights to provide a quick assessment tool.

---

## 🚀 Features

* **Accurate Predictions**: Gradient Boostingl tuned via cross‑validation
* **Interactive Web Interface**: Simple HTML form to input age, sex, and symptoms.
* **RESTful API**: `/predict` endpoint for integrating predictions into other applications.

---

## 📂 Dataset

* Collected by eHealth Africa in Hocus Pocus town.
* Contains demographic fields (Age, Sex) and \~40 binary symptom indicators (e.g., Cough, Fever, Difficulty Breathing).
* Test results labeled as `POSITIVE` or `NEGATIVE`.

> **Note:** Pending results were excluded during preprocessing.

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/victornonso/covid-prediction_flask_app.git

   ```
2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃‍♂️ Usage

### Run Locally

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Navigate to `http://127.0.0.1:5000/` in your browser to access the web form.

### API Endpoint

* **POST** `/predict`

  * **Request Body** (JSON):

    ```json
    {
      "age": 35,
      "sex": "MALE",
      "fever": 1,
      "cough": 0,
      "difficulty_breathing": 1,
      ...
    }
    ```
  * **Response**:

    ```json
    {
      "prediction": 1,       // 1 = POSITIVE, 0 = NEGATIVE
      "probability": 0.87
    }
    ```



---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Data Science**: scikit‑learn, pandas, numpy, matplotlib
* **Deployment**: Gunicorn, Docker (optional)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for enhancements, bug fixes, or new features.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request 📬

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

Made with ❤️ by eHealth Africa Team.
For questions or suggestions, please reach out at [email@example.com](mailto:victornonso44@gmail.com).
