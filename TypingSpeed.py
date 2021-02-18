import time
import PySimpleGUI as sg

sg.theme('LightBlue')
push = input('Enter any key to start: ')
if push is not None:
    fh = open('TypingSpeedSource.txt','r')
    print('\n')
    entireTextList = list()
    entireTextFlat = ''
    lineSpacer = 0
    for line in fh:
        lineSpacer += 1
        line = line.replace('\n','')
        entireTextList.append(line)
        entireTextFlat += line + ' '
        if lineSpacer == 1:
            entireTextFlat += '\n'
            lineSpacer = 0
    print('\n')
    layout = [[sg.Text(size=(16,1), key='-OUTPUT-'), sg.Text(entireTextFlat)],
    [],
    [],
    [sg.Text('Type the text here: ')],
              [sg.Input(key='-IN-')],
              [sg.Button('Start'), sg.Button('Exit')]]
    window = sg.Window('Offline Typing Speed Calculator', layout)
    while True:  # Event Loop
        event, values = window.read()
        if event == 'Start':
            startTime = time.strftime("%H:%M:%S")
            # Make the closing event the enter button.
        if event == sg.WIN_CLOSED or event == 'Exit':
            window['-OUTPUT-'].update(values['-IN-'])
            enteredText = values['-IN-'].split()
            entireTextFlat = entireTextFlat.split()
            score = 0
            flag = 0
            for num in range(len(enteredText)):
                for numTwo in range(len(entireTextFlat)):
                    if enteredText[num] == entireTextFlat[num]:
                        score += 1
                    if num == numTwo:
                        flag = 1
                        break
                if flag == 1:
                    break
            typingAccuracy = score/len(enteredText) * 100
            print('Accuracy:',typingAccuracy,'%')
            endTime = time.strftime("%H:%M:%S")
            tempOne = startTime.split(':')
            minOne = int(tempOne[1])
            secOne = int(tempOne[2])
            tempTwo = endTime.split(':')
            minTwo = int(tempTwo[1])
            secTwo = int(tempTwo[2])
            minElapsed = minTwo - minOne
            secElapsed = secTwo - secOne
            minSecElapsed = minElapsed*60
            totSecElapsed = secElapsed + minSecElapsed
            print('Seconds Elapsed:',totSecElapsed)
            break
        # Update the "output" text element to be the value of "input" element
    window.close()

    # Run the type racer
    ticker = 0
    error = 0
    #entireText = entireText.split()
    #for num in range(len(entireText)):
    #    entireText[num] = entireText[num] + " "
    #for block in entireText:
    #    print(block)
    #    sg.InputText()
    #    userWord = input()
    #    while userWord != block:
    #        error += 1
    #        print(block)
    #        userWord = input()
    #    ticker += 1
        #}
    # Stopwatch stopper, calculations, and Time Print


    print('\n')
#print('WPM:',round(float(ticker)/totSecElapsed * 100,3))
#print('Accuracy:',100 - round(float(error)/ticker * 100,3),'%')
#print('Time:',totSecElapsed,'seconds')
#print('\n')
