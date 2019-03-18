let electron
electron = require('electron')

const app = electron.app

const BrowserWindow = electron.BrowserWindow

let mainWindow
let mainnewWindow
let ses

function createWindow () {

  mainWindow = new BrowserWindow({width: 1500, height: 800})

  ses = mainWindow.webContents.session

  
  mainWindow.loadURL(`file://${__dirname}/index1.html`)

  mainWindow.on('closed', function () {
 
    mainWindow = null

  })

}
setTimeout(createWindow, 28000);
//app.on('ready', createWindow)

//app.on('window-all-closed', function () {
 
//  if (process.platform !== 'darwin') {
//    app.quit()
//  }
//})

//app.on('activate', function () {

//  if (mainWindow === null) {
//    createWindow()
//  }
//});




function createnewWindow () {
  // Create the browser window.

  mainnewWindow = new BrowserWindow({width: 1500, height: 800})

  ses = mainnewWindow.webContents.session

  // and load the index.html of the app.
  
  mainnewWindow.loadURL(`file://${__dirname}/first.html`)

  mainnewWindow.on('closed', function () {
    
    mainnewWindow = null

  })

}

app.on('ready', createnewWindow)

app.on('window-all-closed', function () {

  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
 
  if (mainnewWindow === null) {
    createnewWindow()
  }
});
