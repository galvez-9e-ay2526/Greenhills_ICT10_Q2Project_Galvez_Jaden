# Candidate Verification System

from pyscript import display, document


def view_user(e):
    document.getElementById('result').innerHTML = ' '

    first_Input = document.getElementById('firstname').value
    last_Input = document.getElementById('lastname').value
    candidate_Input = first_Input + ' ' + last_Input

    club_members = [
        'Jaden Galvez',
        'Zangief Briones',
        'Cedric Visorde',
        'Victoria Rivera',
        'Reuben Lim'
    ]

    candidate_checker = candidate_Input in club_members

    display_message = (
        f'Sorry {candidate_Input}, your name is not on the list.',
        f'Congratulations {candidate_Input}! You are now part of the ICT club.'
    )

    display(display_message[candidate_checker], target='result')