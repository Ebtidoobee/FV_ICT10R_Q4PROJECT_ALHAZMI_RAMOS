from pyscript import display, document

# List of students in 10-Ruby
# You can update these names to your actual classmates' names
students = [
    "Al Hazmi, Ebtisam", "Abad, Juan", "Bautista, Maria", "Cruz, Antonio",
    "Del Rosario, Elena", "Estacio, Ricardo", "Fernando, Sofia", "Garcia, Gabriel",
    "Hernandez, Lucia", "Ibarra, Mateo", "Javier, Clara", "Lozano, Diego",
    "Mendoza, Bianca", "Navarro, Paolo", "Ocampo, Regina", "Pascual, Luis",
    "Quinto, Angela", "Reyes, Miguel", "Santos, Isabel", "Tolentino, Rafael",
    "Urbano, Jasmine", "Valdez, Carlos", "Villanueva, Nicole", "Yambao, Kevin",
    "Zabala, Patricia", "Aquino, Lorenzo", "Dela Cruz, Rosa", "Lim, Samuel"
]

def render_students():
    """Generates the HTML cards for each student and displays them in the grid."""
    class_list_div = document.querySelector("#class-list")
    class_list_div.innerHTML = ""  # Clear existing content
    
    for name in sorted(students):
        # Create a new div element for the student card
        card = document.createElement("div")
        card.className = "student-card"
        card.innerText = name
        
        # Add the card to the container
        class_list_div.appendChild(card)

def show_classmates(event=None):
    """Shows the classmates view and hides the welcome view."""
    document.querySelector("#welcome-view").classList.add("hidden")
    document.querySelector("#classmates-view").classList.remove("hidden")
    render_students()

def show_home(event=None):
    """Shows the welcome view and hides the classmates view."""
    document.querySelector("#classmates-view").classList.add("hidden")
    document.querySelector("#welcome-view").classList.remove("hidden")

# Initialize the page
if __name__ == "__main__":
    pass
