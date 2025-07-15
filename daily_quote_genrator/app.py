from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

# ✅ Your custom quotes for the first 5 days
my_quotes = [
    "Small deeds done are better than great deeds planned. — Peter Marshall",
    "Have a passion to fly and the destination will come closer on its own.",
    "Faith is taking the first step even when you don't see the whole staircase.",
    "Nothing is scarier than avoiding your full potential.",
    "Growth begins where comfort ends."
]

def fetch_api_quote():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} — {data[0]['a']}"
        else:
            return "Stay positive. Work hard. Make it happen. — Unknown"
    except:
        return "Your mind is a powerful thing. Keep it strong. — Unknown"

@app.route('/')
def home():
    # Set the day you want to start showing your custom quotes from
    start_date = datetime.date(2025, 7, 1)
    today = datetime.date.today()
    day_diff = (today - start_date).days

    # ✅ Use your quote if within the first 5 days, else switch to API
    if 0 <= day_diff < len(my_quotes):
        quote = my_quotes[day_diff]
    else:
        quote = fetch_api_quote()

    return render_template("index.html", quote=quote)

if __name__ == '__main__':
    app.run(debug=True)