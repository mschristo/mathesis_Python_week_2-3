"""
Να κατασκευάσετε το παιχνίδι «μάντεψε ένα αριθμό».

Ο παίκτης προσπαθεί να μαντέψει ένα αριθμό από το 1 έως το 100, που έχει τυχαία διαλέξει ο υπολογιστής.

Το πρόγραμμα θα περιμένει την είσοδο ενός αριθμού από το χρήστη και θα ελέγχει αν είναι ο ίδιος με αυτόν που έχει διαλέξει ο υπολογιστής.

Εάν ο χρήστης δεν έχει βρει τον αριθμό, το πρόγραμμα θα δίνει το μήνυμα "ΟΧΙ είναι μεγαλύτερος" ή "ΟΧΙ είναι μικρότερος",
ανάλογα με το αν ο αριθμός που έχει διαλέξει ο υπολογιστής είναι μεγαλύτερος ή μικρότερος από αυτόν που έδωσε ο χρήστης.

Ο έλεγχος θα επαναλαμβάνεται μέχρι ο χρήστης να βρει τον αριθμό ή να τερματίσει το παιχνίδι.

Εάν ο χρήστης βρει τον ζητούμενο αριθμό, το πρόγραμμα θα εμφανίζει το μήνυμα
"Το βρήκατε σωστά μετά από Χ προσπάθειες" (όπου Χ ο αριθμός των προσπαθειών).

Χρησιμοποιήστε αμυντικό προγραμματισμό.
* Χρησιμοποιήστε τη βιβλιοθήκη random για τον υπολογισμό του τυχαίου αριθμού.

Το πρόγραμμά σας θα πρέπει να τηρεί τις παρακάτω προϋποθέσεις:

1.Το παιχνίδι να αρχίζει με σαφείς οδηγίες ως προς τους δύο τρόπους τερματισμού του [εύρεση του αριθμού από τον χρήστη και 
  εκούσιος τερματισμός από τον χρήστη] (1/7 μονάδες).
2.To παιχνίδι να εμφανίζει τα κατάλληλα μηνύματα στον χρήστη, 
  όπως περιγράφονται παραπάνω (π.χ. "ΟΧΙ είναι μεγαλύτερος" κ.λπ) (2/7 μονάδες).
3.Αν ο χρήστης δώσει μη αριθμό ή αριθμό μικρότερο από το 1 ή μεγαλύτερο από το 100, 
  το πρόγραμμα να ζητά και πάλι από τον χρήστη την εισαγωγή ενός αριθμού, 
  χωρίς να σταματήσει και χωρίς αυτού του είδους το λάθος να προσμετράται στις προσπάθειες (2/7 μονάδες).
4.Όταν βρεθεί ο αριθμός, το παιχνίδι να τερματίζεται εμφανίζοντας το πλήθος των προσπαθειών που 
  χρειάστηκε ο χρήστης για βρει τον ζητούμενο αριθμό (1/7 μονάδες).
5.Να υπάρχει η δυνατότητα εκούσιου τερματισμού του παιχνιδιού από τον χρήστη πριν την λήξη του, 
  όπως περιγράφεται στις αρχικές οδηγίες (1/7 μονάδες).
"""

import random

def isnum(n = ''):
    if not type(n) is str :
        return False
    n = n.strip()
    if n.isdigit():
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".")<= 1 and isnum(n.replace(".", "")):
            return True
        else:
            return False
    else :
        return False

counter = 0
number = random.randrange(1,100)
print("Οδηγίες παιχνιδιού : \n"
      "- Προσπαθήστε να μαντέψετε τον αριθμό που έχω διαλέξει ο οποίος είναι μεταξύ του 1 και του 100\n"
      "- Το παιχνίδι τελειώνει μόλις καταφέρετε και μαντέψετε τον αριθμό που έχω σκεφτεί\n"
      "- Αν θέλετε να τερματίσετε το παιχνίδι εισάγετε 0 ή τη λέξη telos", end="\n\n");
while True:
    n = input("Μαντέψε ποιον αριθμό σκέφτηκα = ")
    if n == '0' or n == "telos" :
        print("Τα παράτησες μετά απο ", counter, " προσπάθειες. Ο αριθμός που είχα στο μυαλό μου ήταν : ", number, end="\n")
        break
    if n == '' :
        print("Δεν έγραψες τίποτα ! Προσπάθησε ξανά", end="\n\n")
        continue
    if isnum(n) :
        counter += 1
        n = int(n)
        if n == number :
            print("Μπράβο σου ! Βρήκες τον αριθμό που σκέφτηκα μετά απο ", counter, " προσπάθειες : ",counter, end="\n")
            break
        elif n < 1 or n > 100:
            counter -= 1
            print("Εισάγετε έναν αριθμό μεταξύ 1 και 100", end="\n")
        elif n < number :
            print("Ο αριθμός που έχω στο μυαλό μου είναι μεγαλύτερος απο αυτόν που μάντεψες. Προσπάθησε ξανα! (Προσπάθειες : ",counter,")",end="\n\n")
        else :
            print("Ο αριθμός που έχω στο μυαλό μου είναι μικρότερος απο αυτόν που μάντεψες. Προσπάθησε ξανα! (Προσπάθειες : ",counter, ")", end="\n\n")
    else :
        print("Δεν γράψατε αριθμό. Προσπάθησε ξανά.", end="\n\n")







