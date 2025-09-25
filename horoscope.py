import random
from datetime import datetime

# Zodiac calculation
def get_zodiac(day, month):
    zodiac_dates = [
        (120, "Capricorn"), (218, "Aquarius"), (320, "Pisces"), (419, "Aries"),
        (520, "Taurus"), (620, "Gemini"), (722, "Cancer"), (822, "Leo"),
        (922, "Virgo"), (1022, "Libra"), (1121, "Scorpio"), (1221, "Sagittarius"), (1231, "Capricorn")
    ]
    mmdd = month*100 + day
    for date, sign in zodiac_dates:
        if mmdd <= date:
            return sign

# Personality traits
traits_dict = {
    "Aries": ["courageous", "energetic", "willful"],
    "Taurus": ["reliable", "patient", "devoted"],
    "Gemini": ["adaptable", "outgoing", "intelligent"],
    "Cancer": ["intuitive", "emotional", "loyal"],
    "Leo": ["confident", "generous", "cheerful"],
    "Virgo": ["analytical", "kind", "hardworking"],
    "Libra": ["diplomatic", "charming", "social"],
    "Scorpio": ["passionate", "resourceful", "brave"],
    "Sagittarius": ["adventurous", "optimistic", "honest"],
    "Capricorn": ["disciplined", "responsible", "ambitious"],
    "Aquarius": ["innovative", "independent", "humanitarian"],
    "Pisces": ["compassionate", "artistic", "gentle"]
}

# Horoscope generation
def generate_horoscope(zodiac, hour):
    traits = random.sample(traits_dict[zodiac], 2)
    if hour < 6:
        advice = "Early morning brings clarity and peace."
    elif hour < 12:
        advice = "Morning energy is high, act wisely."
    elif hour < 18:
        advice = "Afternoon favors productivity and opportunities."
    else:
        advice = "Evening is ideal for reflection and planning."
    return f"Zodiac: {zodiac}\nTraits: {traits[0]}, {traits[1]}\nHoroscope: {advice}"

# Main
birth_date = input("Enter birth date (YYYY-MM-DD): ")
birth_time = input("Enter birth time (HH:MM): ")
dt = datetime.strptime(birth_date + " " + birth_time, "%Y-%m-%d %H:%M")
zodiac = get_zodiac(dt.day, dt.month)
print(generate_horoscope(zodiac, dt.hour))
