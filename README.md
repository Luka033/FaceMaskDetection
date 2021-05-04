
# Face Mask Detection System
A system built with Raspberry Pi, OpenCV, and TensorFlow Lite


---
![Face Mask Detection (1)](https://user-images.githubusercontent.com/42393044/117066415-8e4b9500-acdd-11eb-9915-85655858a61b.png)
![4](https://user-images.githubusercontent.com/42393044/117066751-0023de80-acde-11eb-948c-aa899b6e25d2.png)
![5](https://user-images.githubusercontent.com/42393044/117066874-277aab80-acde-11eb-87ac-56662596fd80.png)
![6](https://user-images.githubusercontent.com/42393044/117066886-2a759c00-acde-11eb-93ef-59e451752551.png)
![7](https://user-images.githubusercontent.com/42393044/117066894-2cd7f600-acde-11eb-8f5e-afba7f61bc63.png)



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
