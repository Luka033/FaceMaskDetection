# Mask Detection System
Mask detection with tflite on the Raspberry Pi that can be used at entrances. If an entering person is wearing a mask a green LED is turned on. If an entering person is not wearing a mask a red LED is turned on.

---

## Setup

**1. Clone the project**

**2. Go to the project directory:**
```
cd FaceMaskDetection
```
**3. Create conda virtual environment:**
```
conda create -n tflite-env python3.7
```
**4. Activate pipenv:**
```
conda activate tflite-env
```
**5. Install requirements:**
```
bash get_pi_requirements.sh
```
**6. Run script:**
```
python mask_detection.py --modeldir=mask_detection
```
