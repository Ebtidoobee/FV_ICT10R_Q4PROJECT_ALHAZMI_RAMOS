from pyscript import document, display, window
import numpy as np
import matplotlib.pyplot as plt
import logging

# Data setup
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
absence_counts = np.zeros(5)

def generate_graph():
    plt.style.use('fast')
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=100)
    
    ax.plot(days, absence_counts, color='#8BC34A', marker='o', 
            linewidth=4, markersize=10, markerfacecolor='#FFEB3B', 
            markeredgecolor='#33691E', markeredgewidth=2)
    
    ax.fill_between(days, absence_counts, color='#DCEDC8', alpha=0.5)
    
    # Keeping the emoji - the 'warnings' filter above will hide the red error box
    ax.set_title("Ruby Weekly Absence Overview", fontsize=14, pad=20, color='#33691E', fontweight='bold')
    ax.set_ylabel("Number of Absences", fontsize=10, color='#33691E', fontweight='bold')
    
    ax.set_ylim(0, max(np.max(absence_counts) + 2, 5))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#8BC34A')
    ax.spines['bottom'].set_color('#8BC34A')
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='#8BC34A')
    
    display(fig, target="graph-area", append=False)
    plt.close(fig)

def update_data(event):
    day_idx_str = document.getElementById("day-select").value
    abs_val_str = document.getElementById("absences-input").value
    
    if abs_val_str:
        try:
            day_idx = int(day_idx_str)
            absence_counts[day_idx] = int(abs_val_str)
            generate_graph()
            document.getElementById("absences-input").value = ""
        except ValueError:
            pass

window.update_data = update_data
generate_graph()