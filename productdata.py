from promotion import *

data = { "data" : 
    [
        {
            "product_id": "1516241000002" , 
            "object_id": "102641" , 
            "name": "เมาส์ Razer Viper V2 Pro Wireless Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Razer" , 
            "price" : 5490  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/06/Product/razer-viper-v2-pro-wireless-gaming-mouse-black-icon.jpg"] , 
            "option":"Black" ,
            "detail": {"มีสาย/ไร้สาย":"มีสาย",
                        "ไฟ RGB":"มีไฟ" , 
                        "ความไวเมาส์":"200 - 8,000 DPI"},
            "promotion":None
        },    
        {
            "product_id": "1532158000001", 
            "object_id": "94220" , 
            "name": "หูฟัง Logitech G333 In-Ear" , 
            "type": "เกมมิ่ง" , 
            "brand":"Logitech" , 
            "price" : 1690  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/03/4-ogitech-G333-In-Ear.jpg?w=256"] , 
            "option":"Black" ,
            "detail": {"ประเภทหูฟัง":"หูฟังอินเอียร์","มีสาย/ไร้สาย":"มีสาย" ,"การเชื่อมต่อหูฟัง (Input)":"AUX (3.5mm), USB-C","ไมโครโฟน":"มีไมค์" , "ไฟ RGB" : "ไม่มีไฟ" ,
                        "แพล็ตฟอร์ม":"Window, Mac,Nintendo Switch, PlayStation 4, XBOX One, iOS, Android, PlayStation 5","อิมพีแดนซ์":"24Ω ±20%","การตอบสนองความถี่":"20 - 20,000 Hz","ความยาวสาย":"1.2 m",
                        "น้ำหนัก":"19.00 g"},
            "promotion":None
        },   
        {
            "product_id": "1516014000001" , 
            "object_id": "39265" , 
            "name": "หูฟัง Razer Hammerhead Pro v.2 In-Ear" , 
            "type": "เกมมิ่ง" , 
            "brand":"Razer" , 
            "price" : 1090  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2018/02/10-Razer-Hammerhead-Pro-v_2-In-Ear.jpg"] , 
            "option":"" ,
            "detail": {"ประเภทหูฟัง":"หูฟังอินเอียร์",
                        "มีสาย/ไร้สาย":"มีสาย",
                        "การเชื่อมต่อหูฟัง (Input)":"AUX (3.5mm)",
                        "ไมโครโฟน":"มีไมค์",
                        "แพล็ตฟอร์ม":"Window, Mac, iOS, Android",
                        "อิมพีแดนซ์":"32",
                        "การตอบสนองความถี่":"20-20000"},
            "promotion":None
        } ,   
        {
            "product_id": "1516124000001" , 
            "object_id": "87686" , 
            "name": "เมาส์ไร้สาย Razer Basilisk X Hyperspeed Wireless Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Razer" , 
            "price" : 1590  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2019/12/razer-basilisk-x-hyperspeed-wireless-gaming-mouse-icon(1).jpg"] , 
            "option":"" ,
            "detail": {"มีสาย/ไร้สาย":"ไร้สาย",
                        "มาโคร":"มี",
                        "ซอฟต์แวร์":"มี",
                        "ไฟ RGB":"ไม่มีไฟ",
                        "Preferred Hand":"Right-Handed",
                        "Sensor":"Optical",
                        "ประเภทสวิตซ์":"Razer",
                        "รูปแบบการจับเมาส์":"Palm Grip, Claw Grip",
                        "การเชื่อมต่อ":"Wireless, Bluetooth",
                        "ความไวเมาส์":"สูงสุด 16,000 DPI",
                        "น้ำหนัก":"83 กรัม (ไม่รวมแบตเตอรี่)"},
            "promotion":None
        }  , 
        {
            "product_id": "1516206000001" , 
            "object_id": "98385" , 
            "name": "หูฟัง Razer Kraken V3 Gaming Headset" , 
            "type": "เกมมิ่ง" , 
            "brand":"Razer" , 
            "price" : 3890  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/11/Product/razer-kraken-v3-hypersense-gaming-headset-01.jpg"] , 
            "option":"" ,
            "detail": {'ประเภทหูฟัง':'หูฟังครอบหู (Over-Ear)',
                        'มีสาย/ไร้สาย':'มีสาย',
                        'ไมโครโฟน':'มีไมค์',
                        'ไฟ RGB':'มีไฟ',
                        'การเชื่อมต่อหูฟัง (Input)':'USB-A',
                        'อิมพีแดนซ์':'32 Ω',
                        'การตอบสนองความถี่':'12 – 28,000Hz',
                        'น้ำหนัก':'285กรัม',
                        'ความยาวสาย':'1.8 m'},
            "promotion":PercentageDiscount("2023-08-30",1000,10,1000,"ส่วนลด 10%","JOJO")
        },
        {
            "product_id": "1965014000001" , 
            "object_id": "105700" , 
            "name": "คีย์บอร์ด Keychron V1 Mechanical Keyboard (EN/TH)" , 
            "type": "เกมมิ่ง" , 
            "brand":"Keychron" , 
            "price" : 3990  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2023/01/Product/keychron-v1-mechanical-keyboard-en-th-icon.jpg"] , 
            "option":"Red Switch" ,
            "detail": {"มีสาย/ไร้สาย":"มีสาย",
                        "ประเภทคีย์บอร์ด":"Mechanical",
                        "ประเภทสวิตซ์":"Linear, Tactile, Clicky",
                        "มาโคร":"มี",
                        "ซอฟต์แวร์":"มี",
                        "ไฟ RGB":"มีไฟ",
                        "สีสวิตซ์":"Blue, Red, Brown",
                        "ขนาดคีย์บอร์ด":"75%",
                        "วัสดุคีย์แคป":"PBT Double Shot",
                        'การเชื่อมต่อ':'Wired',
                        'รองรับ Hot-Swappable':'ได้',
                        'สวิตซ์':'Keychron',
                        'น้ำหนัก':'970.00 g'},
            "promotion":None
        },
        {
            "product_id": "1859015000001" , 
            "object_id": "93174" , 
            "name": "เมาส์ไร้สาย Glorious Model O Wireless Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Glorious" , 
            "price" : 3590  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2020/12/glorious-model-o-wireless-gaming-mouse-black-icon.jpg"] , 
            "option":"Black" ,
            "detail": {"มีสาย/ไร้สาย":"ไร้สาย",
                        "มาโคร":"มี",
                        "ซอฟต์แวร์":"มี",
                        "ไฟ RGB":"มีไฟ",
                        "Preferred Hand":"Right-Handed",
                        "Sensor":"Optical",
                        "ประเภทสวิตซ์":"Omron",
                        "ความไวเมาส์":"สูงสุด 12,000 DPI"},
            "promotion":None
        },
        {
            "product_id": "1532129000001" , 
            "object_id": "89698" , 
            "name": "เมาส์ Logitech G102 LIGHTSYNC Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Logitech" , 
            "price" : 990  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2020/06/logitech-g102-lightsync-gaming-mouse-black-icon.jpg"] , 
            "option":"Black" ,
            "detail": {"มีสาย/ไร้สาย":"ไร้สาย",
                       "ไฟ RGB":"มีไฟ",
                       "ความไวเมาส์":"200 - 8,000 DPI"},
            "promotion":None
        },
        {
            "product_id": "1532181000001" , 
            "object_id": "96797" , 
            "name": "หูฟัง Logitech G435 Lightspeed Gaming Wireless Headphone" , 
            "type": "เกมมิ่ง" , 
            "brand":"Logitech" , 
            "price" : 2590  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/02/Product/2-Logitech-G435-Lightspeed-Gaming-Wireless-Headphone.jpg"] , 
            "option":"Black and Neon Yellow" ,
            "detail": {"ประเภทหูฟัง":"หูฟังครอบหู (Over-Ear)",
                       "มีสาย/ไร้สาย":"ไร้สาย",
                       "การเชื่อมต่อหูฟัง (Input)":"บลูทูธ, 2.4 GHz wireless",
                       "ไมโครโฟน":"มีไมค์" , 
                       "Headphone Back Type":"Closed Back",
                       "ไฟ RGB" : "ไม่มีไฟ" ,
                       "แพล็ตฟอร์ม":"Window, Mac, PlayStation 4, iOS, Android, PlayStation 5",
                       "อิมพีแดนซ์":"45 โอห์ม",
                       "การตอบสนองความถี่":"20 - 20,000 Hz",
                       "ความยาวสาย":"1.2 m",
                       "น้ำหนัก":"165 กรัม"},
            "promotion":PercentageDiscount("2023-08-30",1000,10,1000,"ส่วนลด 10%","JOJO")
        },
        {
            "product_id": "1740025000001" , 
            "object_id": "97305" , 
            "name": "หูฟัง SoundPeats Air3 True Wireless" , 
            "type": "หูฟัง/ลำโพง" , 
            "brand":"SoundPEATS" , 
            "price" : 1659  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/10/soundpeats-air3-true-wireless-black-icon.jpg"] , 
            "option":"Black" ,
            "detail": {'ไมโครโฟน':'มีไมค์',
                        'ระดับการกันน้ำ':'IPX5',
                        'คุณสมบัติพิเศษ':'ระบบสัมผัส, สั่งการด้วยเสียง',
                        'Bluetooth Version':'5.2',
                        'การกันน้ำ':'กันน้ำ',
                        'พอร์ตการชาร์จ':'USB-C',
                        'รูปแบบหูฟัง':'หูฟัง True Wireless',
                        'การตอบสนองความถี่':'20 - 20000Hz',
                        'แบตฯสูงสุด':'5 ชม.',
                        'CODEC ที่รองรับ':'aptX Adaptive'},
            "promotion":None
        },
        {
            "product_id": "1516199000001" , 
            "object_id": "96432" , 
            "name": "หูฟังไร้สาย Razer Hammerhead True Wireless 2nd Gen" , 
            "type": "หูฟัง/ลำโพง" , 
            "brand":"Razer" , 
            "price" : 2290  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/08/hammerhead%20TWS%202%20gen.jpg"] , 
            "option":"" ,
            "detail": {'ประเภทหูฟัง':'หูฟังทรูไวเลส',
                        'มีสาย/ไร้สาย':'ไร้สาย',
                        'การเชื่อมต่อหูฟัง (Input)':'บลูทูธ',
                        'ไมโครโฟน':'มีไมค์',
                        'ระดับการกันน้ำ':'IPX4',
                        'แพล็ตฟอร์ม':'iOS, Android',
                        'Bluetooth Version':'5.2',
                        'อิมพีแดนซ์':'16 Ω',
                        'การตอบสนองความถี่':'20 Hz – 20 kHz',
                        'น้ำหนัก':'53 กรัม'},
            "promotion":None
        },
        {
            "product_id": "1532129000002" , 
            "object_id": "89698" , 
            "name": "เมาส์ Logitech G102 LIGHTSYNC Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Logitech" , 
            "price" : 990  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2020/06/logitech-g102-lightsync-gaming-mouse-white-icon(1).jpg"] , 
            "option": "White" ,
            "detail": {"มีสาย/ไร้สาย":"ไร้สาย",
                       "ไฟ RGB":"มีไฟ",
                       "ความไวเมาส์":"200 - 8,000 DPI"},
            "promotion":None
        },
        {
            "product_id": "1516241000001" , 
            "object_id": "102641" , 
            "name": "เมาส์ Razer Viper V2 Pro Wireless Gaming Mouse" , 
            "type": "เกมมิ่ง" , 
            "brand":"Razer" , 
            "price" : 5490  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/05/razer-viper-v2-pro-wireless-gaming-mouse-white-icon.jpg"] , 
            "option": "White" ,
            "detail": {"มีสาย/ไร้สาย":"มีสาย",
                       "ไฟ RGB":"มีไฟ" , 
                       "ความไวเมาส์":"200 - 8,000 DPI"},
            "promotion":None
        },
        {
            "product_id": "2156095000001" , 
            "object_id": "101117" , 
            "name": "โต๊ะปรับระดับ Ergotrend Sit2stand RGB L-Shape 60x140 Adjustable Desk" , 
            "type": "โต๊ะคอม" , 
            "brand":"Ergotrend" , 
            "price" : 22900  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/03/ergotrend-sit2stand-rgb-l-shape-60-140-adjustable-desk-front-view.jpg"] , 
            "option": "" ,
            "detail": {"โต๊ะมุม":"ใช่",
                       'วัสดุขาโต๊ะ':'เหล็ก',
                        'ฟีเจอร์พิเศษ':'พอร์ต USB, รองรับการเก็บสายไฟ',
                        'ขนาดท็อปโต๊ะ':'60 x 140 cm',
                        'ระดับควางสูงที่ปรับได้':'73 - 123 cm',
                        'ขนาด':'60 x 140 x 73-123 ซม.'},
            "promotion":None
        },
        {
            "product_id": "2242054000001" , 
            "object_id": "104162" , 
            "name": "โต๊ะเกมมิ่ง Furradec CT-2013 Gaming Desk" , 
            "type": "โต๊ะคอม" , 
            "brand":"Furradec" , 
            "price" : 5480  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/07/Product/furradec-ct-2013-gaming-desk-cover-view.jpg"] , 
            "option": "" ,
            "detail": {"ขนาดท็อปโต๊ะ":"60 x 120 cm",
                       "วัสดุขาโต๊ะ":"เหล็ก" ,
                       "รองรับน้ำหนัก (kg)":"40 กก."},
            "promotion":None
        },
        {
            "product_id": "1532158000004" , 
            "object_id": "94220" , 
            "name": "หูฟัง Logitech G333 In-Ear" , 
            "type": "เกมมิ่ง" , 
            "brand":"Logitech" , 
            "price" : 1690  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/07/Product/logitech-g333-in-ear-white-01.jpg"] , 
            "option": "White" ,
            "detail": {"ประเภทหูฟัง":"หูฟังอินเอียร์",
                       "มีสาย/ไร้สาย":"มีสาย",
                       "การเชื่อมต่อหูฟัง (Input)":"AUX (3.5mm), USB-C","ไมโครโฟน":"มีไมค์" , 
                       "ไฟ RGB" : "ไม่มีไฟ" ,
                       "แพล็ตฟอร์ม":"Window, Mac,Nintendo Switch, PlayStation 4, XBOX One, iOS, Android, PlayStation 5",
                       "อิมพีแดนซ์":"24Ω ±20%",
                       "การตอบสนองความถี่":"20 - 20,000 Hz",
                       "ความยาวสาย":"1.2 m",
                       "น้ำหนัก":"19.00 g"},
            "promotion":None
        },
        {
            "product_id": "2354005000001" , 
            "object_id": "105216" , 
            "name": 'จอคอม IPASON E2429G-Z 23.8" IPS FHD Gaming Monitor 144Hz' , 
            "type": "คอมพิวเตอร์" , 
            "brand":"IPASON" , 
            "price" : 4280  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/11/Product/ipason-e2429g-z-23-8-ips-gaming-monitor-144hz-front-view.jpg"] , 
            "option": "" ,
            "detail": {'ประเภทพาเนล':'IPS',
                        'รูปแบบหน้าจอ':'จอแบน',
                        'ความละเอียดสูงสุด':'1920x1080 (Full HD)',
                        'อัตราส่วนจอ':'16:9',
                        'อัตราการตอบสนอง':'5ms',
                        'การเชื่อมต่อภาพ':'HDMI, Display Port',
                        'แขนจับที่รองรับ':'VESA mount',
                        'ขนาดหน้าจอ':'23.8"',
                        'อัตรารีเฟรช':'144Hz',
                        'ฟีเจอร์เสริม':'HDR10',
                        'AMD Free-Sync':'รองรับ',
                        'การเชื่อมต่ออื่นๆ':'USB A'},
            "promotion":None
        },
        {
            "product_id": "2354005000001" , 
            "object_id": "105216" , 
            "name": 'จอคอม IPASON E2429G-Z 23.8" IPS FHD Gaming Monitor 144Hz' , 
            "type": "คอมพิวเตอร์" , 
            "brand":"IPASON" , 
            "price" : 4280  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/11/Product/ipason-e2429g-z-23-8-ips-gaming-monitor-144hz-front-view.jpg"] , 
            "option": "" ,
            "detail": {'ขนาดหน้าจอ':'27"',
                        'ประเภทพาเนล':'IPS',
                        'รูปแบบหน้าจอ':'จอแบน',
                        'ความละเอียดสูงสุด':'2560 x 1440 (2K QHD)',
                        'อัตราส่วนจอ':'16:9',
                        'อัตราการตอบสนอง':'1ms',
                        'การเชื่อมต่อภาพ':'HDMI, Display Port',
                        'แขนจับที่รองรับ':'VESA mount',
                        'ขนาดหน้าจอ':'27"',
                        'อัตรารีเฟรช':'165Hz',
                        'ฟีเจอร์เสริม':'HDR',
                        'Adaptive Sync':'AMD FreeSync',
                        'การเชื่อมต่ออื่นๆ':'USB A'},
            "promotion":None
        },
          {
            "product_id": "1575040000001" , 
            "object_id": "93686" , 
            "name": 'จอคอม Zowie XL2411K 24" TN FHD Gaming Monitor 144Hz' , 
            "type": "คอมพิวเตอร์" , 
            "brand":"Zowie" , 
            "price" : 8990  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2021/02/zowie-xl2411k-24-gaming-monitor-144hz-icon.jpg"] , 
            "option": "" ,
            "detail": {'ขนาดหน้าจอ':'24"',
                       'พาเนลหน้าจอ':'TN',
                        'ความละเอียดหน้าจอสูงสุด':'1920 x 1080 (Full HD)',
                        'อัตราส่วนหน้าจอ':'16:9',
                        'รูปแบบหน้าจอ':'จอแบน',
                        'จอพกพา':'ไม่ใช่',
                        'อัตราความหน่วงภาพ':'1ms',
                        'ฟีเจอร์เสริม':'Low / Less Blue Light, Flicker free',
                        'การเชื่อมต่อภาพ':'HDMI, DisplayPort',
                        'การเชื่อมต่ออื่นๆ':'AUX 3.5mm',
                        'ช่องยึด VESA':'100 x 100 มม.',
                        'อัตรารีเฟรชหน้าจอ':'144Hz',
                        'ขนาด(กว้าง x ยาว x สูง cm)':'57.1 x 20 x 52.5',
                        'น้ำหนัก':'5.9 kg'},
            "promotion":None
        },
        {
            "product_id": "1740017000001" , 
            "object_id": "94352" , 
            "name": "หูฟังไร้สาย SoundPeats MAC True Wireless" , 
            "type": "หูฟัง" , 
            "brand":"SoundPEATS" , 
            "price" : 699  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/02/Product/7--%2B%2B-ºS%2BT----SoundPeats-MAC-True-Wireless.jpg"] , 
            "option":"" ,
            "detail": {'Bluetooth Version':'5.0',
                        'ไมโครโฟน':'มีไมค์',
                        'ระดับการกันน้ำ':'IPX7',
                        'คุณสมบัติพิเศษ':'ระบบสัมผัส',
                        'Game Mode':'ไม่มี',
                        'ANC':'ไม่มี',
                        'การกันน้ำ':'กันน้ำ',
                        'พอร์ตการชาร์จ':'USB-C',
                        'รูปแบบหูฟัง':'หูฟัง True Wireless',
                        'เหมาะสำหรับ':'ออกกำลังกาย',
                        'แบตฯสูงสุด':'9 ชม.',
                        'CODEC ที่รองรับ':'AAC, SBC'},
            "promotion":None
        },
        {
            "product_id": "1740035000001" , 
            "object_id": "105271" , 
            "name": "หูฟัง SoundPeats Air 3 Deluxe HS True Wireless" , 
            "type": "หูฟัง" , 
            "brand":"SoundPEATS" , 
            "price" : 1990  , 
            "quantity" : 20 , 
            "image" : ["https://mercular.s3.ap-southeast-1.amazonaws.com/images/products/2022/11/Product/soundpeats-air-3-deluxe-hs-true-wireless-back-view.jpg"] , 
            "option":"Black" ,
            "detail": {'ประเภทหูฟัง':'หูฟังทรูไวเลส',
                        'มีสาย/ไร้สาย':'ไร้สาย',
                        'การเชื่อมต่อหูฟัง (Output)':'บลูทูธ',
                        'ไมโครโฟน':'มีไมค์',
                        'ระดับการกันน้ำ':'IPX4',
                        'คุณสมบัติพิเศษ':'LDAC, AAC, การตรวจจับการสวมใส่, SBC, Game Mode',
                        'Bluetooth Version':'5.2',
                        'Game Mode':'มี',
                        'การกันน้ำ':'กันน้ำ',
                        'พอร์ตการชาร์จ':'USB-C', 
                        'การตอบสนองความถี่':'20 - 40,000 Hz'},
            "promotion":None
        }
    ]
}
