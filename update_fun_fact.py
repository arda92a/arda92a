# update_fun_fact.py
import random
import datetime
import re

# Eğlenceli programlama gerçekleri listesi
fun_facts = [
    "The first computer bug was an actual bug - a moth stuck in a relay in 1947! 🐛",
    "Python was named after Monty Python's Flying Circus, not the snake! 🐍",
    "The term 'debugging' was coined by Grace Hopper in 1947! 🔧",
    "Java was originally called Oak, but had to be renamed due to trademark issues! ☕",
    "The first programming language was created in 1883 for the Jacquard loom! 🧵",
    "HTML was invented in 1990, but the first website is still online today! 🌐",
    "The '@' symbol was used in email for the first time in 1971! 📧",
    "Stack Overflow gets over 50 million visitors per month! 📚",
    "The first computer virus was created in 1971 and was called 'Creeper'! 🦠",
    "JavaScript was created in just 10 days in 1995! ⚡",
    "The average programmer drinks 3-4 cups of coffee per day! ☕",
    "Git was created by Linus Torvalds in just 2 weeks! 🚀",
    "The first programmer in history was Ada Lovelace in 1843! 👩‍💻",
    "There are over 700 programming languages in existence! 🌈",
    "The first computer weighed 30 tons and filled an entire room! 🏢",
    "Google's first server was made from LEGO blocks! 🧱",
    "The term 'spam' comes from a Monty Python sketch! 🥫",
    "Linux penguin mascot is named Tux! 🐧",
    "The first domain name ever registered was symbolics.com in 1985! 🌐",
    "NASA still uses software from the 1970s for some systems! 🚀",
    "The first computer mouse was made of wood! 🖱️",
    "Binary code was invented in 1679, way before computers! 🔢",
    "The first computer programmer bug report was filed in 1947! 📋",
    "YouTube was originally designed as a dating site! 💕",
    "The first iPhone had the same processing power as a 1985 Cray-2 supercomputer! 📱",
    "WiFi stands for nothing - it's not an acronym! 📶",
    "The first computer hard drive was 5MB and cost $10,000! 💾",
    "Facebook's original color scheme was blue because Mark Zuckerberg is colorblind! 💙",
    "The first YouTube video was uploaded on April 23, 2005! 📹",
    "Docker containers can start in less than 100 milliseconds! 🐳",
    "Machine learning algorithms can now write their own code! 🤖",
    "The fastest supercomputer can perform 1 quintillion calculations per second! ⚡",
    "There are more possible chess moves than atoms in the observable universe! ♟️",
    "AI can now detect diseases from medical images with 99% accuracy! 👨‍⚕️",
    "Neural networks were inspired by how the human brain works! 🧠",
    "Deep learning models can have billions of parameters! 📊",
    "Computer vision can now identify objects faster than humans! 👁️",
    "The first AI program was written in 1951! 🤖",
    "GPT-3 has 175 billion parameters! 🧠",
    "Quantum computers could break current encryption in seconds! 🔐",
    "The first webcam was used to monitor a coffee pot! ☕",
    "TensorFlow was originally developed by Google Brain team! 🧠",
    "OpenCV was originally developed by Intel in 1999! 👁️",
    "The word 'algorithm' comes from a 9th-century Persian mathematician! 📚",
    "Rubber duck debugging is a real programming technique! 🦆",
    "The first computer game was created in 1962 and was called 'Spacewar!'! 🎮",
    "Python's import antigravity actually opens an xkcd comic! 🚀",
    "The most expensive domain name ever sold was CarInsurance.com for $49.7 million! 💰",
    "The first computer programmer was paid $3 per hour in 1951! 💵",
    "Reddit was originally written in Lisp but was rewritten in Python! 🐍",
    "The first computer with integrated circuits was built in 1958! 🔧"
]

# AI/ML odaklı özel gerçekler (senin alanınla ilgili)
ai_ml_facts = [
    "I can train a neural network to recognize cats vs dogs with 99% accuracy! 🐱🐶",
    "My computer vision models can process 1000 images per second! 👁️⚡",
    "I once debugged a model for 6 hours only to find a missing comma! 😅",
    "My largest dataset had over 10 million images! 📊",
    "I can make a machine learning model that predicts coffee consumption! ☕🤖",
    "My neural networks dream in tensors and gradients! 🧠💭",
    "I speak fluent Python, but still learning TensorFlow slang! 🐍",
    "My GPU fan sounds like a jet engine when training deep models! 🚁",
    "I've trained models that can generate realistic fake faces! 👤",
    "My computer vision projects can detect emotions from facial expressions! 😊",
    "I can build a chatbot that tells programming jokes! 🤖😄",
    "My data preprocessing pipeline is more complex than the actual model! 🔧",
    "I've created models that can style transfer like Van Gogh! 🎨",
    "My reinforcement learning agent can beat me at simple games! 🎮",
    "I can make AI models that generate code from natural language! 💻"
]

def get_daily_fun_fact():
    """Günlük seed kullanarak aynı gün için aynı fact'i döndürür"""
    today = datetime.date.today()
    seed = today.toordinal()  # Gün sayısına göre seed
    
    random.seed(seed)
    
    # %70 genel programlama, %30 AI/ML odaklı
    if random.random() < 0.7:
        return random.choice(fun_facts)
    else:
        return random.choice(ai_ml_facts)

def update_readme():
    """README.md dosyasındaki fun fact'i günceller"""
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Yeni fun fact al
        new_fact = get_daily_fun_fact()
        
        # Fun fact bölümünü bul ve güncelle
        pattern = r'(\*"[^"]*"\*)'
        replacement = f'*"{new_fact}"*'
        
        updated_content = re.sub(pattern, replacement, content)
        
        # Eğer değişiklik varsa kaydet
        if updated_content != content:
            with open('README.md', 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"✅ Fun fact updated: {new_fact}")
        else:
            print("❌ No changes made to README.md")
            
    except FileNotFoundError:
        print("❌ README.md file not found!")
    except Exception as e:
        print(f"❌ Error updating README: {e}")

if __name__ == "__main__":
    update_readme()
