# Face-Recognition


........................................................................................................................

🛠 Step 1: Install Required Dependencies
Before running the project, make sure you have Python and pip installed.

✅ 1. Install Python (if not installed)
Download Python from Python Official Website

Install it and check "Add Python to PATH" during installation

Verify installation by running:


python --version


🖥 Step 2: Set Up a Virtual Environment
To keep dependencies isolated:

✅ 1. Open Command Prompt (cmd)
Press Win + R, type cmd, and hit Enter.

✅ 2. Navigate to Your Project Folder

cd "C:\Users\Amit\Python -Machine Learning\face recognition project"

✅ 3. Create a Virtual Environment

python -m venv face_recognition_env

✅ 4. Activate the Virtual Environment

face_recognition_env\Scripts\activate

................................................................................................
After Activating the Virtual environment. Install the required Libraries for the project.
................................................................................................


📦 Step 3: Install Required Libraries
Once the virtual environment is activated, install dependencies:

✅ 1. Install OpenCV (cv2)

pip install opencv-python

✅ 2. Install dlib (Required for face_recognition)

pip install dlib

✅ 3. Install face_recognition Library

pip install face_recognition

✅ 4. Install Other Required Packages

pip install numpy
pip install imutils
pip install pillow


.................................................................................................................
If there is any installation issue in the above libraries  then first select and 
install required packages from  Microsoft Build Tools in VS Studio.

Also manually download Cmake from the official website  and install it. (cmake-4.0.0-rc5-windows-x86_64.msi)

Also Install Git to downlad required repositery
.......................................................................................................................



🔹 Solution: Install Required Dependencies
Step 1: Install Microsoft C++ Build Tools
Download and install Microsoft Build Tools for Visual Studio from here.

During installation, select the following components:

C++ CMake tools for Windows

Windows 10 SDK

MSVC v142 - VS 2019 C++ x64/x86 build tools

C++ ATL for v142 build tools

C++ CMake tools for Windows

Restart your system after installation.

Step 2: Install cmake
You need cmake installed for building dlib. If you don’t have it, install it via:

pip install cmake

Step 3: Try Installing dlib Again
After installing the dependencies, try running:

pip install dlib


........................................................................................................................


🔹 Alternative: Use Precompiled dlib Wheel (Easier)
If you don’t want to build from source, use a precompiled .whl file:

Download the latest dlib .whl from this site:

Unofficial dlib Wheels

Navigate to the downloaded file’s location and install it using:


pip install dlib‑19.24.0‑cp312‑cp312‑win_amd64.whl
(Adjust the filename based on the downloaded version and Python version.)


.......................................................................................................................



🏗 Step 4: Fix Common Errors
🔹 If You Named Your Script face_recognition.py or face_detect.py, Rename It!
Avoid using library names as script names.
✔ Rename face_recognition.py to face_recognition_app.py or detect_faces.py.

🔹 Delete the Cache Folder (__pycache__)


rm -rf __pycache__
del face_recognition.pyc
or remove it manually from the project folder.

▶ Step 5: Run the Project
Once everything is set up, run your script:


python face_recognition_app.py
or

python detect_faces.py


..........................................................................................



🔹 Step 2: Check Your Python Script
If you're running face_recognition_app.py, make sure you are importing the correct module.
Instead of:

import face_detect

use

import face_recognition
import cv2


🔹 Step 3: Verify the Correct Python Environment


pip list | findstr face-recognition


Check if face_recognition_models is Installed Properly
Run the following command inside your active virtual environment:

python -c "import face_recognition_models; print(face_recognition_models.__file__)"



 Manually Set the face_recognition_models Path
If the package is installed but not detected, manually add it:


set FACE_RECOGNITION_MODELS=C:\Users\Amit\Python -Machine Learning\face recognition project\face_recognition_env\Lib\site-packages\face_recognition_models



Ensure You Are Using the Correct Python

where python
It should only show:


C:\Users\Amit\Python -Machine Learning\face recognition project\face_recognition_env\Scripts\python.exe

If it shows multiple Python versions (Anaconda, System Python, etc.), deactivate the virtual environment and restart:


deactivate

To Activate

face_recognition_env\Scripts\activate
Then try again.
