import numpy as np, sounddevice as sd, threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

class AudioFix:
    def __init__(self):
        self.is_running = False
        self.stop_event = threading.Event()
        
        # Configure Volume and Frequency Here!!!
        self.sample_rate = 44100
        self.frequency = 20
        self.volume = 0.1
        self.duration = 1.0
        
    def audio_loop(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
        wave = (np.sin(2 * np.pi * self.frequency * t) * self.volume).astype(np.float32)
        
        try:
            with sd.OutputStream(samplerate=self.sample_rate, channels=1) as stream:
                while not self.stop_event.is_set():
                    stream.write(wave)
        except Exception as e:
            print(f"Audio error: {e}")
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.stop_event.clear()
            threading.Thread(target=self.audio_loop, daemon=True).start()
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.stop_event.set()

class TrayApp:
    def __init__(self):
        self.audio = AudioFix()
        
    def create_icon_image(self, is_running):
        img = Image.new('RGB', (64, 64), 'black')
        draw = ImageDraw.Draw(img)
        draw.ellipse([16, 16, 48, 48], fill='green' if is_running else 'red')
        return img
    
    def toggle_audio(self, icon, item):
        if self.audio.is_running:
            self.audio.stop()
        else:
            self.audio.start()
        icon.icon = self.create_icon_image(self.audio.is_running)
        icon.update_menu()
    
    def quit_app(self, icon, item):
        self.audio.stop()
        icon.stop()
    
    def run(self):
        menu = Menu(
            MenuItem(lambda _: "Stop" if self.audio.is_running else "Start", self.toggle_audio),
            MenuItem("Close", self.quit_app)
        )
        
        Icon("AudioFix", self.create_icon_image(False), "Audio Sleep Prevention", menu).run()

if __name__ == "__main__":
    TrayApp().run()