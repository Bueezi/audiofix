# AudioFix - 1MORE SonoFlow Pro HQ51 Audio Delay Fix

A lightweight Windows system tray application that fixes the ~1 second audio delay issue on 1MORE SonoFlow Pro HQ51 headphones when used in wired mode (3.5mm jack).

## The Problem

When using the 1MORE SonoFlow Pro HQ51 headphones in wired mode, there's an annoying ~1 second delay before audio resumes after any period of silence. This makes gaming, watching videos, or listening to music with quiet sections frustrating, as the headphones constantly "wake up" with a delay.

## The Solution

AudioFix continuously plays an inaudible 20Hz tone at 10% volume in the background. This keeps the audio connection alive and prevents the headphones from entering sleep mode, eliminating the delay entirely.

## Installation

### Option 1: Download Pre-built EXE (No requirements!)
1. Download `AudioFix.exe` from the [Releases](../../releases) page
2. Run the executable
3. (Optional) Press `Win+R`, type `shell:startup`, and copy the exe there to run automatically on boot

### Option 2: Build from Source (Python required)
```bash
# Clone the repository
git clone https://github.com/bueezi/audiofix.git
cd audiofix

# Run the build script
build.cmd
```

## Usage

1. Run `AudioFix.exe`
2. Look for the red circle icon in your system tray
3. Right-click the icon and select "Start"
4. The icon will turn green - the fix is now active
5. To stop, right-click and select "Stop"
6. To exit completely, select "Close"

## Configuration

You can adjust the frequency and volume by editing `audiofix.py`:

```python
self.frequency = 20      # Frequency in Hz (20Hz is inaudible)
self.volume = 0.1        # Volume level (0.0 to 1.0)
```