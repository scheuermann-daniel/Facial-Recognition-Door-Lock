# Facial Recognition Door Lock
### Daniel Scheuermann
### 3/26/2023
---

## Summary
This program is the code portion for a facial recognition door lock. Since we cannot modify the dorm doors in any way, I decided to make it extra-portable by making it based on the handle. Meaning, you could likely use this on any door with the same handle and carry it around.

To use, attach a camera to the peephole of the door and when it detects the specified people in front, it will turn a motor to pull the door and send an email alert to the specified email receiver.

---

## Installations
### Via 'sudo apt install'
* cmake build-essential pkg-config git
* libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
* libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
* libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
* libatlas-base-dev liblapacke-dev gfortran
* libhdf5-dev libhdf5-103
* python3-dev python3-pip python3-numpy	

### Via 'git clone'
*  https://github.com/opencv/opencv.git
*  https://github.com/opencv/opencv_contrib.git
* https://github.com/carolinedunn/facial_recognition

### Via 'pip install'
* face-recognition
* imutils
* opencv-python
* numpy
* pathlibs
---

## Known Bugs
* In bad lighting, it may not detect the face consistently
* After too many runs, it may not pull the handle all the way as the string moves.

---
## Future Work
* Implement some method to overcome bad lighting. Maybe have a flashlight turn on when it detects someone.
* Make it more compact.
* Allow remote adding of people to the list.

---
## Citations
* https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition
* https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-1-rclocal
* https://pypi.org/project/opencv-python/
* https://forums.raspberrypi.com/viewtopic.php?t=304628
* https://www.youtube.com/watch?v=2bganVdLg5Q
* https://www.reddit.com/r/learnpython/comments/npam5h/filenotfounderror_errno_2_no_such_file_or/
* https://stackoverflow.com/questions/55154397/modulenotfounderror-no-module-named-face-recognition
* https://stackoverflow.com/questions/20518632/importerror-numpy-core-multiarray-failed-to-import
