import os
import subprocess

# Map waar de .htm bestanden zich bevinden
directory = r"O:\WND\conferentieverslagen\00\08\files"  # Gebruik een raw string (r"")

# Controleer of de directory bestaat
if not os.path.isdir(directory):
    print(f"Fout: De opgegeven directory bestaat niet: {directory}")
    exit(1)

# Zoek alle .htm bestanden in de directory
html_files = [f for f in os.listdir(directory) if f.endswith(".htm")]

# Controleer of er .htm bestanden zijn gevonden
if not html_files:
    print("Geen .htm bestanden gevonden in de opgegeven directory.")
    exit(0)

# Converteer elk .htm bestand naar .md met Pandoc
for html_file in html_files:
    html_path = os.path.join(directory, html_file)  # Volledig pad naar HTML bestand
    md_file = os.path.splitext(html_file)[0] + ".md"  # Wijzig extensie naar .md
    md_path = os.path.join(directory, md_file)  # Uitvoerbestand in dezelfde map

    # Run Pandoc met absolute paden
    try:
        subprocess.run(["pandoc", html_path, "-o", md_path, "--from", "html"], check=True)
        print(f"✅ Succes: {html_file} -> {md_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Fout bij conversie van {html_file}: {e}")

print("🚀 Conversie voltooid!")
