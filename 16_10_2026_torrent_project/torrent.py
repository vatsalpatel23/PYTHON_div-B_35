# ==============================================================================
# Project: Torrent Power Electricity Billing System
# Concept: Class, Constructor (__init__) and Inheritance (super())
# Level  : Simple, Small & Student-Friendly (MSc.IT Sem 3)
# Note   : Zero f-strings used (Pure basic Python print & string concatenation)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Base Class: TorrentBill (Parent Class)
# Sabhi connections ke common variables aur methods yahan define hain.
# ------------------------------------------------------------------------------
class TorrentBill:
    # Constructor: Object banate waqt automatic call hota hai
    def __init__(self, cno, name, prev, curr):
        # Chote aur simple variables ka use
        self.cno = cno          # Consumer Number (e.g. 101)
        self.name = name        # Customer ka Naam
        self.prev = float(prev) # Previous Meter Reading
        self.curr = float(curr) # Current Meter Reading
        
        # Units Consumed = Current - Previous
        self.units = self.curr - self.prev
        
        # Torrent Power ka fix fuel charge per unit (FPPPA rate)
        self.fpppa_rate = 2.85
        
        # Initial bill values (Child classes inko calculate karengi)
        self.energy = 0.0   # Bijli ka charge (Units ke hisab se)
        self.fixed = 0.0    # Meter aur connection ka fixed charge
        self.fpppa = 0.0    # Fuel surcharge
        self.duty = 0.0     # Government tax (Electricity Duty)
        self.total = 0.0    # Final Payable Amount
        self.btype = "Base" # Bill ka type (Residential/Commercial/Industrial)

    # Method: FPPPA (Fuel Charge) calculate karna
    def calc_fpppa(self):
        # Formula: Units * Rs. 2.85
        self.fpppa = round(self.units * self.fpppa_rate, 2)
        return self.fpppa

    # Method: Bill ko screen par print karna (Without f-string)
    def show_bill(self):
        print("\n" + "=" * 42)
        print("         TORRENT POWER LIMITED")
        print("        ELECTRICITY BILL INVOICE")
        print("=" * 42)
        print("Consumer No   :", self.cno)
        print("Consumer Name :", self.name)
        print("Bill Type     :", self.btype)
        print("-" * 42)
        print("Reading (Prev):", self.prev, "kWh")
        print("Reading (Curr):", self.curr, "kWh")
        print("Units Used    :", self.units, "Units")
        print("-" * 42)
        print("Energy Charge : Rs.", round(self.energy, 2))
        print("Fixed Charge  : Rs.", round(self.fixed, 2))
        print("FPPPA (Fuel)  : Rs.", round(self.fpppa, 2))
        print("Govt. Duty    : Rs.", round(self.duty, 2))
        print("-" * 42)
        print("TOTAL PAYABLE : Rs.", round(self.total, 2))
        print("=" * 42)


# ------------------------------------------------------------------------------
# 2. Child Class 1: ResidentialBill (Ghar ke liye)
# TorrentBill se inherit karta hai (Single Inheritance)
# ------------------------------------------------------------------------------
class ResidentialBill(TorrentBill):
    # Constructor
    def __init__(self, cno, name, prev, curr, phase="Single"):
        # super() se parent class (TorrentBill) ka constructor call kiya
        super().__init__(cno, name, prev, curr)
        
        # Residential specific variable (String concatenation without f-string)
        self.phase = phase
        self.btype = "Residential (" + str(self.phase) + " Phase)"

    # Method: Ghar ka bill calculate karna (Telescopic Slab System)
    def calc_bill(self):
        # 1. Fixed Charge: Single phase = Rs. 25, Three phase = Rs. 100
        if self.phase.lower() == "three":
            self.fixed = 100.0
        else:
            self.fixed = 25.0

        # 2. Telescopic Slab Calculation (Sasta rate pehle, fir badhta hai):
        # 0 se 50 units   -> Rs. 3.20 per unit
        # 51 se 100 units -> Rs. 3.90 per unit
        # 101 se 250 units-> Rs. 4.50 per unit
        # 250 se upar     -> Rs. 5.30 per unit
        u = self.units
        if u <= 50:
            self.energy = u * 3.20
        elif u <= 100:
            self.energy = (50 * 3.20) + ((u - 50) * 3.90)
        elif u <= 250:
            self.energy = (50 * 3.20) + (50 * 3.90) + ((u - 100) * 4.50)
        else:
            self.energy = (50 * 3.20) + (50 * 3.90) + (150 * 4.50) + ((u - 250) * 5.30)

        # 3. FPPPA fuel surcharge nikalna
        self.calc_fpppa()

        # 4. Electricity Duty: 15% on (Energy + Fixed)
        self.duty = round((self.energy + self.fixed) * 0.15, 2)

        # 5. Total Payable Amount
        self.total = round(self.energy + self.fixed + self.fpppa + self.duty, 2)
        return self.total


# ------------------------------------------------------------------------------
# 3. Child Class 2: CommercialBill (Dukan / Office ke liye)
# TorrentBill se inherit karta hai (Hierarchical Inheritance)
# ------------------------------------------------------------------------------
class CommercialBill(TorrentBill):
    # Constructor
    def __init__(self, cno, name, prev, curr, shop, load):
        # super() se parent class ka constructor call kiya
        super().__init__(cno, name, prev, curr)
        
        # Commercial specific variables (String concatenation without f-string)
        self.shop = shop        # Shop/Office ka naam
        self.load = float(load) # Connected Load (kW me)
        self.btype = "Commercial (" + str(self.shop) + ")"

    # Method: Dukan ka bill calculate karna
    def calc_bill(self):
        # 1. Fixed Charge: Rs. 80 per kW load
        self.fixed = round(self.load * 80.0, 2)

        # 2. Commercial Energy Rate: Flat Rs. 5.20 per unit
        self.energy = round(self.units * 5.20, 2)

        # 3. FPPPA fuel surcharge
        self.calc_fpppa()

        # 4. Commercial Duty: 20% on (Energy + Fixed)
        self.duty = round((self.energy + self.fixed) * 0.20, 2)

        # 5. Total Payable Amount
        self.total = round(self.energy + self.fixed + self.fpppa + self.duty, 2)
        return self.total


# ------------------------------------------------------------------------------
# 4. Child Class 3: IndustrialBill (Factory ke liye)
# TorrentBill se inherit karta hai
# ------------------------------------------------------------------------------
class IndustrialBill(TorrentBill):
    # Constructor
    def __init__(self, cno, name, prev, curr, factory, load):
        # super() se parent class constructor call kiya
        super().__init__(cno, name, prev, curr)
        
        # Industrial specific variables (String concatenation without f-string)
        self.factory = factory  # Factory ka naam
        self.load = float(load) # Factory Load (kW me)
        self.btype = "Industrial (" + str(self.factory) + ")"

    # Method: Factory ka bill calculate karna
    def calc_bill(self):
        # 1. Industrial Load Charge: Rs. 150 per kW load
        self.fixed = round(self.load * 150.0, 2)

        # 2. Industrial Energy Rate: Flat Rs. 4.75 per unit
        self.energy = round(self.units * 4.75, 2)

        # 3. FPPPA fuel surcharge
        self.calc_fpppa()

        # 4. Industrial Duty: 15% on (Energy + Fixed)
        self.duty = round((self.energy + self.fixed) * 0.15, 2)

        # 5. Total Payable Amount
        self.total = round(self.energy + self.fixed + self.fpppa + self.duty, 2)
        return self.total


# ==============================================================================
# MAIN PROGRAM: Teeno Scenarios ka Test Run
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 42)
    print("  TORRENT POWER BILLING SYSTEM (DEMO)")
    print("#" * 42)

    # Scenario 1: Ghar ka bill (Residential)
    b1 = ResidentialBill("101", "Vatsal Patel", 4500, 4720, phase="Single")
    b1.calc_bill()
    b1.show_bill()

    # Scenario 2: Dukan ka bill (Commercial)
    b2 = CommercialBill("202", "Rajesh Shah", 11000, 11650, shop="Shah Electronics", load=5.0)
    b2.calc_bill()
    b2.show_bill()

    # Scenario 3: Factory ka bill (Industrial)
    b3 = IndustrialBill("303", "Kishore Parmar", 30000, 34500, factory="Parmar Works", load=40.0)
    b3.calc_bill()
    b3.show_bill()
