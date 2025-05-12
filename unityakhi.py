import requests
import json
import uuid
import random
from datetime import datetime, timezone
import base64
import gzip
import io
import time
import urllib.parse
#from rich import print

#for method in ['get', 'post', 'put', 'delete', 'head', 'options', 'patch']:
#    setattr(requests, method, lambda *args, m=method, **kwargs: requests.request(m.upper(), *args, verify=True, **kwargs))

game_value = "5852796"
bundle_id = "iT.unity.ads.examplf"
app_version = "1.0"
version_code = 1
time_zone = "EST"
timezone_offset = 1200
apk_sig_value = "e48a165651c8c03ea17828207b29149c576de44e"
network_type = "13"

analyticsSessionId = str(random.randint(20000000000000,99999999999999))
idfi_value = str(uuid.uuid4())
device_make = random.choice([
    "samsung", "google", "huawei", "oneplus", "xiaomi", "lg", "sony",
    "oppo", "vivo", "nokia", "motorola", "asus", "realme", "lenovo", "blackberry"
])
screen_density = random.choice([
    "120", "160", "240", "320", "400", "420", "450", "480", "560", "640"
])
cpu_value = random.choice([
    4, 6, 8
])
screen_size = str(random.choice([
    268435810, 268435826, 268435811, 268435827, 268435812, 268435828,
    268435842, 268435858, 805306386, 805306387, 805306404, 805306402,
    805306418, 805306420]))
adid_value = str(uuid.uuid4())
screen_height = str(random.randint(800,2960))
screen_width = str(random.randint(480,1440))
os_version = random.choice([
    "11", "12", "13", "14"
])
def generate_hex():
    first_1 = ''.join(random.choices('0123456789abcdef', k=12))
    second_2 = ''.join(random.choices('0123456789abcdef', k=3))
    check_y = ''.join(random.choices('ab89', k=1))
    third_1 = ''.join(random.choices('0123456789abcdef', k=15))
    
    return(first_1+"4"+second_2+check_y+third_1)
    
analyticsUserId = generate_hex()
sessionId = generate_hex()
api_level = str(int(os_version)+20)
totalSpace = random.randint(2000000000,9999999999)
deviceFreeSpace = random.randint(20000000,99999999)
freeMemory = random.randint(1000000,9999999)
deviceFreeSpace2 = random.randint(20000000,99999999)
ad_load_duration = random.randint(5000,15000)
freeMemory2 = random.randint(1000000,9999999)

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
networkOperator = operator[1]
networkOperatorName = operator[0]
volume = random.randint(0,15)
batteryStatus = random.randint(1,4)
battery_charging = batteryStatus == 2
battery_level = round(random.uniform(0.40, 1.00), 2)
installHour = int(datetime.now().replace(minute=0, second=0, microsecond=0).timestamp() * 1000)

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
    "ONEPLUS A6000", "ONEPLUS A6010", "ONEPLUS A6013", "ONEPLUS A5010", "ONEPLUS A5000", 
    "ONEPLUS A7000", "ONEPLUS A7001", "ONEPLUS A7003", "ONEPLUS A6013", "ONEPLUS BE2013", 
    "ONEPLUS BE2028", "ONEPLUS BE2012", "ONEPLUS GM1911", "ONEPLUS GM1913", "ONEPLUS GM1901", 
    "ONEPLUS GM1903", "ONEPLUS HD1901", "ONEPLUS HD1903", "ONEPLUS IN2010", "ONEPLUS IN2020", 
    "ONEPLUS IN2021", "ONEPLUS LE2110", "ONEPLUS LE2113", "ONEPLUS LE2115", "ONEPLUS LE2120", 
    "ONEPLUS LE2127", "ONEPLUS LE2123", "ONEPLUS LA2001", "ONEPLUS LA2003", "ONEPLUS LA2020", 
    "ONEPLUS LU2020", "ONEPLUS LU2030", "ONEPLUS LU2033", "ONEPLUS LU2025", "ONEPLUS LU2028", 
    "ONEPLUS X9000", "ONEPLUS X9003", "ONEPLUS X9001", "ONEPLUS X9010", "ONEPLUS RMX1911", 
    "ONEPLUS RMX1913", "ONEPLUS RMX1921", "ONEPLUS RMX1931", "ONEPLUS RMX1993", "ONEPLUS RMX2051", 
    "ONEPLUS RMX2053", "ONEPLUS RMX2063", "ONEPLUS RMX2075", "ONEPLUS RMX2101", "ONEPLUS RMX2103"
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
}.get(device_make)

build_code = {"14": "U", "13": "T", "12": "S", "11": "R"}[os_version]+"P1A."+f"{random.randint(20, 24)}{random.randint(1, 12):02}{random.randint(1, 30):02}"+".007"

chrome_version = random.choice([
    "136.0.7103.60",
    "135.0.7049.111",
    "135.0.7049.100",
    "135.0.7049.79",
    "135.0.7049.38",
    "134.0.6998.135",
    "134.0.6998.108",
    "134.0.6998.95",
    "133.0.6943.137",
    "133.0.6943.121"
])

user_agent = "Dalvik/2.1.0 (Linux; U; Android "+os_version+"; "+device_model+" Build/"+build_code+")"

webviewUa = "Mozilla/5.0 (Linux; Android "+os_version+"; "+device_model+" Build/"+build_code+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+chrome_version+" Mobile Safari/537.36"

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
      "field_1": "unity-android-v3.4.6",
      "field_2": int(battery_level * 100),
      "field_3": 1,
      "field_23": str(os_version),
      "field_24": int(cpu_value),
      "field_25": int(random.randint(100000000,999999999)),
      "field_26": int(random.randint(100000000,999999999)),
      "field_27": int(timezone_offset),
      "field_28": 0,
      "field_29": 0,
      "field_30": 0,
      "field_31": 0,
      "field_32": True,
      "field_33": int(apptime_value),
      "field_34": int(app_uptime),
      "field_35":  int(event_time),
      "field_37": "",
      "field_38": str(apk_sig_value),
      "field_39": str(app_version),
      "field_40": int(version_code),
      "field_41": str(bundle_id),
      "field_42": "com.android.vending",
      "field_48": int(screen_width),
      "field_49": int(screen_height),
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



url = "https://publisher-config.unityads.unity3d.com/privacy/"+game_value+"/state"

payload = {
  "platform": "android",
  "idfi": idfi_value,
  "sdkVersionName": "3.4.6",
  "unity.privacy.permissions.all": False,
  "unity.privacy.permissions.gameExp": False,
  "unity.privacy.permissions.ads": False,
  "unity.privacy.permissions.external": False
}

headers = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)

url2 = "https://publisher-config.unityads.unity3d.com/games/"+game_value+"/configuration?deviceMake="+device_make+"&screenDensity="+screen_density+"&screenSize="+screen_size+"&idfi="+idfi_value+"&advertisingTrackingId="+adid_value+"&limitAdTracking=false&installationId="+idfi_value+"&connectionType=cellular&screenHeight="+screen_height+"&screenWidth="+screen_width+"&usePerPlacementLoad=false&bundleId="+bundle_id+"&encrypted=true&rooted=false&platform=android&sdkVersion=3460&osVersion="+os_version+"&deviceModel="+device_model+"&language=en_US&test=false&first=true&userLevelFlagDetected=false"

headers2 = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip"
}

response2 = requests.get(url2, headers=headers2)

print(response2.status_code)
print(response2.json()["enabled"])

organ_value = response2.json()["organizationId"]
token_value = response2.json()["token"]
project_value = response2.json()["projectId"]
country_value = response2.json()["country"]
appStoreId_value = response2.json()["appStoreId"]
method_value = response2.json()["gamePrivacy"]["method"]
legalFramework_value = response2.json()["legalFramework"]
properties_value = response2.json()["properties"]
abGroup_int = response2.json()["abGroup"]
developerId_int = response2.json()["developerId"]

url3 = "https://thind.unityads.unity3d.com/v1/events"

ts_value = int(time.time()*1000)

payload3 = "{\"common\":{\"gameId\":\""+game_value+"\",\"organizationId\":\""+organ_value+"\",\"analyticsUserId\":\""+analyticsUserId+"\",\"analyticsSessionId\":\""+analyticsSessionId+"\",\"sessionId\":\""+sessionId+"\",\"platform\":\"ANDROID\",\"adsSdkVersion\":\"3.4.6\",\"gamerToken\":\""+token_value+"\",\"limitAdTracking\":false,\"coppaFlagged\":false,\"projectId\":\""+project_value+"\",\"gdprEnabled\":false,\"optOutRecorded\":false,\"optOutEnabled\":false,\"deviceMake\":\""+device_make+"\",\"deviceModel\":\""+device_model+"\",\"connectionType\":\"cellular\",\"country\":\""+country_value+"\",\"storeId\":\""+appStoreId_value+"\",\"privacy\":{\"permissions\":{\"ads\":true,\"external\":true,\"gameExp\":true},\"method\":\""+method_value+"\"},\"installHour\":"+str(installHour)+",\"trackingAuthStatus\":3}}\n{\"type\":\"ads.analytics.appInstall.v2\",\"msg\":{\"ts\":"+str(ts_value)+",\"appVersion\":\""+app_version+"\",\"timeSinceStart\":0}}\n"

headers3 = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json"
}

response3 = requests.post(url3, data=payload3, headers=headers3)

print(response3.status_code)

url4 = "https://thind.unityads.unity3d.com/v1/events"

payload4 = "{\"common\":{\"gameId\":\""+game_value+"\",\"organizationId\":\""+organ_value+"\",\"analyticsUserId\":\""+analyticsUserId+"\",\"analyticsSessionId\":\""+analyticsSessionId+"\",\"sessionId\":\""+sessionId+"\",\"platform\":\"ANDROID\",\"adsSdkVersion\":\"3.4.6\",\"gamerToken\":\""+token_value+"\",\"limitAdTracking\":false,\"coppaFlagged\":false,\"projectId\":\""+project_value+"\",\"gdprEnabled\":false,\"optOutRecorded\":false,\"optOutEnabled\":false,\"deviceMake\":\""+device_make+"\",\"deviceModel\":\""+device_model+"\",\"connectionType\":\"cellular\",\"country\":\""+country_value+"\",\"storeId\":\""+appStoreId_value+"\",\"privacy\":{\"permissions\":{\"ads\":true,\"external\":true,\"gameExp\":true},\"method\":\""+method_value+"\"},\"installHour\":"+str(installHour)+",\"trackingAuthStatus\":3}}\n{\"type\":\"ads.analytics.appStart.v2\",\"msg\":{\"nAppStartDay\":1,\"nAppStartUser\":1,\"ts\":"+str(ts_value)+"}}\n"

headers4 = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json"
}

response4 = requests.post(url4, data=payload4, headers=headers4)

print(response4.status_code)

url5 = "https://auction.unityads.unity3d.com/v6/games/"+game_value+"/requests?idfi="+idfi_value+"&advertisingTrackingId="+adid_value+"&limitAdTracking=false&deviceModel="+device_model+"&platform=android&sdkVersion=3460&stores=google&deviceMake="+device_make+"&screenSize="+screen_size+"&screenDensity="+screen_density+"&apiLevel="+api_level+"&osVersion="+os_version+"&appInstaller=com.android.vending&screenWidth="+screen_width+"&screenHeight="+screen_height+"&connectionType=cellular&networkType="+network_type+""

appStartTime = int(time.time()*1000)

payload5 = {
  "bundleVersion": app_version,
  "bundleId": bundle_id,
  "coppa": False,
  "language": "en_US",
  "gameSessionId": int(analyticsSessionId),
  "timeZone": time_zone,
  "token": token_value,
  "legalFramework": legalFramework_value,
  "agreedOverAgeLimit": "missing",
  "appStartTime": appStartTime,
  "totalSpace": totalSpace,
  "webviewUa": webviewUa,
  "dsp": {
    "skOverlay": True,
    "productPage": True
  },
  "experiments": {
    "fullScreenCtaEnabled": True
  },
  "deviceFreeSpace": deviceFreeSpace,
  "networkOperator": networkOperator,
  "networkOperatorName": networkOperatorName,
  "wiredHeadset": False,
  "volume": volume,
  "batteryStatus": batteryStatus,
  "requestSignal": encode_request_signal(),
  "ext": {
    "seq_num": 0,
    "granular_speed_bucket": "4g",
    "network_metered": True,
    "mobile_device_submodel": device_model,
    "prior_user_requests": 0,
    "device_battery_charging": battery_charging,
    "device_battery_level": battery_level,
    "android_market_version": str(version_code)+"."+bundle_id,
    "prior_click_count": 0,
    "device_incapabilities": "mt",
    "ios_jailbroken": False,
    "iu_sizes": screen_width+"x"+screen_height+"|"+screen_height+"x"+screen_width,
    "ad_load_duration": 0
  },
  "batteryLevel": battery_level,
  "freeMemory": freeMemory,
  "appVersion": app_version,
  "versionCode": version_code,
  "placements": {
    "Interstitial_Android": {
      "adTypes": [
        "MRAID",
        "VIDEO",
        "DISPLAY"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial",
      "placementType": "bidding"
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
      "placementType": "bidding"
    },
    "Banner_Android": {
      "adTypes": [
        "BANNER"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "banner",
      "placementType": "bidding"
    },
    "Unity_Standard_Placement": {
      "adTypes": [
        "MRAID",
        "VIDEO"
      ],
      "allowSkip": True,
      "auctionType": "cpm",
      "adFormat": "interstitial"
    }
  },
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
    "method": method_value,
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True
    }
  },
  "abGroup": abGroup_int,
  "isLoadEnabled": False,
  "omidPartnerName": "Unity3d",
  "omidJSVersion": "1.3.0",
  "srcPayoutType": "cpm",
  "organizationId": organ_value,
  "developerId": developerId_int
}

headers5 = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json"
}

response5 = requests.post(url5, data=json.dumps(payload5), headers=headers5)

print(response5.status_code)

mediaId_value = response5.json()["placementsV2"]["Rewarded_Android"]["mediaId"][0]
content_type = response5.json()["media"][mediaId_value]["contentType"]

print(content_type)

def base_operative_url(data):
    for url in data.get('trackingTemplates', []):
        if url.startswith("https://") and url.endswith("{PLACEMENT_WIDTH}"):
            data_part = url.split("data=")[1].split("&")[0]
            decoded = base64.urlsafe_b64decode(data_part)
            decompressed = gzip.GzipFile(fileobj=io.BytesIO(decoded)).read().decode()
            if "plId=Rewarded_Android" in decompressed:
                return url + "&webview_version=0"
    return None

operative_url = base_operative_url(response5.json())

replacement_op = {
    "{{placement}}": "Rewarded_Android",
    "{{eventType}}": "{{}}",
    "{{isHB}}": "false",
    "%GAMER_SID%": "",
    "%GAME_SESSION_ID%": str(analyticsSessionId),
    "%AD_UNIT_ID%": "Rewarded_Android",
    "%AD_FORMAT%": "rewarded"
}

for key, value in replacement_op.items():
    if operative_url:
        operative_url = operative_url.replace(key, value)

def get_operative_url(eventType):
    if operative_url:
        return operative_url.replace("{{}}", eventType).replace('{', '%7B').replace('}', '%7D').split("?")[1]
    return None


url6 = "https://events.mz.unity3d.com/operative/Rewarded_Android"

headers6 = {
  'User-Agent': webviewUa,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': 'application/x-www-form-urlencoded'
}

url8 = "https://events.mz.unity3d.com/impression/Rewarded_Android"

payload8 = {
  'adFormat': "rewarded",
  'adUnitId': "Rewarded_Android",
  'data': urllib.parse.unquote(response5.json()["placementsV2"]["Rewarded_Android"]["tracking"][0]["events"]["start"]["params"]["datapts"]),
  'gameSessionId': str(analyticsSessionId),
  'gamerSid': "",
  'isHB': "false",
  'isomenabled': "false",
  'key': "11",
  'omvendors': "",
  'webview_version': "0"
}

headers8 = {
  'User-Agent': webviewUa,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip"
}

headers10 = {
  'User-Agent': user_agent,
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json"
}


if content_type == "comet/campaign":
	
	response6 = requests.post(url6, data=get_operative_url("show"), headers=headers6)
	print(response6.status_code)

	response7 = requests.post(url6, data=get_operative_url("loaded"), headers=headers6)
	print(response7.status_code)
	
	response8 = requests.post(url8, data=payload8, headers=headers8)
	print(response8.status_code)


	response9 = requests.post(url6, data=get_operative_url("start"), headers=headers6)
	print(response9.status_code)
	
	content_value = json.loads(response5.json()["media"][mediaId_value]["content"])
	video_events_url = content_value["videoEventUrls"]
	auctionId = response5.json()["auctionId"]
	campaignId = response5.json()["media"][mediaId_value]["campaignId"]
	seatId_int = response5.json()["media"][mediaId_value]["seatId"]
	meta_value = content_value["meta"]
	placemeta_value = response5.json()["placementsV2"]["Rewarded_Android"]["meta"]
	portraitCreativeId = content_value["portraitCreativeId"]
	gameId_int = content_value["gameId"]
	
	
	def generate_payload10(placemeta_value):
		payload10 = {
            "eventId": str(uuid.uuid4()),
            "auctionId": auctionId,
            "gameSessionId": int(analyticsSessionId),
            "campaignId": campaignId,
            "seatId": seatId_int,
            "placementId": "Rewarded_Android",
            "osVersion": os_version,
            "sid": "",
            "deviceModel": device_model,
            "sdkVersion": 3460,
            "bundleId": bundle_id,
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
                "method": method_value,
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
            "networkType": int(network_type),
            "connectionType": "cellular",
            "screenWidth": int(screen_width),
            "screenHeight": int(screen_height),
            "deviceFreeSpace": deviceFreeSpace,
            "isLoadEnabled": False,
            "legalFramework": legalFramework_value,
            "agreedOverAgeLimit": "missing",
            "loadV5Support": False,
            "rai": False,
            "raiReason": "load",
            "batteryLevel": battery_level,
            "batteryStatus": batteryStatus,
            "freeMemory": random.randint(403020, 803020),
            "adFormat": "rewarded",
            "webview_version": 0,
            "aduid": "Rewarded_Android",
            "apiLevel": int(api_level),
            "deviceMake": device_make,
            "screenDensity": int(screen_density),
            "screenSize": int(screen_size),
            "idfi": idfi_value,
            "advertisingTrackingId": adid_value,
            "limitAdTracking": False,
            "videoOrientation": "portrait",
            "webviewUa": webviewUa,
            "placementMeta": placemeta_value,
            "unityCreativeId": portraitCreativeId
        }
		return payload10
    
	response10 = requests.post(video_events_url["video_start"], data=json.dumps(generate_payload10(placemeta_value)), headers=headers10)
	print(response10.status_code)

	
	now = datetime.now(timezone.utc)
	formatted_time = now.strftime('%Y-%m-%dT%H:%M:%S.') + f"{int(now.microsecond / 1000):03d}Z"
	
	
	payload11 = {
        "bundleVersion": app_version,
        "bundleId": bundle_id,
        "coppa": False,
        "language": "en_US",
        "gameSessionId": int(analyticsSessionId),
        "timeZone": time_zone,
        "token": token_value,
        "legalFramework": legalFramework_value,
        "agreedOverAgeLimit": "missing",
        "appStartTime": appStartTime,
        "totalSpace": totalSpace,
        "previousPlacementId": "Rewarded_Android",
        "webviewUa": webviewUa,
        "dsp": {
            "skOverlay": True,
            "productPage": True
        },
        "experiments": {
            "fullScreenCtaEnabled": True
        },
        "deviceFreeSpace": deviceFreeSpace2,
        "networkOperator": networkOperator,
        "networkOperatorName": networkOperatorName,
        "wiredHeadset": False,
        "volume": volume,
        "batteryStatus": batteryStatus,
        "requestSignal": encode_request_signal(),
        "ext": {
            "seq_num": 1,
            "granular_speed_bucket": "4g",
            "network_metered": True,
            "mobile_device_submodel": device_model,
            "prior_user_requests": 1,
            "device_battery_charging": battery_charging,
            "device_battery_level": battery_level,
            "android_market_version": str(version_code) + "." + bundle_id,
            "prior_click_count": 0,
            "device_incapabilities": "mt",
            "ios_jailbroken": False,
            "iu_sizes": screen_width + "x" + screen_height + "|" + screen_height + "x" + screen_width,
            "ad_load_duration": ad_load_duration
        },
        "batteryLevel": battery_level,
        "freeMemory": freeMemory2,
        "appVersion": app_version,
        "cachedCampaigns": [campaignId],
        "versionCode": version_code,
        "placements": {
            "Interstitial_Android": {
                "adTypes": ["MRAID", "VIDEO", "DISPLAY"],
                "allowSkip": True,
                "auctionType": "cpm",
                "adFormat": "interstitial",
                "placementType": "bidding"
            },
            "Rewarded_Android": {
                "adTypes": ["MRAID", "VIDEO", "DISPLAY"],
                "allowSkip": False,
                "auctionType": "cpm",
                "adFormat": "rewarded",
                "placementType": "bidding"
            },
            "Banner_Android": {
                "adTypes": ["BANNER"],
                "allowSkip": True,
                "auctionType": "cpm",
                "adFormat": "banner",
                "placementType": "bidding"
            },
            "Unity_Standard_Placement": {
                "adTypes": ["MRAID", "VIDEO"],
                "allowSkip": True,
                "auctionType": "cpm",
                "adFormat": "interstitial"
            }
        },
        "properties": properties_value,
        "sessionDepth": 1,
        "projectId": project_value,
        "gameSessionCounters": {
            "adRequests": 2,
            "starts": 1,
            "views": 0,
            "startsPerTarget": {
                str(gameId_int): 1
            },
            "viewsPerTarget": {},
            "latestTargetStarts": {
                str(gameId_int): formatted_time
            }
        },
        "gdprEnabled": False,
        "optOutEnabled": False,
        "optOutRecorded": False,
        "privacy": {
            "method": method_value,
            "firstRequest": True,
            "permissions": {
                "ads": True,
                "external": True,
                "gameExp": True
            }
        },
        "abGroup": abGroup_int,
        "isLoadEnabled": False,
        "omidPartnerName": "Unity3d",
        "omidJSVersion": "1.3.0",
        "srcPayoutType": "cpm",
        "organizationId": organ_value,
        "developerId": developerId_int
    }
    
	response11 = requests.post(url5, data=json.dumps(payload11), headers=headers5)
	print(response11.status_code)
	
	placemeta_value2 = response11.json()["placementsV2"]["Rewarded_Android"]["meta"]
	
	
	response12 = requests.post(url6, data=get_operative_url("firstQuartile"), headers=headers6)
	print(response12.status_code)
	

	response13 = requests.post(video_events_url["first_quartile"], data=json.dumps(generate_payload10(placemeta_value2)), headers=headers10)
	print(response13.status_code)
	
	
	response14 = requests.post(url6, data=get_operative_url("midpoint"), headers=headers6)
	print(response14.status_code)
	

	response15 = requests.post(video_events_url["midpoint"], data=json.dumps(generate_payload10(placemeta_value2)), headers=headers10)
	print(response15.status_code)
	
	
	response16 = requests.post(url6, data=get_operative_url("thirdQuartile"), headers=headers6)
	print(response16.status_code)
	

	response17 = requests.post(video_events_url["third_quartile"], data=json.dumps(generate_payload10(placemeta_value2)), headers=headers10)
	print(response17.status_code)
	
	
	response18 = requests.post(url6, data=get_operative_url("complete"), headers=headers6)
	print(response18.status_code)
	

	response19 = requests.post(video_events_url["video_end"], data=json.dumps(generate_payload10(placemeta_value2)), headers=headers10)
	print(response19.status_code)
	