# Voice-Controlled-Vehicle
This project controls a vehicle using voice commands through Fast Fourier Transform (FFT) and Dynamic Time Warping (DTW) techniques.

How to Run the Project
Follow these steps to execute the project:

-Prepare the files: Make sure all audio recordings and source code files are located in the same folder.
Record your voice commands: Run the audio recording script to collect your voice samples. Record a maximum of three audio samples for each command:

         Forward
         Backward
         Left
         Right
         Stop

-Run the main Python script: Execute codigo_principal. Make sure to:

            Specify the correct Arduino COM port.
            Set the paths to your audio recordings in the direcciones variable.

-Upload the Arduino code: Open ESP32_carrito in the Arduino IDE and upload the code to your ESP32 board. Make sure you have an ESP32 available.
-Test the vehicle: Once everything is configured and uploaded, use your voice commands to control the vehicle.
Expected Result
The vehicle should respond to the recorded voice commands and move accordingly. You can see the result in: https://youtu.be/NsSHnQBWH_A?si=81DxOEVYV1Sahy1K
