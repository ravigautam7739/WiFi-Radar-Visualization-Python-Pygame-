# 📡 WiFi Radar Visualization (Python + Pygame)

A visually interactive **WiFi Radar** that displays nearby networks based on signal strength.

Stronger signals appear closer to the center, just like a radar system.

---

# 🚀 Features

✔ Detects nearby WiFi networks
✔ Displays signal strength visually
✔ Radar-style animated interface
✔ Real-time network visualization
✔ Smooth animation using Pygame

---

# 🛠 Technologies Used

* Python
* Pygame
* Subprocess (netsh command)

---

# 📂 Project Structure

```
wifi-radar
│
├── wifi_radar.py
└── README.md
```

---

# ⚙️ Installation

Install dependencies:

```bash
pip install pygame
```

---

# ▶️ How to Run

```bash
git clone https://github.com/ravigautam7739/wifi-radar.git
cd wifi-radar
python wifi_radar.py
```

---

# 🧠 How It Works

1. Uses system command to fetch WiFi networks
2. Extracts SSID and signal strength
3. Converts signal into distance
4. Displays networks on radar screen
5. Animates radar sweep

---

# 💻 Output

* Green radar screen
* Networks shown as dots
* Labels with SSID and signal %
* Moving radar sweep

---

# ⚠️ Note

* Works best on **Windows (netsh command)**
* Demo data used if scan fails

---

# 🔮 Future Improvements

* Cross-platform support
* Real-time refresh
* Device filtering
* UI enhancements

---

# ⭐ Support

Star ⭐ the repo if you like this project!
