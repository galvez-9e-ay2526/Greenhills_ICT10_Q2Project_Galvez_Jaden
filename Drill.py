# Working with Set Operators

from pyscript import document


grade7 = {'DeAaron Fox', 'Maliq Brown', 'Luke Kornet', 'Carter Bryant'}
grade8 = {'Jayden Quaintance', 'Tobias Harris', 'Keldon Johnson', 'Harrison Barnes'}
grade9 = {'Julian Champagnie', 'Stephon Castle', 'Devin Vassell'}
grade10 = {'Jaden Galvez', 'Victor Wembanyama', 'Dylan Harper'}

members = grade7 | grade8 | grade9 | grade10


def add_member(event):
    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()

    members.add(first + " " + last)
    member_list = sorted(members)

    document.getElementById("output").innerHTML = f"""
    All members:<br>
    {"<br>".join(member_list)}
    <br>
    Total members: {len(members)}
    """
 