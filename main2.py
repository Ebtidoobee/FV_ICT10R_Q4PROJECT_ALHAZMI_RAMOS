from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

# classmate class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."


classmates_list = [
    Classmate("Al Hazmi, Ebtisam A.", "10-Ruby", "ICT"),
    Classmate("Alvarez, Yaniszsol Aeiou", "10-Ruby", "Music"),
    Classmate("Belsa, Ethan Drei S.", "10-Ruby", "Mathematics"),
    Classmate("Bernas, Giana Zoe", "10-Ruby", "Science"),
    Classmate("Calaycay, Julianna", "10-Ruby", "Research"),
    Classmate("Castelo, Jamie Alyanna", "10-Ruby", "English"),
    Classmate("Cruz, Francesca Meyer", "10-Ruby", "Arts"),
    Classmate("Defensor, Ely", "10-Ruby", "History"),
    Classmate("Dimasuhid, Dannielle Luna", "10-Ruby", "Filipino"),
    Classmate("Entendez, Drake Arkin", "10-Ruby", "Math"),
    Classmate("Francisco, Althea Mauri", "10-Ruby", "Science"),
    Classmate("Hsu, Cristina Wen", "10-Ruby", "ICT"),
    Classmate("Juatchon, Denise", "10-Ruby", "Biology"),
    Classmate("Judge, Judah", "10-Ruby", "Philosophy"),
    Classmate("Lilagan, Francis", "10-Ruby", "Physics"),
    Classmate("Luna, Sam", "10-Ruby", "History"),
    Classmate("Macaranas, Enzo Josh", "10-Ruby", "PE"),
    Classmate("Mateo, Pain Adler", "10-Ruby", "Mathematics"),
    Classmate("Mondragon, Ashley", "10-Ruby", "Social Studies"),
    Classmate("Naldoza, Lance", "10-Ruby", "English"),
    Classmate("Natividad, Gabriel Emilio", "10-Ruby", "Math"),
    Classmate("Ng, Sofia", "10-Ruby", "Biology"),
    Classmate("Ong, Hendrich Mathis", "10-Ruby", "Chemistry"),
    Classmate("Paz, Trisha", "10-Ruby", "English"),
    Classmate("Ramos, Miguel", "10-Ruby", "Science"),
    Classmate("Ramos, Queeny Haraj", "10-Ruby", "Filipino"),
    Classmate("Ramos, Samantha", "10-Ruby", "Arts"),
    Classmate("Repolona, Vaughn", "10-Ruby", "Computer Science")
]

def display_list(event):
    output_div = document.querySelector("#output")
    output_div.innerHTML = "" 
    
    for person in classmates_list:
        new_p = document.createElement("p")

        new_p.className = "border-b border-[#FFCDD2] pb-1 mb-1 text-[#880E4F]"
        new_p.innerText = "💎 " + person.introduce()
        output_div.appendChild(new_p)

def add_classmate_event(event):
    name_el = document.querySelector("#name")
    sec_el = document.querySelector("#section")
    sub_el = document.querySelector("#subject")
    output_div = document.querySelector("#output")

    if name_el.value.strip() and sec_el.value.strip() and sub_el.value.strip():
        new_person = Classmate(name_el.value, sec_el.value, sub_el.value)
        classmates_list.append(new_person)
        
        output_div.innerHTML = f'<p class="text-[#D32F2F] font-bold">Added: {new_person.name} successfully! 💎</p>'
        
        name_el.value = ""
        sec_el.value = ""
        sub_el.value = ""
    else:
        output_div.innerHTML = '<p class="text-red-500 font-bold">Error, please fill in the required boxes</p>'

# Initialize system message
document.querySelector("#output").innerHTML = "Ready! Ruby System loaded. 💎"
