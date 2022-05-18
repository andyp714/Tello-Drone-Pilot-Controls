'''
Created on Mar 29, 2022

@author: apauley24
'''
import keyboard
#Imports keyboard library for keyboard detection
from djitellopy import tello
#imports drone library
from djitellopy.tello import BackgroundFrameRead
#imports drone library
import cv2
#imports video and editing library
import time
#imports time for wait




def cameraStream(var):
    var.takeoff()
    #Drone Takes off
    inAir = True
    #Sets up a boolean to see if the drone is in air

    while inAir == True:
        #Loops while the drone is in the air
        img = var.get_frame_read().frame
        #Gets the current frame and assigns it to img
        img = cv2.resize(img, (720, 480))
        #Resizes the frame by (witdh, height)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        #Sets up the font type for putting font on video stream
        cv2.putText(img, 
                "X SPEED: " + str(var.get_speed_x()), 
                (30, 30), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_4)
        
        #Puts text on the frame, the text can be anything. Here it is getting the current x speed from the drone. Inputs are location, font, and color
        
        cv2.putText(img, 
                "Y SPEED: "+ str(-1 * var.get_speed_y()), 
                (30, 60), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_4)
        #Same thing as above but with y speed
    
        cv2.putText(img, 
                "Z SPEED: "+ str(-1 * var.get_speed_z()), 
                (30, 90), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_4)
        #Same thing as above but with z speed
        
        cv2.putText(img, 
                "TEMP: "+ str(var.get_temperature()), 
                (30, 120), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_4)
        #Same thing as above but with temperature
    
        cv2.putText(img, 
                "height: "+ str(var.get_height()), 
                (300, 30), 
                font, 1, 
                (255, 255, 255), 
                1, 
                cv2.LINE_4)
        
        #Same thing as above but with height
        
        
       
       
       
        forward_back = 0
        left_right = 0
        up_down = 0
        yaw = 0
        
        #Sets up speed variables for later use, sets them to zero every loop
        
        if keyboard.is_pressed("w"):
            forward_back = 50
            if keyboard.is_pressed("r"):
                forward_back = 100
        elif keyboard.is_pressed("s"):
            forward_back = -50
            if keyboard.is_pressed("r"):
                forward_back = -100
        if keyboard.is_pressed("a"):
            left_right = -50
            if keyboard.is_pressed("r"):
                left_right = -100
        elif keyboard.is_pressed("d"):
            left_right = 50
            if keyboard.is_pressed("r"):
                left_right = 100
        if keyboard.is_pressed("q"):
            up_down = 50
            if keyboard.is_pressed("r"):
                up_down = 100
        elif keyboard.is_pressed("e"):
            up_down = -50
            if keyboard.is_pressed("r"):
                up_down = -100
        if keyboard.is_pressed("y"):
            yaw = 50
        if keyboard.is_pressed("l"):
            var.land()
            inAir = False
        
    
    
        var.send_rc_control(left_right, forward_back, up_down, yaw)
        #sends the speed to the drone
        
        cv2.imshow("Image", img)
        #shows the image
        cv2.waitKey(1)
        #Frame rate wait



def get_frame_read(self) -> 'BackgroundFrameRead':
    #From library have to change the function in the library
    """Get the BackgroundFrameRead object from the camera drone. Then, you just need to call
    backgroundFrameRead.frame to get the actual frame received by the drone.
    Returns:
        BackgroundFrameRead
    """
    while self.background_frame_read is None: #Changed if to while
        address = self.get_udp_video_address()
        self.background_frame_read = BackgroundFrameRead(self, address)  # also sets self.cap
        self.background_frame_read.start()
    return self.background_frame_read









if __name__ == "__main__":
    var = tello.Tello()
    #Connects to Drone and assign it to variable
    var.connect()
    #Initializes the drone connection
    var.streamon()
    #Begins the stream from the drone
    img = var.get_frame_read().frame
    #Gets the frame and assigns it to img variable
    img = cv2.resize(img, (720, 480))
    #rezises the window by (width, height)
    cv2.imshow("Image", img)
    #Shows image on screen
    cv2.waitKey(1)
    #Wait to set framerate
    cameraStream(var)
    #passes drone variable to function




            


    