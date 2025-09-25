random → used to pick random traits so the horoscope doesn’t look the same every time.
datetime → used to parse the user’s birth date and time.
The zodiac is determined by date ranges.
Each zodiac sign is mapped to a list of personality traits.
random.sample(traits_dict[zodiac], 2) → picks two random traits for variety.
if hour < 6 … → horoscope advice depends on time of day.
here i am using a rule based Ai (Expert System)
