import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# SMART ALUMINIUM HPDC MACHINE & CASTING ADVISOR
# Ready-to-run Tkinter Application
# ============================================================


# ============================================================
# PROFESSIONAL COLORS
# ============================================================

BG = "#F4F7FA"
NAVY = "#12355B"
BLUE = "#1F6AA5"
DARK_BLUE = "#0B2942"
LIGHT_BLUE = "#E8F2F9"
WHITE = "#FFFFFF"
TEXT = "#17202A"
GRAY = "#667788"
GREEN = "#198754"
LIGHT_GREEN = "#EAF7EF"
ORANGE = "#E67E22"
LIGHT_ORANGE = "#FFF2E5"
RED = "#C0392B"
LIGHT_RED = "#FCEAEA"
BORDER = "#D5DEE8"


# ============================================================
# MACHINE DATABASE
# ============================================================

MACHINES = [
    (100, "Small HPDC Machine"),
    (160, "Small HPDC Machine"),
    (250, "Small / Medium HPDC Machine"),
    (400, "Medium HPDC Machine"),
    (500, "Medium HPDC Machine"),
    (630, "Medium / Large HPDC Machine"),
    (800, "Large HPDC Machine"),
    (1000, "Large HPDC Machine"),
    (1250, "Large HPDC Machine"),
    (1600, "Very Large HPDC Machine"),
    (2000, "Very Large HPDC Machine"),
    (2500, "Large Structural HPDC"),
    (3200, "Structural HPDC"),
    (4000, "Mega Structural HPDC")
]


# ============================================================
# CASTING PART DATABASE
# ============================================================

PARTS = {

    "Honda CD-70 / 70cc": [
        "Honda CD-70 - Left Crankcase Cover",
        "Honda CD-70 - Right Crankcase / Clutch Cover",
        "Honda CD-70 - Crankcase",
        "Honda CD-70 - Front Wheel Hub",
        "Honda CD-70 - Rear Wheel Hub",
        "Honda CD-70 - Sprocket Hub",
        "Honda CD-70 - Drive Plate",
        "Honda CD-70 - Magneto Coil Plate",
        "Honda CD-70 - Engine Cover",
        "Honda CD-70 - Cylinder Head Cover",
        "Honda CD-70 - Clutch Cover",
        "Honda CD-70 - Handle Holder",
        "Honda CD-70 - Brake Panel",
        "Honda CD-70 - Bridge Plate"
    ],

    "Motorcycles": [
        "Motorcycle - Crankcase",
        "Motorcycle - Crankcase Cover",
        "Motorcycle - Clutch Cover",
        "Motorcycle - Gearbox Housing",
        "Motorcycle - Engine Cover",
        "Motorcycle - Generator Cover",
        "Motorcycle - Magneto Cover",
        "Motorcycle - Cylinder Head Cover",
        "Motorcycle - Oil Pump Housing",
        "Motorcycle - Water Pump Housing",
        "Motorcycle - Intake Manifold",
        "Motorcycle - Brake Caliper Body",
        "Motorcycle - Brake Caliper Bracket",
        "Motorcycle - Master Cylinder Body",
        "Motorcycle - Front Wheel Hub",
        "Motorcycle - Rear Wheel Hub",
        "Motorcycle - Sprocket Hub",
        "Motorcycle - Steering / Fork Bracket",
        "Motorcycle - Footrest Bracket",
        "Motorcycle - Engine Mount Bracket",
        "Motorcycle - Swingarm Bracket",
        "Motorcycle - Electrical Housing",
        "Motorcycle - Regulator Housing",
        "Motorcycle - Headlight Housing"
    ],

    "Tractors": [
        "Tractor - Engine Cover",
        "Tractor - Transmission Housing",
        "Tractor - Gearbox Housing",
        "Tractor - Clutch Housing",
        "Tractor - Hydraulic Valve Body",
        "Tractor - Hydraulic Valve Housing",
        "Tractor - Hydraulic Pump Housing",
        "Tractor - Water Pump Housing",
        "Tractor - Oil Pump Housing",
        "Tractor - Fuel System Housing",
        "Tractor - Filter Housing",
        "Tractor - Thermostat Housing",
        "Tractor - Alternator Housing",
        "Tractor - Starter Motor Housing",
        "Tractor - Fan Housing",
        "Tractor - Fan Cover",
        "Tractor - Tractor Cover",
        "Tractor - Access Cover",
        "Tractor - Bearing Housing",
        "Tractor - Mounting Bracket"
    ],

    "Automobiles": [
        "Car - Engine Cover",
        "Car - Cylinder Head Cover",
        "Car - Gearbox Housing",
        "Car - Transmission Housing",
        "Car - Clutch Housing",
        "Car - Oil Sump",
        "Car - Oil Sump Cover",
        "Car - Water Pump Housing",
        "Car - Oil Pump Housing",
        "Car - Thermostat Housing",
        "Car - Valve Housing",
        "Car - Filter Housing",
        "Car - Alternator Housing",
        "Car - Starter Motor Housing",
        "Car - Motor Housing",
        "Car - Compressor Housing",
        "Car - Pump Housing",
        "Car - Front Wheel Hub",
        "Car - Bracket",
        "Car - Mounting Bracket",
        "Car - Sensor Housing",
        "Car - Electronic Housing"
    ],

    "Rickshaw / Three-Wheeler": [
        "Rickshaw - Crankcase",
        "Rickshaw - Crankcase Cover",
        "Rickshaw - Clutch Cover",
        "Rickshaw - Gearbox Housing",
        "Rickshaw - Wheel Hub",
        "Rickshaw - Sprocket Hub",
        "Rickshaw - Handle Holder",
        "Rickshaw - Engine Cover",
        "Rickshaw - Pump Housing",
        "Rickshaw - Fan Housing"
    ],

    "Electrical / Electronics": [
        "ECU Housing",
        "Electronic Housing",
        "Motor Housing",
        "LED Housing",
        "LED Heat Sink",
        "Battery Housing",
        "Battery Cover",
        "Battery Tray",
        "Electrical Junction Box",
        "Sensor Housing",
        "Regulator Housing",
        "Controller Housing",
        "Inverter Housing"
    ],

    "Industrial / General": [
        "Valve Body",
        "Valve Housing",
        "Pump Housing",
        "Water Pump Housing",
        "Hydraulic Pump Housing",
        "Hydraulic Valve Body",
        "Hydraulic Pump Housing",
        "Compressor Housing",
        "Gearbox Housing",
        "Transmission Case",
        "Motor End Cover",
        "Motor Housing",
        "Fan Housing",
        "Heat Sink",
        "Filter Housing",
        "Bearing Housing",
        "Mounting Bracket",
        "Structural Bracket",
        "Machine Cover",
        "Equipment Housing",
        "Industrial Enclosure",
        "Pipe / Fitting Housing"
    ]
}


# ============================================================
# ALUMINIUM ALLOYS
# ============================================================

ALLOYS = {
    "ADC12": {
        "description": "Common aluminium die-casting alloy with good fluidity and castability.",
        "applications": "Automotive housings, engine components, covers and general HPDC components."
    },

    "A380": {
        "description": "Widely used aluminium die-casting alloy with good strength and castability.",
        "applications": "Automotive and industrial die-cast components."
    },

    "Al-Si Alloy": {
        "description": "Aluminium-silicon alloys provide good fluidity and useful casting properties.",
        "applications": "Various aluminium casting applications."
    },

    "Custom Alloy": {
        "description": "Custom alloy option for a manufacturer-specified aluminium composition.",
        "applications": "Application depends on required mechanical and casting properties."
    }
}


# ============================================================
# DEFECT DATABASE
# ============================================================

DEFECTS = {

    "Porosity": {
        "causes": [
            "Entrapped gas",
            "Poor venting",
            "Excessive turbulence",
            "Moisture",
            "Improper injection conditions"
        ],
        "solutions": [
            "Improve die venting",
            "Optimize injection speed",
            "Control die temperature",
            "Check melt cleanliness",
            "Reduce unnecessary turbulence"
        ]
    },

    "Misrun": {
        "causes": [
            "Low metal temperature",
            "Low die temperature",
            "Insufficient filling speed",
            "Poor filling pattern"
        ],
        "solutions": [
            "Optimize metal temperature",
            "Check die temperature",
            "Optimize filling speed",
            "Review gate and runner design"
        ]
    },

    "Cold Shut": {
        "causes": [
            "Two metal fronts meet at low temperature",
            "Poor filling pattern",
            "Low melt temperature"
        ],
        "solutions": [
            "Improve melt temperature",
            "Optimize die temperature",
            "Review gate and runner design",
            "Improve filling conditions"
        ]
    },

    "Flash": {
        "causes": [
            "Excessive cavity pressure",
            "Insufficient clamping force",
            "Die parting-line problem",
            "Die wear"
        ],
        "solutions": [
            "Check machine clamping force",
            "Inspect die parting line",
            "Optimize injection pressure",
            "Inspect die condition"
        ]
    },

    "Shrinkage": {
        "causes": [
            "Improper solidification",
            "Poor feeding",
            "Incorrect cooling",
            "Local thick sections"
        ],
        "solutions": [
            "Optimize cooling",
            "Review wall thickness",
            "Optimize process parameters",
            "Improve die thermal balance"
        ]
    },

    "Die Soldering": {
        "causes": [
            "Excessive die temperature",
            "Poor lubrication",
            "Aluminium sticking to die surface",
            "Improper cooling"
        ],
        "solutions": [
            "Improve die cooling",
            "Optimize die lubricant",
            "Check die surface condition",
            "Control die temperature"
        ]
    },

    "Cracks": {
        "causes": [
            "Thermal stress",
            "Residual stress",
            "Improper ejection",
            "Rapid or uneven cooling"
        ],
        "solutions": [
            "Optimize cooling",
            "Check ejection system",
            "Review die temperature",
            "Check component design"
        ]
    }
}


# ============================================================
# PROCESS PARAMETERS
# ============================================================

PROCESS_PARAMETERS = {
    "Cold Chamber HPDC": [
        ("Typical application", "Automotive and larger aluminium components"),
        ("Common alloy type", "Aluminium alloys"),
        ("Injection system", "Metal is transferred into shot sleeve"),
        ("Main advantage", "Suitable for aluminium and relatively large castings"),
        ("Important controls", "Metal temperature, die temperature, injection speed, pressure")
    ],

    "Hot Chamber HPDC": [
        ("Typical application", "Lower melting point alloys and suitable small/medium components"),
        ("Common alloy type", "Zinc and selected low-melting alloys"),
        ("Injection system", "Injection system is integrated with molten metal bath"),
        ("Main advantage", "Fast cycle time for suitable alloys"),
        ("Important controls", "Metal temperature, die temperature, injection speed, pressure")
    ]
}


# ============================================================
# MAIN APPLICATION CLASS
# ============================================================

class HPDCApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Smart Aluminium HPDC Machine & Casting Advisor"
        )

        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)
        self.root.configure(bg=BG)

        self.setup_styles()
        self.create_interface()
        self.show_dashboard()


    # ========================================================
    # STYLES
    # ========================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "TCombobox",
            padding=7,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 9)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )


    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def create_interface(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=NAVY,
            width=245
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)


        # Logo
        tk.Label(
            self.sidebar,
            text="SMART HPDC",
            bg=NAVY,
            fg=WHITE,
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(28, 2)
        )

        tk.Label(
            self.sidebar,
            text="Aluminium Die Casting Advisor",
            bg=NAVY,
            fg="#C8DDED",
            font=("Segoe UI", 9)
        ).pack(
            pady=(0, 25)
        )


        # Navigation buttons
        self.add_nav_button(
            "Dashboard",
            self.show_dashboard
        )

        self.add_nav_button(
            "Machine Selector",
            self.show_machine_selector
        )

        self.add_nav_button(
            "Casting Parts",
            self.show_parts
        )

        self.add_nav_button(
            "Tonnage Calculator",
            self.show_calculator
        )

        self.add_nav_button(
            "Defect Diagnosis",
            self.show_defects
        )

        self.add_nav_button(
            "Aluminium Alloys",
            self.show_alloys
        )

        self.add_nav_button(
            "Process Parameters",
            self.show_parameters
        )

        self.add_nav_button(
            "Machine Database",
            self.show_machine_database
        )


        tk.Label(
            self.sidebar,
            text="HPDC ENGINEERING TOOL",
            bg=NAVY,
            fg="#8FB3D1",
            font=("Segoe UI", 8)
        ).pack(
            side="bottom",
            pady=20
        )


        # Main content area
        self.main = tk.Frame(
            self.root,
            bg=BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )


    # ========================================================
    # NAVIGATION BUTTON
    # ========================================================

    def add_nav_button(self, text, command):

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            bg=NAVY,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            relief="flat",
            anchor="w",
            font=("Segoe UI", 10, "bold"),
            padx=22,
            pady=11,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=10,
            pady=2
        )


    # ========================================================
    # CLEAR MAIN SCREEN
    # ========================================================

    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()


    # ========================================================
    # PAGE HEADER
    # ========================================================

    def page_header(self, title, description):

        self.clear_main()

        header = tk.Frame(
            self.main,
            bg=WHITE,
            height=90
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text=title,
            bg=WHITE,
            fg=NAVY,
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(17, 0)
        )

        tk.Label(
            header,
            text=description,
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=32
        )


    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.page_header(
            "Dashboard",
            "Smart engineering support for aluminium high pressure die casting"
        )


        container = tk.Frame(
            self.main,
            bg=BG
        )

        container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        # Welcome panel
        welcome = tk.Frame(
            container,
            bg=NAVY,
            height=145
        )

        welcome.pack(
            fill="x",
            pady=(0, 20)
        )

        welcome.pack_propagate(False)


        tk.Label(
            welcome,
            text="Smart Aluminium HPDC Machine & Casting Advisor",
            bg=NAVY,
            fg=WHITE,
            font=("Segoe UI", 20, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 5)
        )


        tk.Label(
            welcome,
            text="Machine selection • Casting parts • Tonnage • Defects • Alloys • Process parameters",
            bg=NAVY,
            fg="#D7E6F2",
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=27
        )


        # Cards
        cards = tk.Frame(
            container,
            bg=BG
        )

        cards.pack(
            fill="x"
        )


        self.create_card(
            cards,
            "MACHINES",
            str(len(MACHINES)),
            "Machine capacities",
            BLUE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )


        total_parts = sum(
            len(parts)
            for parts in PARTS.values()
        )


        self.create_card(
            cards,
            "CASTING PARTS",
            str(total_parts),
            "HPDC part examples",
            GREEN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )


        self.create_card(
            cards,
            "DEFECTS",
            str(len(DEFECTS)),
            "Common defects",
            ORANGE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )


        self.create_card(
            cards,
            "ALLOYS",
            str(len(ALLOYS)),
            "Alloy information",
            RED
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )


        # Information box
        info = tk.LabelFrame(
            container,
            text="Application Modules",
            bg=WHITE,
            fg=NAVY,
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=15
        )

        info.pack(
            fill="both",
            expand=True,
            pady=25
        )


        modules = [
            (
                "Machine Selector",
                "Select a casting part and estimate required machine capacity."
            ),
            (
                "Casting Parts",
                "Browse motorcycle, tractor, automobile and industrial parts."
            ),
            (
                "Tonnage Calculator",
                "Calculate preliminary required clamping force."
            ),
            (
                "Defect Diagnosis",
                "View possible causes and corrective actions."
            ),
            (
                "Aluminium Alloys",
                "Review common aluminium die-casting alloys."
            ),
            (
                "Process Parameters",
                "Review important HPDC process parameters."
            )
        ]


        for name, description in modules:

            row = tk.Frame(
                info,
                bg=WHITE
            )

            row.pack(
                fill="x",
                pady=4
            )


            tk.Label(
                row,
                text="●",
                bg=WHITE,
                fg=BLUE,
                font=("Arial", 9)
            ).pack(
                side="left"
            )


            tk.Label(
                row,
                text=name + ": ",
                bg=WHITE,
                fg=TEXT,
                font=("Segoe UI", 9, "bold")
            ).pack(
                side="left"
            )


            tk.Label(
                row,
                text=description,
                bg=WHITE,
                fg=GRAY,
                font=("Segoe UI", 9)
            ).pack(
                side="left"
            )


    # ========================================================
    # DASHBOARD CARD
    # ========================================================

    def create_card(
        self,
        parent,
        title,
        number,
        description,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            height=120,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack_propagate(False)


        tk.Label(
            card,
            text=title,
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 8, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(14, 0)
        )


        tk.Label(
            card,
            text=number,
            bg=WHITE,
            fg=accent,
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=15
        )


        tk.Label(
            card,
            text=description,
            bg=WHITE,
            fg=GRAY,
            font=("Segoe UI", 8)
        ).pack(
            anchor="w",
            padx=15
        )


        return card


    # ========================================================
    # MACHINE SELECTOR
    # ========================================================

    def show_machine_selector(self):

        self.page_header(
            "Machine Selector",
            "Estimate preliminary HPDC machine capacity from projected area"
        )


        frame = tk.Frame(
            self.main,
            bg=WHITE,
            padx=30,
            pady=25
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=25
        )


        # Part
        tk.Label(
            frame,
            text="Casting Part",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=10
        )


        self.machine_part = tk.StringVar()


        all_parts = []


        for category, parts in PARTS.items():

            for part in parts:

                all_parts.append(
                    f"{category} | {part}"
                )


        self.machine_part.set(
            all_parts[0]
        )


        ttk.Combobox(
            frame,
            textvariable=self.machine_part,
            values=all_parts,
            width=70,
            state="readonly"
        ).grid(
            row=0,
            column=1,
            padx=20
        )


        # Area
        tk.Label(
            frame,
            text="Projected Area (cm²)",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )


        self.machine_area = tk.Entry(
            frame,
            width=73
        )

        self.machine_area.grid(
            row=1,
            column=1,
            padx=20
        )


        # Chamber
        tk.Label(
            frame,
            text="Casting Process",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=10
        )


        self.machine_chamber = tk.StringVar(
            value="Cold Chamber HPDC"
        )


        ttk.Combobox(
            frame,
            textvariable=self.machine_chamber,
            values=[
                "Cold Chamber HPDC",
                "Hot Chamber HPDC"
            ],
            state="readonly",
            width=70
        ).grid(
            row=2,
            column=1,
            padx=20
        )


        tk.Button(
            frame,
            text="ANALYZE MACHINE",
            command=self.analyze_machine,
            bg=BLUE,
            fg=WHITE,
            activebackground=DARK_BLUE,
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=25,
            pady=11,
            cursor="hand2"
        ).grid(
            row=3,
            column=1,
            sticky="w",
            padx=20,
            pady=20
        )


        self.machine_result = tk.Label(
            self.main,
            text="Enter projected area and click ANALYZE MACHINE.",
            bg=LIGHT_BLUE,
            fg=NAVY,
            font=("Segoe UI", 10, "bold"),
            justify="left",
            anchor="w",
            padx=25,
            pady=20
        )

        self.machine_result.pack(
            fill="x",
            padx=30
        )


    def analyze_machine(self):

        try:

            area = float(
                self.machine_area.get()
            )


            if area <= 0:
                raise ValueError


            pressure = 14
            safety = 1.20


            tonnage = (
                area *
                pressure *
                safety
            ) / 981


            recommended = None


            for capacity, category in MACHINES:

                if capacity >= tonnage:

                    recommended = (
                        capacity,
                        category
                    )

                    break


            if recommended:

                result = (
                    "MACHINE ANALYSIS\n\n"
                    f"Casting part:\n{self.machine_part.get()}\n\n"
                    f"Process:\n{self.machine_chamber.get()}\n\n"
                    f"Projected area: {area:.2f} cm²\n"
                    f"Estimated clamping force: {tonnage:.2f} tons\n\n"
                    f"Recommended machine: {recommended[0]} tons\n"
                    f"Machine category: {recommended[1]}\n\n"
                    "Engineering note:\n"
                    "This is a preliminary estimate. Actual machine selection "
                    "also requires die projected area including runner/overflow, "
                    "shot weight, die dimensions, tie-bar spacing and injection capacity."
                )

            else:

                result = (
                    f"Estimated requirement: {tonnage:.2f} tons\n\n"
                    "The required capacity is above the current machine database."
                )


            self.machine_result.config(
                text=result
            )


        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid positive projected area."
            )


    # ========================================================
    # CASTING PARTS
    # ========================================================

    def show_parts(self):

        self.page_header(
            "Casting Parts Database",
            "HPDC part examples for automotive, motorcycle, tractor and industrial applications"
        )


        outer = tk.Frame(
            self.main,
            bg=WHITE
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        top = tk.Frame(
            outer,
            bg=WHITE
        )

        top.pack(
            fill="x",
            padx=15,
            pady=15
        )


        tk.Label(
            top,
            text="Category:",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(
            side="left"
        )


        category_var = tk.StringVar(
            value=list(PARTS.keys())[0]
        )


        category_menu = ttk.Combobox(
            top,
            textvariable=category_var,
            values=list(PARTS.keys()),
            state="readonly",
            width=30
        )

        category_menu.pack(
            side="left",
            padx=15
        )


        tree_frame = tk.Frame(
            outer,
            bg=WHITE
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=15
        )


        scrollbar = ttk.Scrollbar(
            tree_frame
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


        tree = ttk.Treeview(
            tree_frame,
            columns=("No", "Part"),
            show="headings",
            yscrollcommand=scrollbar.set
        )


        tree.heading(
            "No",
            text="#"
        )

        tree.heading(
            "Part",
            text="Casting Part"
        )


        tree.column(
            "No",
            width=60
        )

        tree.column(
            "Part",
            width=700
        )


        tree.pack(
            fill="both",
            expand=True
        )


        scrollbar.config(
            command=tree.yview
        )


        def update_parts(event=None):

            tree.delete(
                *tree.get_children()
            )


            selected = category_var.get()


            for i, part in enumerate(
                PARTS[selected],
                start=1
            ):

                tree.insert(
                    "",
                    "end",
                    values=(i, part)
                )


        category_menu.bind(
            "<<ComboboxSelected>>",
            update_parts
        )


        update_parts()


    # ========================================================
    # TONNAGE CALCULATOR
    # ========================================================

    def show_calculator(self):

        self.page_header(
            "Clamping Force Calculator",
            "Preliminary calculation of required HPDC machine clamping force"
        )


        frame = tk.Frame(
            self.main,
            bg=WHITE,
            padx=35,
            pady=25
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=25
        )


        fields = [
            "Projected Area (cm²)",
            "Effective Pressure (MPa)",
            "Safety Factor"
        ]


        for i, label in enumerate(fields):

            tk.Label(
                frame,
                text=label,
                bg=WHITE,
                fg=TEXT,
                font=("Segoe UI", 10, "bold")
            ).grid(
                row=i,
                column=0,
                sticky="w",
                pady=10
            )


        self.area_entry = tk.Entry(
            frame,
            width=35
        )

        self.pressure_entry = tk.Entry(
            frame,
            width=35
        )

        self.safety_entry = tk.Entry(
            frame,
            width=35
        )


        self.area_entry.grid(
            row=0,
            column=1,
            padx=30
        )

        self.pressure_entry.grid(
            row=1,
            column=1,
            padx=30
        )

        self.safety_entry.grid(
            row=2,
            column=1,
            padx=30
        )


        self.pressure_entry.insert(
            0,
            "60"
        )

        self.safety_entry.insert(
            0,
            "1.2"
        )


        tk.Button(
            frame,
            text="CALCULATE TONNAGE",
            command=self.calculate_tonnage,
            bg=GREEN,
            fg=WHITE,
            activebackground="#146C43",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=25,
            pady=10,
            cursor="hand2"
        ).grid(
            row=3,
            column=1,
            sticky="w",
            padx=30,
            pady=20
        )


        self.calculator_result = tk.Label(
            self.main,
            text="Enter values above to calculate.",
            bg=LIGHT_GREEN,
            fg=NAVY,
            font=("Segoe UI", 10, "bold"),
            justify="left",
            anchor="w",
            padx=25,
            pady=25
        )

        self.calculator_result.pack(
            fill="x",
            padx=30
        )


    def calculate_tonnage(self):

        try:

            area = float(
                self.area_entry.get()
            )

            pressure = float(
                self.pressure_entry.get()
            )

            safety = float(
                self.safety_entry.get()
            )


            if (
                area <= 0
                or pressure <= 0
                or safety <= 0
            ):

                raise ValueError


            tonnage = (
                area *
                pressure *
                safety
            ) / 981


            machine = None


            for capacity, category in MACHINES:

                if capacity >= tonnage:

                    machine = (
                        capacity,
                        category
                    )

                    break


            if machine:

                result = (
                    "CALCULATION RESULT\n\n"
                    f"Projected area: {area:.2f} cm²\n"
                    f"Effective pressure: {pressure:.2f} MPa\n"
                    f"Safety factor: {safety:.2f}\n\n"
                    f"Estimated clamping force:\n"
                    f"{tonnage:.2f} tons\n\n"
                    f"Recommended machine:\n"
                    f"{machine[0]} tons\n"
                    f"{machine[1]}\n\n"
                    "Formula:\n"
                    "Tonnage = Area × Pressure × Safety Factor / 981"
                )

            else:

                result = (
                    f"Estimated clamping force:\n"
                    f"{tonnage:.2f} tons\n\n"
                    "No suitable machine was found in the current database."
                )


            self.calculator_result.config(
                text=result
            )


        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid positive numbers."
            )


    # ========================================================
    # DEFECT DIAGNOSIS
    # ========================================================

    def show_defects(self):

        self.page_header(
            "Defect Diagnosis",
            "Possible causes and corrective actions for common HPDC defects"
        )


        frame = tk.Frame(
            self.main,
            bg=WHITE,
            padx=30,
            pady=25
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=25
        )


        tk.Label(
            frame,
            text="Select Defect:",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w"
        )


        self.defect_var = tk.StringVar(
            value=list(DEFECTS.keys())[0]
        )


        ttk.Combobox(
            frame,
            textvariable=self.defect_var,
            values=list(DEFECTS.keys()),
            state="readonly",
            width=40
        ).pack(
            anchor="w",
            pady=10
        )


        tk.Button(
            frame,
            text="DIAGNOSE DEFECT",
            command=self.diagnose_defect,
            bg=ORANGE,
            fg=WHITE,
            activebackground="#BA6418",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(
            anchor="w",
            pady=10
        )


        self.defect_result = tk.Text(
            self.main,
            height=18,
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1,
            padx=20,
            pady=20
        )

        self.defect_result.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )


    def diagnose_defect(self):

        defect = self.defect_var.get()

        data = DEFECTS[defect]


        self.defect_result.delete(
            "1.0",
            tk.END
        )


        self.defect_result.insert(
            tk.END,
            defect.upper() + "\n\n"
        )


        self.defect_result.insert(
            tk.END,
            "POSSIBLE CAUSES\n\n"
        )


        for cause in data["causes"]:

            self.defect_result.insert(
                tk.END,
                "• " + cause + "\n"
            )


        self.defect_result.insert(
            tk.END,
            "\n\nRECOMMENDED ACTIONS\n\n"
        )


        for solution in data["solutions"]:

            self.defect_result.insert(
                tk.END,
                "• " + solution + "\n"
            )


    # ========================================================
    # ALLOYS
    # ========================================================

    def show_alloys(self):

        self.page_header(
            "Aluminium Alloys",
            "Basic information about commonly used aluminium die-casting alloys"
        )


        outer = tk.Frame(
            self.main,
            bg=BG
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        for alloy, data in ALLOYS.items():

            card = tk.Frame(
                outer,
                bg=WHITE,
                highlightbackground=BORDER,
                highlightthickness=1,
                padx=20,
                pady=15
            )

            card.pack(
                fill="x",
                pady=6
            )


            tk.Label(
                card,
                text=alloy,
                bg=WHITE,
                fg=NAVY,
                font=("Segoe UI", 13, "bold")
            ).pack(
                anchor="w"
            )


            tk.Label(
                card,
                text="Description: " + data["description"],
                bg=WHITE,
                fg=TEXT,
                font=("Segoe UI", 9),
                wraplength=850,
                justify="left"
            ).pack(
                anchor="w",
                pady=(6, 2)
            )


            tk.Label(
                card,
                text="Applications: " + data["applications"],
                bg=WHITE,
                fg=GRAY,
                font=("Segoe UI", 9),
                wraplength=850,
                justify="left"
            ).pack(
                anchor="w"
            )


    # ========================================================
    # PROCESS PARAMETERS
    # ========================================================

    def show_parameters(self):

        self.page_header(
            "HPDC Process Parameters",
            "Basic process information for hot chamber and cold chamber die casting"
        )


        outer = tk.Frame(
            self.main,
            bg=BG
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        for process, parameters in PROCESS_PARAMETERS.items():

            box = tk.LabelFrame(
                outer,
                text=process,
                bg=WHITE,
                fg=NAVY,
                font=("Segoe UI", 12, "bold"),
                padx=20,
                pady=15
            )

            box.pack(
                fill="x",
                pady=8
            )


            for name, value in parameters:

                row = tk.Frame(
                    box,
                    bg=WHITE
                )

                row.pack(
                    fill="x",
                    pady=4
                )


                tk.Label(
                    row,
                    text=name + ":",
                    bg=WHITE,
                    fg=TEXT,
                    width=22,
                    anchor="w",
                    font=("Segoe UI", 9, "bold")
                ).pack(
                    side="left"
                )


                tk.Label(
                    row,
                    text=value,
                    bg=WHITE,
                    fg=GRAY,
                    anchor="w",
                    font=("Segoe UI", 9)
                ).pack(
                    side="left"
                )


        note = tk.Label(
            outer,
            text=(
                "Engineering note: Actual process parameters depend on alloy, "
                "machine, die design, casting geometry and production requirements."
            ),
            bg=LIGHT_BLUE,
            fg=NAVY,
            font=("Segoe UI", 9, "bold"),
            padx=15,
            pady=15,
            wraplength=850,
            justify="left"
        )

        note.pack(
            fill="x",
            pady=15
        )


    # ========================================================
    # MACHINE DATABASE
    # ========================================================

    def show_machine_database(self):

        self.page_header(
            "Machine Database",
            "Reference machine capacity range used by the application"
        )


        frame = tk.Frame(
            self.main,
            bg=WHITE
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        tree = ttk.Treeview(
            frame,
            columns=("Capacity", "Category"),
            show="headings"
        )


        tree.heading(
            "Capacity",
            text="Machine Capacity (tons)"
        )


        tree.heading(
            "Category",
            text="Machine Category"
        )


        tree.column(
            "Capacity",
            width=250
        )


        tree.column(
            "Category",
            width=600
        )


        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        for capacity, category in MACHINES:

            tree.insert(
                "",
                "end",
                values=(
                    capacity,
                    category
                )
            )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = HPDCApp(root)

    root.mainloop()
