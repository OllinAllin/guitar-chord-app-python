##################################### main.py #####################################

import customtkinter as ctk
import os
from PIL import Image
from music_logic import get_scale, MAJOR_DEGREES, MAJOR_QUALITIES, MINOR_DEGREES, MINOR_QUALITIES


class GuitarChordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assets_path = os.path.join(base_dir, "assets", "chords")
        fallback_path = os.path.join(self.assets_path, "image_coming_soon.png")
        fallback_data = Image.open(fallback_path)
        self.fallback_image = ctk.CTkImage(light_image=fallback_data, dark_image=fallback_data, size=(160, 200))

        self.title("Chords in Any Key")
        self.geometry("1500x500")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.sidebar.grid_columnconfigure(0, weight=1)

        self.sidebar.grid_rowconfigure(5, weight=1)
        
        self.title_label = ctk.CTkLabel(self.sidebar, text="Choose a Scale", font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.major_btn = ctk.CTkButton(self.sidebar, text="Major Scale", command=lambda:self.run_logic("major"))
        self.major_btn.grid(row=1, column=0, padx=20, pady=20)

        self.minor_btn = ctk.CTkButton(self.sidebar, text="Minor Scale", command=lambda:self.run_logic("minor"))
        self.minor_btn.grid(row=2, column=0, padx=20, pady=20)

        self.clear_btn = ctk.CTkButton(self.sidebar, text="Clear", command=self.clear_all, fg_color="#CC3333", hover_color="#990000")
        self.clear_btn.grid(row=5, column=0, padx=20, pady=20, sticky="s")

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Key (e.g. C#)", placeholder_text_color="gray", width=200)
        self.entry.pack(pady=10)

        self.title_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.title_container.pack(pady=10)

        self.note_label = ctk.CTkLabel(self.title_container, text="--", font=("Archivo Black", 50, "bold", "italic"), text_color="#FFCC00")
        self.note_label.grid(row=0, column=0, padx=5)

        self.type_label = ctk.CTkLabel(self.title_container, text="", font=("Archivo Black", 35, "italic"), text_color="gray")
        self.type_label.grid(row=0, column=1, padx=5, sticky="s")

        self.scale_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.scale_container.pack(pady=20, fill="x")

        self.degree_labels = [] 
        self.note_labels = []

        self.after(100, lambda: self.focus_set()) 

    def run_logic(self, mode):
        user_input = self.entry.get().strip()
       
        if user_input:
            scale_list = get_scale(user_input, mode)
            if scale_list:
                self.display_scale(scale_list, mode)
                self.note_label.configure(text=user_input.title())
                self.type_label.configure(text=f"{mode.title()} scale")

    def display_scale(self, scale_notes, mode):
        for widget in self.scale_container.winfo_children():
            widget.destroy()

        qualities = MAJOR_QUALITIES if mode == "major" else MINOR_QUALITIES
        degrees = MAJOR_DEGREES if mode == "major" else MINOR_DEGREES

        for i, note in enumerate(scale_notes):
            cell = ctk.CTkFrame(self.scale_container, fg_color="transparent")
            cell.grid(row=0, column=i, padx=10)
            ctk.CTkLabel(cell, text=degrees[i], font=("Helvetica", 40), text_color="gray").pack()
            ctk.CTkLabel(cell, text=note, font=("Helvetica", 36, "bold"), text_color="#FFCC00").pack()
            chord_img = self.get_chord_image(note, qualities[i])
            img_label = ctk.CTkLabel(cell, text="", image=chord_img)
            img_label.image = chord_img 
            img_label.pack(pady=5)

    def get_chord_image(self, note_name, quality):
        clean_note = note_name.replace("#", "_sharp").replace("b", "_flat")
        filename = f"{clean_note}_{quality}.png"
        image_path = os.path.join(self.assets_path, filename)
        if os.path.exists(image_path):
            img_data = Image.open(image_path)
            return ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(160, 200))
        else:
            return self.fallback_image
            
    def clear_all(self):
        self.entry.delete(0, "end")
        current_placeholder = self.entry.cget("placeholder_text")
        self.entry.configure(placeholder_text=current_placeholder)
        self.focus()
        self.note_label.configure(text="--")
        self.type_label.configure(text="")

    def clear_scale_display(self):
        for widget in self.scale_container.winfo_children():
            widget.destroy()     

if __name__ == "__main__":
    app = GuitarChordApp()
    app.mainloop()
