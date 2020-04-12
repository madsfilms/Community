import tkinter as tk
from random import randint


epi_list = ["S01E01: Pilot",
            "S01E02: Spanish 101",
            "S01E03: Introduction to Film",
            "S01E04: Social Pschology",
            "S01E05: Advanced Criminal Law",
            "S01E06: Football, Feminism and You",
            "S01E07: Introduction to Statistics",
            "S01E08: Home Economics",
            "S01E09: Debate 109",
            "S01E10: Environmental Science",
            "S01E11: The Politics of Human Sexuality",
            "S01E12: Comparative Religion",
            "S01E13: Investigative Journalism",
            "S01E14: Interpretive Dance",
            "S01E15: Romantic Expressionism",
            "S01E16: Communication Studies",
            "S01E17: Physical Education",
            "S01E18: Basic Geneology",
            "S01E19: Beginner Pottery",
            "S01E20: The Science of Illusion",
            "S01E21: Contemporary American Poultry",
            "S01E22: The Art of Discourse",
            "S01E23: Modern Warfare",
            "S01E24: English as a Second Language",
            "S01E25: Pascal's Triangle Revisited",
            "S02E01: Anthropology 101",
            "S02E02: Accounting for Lawyers",
            "S02E03: The Psychology of Letting Go",
            "S02E04: Basic Rocket Science",
            "S02E05: Messianic Myths and Ancient Peoples",
            "S02E06: Epidemiology",
            "S02E07: Aerodynamics of Gender",
            "S02E08: Cooperative Calligraphy",
            "S02E09: Conspiracy Theories and Interior Design",
            "S02E10: Mixology Certification",
            "S02E11: Abed's Uncontrollable Christmas",
            "S02E12: Asian Population Studies",
            "S02E13: Celebrity Pharmacology 212",
            "S02E14: Advanced Dungeons & Dragons",
            "S02E15: Early 21st Century Romanticism",
            "S02E16: Intermediate Documentary Filmmaking",
            "S02E17: Intro to Political Science",
            "S02E18: Custody Law and Eastern European Diplomacy",
            "S02E19: Critical Film Studies",
            "S02E20: Competitive Wine Tasting",
            "S02E21: Paradigms of Human Memory",
            "S02E22: Applied Anthropology and Culinary Arts",
            "S02E23: A Fistful of Paintballs",
            "S02E24: For a Few Paintballs More",
            "S03E01: Biology 101",
            "S03E02: Geography of Global Conflict",
            "S03E03: Competitive Ecology",
            "S03E04: Remedial Chaos Theory",
            "S03E05: Horror Fiction in Seven Spooky Steps",
            "S03E06: Advanced Gay",
            "S03E07: Studies in Modern Movement",
            "S03E08: Documentary Filmmaking: Redux",
            "S03E09: Foosball and Nocturnal Vigilantism",
            "S03E10: Regional Holiday Music",
            "S03E11: Urban Matrimony and the Sandwich Arts",
            "S03E12: Contemporary Impressionists",
            "S03E13: Digital Exploration of Interior Design",
            "S03E14: Pillows and Blankets",
            "S03E15: Origins of Vampire Mythology",
            "S03E16: Virtual Systems Analysis",
            "S03E17: Basic Lupine Urology",
            "S03E18: Course Listing Unavailable",
            "S03E19: Curriculum Unavailable",
            "S03E20: Digital Estate Planning",
            "S03E21: The First Change Dynasty",
            "S03E22: Introduction to Finality",
            "S04E01: History 101",
            "S04E02: Paranormal Parentage",
            "S04E03: Conventions of Space and Time",
            "S04E04: Alternative History of the German Invasion",
            "S04E05: Cooperative Escapism in Familial Relations",
            "S04E06: Advanced Documentary Filmmaking",
            "S04E07: Economics of Marine Biology",
            "S04E08: Herstory of Dance"
            "S04E09: Intro to Felt Surrogacy",
            "S04E10: Intro to Knots",
            "S04E11: Basic Human Anatomy",
            "S04E12: Heroic Origins",
            "S04E13: Advanced Introduction to Finality",
            "S05E01: Repilot",
            "S05E02: Introduction to Teaching",
            "S05E03: Basic Intergluteal Numismatics",
            "S05E04: Cooperative Polygraphy",
            "S05E05: Geothermal Escapism",
            "S05E06: Analysis of Cork Board Networking",
            "S05E07: Bondage and Beta Male Sexuality",
            "S05E08: App Development and Condiments",
            "S05E09: VCR Maintenance and Educational Publishing",
            "S05E10: Advanced Advanced Dungeons & Dragons",
            "S05E11: G.I. Jeff",
            "S05E12: Basic Story",
            "S05E13: Basic Sandwich",
            "S06E01: Ladders",
            "S06E02: Lawnmower Maintenance and Postnatal Care",
            "S06E03: Basic Crisis Room Decorum",
            "S06E04: Queer Studies and Advanced Waxing",
            "S06E05: Laws of Robotics and Party Rights",
            "S06E06: Basic Email Security",
            "S06E07: Advanced Safety Features",
            "S06E08: Intro to Recycled Cinema",
            "S06E09: Grifting 101",
            "S06E10: Basic RV Repair and Palmistry",
            "S06E11: Modern Espionage",
            "S06E12: Wedding Videography",
            "S06E13: Emotional Consequences of Broadcast Television"]

def epi_number():
    for _ in range(1):
        value = randint(0, 108)
        print(epi_list[value])

def new_number():
    for _ in range(1):
        value = randint(0, 108)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   height=4,
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   height=4,
                   text="Generate Random Episode",
                   command=epi_number) 
slogan.pack(side=tk.LEFT)

root.mainloop()
    
            
            
