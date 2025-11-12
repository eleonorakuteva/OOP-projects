# 🧗‍♂️ Climbers and Peaks – Summit Quest Manager

A Python OOP project that simulates climbers attempting to conquer various peaks based on their strength, preparedness, and available gear.

---

## 📋 Overview

This project models a **mountain climbing expedition system**, where:
- Climbers register for expeditions.
- Peaks with different difficulty levels are added to a wish list.
- Climbers check their equipment before attempting climbs.
- Successful climbs and statistics are tracked.

The app’s main entry point is the **`SummitQuestManagerApp`** class.

---

## 🏗️ Project Structure

climbers_and_peaks/  
│   
└── project/  
    │  
    ├── climbers/  
    │   ├── base_climber.py  
    │   ├── arctic_climber.py  
    │   └── summit_climber.py  
    │  
    ├── tests/  
    │   └── test_summit_quest_manager_app.py  
    │  
    ├── peaks/  
    │   ├── base_peak.py  
    │   ├── arctic_peak.py  
    │   └── summit_peak.py  
    │  
    ├── summit_quest_manager_app.py  
    └── README.md  



 


---

## 🧩 Key Components

### 🧍‍♂️ **Climbers**
- **`BaseClimber`** – Abstract class with shared attributes (`name`, `strength`, `conquered_peaks`).
- **`ArcticClimber`** – Strong climber suited for extreme arctic conditions.
- **`SummitClimber`** – Skilled technical climber specialized in high-altitude peaks.

### 🏔️ **Peaks**
- **`BasePeak`** – Abstract class for peak properties and validation.
- **`ArcticPeak`** – Peak type with ice and cold-weather gear requirements.
- **`SummitPeak`** – Peak type requiring advanced climbing equipment.

### 🚀 **SummitQuestManagerApp**
The main application class that:
- Registers climbers and peaks.
- Checks if climbers have required gear.
- Performs climbs based on conditions.
- Generates statistics of conquered peaks.

---


