
import matplotlib.pyplot as plt

# Create a list of ten artificial particle-energy values explicitly labelled in GeV

energies = [5.3, 12.5, 8.4, 22.2, 15.6, 17.2, 25.5, 28.6, 10.2, 30.3]
print("Particle energies (GeV):", energies)
print()

# Print the number of values, the minimum and the maximum


number_of_values = len(energies)
minimum_energy = min(energies)
maximum_energy = max(energies)

print("Number of values:", number_of_values)
print("Minimum energy:", minimum_energy, "GeV")
print("Maximum energy:", maximum_energy, "GeV")
print()

# Use a loop and an if statement to select values above a threshold

threshold = 15

selected_energies = []

for energy in energies:
    if energy > threshold:
        selected_energies.append(energy)

print("Threshold:", threshold, "GeV")
print("Values above threshold:", selected_energies)
print()

# Put the selection into a function
def select_above_threshold(values, threshold):
    selected = []

    for value in values:
        if value > threshold:
            selected.append(value)

    return selected

selected_energies = select_above_threshold(energies, threshold)

print("Values selected using the function:", selected_energies)
print()

# Plot the original values as a histogram using Matplotlib with labelled axes

plt.hist(energies, bins=5, edgecolor="black")

plt.xlabel("Particle Energy (GeV)")
plt.ylabel("Number of Particles")
plt.title("Distribution of Particle Energies")
plt.show()

# New threshold
new_threshold = 20

# Select values above the new threshold
new_selected_energies = select_above_threshold(energies, new_threshold)

print("New threshold:", new_threshold, "GeV")
print("Values above new threshold:", new_selected_energies)

# New histogram with different binning
plt.hist(energies, bins=10, edgecolor="black")
plt.xlabel("Particle Energy (GeV)")
plt.ylabel("Number of Particles")
plt.title("Particle Energy Distribution - 10 Bins")

plt.show()
#Explanation
print("Explanation:")
print("1. Increasing the threshold from 15 GeV to 20 GeV selects fewer particle-energy values.")
print("2. Only values greater than 20 GeV are included in the selection.")
print("3. Increasing the number of bins from 5 to 10 provides a more detailed view of the energy distribution.")
print("4. More bins divide the same energy range into smaller intervals.")
print("5. Changing the threshold or binning does not change the original particle-energy values.")