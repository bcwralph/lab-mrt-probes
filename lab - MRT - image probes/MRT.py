import os,sys, pygame, numpy, random, EasyDialogs, datasaver, text_wrapper, webbrowser
pygame.init()
clock=pygame.time.Clock()

#collect subject information
subject = int(EasyDialogs.AskString("Please enter the subject number:")) #int. says it must be an integer
sona_id = int(EasyDialogs.AskString("Please enter the subject's sona id:"))
subject_sex = str(EasyDialogs.AskString("Enter participant's sex (m or f):"))
subject_age = str(EasyDialogs.AskString("Enter participant's age:"))

#create data file
#datasaver.save("data/"+str(subject),("subject", "sona_id", "sex", "age", "trial", "omission", "RT_from_metronome", "probeType", "probeOneResp", "probeTwoResp", "asrs1", "asrs2", "asrs3", "asrs4", "asrs5", "asrs6"))
datasaver.save("data/"+str(subject),("subject", "sona_id", "sex", "age", "trial", "omission", "RT_from_metronome", "probeType", "probeOneResp", "probeTwoResp"))

# Set up window
window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
window.fill((0,0,0))
pygame.display.flip()
centre=window.get_rect().center
font=pygame.font.Font(pygame.font.match_font('helvetica, calibri, arial'), 28)
pygame.mouse.set_visible(False)

#colours
black = (0, 0, 0); white = (255, 255, 255)

#set keys
exitKey = pygame.K_e
continueKey = pygame.K_SPACE
skipKey = pygame.K_n
terminate = pygame.K_t
startKey = pygame.K_s
#selfCaughtKey = pygame.K_m
#Probe 1=On task or MW, if MW, Probe 2 = Spontaneous or Deliberate
#Self caught -- Probe 2

#display messages
text_pos = (100,100)

instructionsP1 = text_wrapper.drawText('For this experiment, you will hear a metronome sound presented at a constant rate via the headphones.' 
+'\n\nYour task is to press the SPACEBAR in synchrony with the onset of the metronome,'
+' so that you press the space bar exactly when each metronome sound is presented.'
+' Please keep your eyes fixated on the monitor while you complete this task.'
+'\n\nEvery once in a while, the task will temporarily stop and you will be presented with a thought-sampling screen'
+' that will ask you to indicate whether you were ON TASK or MIND WANDERING just before the thought-sampling screen appeared.', 
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

instructionsP2 = text_wrapper.drawText('Being ON TASK means that, JUST BEFORE the thought-sampling screen appeared,'
+' you were focused on completing the task. Some examples of ON TASK thoughts include thoughts about your performance'
+' on the task or thoughts about your response.'
+'\n\nOn the other hand, MIND WANDERING means that, JUST BEFORE the thought-sampling screen appeared,'
+' you were thinking about something completely unrelated to the task. Some examples of MIND WANDERING include thoughts about what'
+' to eat for dinner, thoughts about plans you have with friends, or thoughts about an upcoming test. Any thoughts that you have'
+' that are not related to this task count as MIND WANDERING.'
+'\n\nThe thought-sampling screen will look like this:'
+'\n\nSTOP!'
+'\nWhich of the following best characterizes your mental state JUST BEFORE this screen appeared:'
+'\n\n     (1) On TASK'
+'\n\n     (2) MIND WANDERING'
+'\n\nPlease use the keyboard to select the response option that best describes your mental state just before this screen appeared.',
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

instructionsP3 = text_wrapper.drawText('MIND WANDERING can also occur either because you INTENTIONALLY decided to think about things'
+' that are unrelated to the task, OR because your thoughts UNINTENTIONALLY drifted away to task-unrelated thoughts, despite your best intentions'
+' to focus on the task.'
+'\n\nWhen the thought-sampling screen is presented, if you indicate that you are MIND WANDERING, we will also ask you to indicate'
+' whether the MIND WANDERING you are experiencing is INTENTIONAL or UNINTENTIONAL.'
+'\n\nIf you indicate that you are MIND WANDERING on the previous thought-sampling screen, you will then be presented with the following thought-sampling screen:'
+'\n\nWhich of the following best characterizes your MIND WANDERING:'
+'\n\n     (1) INTENTIONAL MIND WANDERING'
+'\n\n     (2) UNINTENTIONAL MIND WANDERING'
+'\n\nPlease use the keyboard to select the response option that best describes your mind wandering.'
,white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

instructionsP4 = text_wrapper.drawText("You are now going to complete a brief practice session to help you to become familiar with the task."
+"\n\nDo you have any questions?"
+"\n\nWhen you are ready to proceed, please press the SPACEBAR to begin the practice session.",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

instructions= [instructionsP1[0], instructionsP2[0], instructionsP3[0], instructionsP4[0]]
    
practice_over = text_wrapper.drawText('The practice trials are now over.'
+'\n\n\nPlease remove your headphones and wait for further instructions from the researcher.', 
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)
# s key to start

thank_you = text_wrapper.drawText("The metronome task is now over. Please sit quietly and wait for further instructions from the researcher.", 
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

probeScreenOne = text_wrapper.drawText('STOP!'
+'\nWhich of the following best characterizes your mental state JUST BEFORE this screen appeared:'
+'\n\n     (1) On TASK'
+'\n\n     (2) MIND WANDERING'
+'\n\nPlease use the keyboard to select the response option that best describes your mental state just before this screen appeared.',
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

probeScreenTwo = text_wrapper.drawText('Which of the following best characterizes your MIND WANDERING:'
+'\n\n     (1) INTENTIONAL MIND WANDERING'
+'\n\n     (2) UNINTENTIONAL MIND WANDERING'
+'\n\nPlease use the keyboard to select the response option that best describes your mind wandering.',
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)
'''
asrs = text_wrapper.drawText("Please answer the following questions, rating yourself on each of the criteria shown in the scale below."
+" Choose the option that best describes how you have felt and conducted yourself over the past 6 months."
+"\n\nSimply press the number on the keyboard (1-5) to indicate your response."
"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often"
+"\n\nWhen you are ready to begin, please press the 's' key.",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs1 = text_wrapper.drawText("How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs2 = text_wrapper.drawText("How often do you have difficulty getting things done in order when you have to do a task that requires organization?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs3 = text_wrapper.drawText("How often do you have problems remembering appointments or obligations?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs4 = text_wrapper.drawText("When you have a task that requires a lot of thought, how often do you avoid or delay getting started?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs5 = text_wrapper.drawText("How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrs6 = text_wrapper.drawText("How often do you feel overly active and compelled to do things, like you were driven by a motor?"
+"\n\n1) never \n2) rarely \n3) sometimes \n4) often \n5) very often",
white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

asrsQs = {asrs1[0]:'',asrs2[0]:'',asrs3[0]:'',asrs4[0]:'',asrs5[0]:'',asrs6[0]:''}
'''
#load sound
metronome = pygame.mixer.Sound('metronomeMono.wav')

#load image
resume = text_wrapper.drawText('Please press the space bar to resume the task', white, surface=pygame.transform.scale(window, (1200,1200)), lineSpacing = 3, font=font)

#trial parameters
pre_targ = 650 #in milliseconds
targ_time = 75
post_targ = 575 #total trial time = 1300 ms

num_practice = 18
num_trials = 900 #19 minutes

num_probes = 18 # in 50 trial blocks (900 / 50) = 18
#press space bar to resume
probeBlocks=range(0,950,50)
probeList = []
for i in range(num_probes):
    probeList.append(random.randint(probeBlocks[i],probeBlocks[i+1]-1))

def drawProbe(stop, probeOneResp, probeTwoResp, probeType):
    
    if probeType == "probe": #if probe caught, draw first probe asking about on-task or mind wandering
        window.fill(black)
        window.blit(probeScreenOne[0],text_pos)
        pygame.display.flip()
        
        done=False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == exitKey: stop = True
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_1: done=True; probeOneResp="on_task" #on task
                    elif event.key == pygame.K_2:done=True; probeOneResp="MW" #mind wandering
                    else:continue
                else:continue
            if stop:break
        
    if stop == False and probeOneResp != "on_task":#Otherwise, if on-task not selected, ask Deliberate/Spontaneous
        window.fill(black)
        window.blit(probeScreenTwo[0],text_pos)
        pygame.display.flip()
        
        done=False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == exitKey: stop = True
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_1: done=True; probeTwoResp="int" #deliberate
                    elif event.key == pygame.K_2:done=True; probeTwoResp="unint" #spontaneous
                    else:continue
                else:continue
            if stop:break    
    
    window.fill(black)
    window.blit(resume[0],text_pos)
    pygame.display.flip()
    done = False
    quitEarly = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True; quitEarly = True
            if event.type == pygame.KEYDOWN:
                if event.key == exitKey: done = True; quitEarly = True
                if event.key == continueKey: done = True
    if quitEarly:
        pygame.quit()
        sys.exit()
    
    window.fill(black)
    pygame.display.flip()
    
    return stop, probeOneResp, probeTwoResp, probeType

#### trial builder
def doTrial(recordData, trial, probeList):
    probeType=''
    probeOneResp=''
    probeTwoResp=''
    
    RT = ''
    stop = False
    resp = False
    omission = 1
    
    trialOver = False
    trial_start = pygame.time.get_ticks()
    while not trialOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == exitKey: stop = True
            elif not resp and event.type == pygame.KEYDOWN and event.key == continueKey: 
                now = pygame.time.get_ticks() - trial_start
                RT = now - pre_targ # get RT in reference to when tone is presented
                resp = True            
                omission = 0
                '''
            elif event.type==pygame.KEYDOWN and event.key == selfCaughtKey:
                [stop, probeOneResp, probeTwoResp, probeType] = drawProbe(stop, probeOneResp, probeTwoResp, "self")
                omission = 0
                trialOver=True; break
                '''
            else: continue
       
        if trialOver==False:
            if (pygame.time.get_ticks() - trial_start) == pre_targ: metronome.play()
            elif (pygame.time.get_ticks() - trial_start) == 1300: trialOver = True        
        else:continue
        if stop: break
        #clock.tick(1)
        
    if trial in probeList:
        [stop, probeOneResp, probeTwoResp, probeType] = drawProbe(stop, probeOneResp, probeTwoResp, "probe")
           
    if recordData:
        data = [subject, sona_id, subject_sex, subject_age, trial, omission, RT, probeType, probeOneResp, probeTwoResp]
        datasaver.save("data/"+str(subject), data)   #Save Data
    
    return stop
'''
def drawQs(item, qKeys):
    #asrsQs = {asrs1[0]:0,asrs2[0]:1,asrs3[0]:2,asrs4[0]:3,asrs5[0]:4,asrs6[0]:5}
    
    window.fill(black)
    window.blit(item, text_pos)
    pygame.display.flip()
    asrs_response=''
    done = False
    stop = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == exitKey: stop = True
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_1: done=True; asrs_response=1
                elif event.key == pygame.K_2:done=True; asrs_response=2
                elif event.key == pygame.K_3:done=True; asrs_response=3
                elif event.key == pygame.K_4:done=True; asrs_response=4
                elif event.key == pygame.K_5:done=True; asrs_response=5
                else:continue
            else:continue
        if stop:break
    
    asrsQs[item]=asrs_response
    #myData[asrsQs{i[1]}]
    #asrsData.append(asrs_response)
    #asrsData
    
    return stop, asrsQs
'''
#### Instructions
window.fill(black)
for i in range(len(instructions)):
    window.fill(black)
    window.blit(instructions[i],text_pos)
    pygame.display.flip()
    done = False
    quitEarly = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done = True; quitEarly = True
            if event.type == pygame.KEYDOWN:
                if event.key == exitKey: done = True; quitEarly = True
                if event.key == continueKey: done = True
    if quitEarly:
        pygame.quit()
        sys.exit()   

#### Practice Trials
window.fill(black)
pygame.display.flip()
recordData = False
practiceProbe = [num_practice/2]
for p in range(num_practice):
    stop = doTrial(recordData, p, practiceProbe)
    if stop:
        break

#### Intermission
window.fill(black)
window.blit(practice_over[0], text_pos)
pygame.display.flip()
done = False
quitEarly = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True; quitEarly = True
        if event.type == pygame.KEYDOWN:
            if event.key == exitKey: done = True; quitEarly = True
            if event.key == startKey: done = True
if quitEarly:
    pygame.quit()
    sys.exit()

#### Experimental Trials
window.fill(black)
pygame.display.flip()
recordData = True
for trial in range(num_trials):
    stop = doTrial(recordData, trial, probeList)
    if stop:
        break
'''
### Questionnaire instructions
window.fill(black)
window.blit(asrs[0], text_pos)
pygame.display.flip()
done = False
quitEarly = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True; quitEarly = True
        if event.type == pygame.KEYDOWN:
            if event.key == exitKey: done = True; quitEarly = True
            if event.key == startKey: done = True
if quitEarly:
    pygame.quit()
    sys.exit()
    
### Questionnaire
qKeys = asrsQs.keys()
random.shuffle(qKeys)

for item in qKeys:
    stop, asrsQs = drawQs(item, qKeys)
    if stop:
        break
    
#asrsData = [subject,sona_id,subject_sex,subject_age,"ASRS",'null','null','null','null','null', asrsQs[asrs1[0]], asrsQs[asrs2[0]], asrsQs[asrs3[0]], asrsQs[asrs4[0]], asrsQs[asrs5[0]], asrsQs[asrs6[0]]]
    
datasaver.save("data/"+str(subject),asrsData)

#asrsQs = {asrs1[0]:'',asrs2[0]:'',asrs3[0]:'',asrs4[0]:'',asrs5[0]:'',asrs6[0]:''}
'''
#### EXIT
window.fill(black)
window.blit(thank_you[0], text_pos)
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        elif event.type == pygame.KEYDOWN and event.key == terminate: done = True
#pygame.quit()
#sys.exit()
#os.system("start https://psychologyuwaterloo.qualtrics.com/SE/?SID=SV_8elrG3oBBkab4Z7/?id="+str(subject))
webbrowser.open("https://psychologyuwaterloo.qualtrics.com/SE/?SID=SV_8elrG3oBBkab4Z7&id="+str(subject))
pygame.quit()
sys.exit()
