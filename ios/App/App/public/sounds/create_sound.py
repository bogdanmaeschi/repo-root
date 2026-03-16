import struct
import math
import wave

def create_notification_sound():
    # Parameters
    sample_rate = 44100
    duration = 0.3  # 300ms
    frequency = 800  # Hz - notification-like frequency
    
    # Generate samples
    num_samples = int(sample_rate * duration)
    samples = []
    
    for i in range(num_samples):
        # Create envelope (fade in/out)
        envelope = 1.0
        if i < num_samples * 0.1:
            envelope = i / (num_samples * 0.1)
        elif i > num_samples * 0.8:
            envelope = (num_samples - i) / (num_samples * 0.2)
        
        # Generate sine wave with envelope
        value = envelope * math.sin(2 * math.pi * frequency * i / sample_rate)
        
        # Convert to 16-bit integer
        samples.append(int(value * 32767))
    
    # Write WAV file
    with wave.open('/app/frontend/public/sounds/notification.wav', 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Pack samples
        for sample in samples:
            wav_file.writeframes(struct.pack('h', sample))

if __name__ == '__main__':
    create_notification_sound()
    print("Notification sound created successfully!")

