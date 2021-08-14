import soundcard as sc

mics = "\n".join(f"- {i.name}" for i in sc.all_microphones())

print("**THE MICROPHONES AVAILABLE ON THIS DEVICE ARE**")
print(mics)