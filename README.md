# Mask Detection System
Mask detection with tflite on the Raspberry Pi that can be used at entrances. If an entering person is wearing a mask a green LED is turned on. If an entering person is not wearing a mask a red LED is turned on.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-GJLy0X9fAs/0.jpg)](https://www.youtube.com/watch?v=-GJLy0X9fAs)

---

## Setup

**1. Clone the project**

**2. Go to the project directory:**
```
cd FaceMaskDetection
```
**3. Download pipenv if you dont have it:**
```
sudo pip3 install virtualenv
```
**4. Create virtual environment:**
```
python3 -m venv tflite-env
```
**5. Activate pipenv:**
```
source tflite-env/bin/activate
```
**6. Install requirements:**
```
bash get_pi_requirements.sh
```
**7. Run script:**
```
python3 mask_detection.py --modeldir=mask_model
```
