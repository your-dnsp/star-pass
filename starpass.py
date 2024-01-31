import random
import string

# Astrology-related words
astrology_words = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
    "Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn",
    "Uranus", "Neptune", "Pluto", "Chiron", "Sirius", "Vega", "Rigel",
    "Betelgeuse", "Aldebaran", "Spica", "Regulus", "Antares", "Fomalhaut",
    "Orion", "Andromeda", "Lyra", "Draco", "Phoenix", "Centaurus", "Cassiopeia",
    "Cygnus", "Hercules", "Pegasus", "Perseus", "UrsaMajor", "UrsaMinor",
    "Aquila", "Ara", "Aries", "Auriga", "Bootes", "Caelum",
    "Camelopardalis", "Cancer", "CanesVenatici", "CanisMajor", "CanisMinor", "Capricornus",
    "Carina", "Cassiopeia", "Centaurus", "Cepheus", "Cetus", "Chamaeleon",
    "Circinus", "Columba", "ComaBerenices", "CoronaAustralis", "CoronaBorealis", "Corvus",
    "Crater", "Crux", "Cygnus", "Delphinus", "Dorado", "Draco",
    "Equuleus", "Eridanus", "Fornax", "Gemini", "Grus", "Hercules",
    "Horologium", "Hydra", "Hydrus", "Indus", "Lacerta", "Leo",
    "LeoMinor", "Lepus", "Libra", "Lupus", "Lynx", "Lyra",
    "Mensa", "Microscopium", "Monoceros", "Musca", "Norma", "Octans",
    "Ophiuchus", "Orion", "Pavo", "Pegasus", "Perseus", "Phoenix",
    "Pictor", "Pisces", "PiscisAustrinus", "Puppis", "Pyxis", "Reticulum",
    "Sagitta", "Sagittarius", "Scorpius", "Sculptor", "Scutum", "Serpens",
    "Sextans", "Taurus", "Telescopium", "Triangulum", "TriangulumAustrale", "Tucana",
    "UrsaMajor", "UrsaMinor", "Vela", "Virgo", "Volans", "Vulpecula",
    "Conjunction", "Opposition", "Trine", "Square", "Sextile", "Quincunx",
    "Semisextile", "Semisquare", "Sesquiquadrate", "Biquintile", "Quintile", "Ascendant",
    "Descendant", "Midheaven", "IC", "NorthNode", "SouthNode", "Retrograde",
    "Direct", "Stationary", "Eclipse", "Solstice", "Equinox", "Transit",
    "Progression", "Return", "Ingress", "Aspect", "Orbit", "Ephemeris"
]


# Leet speak substitutions
leet_speak = {
    'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '1',
    'l': '1', 'o': '0', 's': '$', 't': '7', 'z': '2',
    'c': '<', 'd': '6', 'h': '#', 'k': '|<', 'p': '|D',
    'r': '|2', 'x': '%', 'q': '9'
}



def generate_password(sign, length):
    # Select two random astrology words
    words = random.sample(astrology_words, 2)

    # Convert to leet speak randomly
    password = ''
    for word in words:
        for char in word:
            if char.lower() in leet_speak and random.choice([True, False]):
                password += leet_speak[char.lower()]
            else:
                password += char

    # Add random characters to meet the desired length
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Trim to match the exact length without shuffling
    password = password[:length]

    return password

# User interaction
print("What is your sign? (You can respond with 'I don't know')")
user_sign = input()

# Ensuring password length is at least 14 characters
while True:
    print("How many characters do you want your password to be? (Minimum 14 characters)")
    password_length = int(input())
    if password_length >= 14:
        break
    print("Password length must be at least 14 characters.")

generated_password = generate_password(user_sign, password_length)
print("Generated Password:", generated_password)
