MONETDB_USERNAME = 'vesselai'
MONETDB_PASSWORD = 'vesselai'
DB_URL = '128.214.253.154'
LOCAL_FILE = 'nari_combined.csv'
DB_NAME = 'ais_data'
HTML_FILE = 'folium_map.html'
COLUMN_NAMES = {'mmsi' : 'sourcemmsi', "shiptype":"shiptype", 'heading' : 'trueheading', 'speed' : 'speedoverground', 'status' : 'navigationalstatus', 'time' : 't', 'lon' : 'lon', 'lat' : 'lat'}

STORE_TRAIN_DATA = True

TRAIN_DATA_FROM_DB = True
STORE_VIZ_DATA = True