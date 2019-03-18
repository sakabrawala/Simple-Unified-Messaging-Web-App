# Full-Stack-Application
IGN: FULL STACK Project

This project has some additional functionalities including the required set of tasks that were asked to be completed. A lot of effort and hard work has been applied in order to complete this project as working for IGN has been one of my dreams. I have been following IGN entertainment since I was a child and have been a regular user on this website. From movie to game reviews, from game walkthroughs through podcasts, everything IGN does is wonderful. IGN has a global impact and that motivated me to apply and work for IGN one day. Whatever you work upon is seen and followed by thousands and thousands of people. That’s simply amazing. So, let's get started with this assessment. I hope you like it.  :)

Steps to get started and run this project:

Make a directory name - Full Stack (In my scenario) and git clone the project into the directory.
Open CMD (Command Prompt) and change the directory by typing this
cd C:\xampp\htdocs\Full Stack

You will see two folders after cloning the repository from Github.
1) Chat-server
2) IGN - Chat_Webpage

Now since our project is based on Electron framework which is essentially a node.js application. Every electron application will be having this basic structure as shown below.
your-app/
├── package.json
├── main.js
└── index.html
So now we need to install npm (a package manager for the JavaScript programming language) and to get started with our website.
cd C:\xampp\htdocs\Full Stack\chat-server
npm install
npm install electron -g
Now try starting the electron framework by typing in 
start electron

Most probably you will be getting an error because a folder named node_modules is not there. Packages are installed and grouped together in this folder. You need to install the missing package shown in the error and the folder will be formed following with installation of all the missing packages required for the running of the project.
In our case we had this an error of Express is missing. This can be solved by typing in 
npm install express

And now start the server using Electron. Type this in the same CMD terminal window.
start electron

//a new window will open and then type this in the new opened terminal window

electron server.js


“Server listening on port 3010” - The message confirms that the server has started.

Now we need to connect the website to this server.
Minimize the terminal windows and open the other folder.


Open CMD in this window and type this:
cd C:\xampp\htdocs\Full Stack\IGN-Chat_Webpage

Follow the same commands we typed to start the server.
npm install express
start electron

A new window will open and then type:
electron index1.html


This is a Unified Messenger designed and coded by me for this project. It simplifies the messaging services by integrating them in one website. 
Whatsapp, Slack have been added as an example.
NativeChat is the one we will be using to chat internally on the localhost.
Open index2 in another electron window,





Hence we can chat in real time using our very own unified messaging application!
