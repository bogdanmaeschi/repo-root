import struct
import math
import wave

def create_sound(filename, frequency, duration, wave_type='sine'):
    """
    Create a notification sound with customizable parameters
    
    Args:
        filename: Output WAV filename
        frequency: Frequency in Hz (higher = higher pitch)
        duration: Duration in seconds
        wave_type: 'sine', 'double', or 'triple' (for multiple tones)
    """
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    samples = []
    
    for i in range(num_samples):
        # Create envelope (fade in/out)
        envelope = 1.0
        fade_in = num_samples * 0.1
        fade_out_start = num_samples * 0.7
        
        if i < fade_in:
            envelope = i / fade_in
        elif i > fade_out_start:
            envelope = (num_samples - i) / (num_samples - fade_out_start)
        
        # Generate waveform
        t = i / sample_rate
        if wave_type == 'sine':
            value = envelope * math.sin(2 * math.pi * frequency * t)
        elif wave_type == 'double':
            # Two tone beep (pleasant)
            value = envelope * (
                0.6 * math.sin(2 * math.pi * frequency * t) +
                0.4 * math.sin(2 * math.pi * frequency * 1.5 * t)
            )
        elif wave_type == 'triple':
            # Three tone chord (rich sound)
            value = envelope * (
                0.5 * math.sin(2 * math.pi * frequency * t) +
                0.3 * math.sin(2 * math.pi * frequency * 1.25 * t) +
                0.2 * math.sin(2 * math.pi * frequency * 1.5 * t)
            )
        
        samples.append(int(value * 32767))
    
    # Write WAV file
    with wave.open(f'/app/frontend/public/sounds/{filename}', 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))

# Generate different sound options
print("Generating notification sounds...")

# Option 1: Current (Pleasant beep)
create_sound('notification.wav', 800, 0.3, 'sine')
print("✅ notification.wav - Current sound (Pleasant beep, 800Hz)")

# Option 2: Higher pitch (More attention-grabbing)
create_sound('notification-high.wav', 1000, 0.25, 'sine')
print("✅ notification-high.wav - Higher pitch (1000Hz)")

# Option 3: Lower pitch (Softer, subtle)
create_sound('notification-low.wav', 600, 0.35, 'sine')
print("✅ notification-low.wav - Lower pitch (600Hz)")

# Option 4: Double tone (Pleasant chord)
create_sound('notification-chord.wav', 800, 0.4, 'double')
print("✅ notification-chord.wav - Double tone chord")

# Option 5: Triple tone (Rich, musical)
create_sound('notification-rich.wav', 700, 0.5, 'triple')
print("✅ notification-rich.wav - Triple tone (Rich sound)")

# Option 6: Quick beep (Fast, discrete)
create_sound('notification-quick.wav', 900, 0.15, 'sine')
print("✅ notification-quick.wav - Quick beep (0.15s)")

print("\nAll sounds generated! Choose your favorite:")
print("1. notification.wav (current) - Pleasant beep")
print("2. notification-high.wav - Higher pitch")
print("3. notification-low.wav - Lower/softer")
print("4. notification-chord.wav - Double tone")
print("5. notification-rich.wav - Rich/musical")
print("6. notification-quick.wav - Quick/discrete")
