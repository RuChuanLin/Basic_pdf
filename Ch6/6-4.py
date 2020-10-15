# 6-3===================================================================
# ----------------------------------------------------------------------
dictionary = {
    'You': '你、妳、你們',
    'I': '我',
    'He': '他',
    'She': '她',
    'It': '它',
    }
# ----------------------------------------------------------------------
print("You: " + dictionary['You'])
print("I: " + dictionary['I'])
print("He: " + dictionary['He'])
print("She: " + dictionary['She'])
print("It :" + dictionary['It'])
# ----------------------------------------------------------------------
print("\nYou: " + dictionary['You'] +
      "\nI: " + dictionary['I'] +
      "\nHe: " + dictionary['He'] +
      "\nShe: " + dictionary['She'] +
      "\nIt :" + dictionary['It']
      )
# 6-4===================================================================
dictionary = {
    'You': '你、妳、你們',
    'I': '我',
    'He': '他',
    'She': '她',
    'It': '它',
    }


for English, Chinese in dictionary.items(): # .items() 請務必記得加！
    print(English + ": " + Chinese)
# ----------------------------------------------------------------------
dictionary = {
    'You': '你、妳、你們',
    'I': '我',
    'He': '他',
    'She': '她',
    'It': '它',
    'Your': '你的、妳的、你們的',
    'My': '我的',
    'His': '他的',
    'Her': '她的',
    'Its': '它的'
    }


for English, Chinese in dictionary.items(): # .items() 請務必記得加！
    print(English + ": " + Chinese)
# ----------------------------------------------------------------------