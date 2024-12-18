# User Guide for PokR Program

This guide explains how to use the PokR tool, which calculates winning probabilities for Texas Hold'em poker using a combination of computer vision and web automation.

---



## Step 1: Select Program Options
Before starting the program, select the appropriate mode and configuration settings:

### Modes
1. **Screen Recording Mode**:
   - Use the program to analyze a region of your screen (e.g., a video or game).
   - The region can be selected dynamically by clicking and dragging.

2. **Camera Mode**:
   - Use an external camera (e.g., webcam) to capture the cards for analysis.

---

### Configuration Settings
- **`screen_record`**:
  - Set to `True` for screen recording mode.
  - Set to `False` for camera mode.
- **`num_opponents`**:
  - Specify the number of opponents in the poker game (default: `4`, range: `[1, 10]`).
- **`conf_value`**:
  - Confidence threshold for YOLO detection (default: `0.25`, range: `[0, 1]`).
- **`iou_value`**:
  - Intersection over Union (IoU) threshold for filtering overlapping detections. IoU measures the overlap between two bounding boxes, and this value determines whether a box is retained or discarded during filtering (default: `0.5`, range: `[0, 1]`).

---

### Model Selection and Detection Process

The program leverages the following logic to process detections using selected YOLO models and filters results based on the Intersection over Union (IoU) metric.

#### **Model Selector: `list_models`**
The `list_models` variable allows you to specify which YOLO models are used for detection. You can customize it by uncommenting the desired models. The available models are:

- **YOLOv8 Models**:
  - `yolov8n_last.pt` - Last checkpoint for YOLOv8n.
  - `yolov8n_best.pt` - Best checkpoint for YOLOv8n.

- **YOLO11 Models**:
  - `yolo11n_last.pt` - Last checkpoint for YOLO11n.
  - `yolo11n_best.pt` - Best checkpoint for YOLO11n.
  - `yolo11m_last.pt` - Last checkpoint for YOLO11m.
  - `yolo11m_best.pt` - Best checkpoint for YOLO11m.
  - `yolo11m_42_last.pt` - Last checkpoint for YOLO11m (epoch 42).
  - `yolo11m_42_best.pt` - Best checkpoint for YOLO11m (epoch 42).

**Default Configuration**:
The program defaults to the `yolo11m_42_best.pt` model:
```python
list_models = [
    model_11m_42_best
]
```

---

## Step 2A: Using Screen Recording Mode
1. Set `screen_record = True` in the code.
2. When the program starts, you will be prompted to define the region of your screen:
   - A transparent overlay will appear.
   - **Click and drag** to select the rectangular area to capture.
   - Release the mouse to confirm the selection.
3. The program will use this region as input for detection and analysis.
<p align="center">
  <img src="..\INIT_GITHUB\PokR\Image_screenshot_select_area.png" title="Poker Card Detection" alt="Poker Card Detection" height="350" />
</p>
<p align="center">
  <img src="..\INIT_GITHUB\PokR\Image_screenshot_poker_combined.png" title="Poker Card Detection" alt="Poker Card Detection" height="400" />
</p>

<p align="center">
  <img src="..\INIT_GITHUB\PokR\Image_screenshot_omni_combined.png" title="Poker Card Detection" alt="Poker Card Detection" width="700" />
</p>
---

## Step 2B: Using Camera Mode
1. Set `screen_record = False` in the code.
2. Ensure your external camera is connected and recognized by the program.
3. The program will automatically start capturing input from your camera.

<p align="center">
  <img src="..\INIT_GITHUB\PokR\Image_real_combined.png" title="Poker Card Detection" alt="Poker Card Detection" width="900" />
</p>

---

## Step 3: Running the Program
Once the input source is selected, the program will:
1. Display a real-time feed of the selected region (screen or camera) in an OpenCV window titled **"YOLO Detection"**.
2. Highlight detected cards with bounding boxes and labels (class name and confidence score).

---

## Step 4: Controls
### Key Actions:
- **`Spacebar`**:
  - Toggles between **Live Mode** and **Freeze Mode**.
  - In **Freeze Mode**:
    - The current frame is captured and analyzed.
    - Detected cards are extracted from the frame and passed to the poker odds calculator for evaluation.
    - A browser window is automatically opened to compute the odds based on the identified cards.
  - In **Live Mode**:
    - The program continuously captures and displays the live video feed, without analysis.
    - You can interact with the program, but no card analysis or poker odds calculation takes place.
    
- **`Q`**:
  - Closes the program, quitting the live feed, and shutting down all windows.

---

## Step 5: Viewing Results
1. **In Freeze Mode**:
   - Once the frame is frozen, the detected cards are displayed within the OpenCV window.
   - Simultaneously, a browser window opens, showing the poker odds calculator, with the detected cards already populated in the input fields.
   - The user can then see the probabilities based on the current hand.
   
2. **In Live Mode**:
   - The camera feed continues to be displayed in real-time without interruption.
   - No card analysis occurs in this mode, allowing the user to freely observe the live feed and navigate to other tasks.

---

## Tips and Troubleshooting
- **Accuracy**:
  - If detection is not optimal, adjust the `conf_value` and `iou_value` settings to enhance the model’s performance. Fine-tuning these values can improve detection precision, particularly in varying lighting conditions or when objects are overlapping.
  
- **Screen Region Selection**:
  - Ensure that the selected screen region only contains the cards you wish to analyze. Including unnecessary background or additional objects can degrade the accuracy of the card detection.

- **Camera Feed Issues**:
  - If the camera feed does not open, ensure the device is properly connected and recognized by the system. Additionally, confirm that the program has the necessary permissions to access the camera hardware.

---

## Example Usage
1. **Start the Program**:
   - Set `screen_record = True` to begin the process with screen recording. Alternatively, adjust the setting for live camera mode if preferred.
   
2. **Select the Region**:
   - Define the area on the screen that contains the cards by selecting the region via the interface.

3. **Toggle to Freeze Mode**:
   - Press the **spacebar** to freeze the current frame. The program will capture and analyze the detected cards.
   - The browser will open, displaying the odds calculator with the detected cards pre-filled for immediate evaluation.

4. **View Results**:
   - In Freeze Mode, observe the cards and their corresponding odds in the browser.
   - In Live Mode, continue observing the live feed as the program captures and displays the video.

5. **Exit the Program**:
   - Press **Q** to terminate the program, closing the OpenCV window and shutting down all operations.

---

This detailed guide ensures you can operate the system efficiently and make real-time decisions based on the detected cards. The toggling of freeze mode allows you to seamlessly switch between monitoring and calculating the poker odds, optimizing your analysis workflow.

---

### 🛠️ Dependencies / Requirements

Below are the required dependencies and libraries used in this project:

| **Category**         | **Dependencies**                                                                 |
|-----------------------|----------------------------------------------------------------------------------|
| **Visualization**     | `matplotlib`, `Pillow (PIL)`                                                    |
| **Computer Vision**   | `cv2 (OpenCV)`, `numpy`, `ultralytics` (YOLO for object detection)              |
| **Web Automation**    | `selenium` (WebDriver, Chrome Service, Chrome Options, Action Chains)           |
| **Screen Interaction**| `pyautogui` (for screen recording and control), `tkinter` (GUI for region selection) |
| **Miscellaneous**     | `time` (for delays and timing operations)                                       |

### Installation

Install all required libraries using the following command:

```bash
pip install matplotlib pillow opencv-python ultralytics selenium pyautogui
```

## 📝 Credits and Acknowledgments

This project leverages the following datasets, tools, and software:

### Datasets
- **Playing Cards Dataset**  
  - Title: *Playing Cards Dataset*  
  - Author: Augmented Startups  
  - Type: Open Source Dataset  
  - Publisher: Roboflow  
  - Source: [Playing Cards Dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d)  
  - Year: 2023 (Accessed: Dec 16, 2024)

### Tools
- **Poker Odds Calculator**  
  - Author: de Wet, R.  
  - Source: [Poker Odds Calculator](https://www.omnicalculator.com/other/poker-odds)  
  - Accessed: Dec 16, 2024

### Software
- **Ultralytics YOLO11**  
  - Authors: Glenn Jocher, Jing Qiu  
  - Version: 11.0.0  
  - Year: 2024  
  - License: AGPL-3.0  
  - Source: [YOLO11 on GitHub](https://github.com/ultralytics/ultralytics)

- **Ultralytics YOLOv8**  
  - Authors: Glenn Jocher, Ayush Chaurasia, Jing Qiu  
  - Version: 8.0.0  
  - Year: 2023  
  - License: AGPL-3.0  
  - Source: [YOLOv8 on GitHub](https://github.com/ultralytics/ultralytics)

