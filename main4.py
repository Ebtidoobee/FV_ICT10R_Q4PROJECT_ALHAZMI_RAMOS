from pyscript import document

# List of all 28 students with their exact provided image paths
gallery_data = [
    {"name": "Al Hazmi, Ebtisam A.", "activity": "Class Activity", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\image0.jpg"},
    {"name": "Entendez, Drake Arkin", "activity": "Marching Band", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 2.20.26 PM.png"},
    {"name": "Alvarez, Yaniszsol Aeiou", "activity": "Music Performance", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 105223.png"},
    {"name": "Belsa, Ethan Drei S.", "activity": "Volleyball Match", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\58c53dad-4472-4f60-96ef-5c733701d6c9.jpg"},
    {"name": "Bernas, Giana Zoe", "activity": "Science Lab", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Image_20260213_202745_473.jpeg"},
    {"name": "Calaycay, Julianna", "activity": "Chemistry Group", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Image_20260213_202745_319.jpeg"},
    {"name": "Castelo, Jamie Alyanna", "activity": "Public Speaking", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\JCO.webp"},
    {"name": "Cruz, Francesca Meyer", "activity": "Class Photo", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\10 Ruby (With Lights 2).JPG"},
    {"name": "Defensor, Ely", "activity": "Photography", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 10.53.04 AM.png"},
    {"name": "Dimasuhid, Dannielle Luna", "activity": "Halloween Event", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Photo on 2-19-26 at 7.07 AM #2.jpg"},
    {"name": "Francisco, Althea Mauri", "activity": "Group Discussion", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\10 Ruby (With Lights 2).JPG"},
    {"name": "Hsu, Cristina Wen", "activity": "ICT Project", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 10.53.04 AM.png"},
    {"name": "Juatchon, Denise", "activity": "Band Practice", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\WIN_20260105_12_07_25_Pro.jpg"},
    {"name": "Judge, Judah", "activity": "School Assembly", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 10.53.04 AM.png"},
    {"name": "Lilagan, Francis", "activity": "Physics Lab", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\IMG_0024.jpeg"},
    {"name": "Luna, Sam", "activity": "Poetry Festival", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\ictp1.jpg"},
    {"name": "Macaranas, Enzo Josh", "activity": "Halloween Presentation", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Image_20251025_141445_408.jpeg"},
    {"name": "Mateo, Pain Adler", "activity": "Marching Trio", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\image.jpeg"},
    {"name": "Mondragon, Ashley", "activity": "Art Design", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\690171475_1247671300690031_8233115486725913254_n.jpg"},
    {"name": "Naldoza, Lance", "activity": "Lab Experiment", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Image_20260417_202208_841.jpeg"},
    {"name": "Natividad, Gabriel Emilio", "activity": "Robotics Prep", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 110446.png"},
    {"name": "Ng, Sofia", "activity": "Environment Project", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\WIN_20260120_14_40_06_Pro.jpg"},
    {"name": "Ong, Hendrich Mathis", "activity": "Chemistry Lab", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 10.53.04 AM.png"},
    {"name": "Paz, Trisha", "activity": "Public Speaking", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\WIN_20260105_12_07_25_Pro.jpg"},
    {"name": "Ramos, Miguel", "activity": "Volleyball Action", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\Screenshot 2026-05-06 at 2.20.26 PM.png"},
    {"name": "Queeny Haraj Ramos", "activity": "Leadership Camp", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\9A7D9AEF-9596-4BA1-8DDB-A300602D84A3.jpg"},
    {"name": "Ramos, Samantha", "activity": "Painting Project", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\IMG_7761.PNG"},
    {"name": "Repolona, Vaughn", "activity": "Tech Media", "img": "C:\Users\admin\OneDrive\Desktop\ICT 25-26\4th Quarter\PROJECT\8CB7427E-0497-4498-9D5A-922E64D659F9.jpeg"}
]

def load_gallery():
    container = document.querySelector("#gallery-container")
    if container:
        container.innerHTML = ""
        
        for student in gallery_data:
            # Create Card
            card = document.createElement("div")
            card.className = "photo-card"
            
            # Create Image Element
            img_element = document.createElement("img")
            # Using get() to ensure it finds the 'img' key
            img_element.src = student.get("img", "https://via.placeholder.com/400x300?text=Ruby+Gem")
            img_element.className = "w-full h-[160px] object-cover"
            img_element.alt = f"Photo of {student['name']}"
            
            # Create Info Area
            info = document.createElement("div")
            info.className = "card-info"
            
            name_div = document.createElement("div")
            name_div.className = "student-name"
            name_div.innerText = student["name"]
            
            activity_div = document.createElement("div")
            activity_div.className = "activity-tag"
            activity_div.innerText = student["activity"]
            
            # Assemble
            info.appendChild(name_div)
            info.appendChild(activity_div)
            card.appendChild(img_element)
            card.appendChild(info)
            container.appendChild(card)

# Execute the function
load_gallery()