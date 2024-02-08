f =open("test.txt","w")
while True:
    request = input("Введите какую либо запись:     ")
    
    if request.lower() != "стоп":
        
        f.write(f"{request}\n")
    else:
        print("Запись сохранена!")
        
        f.close()
        
        break
    