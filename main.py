from pyscript import document

def compute_average(event):
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    science = float(document.getElementById("science").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    document.getElementById("math_output").innerText = math
    document.getElementById("english_output").innerText = english
    document.getElementById("science_output").innerText = science
    document.getElementById("filipino_output").innerText = filipino
    document.getElementById("ict_output").innerText = ict
    document.getElementById("pe_output").innerText = pe

    total = math + english + science + filipino + ict + pe
    average = total / 6

    first = document.getElementById("first").value
    last = document.getElementById("last").value


    document.getElementById("name").innerText = f"Name: {first} {last}"
    document.getElementById("output").innerText = f"Your General Weighted Average is {round(average, 2)}"

    document.getElementById("grades_container").style.display = "block"