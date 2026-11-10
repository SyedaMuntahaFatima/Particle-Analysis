import matplotlib.pyplot as plt

#Create particle-energy values in GeV

energies = [5.3, 12.5, 8.4, 22.2, 15.6,
            17.2, 25.5, 28.6, 10.2, 30.3]

print("Particle energies (GeV):", energies)
print()
# Print number, minimum and maximum

number_of_values = len(energies)
minimum_energy = min(energies)
maximum_energy = max(energies)

print("Number of values:", number_of_values)
print("Minimum energy:", minimum_energy, "GeV")
print("Maximum energy:", maximum_energy, "GeV")
print()
# Select values above a threshold using loop and if

threshold = 15

selected_energies = []

for energy in energies:
    if energy > threshold:
        selected_energies.append(energy)

print("Threshold:", threshold, "GeV")
print("Values above threshold:", selected_energies)
print()
#Put selection into a function

def select_above_threshold(values, threshold):
    selected = []

    for value in values:
        if value > threshold:
            selected.append(value)

    return selected


selected_energies = select_above_threshold(energies, threshold)

print("Values selected using function:", selected_energies)
print()

# Change threshold and binning

new_threshold = 20

new_selected_energies = select_above_threshold(energies, new_threshold)

print("New threshold:", new_threshold, "GeV")
print("Values above new threshold:", new_selected_energies)

# Create both histograms

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# First histogram: 5 bins and threshold 15 GeV

axes[0].hist(energies, bins=5, range=(0, 50),edgecolor="black", color="skyblue")

axes[0].axvline(threshold, color="red",linestyle="--", linewidth=2,label="Threshold = 15 GeV")
axes[0].set_xlabel("Particle Energy (GeV)")
axes[0].set_ylabel("Number of Particles")
axes[0].set_title("5 Bins | Threshold = 15 GeV")
axes[0].legend()
axes[0].grid(alpha=0.3)


# Second histogram: 10 bins and threshold 20 GeV

axes[1].hist(energies, bins=10, range=(0, 50),
             edgecolor="black", color="lightgreen")
axes[1].axvline(new_threshold, color="red",linestyle="--", linewidth=2,label="Threshold = 20 GeV")

axes[1].set_xlabel("Particle Energy (GeV)")
axes[1].set_ylabel("Number of Particles")
axes[1].set_title("10 Bins | Threshold = 20 GeV")
axes[1].legend()
axes[1].grid(alpha=0.3)


fig.suptitle("Comparison of Particle Energy Distributions",
             fontsize=14)

plt.tight_layout()

# Save and display both graphs

plt.savefig("particle_energy_comparison.png", dpi=300)

plt.show()