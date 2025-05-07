import requests
import uuid
import time
import gzip
import json
from io import BytesIO
import random
import base64
import re
from datetime import datetime

game_value = "5849541"
pack_value = "xyz.lovecode_partner"
version_value = "5.0.1"
version_code = 446
sig_value = "9eb3cb2056dcf011d4fae5b13ecc8b98e94968e4"
insataller_pack = "com.android.vending"
time_zone = "CST"
timezone_offset = -21600
timezone_offset2 = 1080
idfi_value = str(uuid.uuid4())
adid_value = str(uuid.uuid4())

ts_value = int(time.time() * 1000)
ts_value2 = int(time.time() * 1000)
start_time = ts_value // 1000

formatted_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.') + f"{datetime.utcnow().microsecond // 1000:03d}Z"

def generate_hex():
    first_1 = ''.join(random.choices('0123456789abcdef', k=12))
    second_2 = ''.join(random.choices('0123456789abcdef', k=3))
    check_y = ''.join(random.choices('ab89', k=1))
    third_1 = ''.join(random.choices('0123456789abcdef', k=15))
    
    return(first_1+"4"+second_2+check_y+third_1)

analytics_value1 = generate_hex()
analytics_value2 = generate_hex()

device_makes = random.choice([
    "samsung", "google", "huawei", "oneplus", "xiaomi", "lg", "sony",
    "oppo", "vivo", "nokia", "motorola", "asus", "realme", "lenovo", "blackberry"
])


samsung_model = random.choice([
    "SM-A156M", "SM-G991B", "SM-A715F", "SM-N986B", "SM-G998B", "SM-A325F",
    "SM-M525F", "SM-S901E", "SM-F916B", "SM-G780G", "SM-A136B", "SM-N975F",
    "SM-G973F", "SM-G950F", "SM-A525F", "SM-A102U", "SM-G935F", "SM-N960F",
    "SM-A115F", "SM-G570F", "SM-A135F", "SM-N975U", "SM-G965F", "SM-A515F",
    "SM-S908B", "SM-G970F", "SM-N975W", "SM-G973U", "SM-A325U", "SM-G928F",
    "SM-A710F", "SM-G920F", "SM-G935W8", "SM-G977B", "SM-A520F", "SM-G950U",
    "SM-J530F", "SM-N950F", "SM-A703F", "SM-G965U", "SM-G965W", "SM-G800F",
    "SM-N976B", "SM-G780F", "SM-A707F", "SM-G570Y", "SM-A125F", "SM-N975F",
    "SM-S767V", "SM-A328B", "SM-N960U", "SM-G670F", "SM-A505F"
])
google_model = random.choice([
    "GD1YQ", "G025I", "G020A", "G020B", "G020F", "G020J", "G020P", "G020X", "G020Q", "G020R",
    "G020U", "G020V", "G021A", "G021B", "G021C", "G021F", "G0220", "G0221", "G0222", "G0230",
    "G0231", "G0232", "G0240", "G0241", "G0242", "G0243", "G025A", "G025B", "G025C", "G026A",
    "G027A", "G028A", "G029A", "G030A", "G030B", "G030C", "G030D", "G031A", "G031B", "G031C",
    "G032A", "G032B", "G033A", "G033B", "G034A", "G034B", "G035A", "G036A", "G037A", "G038A"
])
huawei_model = random.choice([
    "ANA-AL00", "CLT-AL00", "ELE-AL00", "BND-AL00", "MRD-LX1", "VOG-L29", "NOVA-LX3", "POT-LX1", 
    "LYA-AL10", "PRA-AL00", "EML-L29", "EVR-L29", "STF-AL00", "HWE-AL00", "JHN-AL00", "GRA-AL00", 
    "NCE-AL00", "PRA-TL00", "SNE-AL00", "KNT-AL00", "LDN-LX1", "INE-LX1", "WAS-LX1", "ALP-L09", 
    "MLA-L29", "CAN-L11", "TRT-LX1", "CUN-LX1", "CAY-L21", "SNE-AL00", "VTR-L09", "VTR-L29", 
    "ELS-AL10", "NEM-AL10", "HWI-AL00", "MRD-L29", "VNS-L31", "CHM-AL00", "LYA-L09", "JMM-AL00", 
    "PRA-LX1", "TAS-AL00", "TAP-AL00", "JRD-LX1", "CIT-AL00", "PCT-AL00", "SLA-AL00", "CAG-L21", 
    "VOG-L29", "CLT-L29", "ALP-L21", "ALP-L23"
])
oneplus_model = random.choice([
    "A6000", "A6010", "A6013", "A5010", "A5000", 
    "A7000", "A7001", "A7003", "BE2013", "BE2028", 
    "BE2012", "GM1911", "GM1913", "GM1901", "GM1903", 
    "HD1901", "HD1903", "IN2010", "IN2020", "IN2021", 
    "LE2110", "LE2113", "LE2115", "LE2120", "LE2127", 
    "LE2123", "LA2001", "LA2003", "LA2020", "LU2020", 
    "LU2030", "LU2033", "LU2025", "LU2028", "X9000", 
    "X9003", "X9001", "X9010", "RMX1911", "RMX1913", 
    "RMX1921", "RMX1931", "RMX1993", "RMX2051", "RMX2053", 
    "RMX2063", "RMX2075", "RMX2101", "RMX2103"
])
xiaomi_model = random.choice([
    "M2001J2G", "M2003J15SC", "M2004J19C", "M2005J5BC", "M2006C3LI", "M1902F1G", "M1901F7G", 
    "M1901F9G", "M1908C3JH", "M2101K6G", "M2102J20SG", "M2103K19AG", "M2103J20SI", "M2104J19PI", 
    "M2105K81AC", "M2105K81C", "M2010J19SC", "M2010J19SI", "M2104J19AG", "M2102J20IC", "M2012K11AG", 
    "M2013K19G", "M2003J6A1", "M1904F3GT", "M2007J3SG", "M2004J11G", "M1906J15SG", "M2006C3LG", 
    "M2101K7AG", "M2005J5AI", "M2010J19CG", "M1901F9G", "M2011K9G", "M2004J19IG", "M2105K81AG", 
    "M2006C3KG", "M2101K6G", "M2004J9G", "M2101K6AG", "M2005J5AI", "M2006J1AC", "M2003J7BC", 
    "M2004J10CG", "M2007J3AG", "M2008J3SG", "M1905F9G", "M2009J2SC", "M2101K7SG"
])
lg_model = random.choice([
    "LM-G820N", "LM-G710EM", "LM-V405EBW", "LG-H873", "LG-H870", "LG-H990DS", "LG-K420", 
    "LG-M255", "LG-D850", "LG-D855", "LG-K10", "LG-K20", "LG-K40", "LG-K50", "LG-K60", 
    "LG-M255", "LG-Q6", "LG-Q7", "LG-Q8", "LG-G5", "LG-G6", "LG-G7", "LG-G8", "LG-V10", 
    "LG-V20", "LG-V30", "LG-V40", "LG-V50", "LG-V60", "LG-W30", "LG-W30 Pro", "LG-W41", 
    "LG-W41+", "LG-W51", "LG-W51+", "LG-X210", "LG-X410", "LG-X520", "LG-X540", "LG-X600", 
    "LG-X620", "LG-X500", "LG-X5", "LG-H830", "LG-V50S", "LG-LM-X420", "LG-TP260", "LG-LM-V405EBW", 
    "LG-X510", "LG-X420", "LG-X320", "LG-F660", "LG-K525", "LG-F520"
])
sony_model = random.choice([
    "Xperia XZ1", "Xperia XZ2", "Xperia XZ3", "Xperia XA1", "Xperia XA2", "Xperia XA3", 
    "Xperia XZ Premium", "Xperia XZ1 Compact", "Xperia XZ2 Compact", "Xperia XZ3 Compact", 
    "Xperia 1", "Xperia 1 II", "Xperia 1 III", "Xperia 5", "Xperia 5 II", "Xperia 5 III", 
    "Xperia 10", "Xperia 10 II", "Xperia 10 III", "Xperia L1", "Xperia L2", "Xperia L3", 
    "Xperia X", "Xperia Z1", "Xperia Z2", "Xperia Z3", "Xperia Z4", "Xperia Z5", "Xperia Z5 Compact", 
    "Xperia Z5 Premium", "Xperia M4 Aqua", "Xperia M5", "Xperia C5 Ultra", "Xperia C4", 
    "Xperia E3", "Xperia E4", "Xperia E5", "Xperia T3", "Xperia T2 Ultra", "Xperia Z Ultra", 
    "Xperia X Compact", "Xperia X Performance", "Xperia XZ", "Xperia XZ2 Premium", "Xperia XZ4", 
    "Xperia XZ2 Force", "Xperia R1", "Xperia R1 Plus", "Xperia XZ2 Dual", "Xperia XZ3 Dual"
])
oppo_model = random.choice([
    "CPH1923", "CPH1917", "CPH1909", "CPH1903", "CPH1819", "CPH1609", "CPH1591", "CPH1581",
    "CPH1571", "CPH1561", "CPH1541", "CPH1523", "CPH1511", "CPH1505", "CPH1491", "CPH1481",
    "CPH1461", "CPH1451", "CPH1441", "CPH1431", "CPH1419", "CPH1409", "CPH1393", "CPH1385",
    "CPH1373", "CPH1365", "CPH1355", "CPH1343", "CPH1339", "CPH1327", "CPH1311", "CPH1309",
    "CPH1303", "CPH1299", "CPH1297", "CPH1291", "CPH1289", "CPH1281", "CPH1277", "CPH1273",
    "CPH1265", "CPH1257", "CPH1249", "CPH1239", "CPH1223", "CPH1215", "CPH1205", "CPH1195",
    "CPH1185", "CPH1177", "CPH1169"
])
vivo_model = random.choice([
    "V1936A", "V1820A", "V1911A", "V1932A", "V1928A", "V1822A", "V1838A", "V1818A", 
    "V1825A", "V1933A", "V1916A", "V1918A", "V1858A", "V1860A", "V1845A", "V1831A", 
    "V1875A", "V1865A", "V1922A", "V1819A", "V1852A", "V1826A", "V1859A", "V1871A", 
    "V1815A", "V1904A", "V1906A", "V1851A", "V1848A", "V1910A", "V1912A", "V1931A", 
    "V1823A", "V1839A", "V1854A", "V1814A", "V1846A", "V1886A", "V1868A", "V1902A", 
    "V1827A", "V1862A", "V1903A", "V1843A", "V1824A", "V1879A", "V1857A", "V1888A", 
    "V1874A", "V1890A", "V1901A"
])
nokia_model = random.choice([
    "TA-1032", "TA-1043", "TA-1052", "TA-1062", "TA-1073", "TA-1083", "TA-1095", "TA-1109", 
    "TA-1111", "TA-1112", "TA-1116", "TA-1120", "TA-1123", "TA-1130", "TA-1132", "TA-1153", 
    "TA-1154", "TA-1170", "TA-1183", "TA-1190", "TA-1200", "TA-1209", "TA-1210", "TA-1216", 
    "TA-1221", "TA-1233", "TA-1234", "TA-1241", "TA-1242", "TA-1253", "TA-1261", "TA-1270", 
    "TA-1273", "TA-1282", "TA-1285", "TA-1295", "TA-1297", "TA-1305", "TA-1306", "TA-1310", 
    "TA-1320", "TA-1346", "TA-1350", "TA-1360", "TA-1384", "TA-1387", "TA-1390", "TA-1400", 
    "TA-1411", "TA-1420", "TA-1421"
])
motorola_model = random.choice([
    "XT1941-2", "XT1962-4", "XT1944-2", "XT1943-5", "XT2051-4", "XT2081-2", "XT2061-3", 
    "XT2053-3", "XT2043-4", "XT2000-3", "XT1980-3", "XT1970-3", "XT1963-4", "XT1920-2", 
    "XT1789-05", "XT1799-03", "XT1955-1", "XT2045-3", "XT2055-3", "XT2091-8", "XT2075-4", 
    "XT1900-4", "XT1924-1", "XT1932-5", "XT1930-2", "XT2041-2", "XT2021-2", "XT2023-3", 
    "XT2047-4", "XT1900-2", "XT2056-5", "XT2042-6", "XT2092-4", "XT2044-5", "XT2024-1", 
    "XT2058-1", "XT2096-5", "XT2092-2", "XT1925-3", "XT1919-3", "XT2046-3", "XT1926-5", 
    "XT1902-5", "XT1989-3", "XT2072-3", "XT2020-3", "XT1950-3", "XT2002-1", "XT2074-2"
])
asus_model = random.choice([
    "ZS570KL", "ZS600KL", "ZC554KL", "ZB602KL", "ZB601KL", "ZC520TL", "ZC553KL", "ZC554KL", 
    "ZB602KL", "ZB601KL", "ZS600KL", "ZB570TL", "ZB552KL", "ZC520KL", "ZC553KL", "ZS660KL", 
    "ZS676KL", "ZB633KL", "ZB634KL", "ZC580KL", "ZC555KL", "ZS550KL", "ZB555KL", "ZC590KL", 
    "ZC580KL", "ZB631KL", "ZS670KL", "ZC551KL", "ZC570KL", "ZC650KL", "ZB550KL", "ZB560KL", 
    "ZS660KL", "ZB633KL", "ZB636KL", "ZC551KL", "ZC550KL", "ZS602KL", "ZB634KL", "ZC545KL", 
    "ZB640KL", "ZC600KL", "ZB637KL", "ZS680KL", "ZS620KL", "ZC510KL", "ZB643KL", "ZC560KL", 
    "ZC500KL", "ZS655KL", "ZS618KL"
])
realme_model = random.choice([
    "RMX1801", "RMX1831", "RMX1921", "RMX1925", "RMX1931", "RMX1971", "RMX2040", "RMX2041", 
    "RMX2061", "RMX2075", "RMX2076", "RMX2081", "RMX2085", "RMX2095", "RMX2101", "RMX2103", 
    "RMX2201", "RMX2202", "RMX2233", "RMX2235", "RMX2242", "RMX2255", "RMX2256", "RMX2261", 
    "RMX2300", "RMX2301", "RMX2310", "RMX2312", "RMX2321", "RMX2333", "RMX2341", "RMX2345", 
    "RMX2355", "RMX2401", "RMX2403", "RMX2410", "RMX2412", "RMX2451", "RMX2500", "RMX2501", 
    "RMX2510", "RMX2520", "RMX2530", "RMX2550", "RMX2561", "RMX2600", "RMX2610", "RMX2620", 
    "RMX2700", "RMX2710", "RMX2720"
])
lenovo_model = random.choice([
    "L78011", "L19041", "L18011", "L85071", "L45071", "L68031", "L81031", "L18041", 
    "L71041", "L78021", "L19051", "L71061", "L82031", "L86031", "L35011", "L22061", 
    "L19021", "L40031", "L70051", "L71051", "L65021", "L33021", "L31021", "L32061", 
    "L10021", "L16031", "L82041", "L85051", "L86041", "L75021", "L84021", "L60051", 
    "L91051", "L73011", "L78031", "L40021", "L31051", "L55011", "L52031", "L43021", 
    "L44051", "L42051", "L46011", "L35031", "L22031", "L43031", "L20051", "L41061", 
    "L31031", "L32041"
])
blackberry_model = random.choice([
    "STH100-1", "STH100-2", "STH100-3", "STH100-4", "STV100-1", "STV100-2", "STV100-3", 
    "STV100-4", "SQC100-1", "SQC100-2", "SQC100-3", "SQC100-4", "RHM100-1", "RHM100-2", 
    "RHM100-3", "RHM100-4", "BBD100-1", "BBD100-2", "BBD100-3", "BBD100-4", "PRD-62710-003", 
    "PRD-62910-001", "PRD-63110-001", "RIM-100", "RIM-101", "RIM-102", "RIM-103", "RIM-104", 
    "RIM-105", "RIM-106", "RIM-107", "RIM-108", "RIM-109", "RIM-110", "RIM-111", "RIM-112", 
    "RIM-113", "RIM-114", "RIM-115", "RIM-116", "RIM-117", "RIM-118", "RIM-119", "RIM-120", 
    "RIM-121", "RIM-122", "RIM-123", "RIM-124", "RIM-125", "RIM-126"
])

device_model = {
    "samsung": samsung_model,
    "google": google_model,
    "huawei": huawei_model,
    "oneplus": oneplus_model,
    "xiaomi": xiaomi_model,
    "lg": lg_model,
    "sony": sony_model,
    "oppo": oppo_model,
    "vivo": vivo_model,
    "nokia": nokia_model,
    "motorola": motorola_model,
    "asus": asus_model,
    "realme": realme_model,
    "lenovo": lenovo_model,
    "blackberry": blackberry_model
}.get(device_makes)


user_agent = "Dalvik/2.1.0 (Linux; U; Android 14; V2352A Build/UP1A.231005.007)"

os_version = random.choice([
    "11", "12", "13", "14"
])

cpu_value = random.choice([
    4, 6, 8, 12
])
api_value = str(int(os_version)+20)
net_value = str(random.randint(13,21))

battery_label = round(random.uniform(0.40, 1.00), 2)
volume_value = random.randint(0,15)
battery_value = random.randint(1,4)

height_value = str(random.randint(800,2960))
width_value = str(random.randint(480,1440))

device_up_time = random.randint(100000000,300000000)

space_value = random.randint(20000000,99999999)*10

device_free_space = random.randint(10000000,19999999)*10

free_momory = random.randint(100000,199999)

total_momory = random.randint(200000,999999)

screen_size = random.randint(10000000,99999999)*10

e_real_time = random.randint(200000000,999999999)

screen_densities = random.choice([
    "120", "160", "240", "320", "400", "420", "450", "480", "560", "640"
])

network_operators = {
    "AT&T": "310410",
    "Verizon Wireless": "310012",
    "T-Mobile": "310260",
    "Sprint": "310120",
    "US Cellular": "311480",
    "Cricket Wireless": "310150",
    "Boost Mobile": "310000",
    "Metro by T-Mobile": "310260",
    "Simple Mobile": "310260",
    "Mint Mobile": "310260"
}


operator = random.choice(list(network_operators.items()))
network_name =  operator[0]
network_operator = operator[1]

id = uuid.uuid4()
numeric_uuid = f"{id.int >> 64}{id.int & ((1 << 64) - 1)}"
game_session_id = int(numeric_uuid.replace("-", "")[0:12])

chrome_version = random.choice(["130.0.6723.73", "130.0.6723.58", "129.0.6668.100","129.0.6668.81","129.0.6668.70","128.0.6613.146","128.0.6613.127","128.0.6613.100","128.0.6613.99","128.0.6613.88","127.0.6533.103","127.0.6533.84","127.0.6533.64"])

build_code = {"14": "U", "13": "T", "12": "S", "11": "R"}[os_version]+"P1A."+f"{random.randint(20, 24)}{random.randint(1, 12):02}{random.randint(1, 30):02}"+".007"

user_agent = "Mozilla/5.0 (Linux; Android "+os_version+"; "+device_model+" Build/"+build_code+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+chrome_version+" Mobile Safari/537.36"


finger_print = device_makes+"/"+device_model.replace(" ", "")+"/"+device_model.replace(" ", "")+":"+os_version+"/"+build_code+"/compiler"+str(random.randint(10000000,99999999))+":user/release-keys"

url = "https://configv2.unityads.unity3d.com/webview/4.6.1/release/config.json"


payload = {
    "sdkVersionName": "4.6.1",
    "gameId": game_value,
    "sdkVersion": 4610,
    "unifiedconfig.data.gameSessionId": game_session_id,
    "platform": "android",
    "callType": "privacy",
    "idfi": idfi_value,
    "ts": ts_value
}


encoded_payload = json.dumps(payload)


buffer = BytesIO()
with gzip.GzipFile(fileobj=buffer, mode='wb') as f:
    f.write(encoded_payload.encode('utf-8'))
compressed_payload = buffer.getvalue()


headers = {
    'User-Agent': user_agent,
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded"  
}

response = requests.post(url, headers=headers, data=compressed_payload)


print(response.status_code)


payload2 = {
    "language": "en_US",
    "deviceElapsedRealtime": e_real_time,
    "connectionType": "wifi",
    "callType": "token_srr",
    "screenSize": screen_size,
    "usbConnected": False,
    "deviceFreeSpace": device_free_space,
    "apiLevel": api_value,
    "cpuCount": cpu_value,
    "networkOperatorName": network_name,
    "test": False,
    "wiredHeadset": False,
    "adbEnabled": False,
    "timeZone": time_zone,
    "appStartTime": start_time,
    "unifiedconfig.data.gameSessionId": game_session_id,
    "deviceUpTime": device_up_time,
    "idfi": idfi_value,
    "volume": volume_value,
    "sdkVersion": 4610,
    "screenDensity": int(screen_densities),
    "networkMetered": True,
    "screenWidth": int(width_value),
    "networkOperator": network_operator,
    "bundleVersion": version_value,
    "timeZoneOffset": timezone_offset,
    "appActive": True,
    "apkDeveloperSigningCertificateHash": sig_value,
    "platform": "android",
    "limitAdTracking": False,
    "androidFingerprint": finger_print,
    "osVersion": os_version,
    "rooted": False,
    "networkType": int(net_value),
    "batteryLevel": battery_label,
    "sdkVersionName": "4.6.1",
    "gameId": game_value,
    "stores": "google",
    "screenHeight": int(height_value),
    "bundleId": pack_value,
    "deviceMake": device_makes,
    "user.nonBehavioral": False,
    "versionCode": 4610,
    "unifiedconfig.pii.advertisingTrackingId": adid_value,
    "encrypted": False,
    "batteryStatus": battery_value,
    "webviewUa": user_agent,
    "deviceModel": device_model,
    "eventTimeStamp": start_time,
    "ts": ts_value+random.randint(100,999)
}


encoded_payload2 = json.dumps(payload2)


buffer2 = BytesIO()
with gzip.GzipFile(fileobj=buffer2, mode='wb') as f:
    f.write(encoded_payload2.encode('utf-8'))
compressed_payload2 = buffer2.getvalue()

response2 = requests.post(url, headers=headers, data=compressed_payload2)

print(response2.status_code)

organ_id = response2.json()["SRR"]["organizationId"]

developer_id = response2.json()["SRR"]["developerId"]

token_value = response2.json()["SRR"]["token"]

project_value = response2.json()["SRR"]["projectId"]

country_value = response2.json()["SRR"]["country"]

ab_value = str(response2.json()["SRR"]["abGroup"])

properties_value = str(response2.json()["SRR"]["properties"])

url3 = "https://thind.unityads.unity3d.com/v1/events"

payload3 = json.dumps([
    {
        "common": {
            "gameId": game_value,
            "organizationId": organ_id,
            "analyticsUserId": analytics_value1,
            "analyticsSessionId": str(game_session_id),
            "sessionId": analytics_value2,
            "platform": "ANDROID",
            "adsSdkVersion": "4.6.1",
            "gamerToken": token_value,
            "limitAdTracking": False,
            "coppaFlagged": False,
            "projectId": project_value,
            "gdprEnabled": False,
            "optOutRecorded": False,
            "optOutEnabled": False,
            "deviceMake": device_makes,
            "deviceModel": device_model,
            "connectionType": "wifi",
            "country": country_value,
            "storeId": pack_value,
            "privacy": {
                "permissions": {"ads": True, "external": True, "gameExp": True},
                "method": "default"
            },
            "installHour": (ts_value//1000000)*1000000
        }
    },
    {
        "type": "ads.analytics.appStart.v2",
        "msg": {"nAppStartDay": 1, "nAppStartUser": 1, "ts": ts_value2}
    }
])

headers3 = {
    'User-Agent': user_agent,
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json"
}

response3 = requests.post(url3, data=payload3, headers=headers3)

print(response3.status_code)

payload3_list = json.loads(payload3)
payload3_list[1]["type"] = "ads.analytics.appInstall.v2"

new_msg_value = {"ts":ts_value2,"appVersion":version_value,"timeSinceStart":0}
 
payload3_list[1]["msg"] = new_msg_value

updated_payload3 = json.dumps(payload3_list)

response4 = requests.post(url3, data=updated_payload3, headers=headers3)

print(response4.status_code)


url5 = "https://events.mz.unity3d.com/operative/Rewarded_Android"

payload5 = {
  'eventType': "load",
  'token': token_value,
  'abGroup': ab_value,
  'gameId': game_value,
  'campaignId': "005472656d6f7220416e6472",
  'adUnitId': "Rewarded_Android",
  'coppa': "false",
  'optOutEnabled': "false",
  'frameworkName': "",
  'frameworkVersion': "",
  'platform': "android",
  'sdkVersion': "4610",
  'seatId': "",
  'country': country_value,
  'lv5s': "true",
  'osv': os_version,
  'oor': "false",
  'le': "true",
  'tas': "",
  'limitAdTracking': "false",
  'auctionId': "",
  'mediationName': "",
  'mediationVersion': "",
  'gameSessionId': str(game_session_id),
  'adFormat': "rewarded",
  'adType': "MRAID,VIDEO,DISPLAY",
  'webview_version': "0"
}

headers5 = {
  'User-Agent': user_agent,
  'Content-Type': "application/x-www-form-urlencoded",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip"
}

response5 = requests.post(url5, data=payload5, headers=headers5)

print(response5.status_code)




def encode_request_signal():
    def write_uint32(value):
        buf = []
        while True:
            byte = value & 0x7F
            value >>= 7
            if value:
                buf.append(byte | 0x80)
            else:
                buf.append(byte)
                break
        return buf

    metadata = {
        "field_1": 10,
        "field_2": 16,
        "field_3": 24,
        "field_23": 186,
        "field_24": 192,
        "field_25": 200,
        "field_26": 208,
        "field_27": 216,
        "field_28": 224,
        "field_29": 232,
        "field_30": 240,
        "field_31": 248,
        "field_32": 256,
        "field_33": 264,
        "field_34": 272,
        "field_35": 280,
        "field_37": 298,
        "field_38": 306,
        "field_39": 314,
        "field_40": 320,
        "field_41": 330,
        "field_42": 338,
        "field_48": 384,
        "field_49": 392,
        "field_50": 400
    }
    event_time =  int(time.time())
    app_uptime = random.randint(100000,999999)
    apptime_value = event_time-app_uptime
     
    request_signal = {
      "field_1": "unity-android-v4.6.1",
      "field_2": int(battery_label * 100),
      "field_3": 1,
      "field_23": str(os_version),
      "field_24": int(cpu_value),
      "field_25": int(random.randint(100000000,999999999)),
      "field_26": int(random.randint(100000000,999999999)),
      "field_27": int(timezone_offset2),
      "field_28": 0,
      "field_29": 0,
      "field_30": 0,
      "field_31": 1,
      "field_32": True,
      "field_33": int(apptime_value),
      "field_34": int(app_uptime),
      "field_35":  int(event_time),
      "field_37": "",
      "field_38": str(sig_value),
      "field_39": str(version_value),
      "field_40": int(version_code),
      "field_41": str(pack_value),
      "field_42": str(insataller_pack),
      "field_48": int(width_value),
      "field_49": int(height_value),
      "field_50": 1
    }

    byte_data = []
    for field, value in request_signal.items():
        metadata_value = metadata.get(field, None)
        if metadata_value is not None:
            encoded_metadata = write_uint32(metadata_value)
            
            if isinstance(value, int):
                encoded_value = write_uint32(value)
                combined_values = encoded_metadata + encoded_value
            elif isinstance(value, str):
                ascii_values = [ord(char) for char in value]
                length_encoded = write_uint32(len(ascii_values))
                combined_values = encoded_metadata + length_encoded + ascii_values
            elif isinstance(value, bool):
                encoded_value = [1 if value else 0]
                combined_values = encoded_metadata + encoded_value
            else:
                continue

            byte_data.extend(combined_values)

    byte_data_length = len(byte_data)
    encoded_data = write_uint32(10) + write_uint32(byte_data_length) + byte_data + [24, 2, 32, 3]

    encoded_string = base64.b64encode(bytes(encoded_data)).decode('utf-8')
    signal_value = re.sub(r'=+$', '', encoded_string.replace('/', '_').replace('+', '-'))
    
    return signal_value
    
 

def payload14():
    return {
        "eventId": str(uuid.uuid4()),
        "auctionId": auction_value,
        "gameSessionId": game_session_id,
        "campaignId": campaign_value,
        "seatId": seat_value,
        "placementId": "Rewarded_Android",
        "osVersion": os_version,
        "sid": "",
        "deviceModel": device_model,
        "sdkVersion": 4610,
        "bundleId": pack_value,
        "meta": meta_value,
        "platform": "android",
        "language": "en_US",
        "cached": True,
        "cachedOrientation": "portrait",
        "token": token_value,
        "gdprEnabled": False,
        "optOutEnabled": False,
        "optOutRecorded": False,
        "privacy": {
            "method": "default",
            "firstRequest": True,
            "permissions": {
                "ads": True,
                "external": True,
                "gameExp": True
            }
        },
        "gameSessionCounters": {
            "adRequests": 1,
            "starts": 0,
            "views": 0,
            "startsPerTarget": {},
            "viewsPerTarget": {},
            "latestTargetStarts": {}
        },
        "networkType": int(net_value),
        "connectionType": "wifi",
        "screenWidth": int(width_value),
        "screenHeight": int(height_value),
        "deviceFreeSpace": device_free_space,
        "isLoadEnabled": True,
        "legalFramework": "none",
        "agreedOverAgeLimit": "missing",
        "loadV5Support": True,
        "rai": False,
        "raiReason": "load",
        "batteryLevel": battery_label,
        "batteryStatus": battery_value,
        "freeMemory": free_momory,
        "adFormat": "rewarded",
        "webview_version": 0,
        "aduid": "Rewarded_Android",
        "clientTs": int(time.time() * 1000),
        "apiLevel": int(api_value),
        "deviceMake": device_makes,
        "screenDensity": int(screen_densities),
        "screenSize": int(screen_size),
        "idfi": idfi_value,
        "auid": "",
        "advertisingTrackingId": adid_value,
        "limitAdTracking": False,
        "videoOrientation": "portrait",
        "webviewUa": user_agent,
        "placementMeta": place_meta_value,
        "unityCreativeId": creative_value
    }

url6 = "https://auction-load.unityads.unity3d.com/v6/games/"+game_value+"/requests"

params6 = {
  'idfi': idfi_value,
  'auid': "",
  'advertisingTrackingId': adid_value,
  'limitAdTracking': "false",
  'deviceModel': device_model,
  'platform': "android",
  'sdkVersion': "4610",
  'stores': "google",
  'deviceMake': device_makes,
  'screenSize': str(screen_size),
  'screenDensity': screen_densities,
  'apiLevel': api_value,
  'osVersion': os_version,
  'appInstaller': insataller_pack,
  'screenWidth': width_value,
  'screenHeight': height_value,
  'connectionType': "wifi",
  'networkType': net_value
}
ts_value3 = int(time.time() * 1000)
payload6 = {
  "bundleVersion": version_value,
  "bundleId": pack_value,
  "coppa": False,
  "language": "en_US",
  "gameSessionId": game_session_id,
  "timeZone": time_zone,
  "token": token_value,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "appStartTime": ts_value3,
  "totalSpace": space_value,
  "clientTs": ts_value3+random.randint(100,999),
  "tcString": "",
  "sessionFeatures": {
    "global_ads_focus_time": 0,
    "global_ads_focus_change_count": 0,
    "bidding_load_count": 0,
    "waterfall_load_count": 1,
    "focus_change_count": 0,
    "skip_count": 0
  },
  "cachingSpeed": {
    "unknown": 0,
    "wifi": 0,
    "cellular": 0
  },
  "webviewUa": user_agent,
  "requestReason": "initialization",
  "dsp": {
    "skOverlay": True,
    "productPage": True
  },
  "experiments": {},
  "deviceFreeSpace": device_free_space,
  "networkOperator": network_operator,
  "networkOperatorName": network_name,
  "wiredHeadset": False,
  "volume": volume_value,
  "batteryStatus": battery_value,
  "requestSignal": encode_request_signal(),
  "ext": {
    "seq_num": 0,
    "granular_speed_bucket": "wi",
    "network_metered": True,
    "mobile_device_submodel": device_model,
    "prior_user_requests": 0,
    "device_battery_charging": battery_value == 2,
    "device_battery_level": battery_label,
    "android_market_version": "1."+pack_value,
    "prior_click_count": 0,
    "device_incapabilities": "mt",
    "ios_jailbroken": False,
    "iu_sizes": width_value+"x"+height_value+"|"+height_value+"x"+width_value,
    "ad_load_duration": 0
  },
  "batteryLevel": battery_label,
  "freeMemory": free_momory,
  "appVersion": version_value,
  "versionCode": version_code,
  "placements": {},
  "properties": properties_value,
  "sessionDepth": 0,
  "projectId": project_value,
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True
    }
  },
  "abGroup": int(ab_value),
  "isLoadEnabled": True,
  "omidPartnerName": "Unity3d",
  "omidJSVersion": "1.3.0",
  "srcPayoutType": "cpm",
  "organizationId": organ_id,
  "developerId": developer_id,
  "loadV5Support": True,
  "preload": True,
  "load": False,
  "preloadPlacements": {
    "Interstitial_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial",
      "placementType": "waterfall",
      "adUnitId": "Interstitial_Android"
    },
    "Rewarded_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": False,
      "auctionType": "cpm",
      "adFormat": "rewarded",
      "placementType": "waterfall",
      "adUnitId": "Rewarded_Android"
    },
    "Unity_Standard_Placement": {
      "adTypes": [
        "MRAID",
        "VIDEO"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial",
      "adUnitId": "Unity_Standard_AdUnit"
    }
  },
  "preloadData": {}
}

response6 = requests.post(url6, params=params6, data=json.dumps(payload6), headers=headers3)

print(response6.status_code)


payload7 = {
  "bundleVersion": version_value,
  "bundleId": pack_value,
  "coppa": False,
  "language": "en_US",
  "gameSessionId": game_session_id,
  "timeZone": time_zone,
  "token": token_value,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "appStartTime": ts_value3,
  "totalSpace": space_value,
  "clientTs": ts_value3+random.randint(100,999),
  "tcString": "",
  "sessionFeatures": {
    "global_ads_focus_time": 0,
    "global_ads_focus_change_count": 0,
    "bidding_load_count": 0,
    "waterfall_load_count": 1,
    "focus_change_count": 0,
    "skip_count": 0
  },
  "cachingSpeed": {
    "unknown": 0,
    "wifi": 0,
    "cellular": 0
  },
  "webviewUa": user_agent,
  "dsp": {
    "skOverlay": True,
    "productPage": True
  },
  "experiments": {},
  "deviceFreeSpace": device_free_space-random.randint(100,999),
  "networkOperator": network_operator,
  "networkOperatorName": network_name,
  "wiredHeadset": False,
  "volume": volume_value,
  "batteryStatus": battery_value,
  "requestSignal": encode_request_signal(),
  "ext": {
    "seq_num": 1,
    "granular_speed_bucket": "wi",
    "network_metered": True,
    "mobile_device_submodel": device_model,
    "prior_user_requests": 0,
    "device_battery_charging": battery_value == 2,
    "device_battery_level": battery_label,
    "android_market_version": "1."+pack_value,
    "prior_click_count": 0,
    "device_incapabilities": "mt",
    "ios_jailbroken": False,
    "iu_sizes": width_value+"x"+height_value+"|"+height_value+"x"+width_value,
    "ad_load_duration": 0
  },
  "batteryLevel": battery_label,
  "freeMemory": free_momory,
  "appVersion": version_value,
  "versionCode": version_code,
  "placements": {
    "Rewarded_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": False,
      "auctionType": "cpm",
      "adFormat": "rewarded",
      "placementType": "waterfall",
      "adUnitId": "Rewarded_Android"
    }
  },
  "properties": properties_value,
  "sessionDepth": 1,
  "projectId": project_value,
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True
    }
  },
  "abGroup": int(ab_value),
  "isLoadEnabled": True,
  "omidPartnerName": "Unity3d",
  "omidJSVersion": "1.3.0",
  "srcPayoutType": "cpm",
  "organizationId": organ_id,
  "developerId": developer_id,
  "loadV5Support": True,
  "load": True,
  "preload": False,
  "preloadData": {
    "Rewarded_Android": {
      "campaignAvailable": False
    }
  },
  "preloadPlacements": {}
}
response7 = requests.post(url6, params=params6, data=json.dumps(payload7), headers=headers3)

print(response7.status_code)

time_stamp = random.randint(100000000,999999999)

url8 = "https://httpkafka.unityads.unity3d.com/v1/events"

payload18 = {
    "common": {
        "client": {
            "gameId": game_value,
            "testMode": False,
            "bundleId": pack_value,
            "bundleVersion": version_value,
            "sdkVersion": 4610,
            "sdkVersionName": "4.6.1",
            "encrypted": True,
            "configUrl": url,
            "webviewUrl": response2.json()["url"],
            "webviewHash": response2.json()["hash"],
            "webviewVersion": response2.json()["version"],
            "initTimestamp": time_stamp,
            "reinitialized": False,
            "usePerPlacementLoad": True,
            "isWebViewUpdateAvailable": False,
            "loadCompleteTimestamp": time_stamp+random.randint(1000,2000),
            "stateId": "",
            "platform": "android"
        },
        "device": {
            "osVersion": os_version,
            "deviceModel": device_model,
            "connectionType": "wifi",
            "networkType": net_value,
            "screenWidth": int(width_value),
            "screenHeight": int(height_value),
            "networkOperator": network_operator,
            "networkOperatorName": network_name,
            "timeZone": time_zone,
            "headset": False,
            "language": "en_US",
            "deviceVolume": volume_value,
            "screenBrightness": 1,
            "freeSpaceInternal": device_free_space,
            "totalSpaceInternal": space_value,
            "batteryLevel": battery_label,
            "batteryStatus": battery_value,
            "freeMemory": free_momory,
            "totalMemory": total_momory,
            "rooted": False,
            "apiLevel": int(api_value),
            "deviceMake": device_makes,
            "screenLayout": screen_size,
            "screenDensity": int(screen_densities),
            "displayMetricDensity": random.randint(1, 6),
            "totalSpaceExternal": space_value,
            "freeSpaceExternal": device_free_space,
            "ringerMode": 1,
            "userAgent": user_agent
        },
        "country": country_value
    }
}

payload28 = {
    "type": "ads.events.availability.v1.json",
    "msg": {
        "v": 1,
        "mwu": False,
        "arCameraPermission": False,
        "loadApiEnabled": True
    }
}

data8 = f"{json.dumps(payload18)}\n{json.dumps(payload28)}"

#response8 = requests.post(url8, data=data8, headers=headers3)

#print(response8.status_code)

media_value = response7.json()["placementsV2"]["Rewarded_Android"]["mediaId"][0]

seat_value = response7.json()["media"][media_value]["seatId"]

campaign_value = response7.json()["media"][media_value]["campaignId"]

auction_value = response7.json()["auctionId"]

content_type = response7.json()["media"][media_value]["contentType"]

print(content_type)

datapts_value = response7.json()["placementsV2"]["Rewarded_Android"]["tracking"][0]["events"]["start"]["params"]["datapts"]

if len(campaign_value) == 24:
    campaign_value = campaign_value
else:
    campaign_value = "005472656d6f7220416e6472"
    
payload5["eventType"]="fill"
payload5["campaignId"]=campaign_value
payload5["seatId"]=seat_value
payload5["auctionId"]=auction_value

response9 = requests.post(url5, data=payload5, headers=headers5)

print(response9.status_code)

for item in reversed(response7.json()["trackingTemplates"]):
    if item.endswith("${PLACEMENT_WIDTH}"):

        break
        
item = item+"&webview_version=0"

url_10 = item.replace("{{placement}}", "Rewarded_Android") \
                 .replace("{{eventType}}", "{{eventType}}") \
                 .replace("{{isHB}}", "false") \
                 .replace("%GAMER_SID%", "") \
                 .replace("%GAME_SESSION_ID%", str(game_session_id)) \
                 .replace("%AD_UNIT_ID%", "Rewarded_Android") \
                 .replace("%AD_FORMAT%", "rewarded")
                 
if content_type == "comet/campaign":
    
    url10 = url_10.replace("{{eventType}}", "show")
    response10 = requests.post(url10, headers=headers5)
    print(response10.status_code)

    url11 = url_10.replace("{{eventType}}", "loaded")
    response11 = requests.post(url11, headers=headers5)
    print(response11.status_code)

    url12 = url_10.replace("{{eventType}}", "start")
    response12 = requests.post(url12, headers=headers5)
    print(response12.status_code)

    for item_im in reversed(response7.json()["trackingTemplates"]):
        if item_im.startswith("https://events.mz.unity3d.com/impression"):
            break

    item_im = item_im + "&webview_version=0"

    url13 = item_im.replace("{{placement}}", "Rewarded_Android") \
                   .replace("{{datapts}}", datapts_value) \
                   .replace("{{isHB}}", "false") \
                   .replace("%25GAMER_SID%25", "") \
                   .replace("%25GAME_SESSION_ID%25", str(game_session_id)) \
                   .replace("%25AD_UNIT_ID%25", "Rewarded_Android") \
                   .replace("%25AD_FORMAT%25", "rewarded") \
                   .replace("%25OM_ENABLED%25", "false") \
                   .replace("%25OM_VENDORS%25", "")
                   
    response13 = requests.post(url13, headers=headers5)
    print(response13.status_code)

    place_meta_value = response7.json()["placementsV2"]["Rewarded_Android"]["meta"]
    content_value = response7.json()["media"][media_value]["content"]
    parsed_content4 = json.loads(content_value)
    meta_value = parsed_content4["meta"]
    creative_value = parsed_content4.get("portraitCreativeId", parsed_content4.get("creativeId"))
    video_event_value = parsed_content4["videoEventUrls"]
    game_event_value = str(parsed_content4["gameId"])

    response14 = requests.post(video_event_value["video_start"], data=json.dumps(payload14()), headers=headers3)
    print(response14.status_code)

    payload15 = {
  "bundleVersion": version_value,
  "bundleId": pack_value,
  "coppa": False,
  "language": "en_US",
  "gameSessionId": game_session_id,
  "timeZone": time_zone,
  "token": token_value,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "appStartTime": ts_value3,
  "totalSpace": space_value,
  "clientTs": ts_value3+random.randint(100,999),
  "tcString": "",
  "sessionFeatures": {
    "global_ads_focus_time": 0,
    "global_ads_focus_change_count": 1,
    "bidding_load_count": 0,
    "waterfall_load_count": 1,
    "focus_change_count": 2,
    "skip_count": 0
  },
  "cachingSpeed": {
    "unknown": 0,
    "wifi": random.randint(500,1000),
    "cellular": 0
  },
  "previousPlacementId": "Rewarded_Android",
  "webviewUa": user_agent,
  "requestReason": "impression-started",
  "dsp": {
    "skOverlay": True,
    "productPage": True
  },
  "experiments": {},
  "deviceFreeSpace": device_free_space,
  "networkOperator": network_operator,
  "networkOperatorName": network_name,
  "wiredHeadset": False,
  "volume": volume_value,
  "batteryStatus": battery_value,
  "requestSignal": encode_request_signal(),
  "ext": {
    "seq_num": 1,
    "granular_speed_bucket": "wi",
    "network_metered": True,
    "mobile_device_submodel": device_model,
    "prior_user_requests": 0,
    "device_battery_charging": battery_value == 2,
    "device_battery_level": battery_label,
    "android_market_version": "1."+pack_value,
    "prior_click_count": 0,
    "device_incapabilities": "mt",
    "ios_jailbroken": False,
    "iu_sizes": width_value+"x"+height_value+"|"+height_value+"x"+width_value,
    "ad_load_duration": 0
  },
  "batteryLevel": battery_label,
  "freeMemory": free_momory,
  "appVersion": version_value,
  "versionCode": version_code,
  "placements": {},
  "properties": properties_value,
  "sessionDepth": 1,
  "projectId": project_value,
  "gameSessionCounters": {
    "adRequests": 2,
    "starts": 1,
    "views": 0,
    "startsPerTarget": {
      game_event_value: 1
    },
    "viewsPerTarget": {},
    "latestTargetStarts": {
      game_event_value: formatted_time_utc
    }
  },
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True
    }
  },
  "abGroup": int(ab_value),
  "isLoadEnabled": True,
  "omidPartnerName": "Unity3d",
  "omidJSVersion": "1.3.0",
  "srcPayoutType": "cpm",
  "organizationId": organ_id,
  "developerId": developer_id,
  "loadV5Support": True,
  "load": True,
  "preload": True,
  "preloadPlacements": {
    "Interstitial_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial",
      "placementType": "waterfall",
      "adUnitId": "Interstitial_Android"
    },
    "Rewarded_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": False,
      "auctionType": "cpm",
      "adFormat": "rewarded",
      "placementType": "waterfall",
      "adUnitId": "Rewarded_Android"
    },
    "Unity_Standard_Placement": {
      "adTypes": [
        "MRAID",
        "VIDEO"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial",
      "adUnitId": "Unity_Standard_AdUnit"
    }
  },
  "preloadData": {}
    }
    response15 = requests.post(url6, params=params6, data=json.dumps(payload15), headers=headers3)
    print(response15.status_code)

    url16 = url_10.replace("{{eventType}}", "firstQuartile")
    response16 = requests.post(url16, headers=headers5)
    print(response16.status_code)

    response17 = requests.post(video_event_value["first_quartile"], data=json.dumps(payload14()), headers=headers3)
    print(response17.status_code)

    url18 = url_10.replace("{{eventType}}", "midpoint")
    response18 = requests.post(url18, headers=headers5)
    print(response18.status_code)

    response19 = requests.post(video_event_value["midpoint"], data=json.dumps(payload14()), headers=headers3)
    print(response19.status_code)

    url20 = "https://publisher-event.unityads.unity3d.com/events/v2/timing"
    payload_20 = {
        "origin": "video-screen",
        "triggerAtMs": 10000,
        "event": "view"
    }
    payload20 = payload14()
    payload20["timingDetails"] = payload_20
    response20 = requests.post(url20, data=json.dumps(payload20), headers=headers3)
    print(response20.status_code)

    url21 = url_10.replace("{{eventType}}", "thirdQuartile")
    response21 = requests.post(url21, headers=headers5)
    print(response21.status_code)

    response22 = requests.post(video_event_value["third_quartile"], data=json.dumps(payload14()), headers=headers3)
    print(response22.status_code)

    url23 = url_10.replace("{{eventType}}", "complete")
    response23 = requests.post(url23, headers=headers5)
    print(response23.status_code)

    response24 = requests.post(video_event_value["video_end"], data=json.dumps(payload14()), headers=headers3)
    print(response24.status_code)

    url25 = "https://publisher-event.unityads.unity3d.com/events/v2/lifecycle"
    payload25 = {
        "duration": random.randint(26000, 30000),
        "evt": "completed",
        "placementId": "Rewarded_Android",
        "auid": auction_value,
        "meta": meta_value,
        "token": token_value,
        "placementMeta": place_meta_value
    }
    response25 = requests.post(url25, data=json.dumps(payload25), headers=headers3)
    print(response25.status_code)
    
if content_type == "programmatic/vast-vpaid":
	
    url10 = url_10.replace("{{eventType}}", "resume")
    response10 = requests.post(url10, headers=headers5)
    print(response10.status_code)

    url11 = url_10.replace("{{eventType}}", "resume")
    response11 = requests.post(url11, headers=headers5)
    print(response11.status_code)

    url12 = url_10.replace("{{eventType}}", "creativeView")
    response12 = requests.post(url12, headers=headers5)
    print(response12.status_code)

    
    for item_im in reversed(response7.json()["trackingTemplates"]):
        if item_im.startswith("https://events.mz.unity3d.com/impression"):
            break

    item_im = item_im + "&webview_version=0"

    url13 = item_im.replace("{{placement}}", "Rewarded_Android") \
                   .replace("{{datapts}}", datapts_value) \
                   .replace("{{isHB}}", "false") \
                   .replace("%25GAMER_SID%25", "") \
                   .replace("%25GAME_SESSION_ID%25", str(game_session_id)) \
                   .replace("%25AD_UNIT_ID%25", "Rewarded_Android") \
                   .replace("%25AD_FORMAT%25", "rewarded") \
                   .replace("%25OM_ENABLED%25", "false") \
                   .replace("%25OM_VENDORS%25", "")
                   
    response13 = requests.post(url13, headers=headers5)
    print(response13.status_code)        
                