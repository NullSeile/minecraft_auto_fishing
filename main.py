from pynput.mouse import Button, Controller
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = "D:/Tools/Tesseract-OCR/tesseract.exe"

mouse = Controller()

timer = time.time()

count = 0

while True:

	screen = pyautogui.screenshot()
	
	screen = screen.crop((1500, 600, 1920, 1000))
	
	
	if "Fishing Gobber" in pytesseract.image_to_string(screen) or time.time() - timer > 30:
		
		count += 1
		
		print(f"FISH {count}!!!")
		
		timer = time.time()
		
		mouse.click(Button.right, 1)
		
		time.sleep(1)
		
		mouse.click(Button.right, 1)
		
		time.sleep(3)
		
		