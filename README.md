# foyer-info-screen-app
Web application running on a linux appliance that displays information about student projects and other relevant goings on in the CSMP department

This web application is designed to have a raspberry pi acting as a linux appliance connect to it via a browser. Some settings to help get all of this set up are:
  1) Turn off device sleep timer
  2) Set up user account and password
  3) Enable SSH to allow remote editing
  4) Edit the autostart file to launch browser
    Ex: Launch Chromium in fullscreen without error bubbles and have it connect to google.com
      ```
      $ cd /etc/xdg/lxsession/LXDE-pi
      $ sudo nano autostart
      ```
    
     At the bottom of the autostart file, add the following command:
        ```
        @chromium-browser --kiosk --disable-session-crashed-bubble --disable-infobars http://google.com/
        ```
        Write out with CTRL-O and exit with CTRL-X

Some additional options to be considered:
  - Enable "Wait for Network to Boot" to allow time for the network to restart before the Pi tries to connect to the web application
  
