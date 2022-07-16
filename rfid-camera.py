from time import sleep
from lcd import lcd

try:
    lcd.text('silahkan tap kartu', 1)

    import read
    nama = "id: " + "{}".format(read.id)
    lcd.text(nama, 1)
    lcd.text(read.text, 2)
    sleep(5)
    lcd.clear()
    lcd.text('silahkan pose', 1)
    sleep(5)
    lcd.clear()
    import camera

    lcd.text('selesai', 1)

finally:
    lcd.clear()
