import keyboard

keyboard.add_hotkey('w', lambda : keyboard.write('cima'))
keyboard.add_hotkey('a', lambda : keyboard.write('esquerda'))
keyboard.add_hotkey('s', lambda : keyboard.write('baixo'))
keyboard.add_hotkey('d', lambda : keyboard.write('direita'))
keyboard.add_hotkey('w+d', lambda : keyboard.write('cima direita'))
keyboard.add_hotkey('w+a', lambda : keyboard.write('cima esquerda'))
keyboard.add_hotkey('a+s', lambda : keyboard.write('baixo esquerda'))
keyboard.add_hotkey('s+d', lambda : keyboard.write('baixo direita'))

keyboard.wait('esc')
