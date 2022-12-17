
# -*- coding: utf-8 -*-

import sys
import MVGLive
import pyowm
import datetime
import urllib.request


from PyQt4.QtCore import QTimer

from PyQt4.QtGui import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt4.QtGui import QPixmap, QImage

from ui_mainwindow import Ui_Form


class MainApp(QMainWindow, Ui_Form):
	def __init__(self, parent=None):
		
		self.owm = pyowm.OWM('')	#TODO: Insert owm personal API key
		self.mvg = MVGLive.MVGLive()
		
		super(MainApp, self).__init__(parent)
		# init ui
		self.setupUi(self)
		self.initUi()
		
	def initUi(self):
		
		self.timer = QTimer()
		self.timer.timeout.connect(self.tick)
		self.timer.start(5000)
		self.station="" #TODO: Insert station name

	def tick(self):
		self.text_date.setText(datetime.date.today().strftime('%d.%m.%Y'))
		self.text_time.setText(datetime.datetime.now().strftime('%H:%M'))
		self.text_station.setText(self.station)
		
 
		observation = self.owm.weather_at_place('')	#TODO: Insert city
		w = observation.get_weather()
		
		self.text_temp.setText(str(w.get_temperature('celsius')['temp'])+"°")
		self.text_min_temp.setText(str(w.get_temperature('celsius')['temp_min'])+"°")
		self.text_max_temp.setText(str(w.get_temperature('celsius')['temp_max'])+"°")
		#self.TextWeather.append(w.get_detailed_status())
		#self.TextWeather.append("Sunrise: "+w.get_sunrise_time('iso'))
		#self.TextWeather.append("Sunset: "+w.get_sunset_time('iso'))
		#self.TextWeather.append("Humidity: "+str(w.get_humidity())) 
		#self.TextWeather.append("Temperature: "+str(w.get_temperature('celsius')['temp'])+"°")
		data = self.mvg.getlivedata(self.station)

		img_data= urllib.request.urlopen(data[0]['linesymbolurl']).read()
		image=QImage()
		image.loadFromData(img_data)
		self.draw_mvg1.setPixmap(QPixmap(image))

		img_data= urllib.request.urlopen(data[1]['linesymbolurl']).read()
		image=QImage()
		image.loadFromData(img_data)
		self.draw_mvg2.setPixmap(QPixmap(image))
		
		img_data= urllib.request.urlopen(data[2]['linesymbolurl']).read()
		image=QImage()
		image.loadFromData(img_data)
		self.draw_mvg3.setPixmap(QPixmap(image))
		
		img_data= urllib.request.urlopen(data[3]['linesymbolurl']).read()
		image=QImage()
		image.loadFromData(img_data)
		self.draw_mvg4.setPixmap(QPixmap(image))
		
		img_data= urllib.request.urlopen(data[4]['linesymbolurl']).read()
		image=QImage()
		image.loadFromData(img_data)
		self.draw_nvg5.setPixmap(QPixmap(image))
		
		self.text_dest_1.setText(data[0]['destination'])
		self.text_dest2.setText(data[1]['destination'])
		self.text_dest3.setText(data[2]['destination'])
		self.text_dest4.setText(data[3]['destination'])
		self.text_dest5.setText(data[4]['destination'])
		
		self.text_mvg_time1.setText(str(data[0]['time'])+" min(s)")
		self.text_mvg_time2.setText(str(data[1]['time'])+" min(s)")
		self.text_mvg_time3.setText(str(data[2]['time'])+" min(s)")
		self.text_mvg_time4.setText(str(data[3]['time'])+" min(s)")
		self.text_mvg_time5.setText(str(data[4]['time'])+" min(s)")
		

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
      
    form = MainApp()
    form.showFullScreen()
    #form.show()
     
    sys.exit(app.exec_())
