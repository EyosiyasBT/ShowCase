# ShowCase - The Home of Proof of Concepts
Welcome to **ShowCase**, a collection of projects, ideas, and experiments I’ve worked on — whether completed, attempted, or failed [hopefully this will be a place of only completed projects]. For me, programming is about exploring crazy ideas and trying to bring them to life. Most things can be created, and most problems solved, given enough time, effort, and simplifications.

---

## PokR - v1.0
**PokR** is a proof-of-concept tool designed to calculate the winning probability in Texas Hold'em poker (1 deck, 2-hand poker with 5 community cards). It combines object detection with automated probability calculation to make analyzing poker scenarios easy and efficient. This version, v1.0, works with both a physical camera and with screenrecording.\
*This project from the research, exploration, training, programming, fixing the gui, and writing the documentation has taken me 39 hours and 10 minutes.*

<p align="center">
  <img src="INIT_GITHUB\PokR\Image_real_combined.png" title="Poker Card Detection" alt="Poker Card Detection" width="1000" />
</p>

---

### 🔑 Features
- **Multi-Mode Input**: Analyze cards using screen recording or an external camera.
- **Real-Time Detection**: Leverages YOLOv8 and YOLO11 for poker card detection.
- **Automated Odds Calculation**: Detected cards are seamlessly passed to an online poker odds calculator.
- **Customizable Settings**: Adjust detection thresholds, input sources, and more.

---

### ⚙️ Key Options
| **Option**          | **Default** | **Description**                                                                                  |
|----------------------|-------------|--------------------------------------------------------------------------------------------------|
| **`screen_record`** | `True`      | Use screen recording (`True`) or an external camera (`False`).                                   |
| **`num_opponents`** | `4`         | Number of opponents in the poker game (1–10).                                                   |
| **`conf_value`**    | `0.25`      | Confidence threshold for detection (0–1).                                                      |
| **`iou_value`**     | `0.5`       | Intersection over Union (IoU) threshold for filtering overlapping detections (0–1).             |

---

### 🛠️ Tech Stack
- **Language**: Python
- **Models**: YOLOv8, YOLO11
- **Key Libraries**: Selenium, OpenCV, pyautogui, tkinter, Pillow

---

### 📝 Credits
- **Dataset**: [Playing Cards Dataset by Augmented Startups](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d)
- **Calculator**: [Poker Odds Calculator by de Wet, R.](https://www.omnicalculator.com/other/poker-odds)
- **Models**: [YOLOv8 and YOLO11 by Ultralytics](https://github.com/ultralytics/ultralytics)
