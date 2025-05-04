# quickhealth.py

import time

print("🩺 Welcome to Quick Health Checker")
time.sleep(5)

# 1. User Profile
name = input("👤 Enter your name: ")
age_input = input("🎂 Enter your age (numeric): ")
gender = input("⚧️ Enter your gender (male/female/other): ")
city = input("🌆 Enter your city: ")

# Basic age validation
if age_input.isnumeric():
    age = int(age_input)
else:
    print("❌ Invalid age. Please restart the script and enter a number.")
    exit()

# 2. Health Inputs
symptom = input("🤒 Main symptom (fever, cough, fatigue, headache, chest pain, breathlessness): ")
temp_input = input("🌡️ Enter your body temperature in °F: ")
days_sick_input = input("📅 How many days have you been sick?: ")
smoking = input("🚬 Do you smoke? (yes/no): ")
sleep_input = input("🛌 How many hours do you sleep per day?: ")
mood = input("🧠 What's your current mood? (calm, anxious, sad, irritable): ")
pre_condition = input("🏥 Do you have any pre-existing conditions? (yes/no): ")

# Directly converting inputs without validation
temperature = float(temp_input)
sick_days = int(days_sick_input)
sleep = int(sleep_input)

# 3. Risk Scoring
score = 0

if temperature >= 102 or sick_days > 3:
    score += 3

if age >= 60 and symptom == "fever":
    score += 2

if symptom == "cough" and sick_days >= 5:
    score += 2

if symptom == "fatigue" and age > 30:
    score += 2

if symptom == "headache" and temperature > 100:
    score += 2

if symptom == "chest pain":
    score += 3

if symptom == "breathlessness":
    score += 4

if smoking == "yes":
    score += 2

if sleep < 6:
    score += 1

if mood in ["anxious", "sad", "irritable"]:
    score += 1

if pre_condition == "yes":
    score += 2

# 4. Risk Result
print(f"\n🔍 Health Risk Analysis for {name}")
print("📊 Total Score:")
time.sleep(5)

if score <= 3:
    print("🟢 You are at Low Risk. Stay healthy! 🍀")
elif score <= 6:
    print("🟠 You are at Moderate Risk. Monitor your symptoms. 🤒")
else:
    print("🔴 You are at High Risk. Please consider medical attention. 🚑")
time.sleep(5)

# 5. Personalized Advice
print("\n💡 Personalized Health Advice:")
if gender == "female" and age >= 45:
    print("- 👩‍⚕️ Consider going for a full health screening.")

if gender == "male" and smoking == "yes":
    print("- 🚭 Quitting smoking is highly recommended.")

if sleep < 6:
    print("- 💤 Try to get at least 6–8 hours of sleep.")

if mood == "anxious":
    print("- 🧘 Practice relaxation or box breathing techniques.")

if pre_condition == "yes":
    print("- 📞 Monitor your symptoms and consult a doctor soon.")

print(f"- 🏥 Nearest urgent care is in your city: {city}")
time.sleep(5)

# 6. Mental Health Tip
print("\n🧘 Mental Health Tip:")
if mood == "calm":
    print("🌟 Keep up the positive attitude!")
elif mood == "sad":
    print("💬 Talk to a friend or therapist.")
elif mood == "anxious":
    print("🫁 Try 4-7-8 breathing: inhale 4s, hold 7s, exhale 8s.")
elif mood == "irritable":
    print("🛑 Take a short break or walk to reset.")
time.sleep(5)

print("\n✅ Thank you for using Quick Health Checker! Stay safe and take care. 🤗")
