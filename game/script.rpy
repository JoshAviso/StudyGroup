# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg library       = "images/backgrounds/library.png"
image bg studyroom     = "images/backgrounds/study.png"

define narrator = Character(what_color="#ffb6ce", what_italic=True, what_size=26, what_text_align=0.5, what_xalign=0.5)

define Aurora           = Character("Aurora", color="#ff4885", what_color="#ffdfea", what_size=26)
image Aurora Neutral    = "images/characters/aurora_neutral.png"
image Aurora Happy      = "images/characters/aurora_happy.png"
image Aurora Sad        = "images/characters/aurora_sad.png"
image Aurora Confused   = "images/characters/aurora_confused.png"

define Celestia = Character("Celestia", color="#9e00c9", what_color="#f8dfff", what_size=26)
image Celestia Neutral  = "images/characters/celestia_netural.png"
image Celestia Happy    = "images/characters/celestia_happy.png"
image Celestia Sad      = "images/characters/celestia_sad.png"
image Celestia Mad      = "images/characters/celestia_mad.png"

define Luis     = Character("Luis", color="#007232", what_color="#daffea", what_size=26)
image Luis Neutral      = "images/characters/luis_neutral.png"
image Luis Happy        = "images/characters/luis_happy.png"
image Luis Sad          = "images/characters/luis_sad.png"
image Luis Mad          = "images/characters/luis_mad.png"

define Anthony  = Character("Anthony", color="#ffcc00", what_color="#fff6d3", what_size=26)
image Anthony Neutral   = "images/characters/anthony_neutral.png"
image Anthony Happy     = "images/characters/anthony_happy.png"
image Anthony Sad       = "images/characters/anthony_sad.png"
image Anthony Mad       = "images/characters/anthony_mad.png"

define Rafael   = Character("Rafael", color="#71d4e8", what_color="#dffaff", what_size=26)
image Rafael Neutral    = "images/characters/rafael_neutral.png"
image Rafael Happy      = "images/characters/rafael_happy.png"
image Rafael Sad        = "images/characters/rafael_sad.png"
image Rafael Mad        = "images/characters/rafael_mad.png"

define Jonathan = Character("Jonathan", color="#8991a0", what_color="#dce8ff", what_size=26)
image Jonathan Neutral  = "images/characters/jonathan_neutral.png"
image Jonathan Happy    = "images/characters/jonathan_happy.png"
image Jonathan Sad      = "images/characters/jonathan_sad.png"
image Jonathan Mad      = "images/characters/jonathan_mad.png"

define centerAnchor = Position(xanchor=0.5, yanchor=0.0)
define offscreen_left = (-0.25, 0.0)
transform offsceen_left_pos:    
    xalign -0.25
define far_left = (0.1, 0.0)
transform far_left_pos:         
    xalign 0.1
define left_left = (0.2, 0.0)
transform left_left_pos:        
    xalign 0.2
define left = (0.25, 0.0)
transform left_pos:             
    xalign 0.25
define left_right = (0.3, 0.0)
transform left_right_pos:       
    xalign 0.3
define center_left = (0.4, 0.0)
transform center_left_pos:      
    xalign 0.4
define center = (0.5, 0.0)
transform center_pos:           
    xalign 0.5
define center_right = (0.6, 0.0)
transform center_right_pos:     
    xalign 0.6
define right_left = (0.7, 0.0)
transform right_left_pos:       
    xalign 0.7
define right = (0.75, 0.0)
transform right_pos:            
    xalign 0.75
define right_right = (0.8, 0.0)
transform right_right_pos:      
    xalign 0.8
define far_right = (0.9, 0.0)
transform far_right_pos:        
    xalign 0.9
define offscreen_right = (1.25, 0.0)
transform offscreen_right_pos:  
    xalign 1.25

# The game starts here.

label start:
    $ went_route_113 = False
    $ went_route_121 = False
    $ went_route_131 = False
    $ went_route_132 = False
    $ went_route_21 = False
    $ went_route_22 = False
    $ went_route_31 = False
    $ went_route_32 = False
    $ went_route_33 = False

    scene bg library

    show Aurora Happy at center_pos
    "Woah, the library really is amazing here. My first year at such a prestigious school, all thanks to the hard work I put in to getting accepted in Business Management."

    show Aurora Sad at Move((0.5,0.0), (0.4,0.0), 1.0), Position(xanchor=0.5, yanchor=0.0)
    "But, that's the least of my worries, now I have to overcome the hardest challenge yet! Getting to know my new study mates..."

    show Aurora at Move((0.4,0.0), (0.25,0.0), 1.0), Position(xanchor=0.5, yanchor=0.0)
    show Luis Happy at Move(offscreen_right, right, 1.0), Position(xanchor=0.5, yanchor=0.0)
    voice "voice/L_1_1.mp3"
    Luis "Oh! Hello there beautiful..."

    show Aurora Confused
    Aurora "Oh?! Erm... Ah! Hello?"

    voice "voice/L_1_2.mp3"
    Luis "Oh my, a cutie we have here... If you don't mind me asking, Ms. Cutie, if you would happen to know where Business Management Study Group A would be?"

    show Aurora Happy
    Aurora "Oh! Ah! Yes! Uhm, actually, I'm part of Study Group A! Hahaha! My name's Aurora... Uhm.. How'd you figure out I was a business student?"

    voice "voice/L_1_3.mp3"
    Luis "Oho, Ms Aurora... What an elegant name. As for how I knew, I have experience in business, you see. I have a knack for picking out people in a crowd..."

    voice "voice/C_1_1.mp3"
    Celestia "Luis! Luis M. Labrador! Pft! Unbecoming! How unbecoming of you! I let down my guard for one second and you go off to pick up another girl! Let me remind you that you're the future heir to THE Labrador Technical Consultancy..."

    voice "voice/L_1_4.mp3"
    Luis "Oh! Celestia! My dear fiance, don't worry, I was simply asking Ms Aurora for the location of Study Group A. Luck would have it, she is actually part of our group."

    voice "voice/C_1_2.mp3"
    Celestia "Oh... Ms Aurora... Hmm... Well I wont blame someone of your background for being blindsided by this buffoon."

    voice "voice/C_1_3.mp3"
    Celestia "But I would like to warn you, I, Celestia Belmonte, daughter of THE Belmonte Real-Estate Family, am rightfully betrothed to Luis. I hope you do not think you could win his heart with your plain looks and mundane charms. Pft!"
    # (Celestia walks off)

    Aurora "Ah! Erm..."

    voice "voice/L_1_5.mp3"
    Luis "Oh, don't worry about her, she may be my betrothed, but only because of the arrangement between our families. Yes, she may be beautiful, but it really is what's in the heart that counts. As for you my dear Aurora, I actually find you quite beautiful, from the outside, and I suspect on the inside too."

    # (Luis walks to follow Celestia)

    Aurora "Woah! So I ended up with both Luis Labrador and Celestia Belmonte? I know this was a school known for its business curriculum, but to think those two would be enrolled here."

    "After taking a moment to compose myself, I decide to follow after them to the study room."
    
    scene bg studyroom

    voice "voice/A_1_1.mp3"
    Anthony "And that's member number six for six! Alright! That makes us complete for our first session and a perfect time for us to get to know each other. I'll go first, name's Anthony, Anthony Tolentino, model, athlete, and Business Management major. Great to meet you all. And you Ms..?"

    Aurora "Aurora... Aurora Mirasol, Business Management as well..."

    voice "voice/A_1_2.mp3"
    Anthony "Oho! Great to hear, you don't have to worry, I don't bite, but how about missy over here?"

    voice "voice/C_1_4.mp3"
    Celestia "Celestia Belmonte, heir to the Belmontes, and here is my fiance Luis Labrador. Both Business Management as well... If you don't mind, could you keep your voice down, we would be disturbing those in the adjacent rooms."

    voice "voice/A_1_3.mp3"
    Anthony "Oh! Sorry, I'll be mindful of my voice, but how about Sir Luis' introduction?"

    voice "voice/L_1_6.mp3"
    Luis "Hello, yes, as my dear Celestia mentioned, I am Luis Labrador, heir to the Labrador family and, perhaps, betrothed to my dear Celestia."

    voice "voice/A_1_4.mp3"
    Anthony "And that leaves mister quiet over here..."

    voice "voice/R_1_1.mp3"
    Rafael "Oh! yes. Business major, Rafael Flores. Nice to meet you. Oh and.. Aurora... nice to see you after all this time..."

    Aurora "Rafael! Long time no see..."

    voice "voice/A_1_5.mp3"
    Anthony "Oh! You're Rafael Flores! The one who got the top marks in this year's entrance exam! You're a legend among us second years, getting perfect marks in that notoriously difficult exam."

    voice "voice/R_1_2.mp3"
    Rafael "Ah.. Yes... I did get the highest score, but.. that's only the first step."

    voice "voice/A_1_6.mp3"
    Anthony "And my oh my, humble too! I guess that's everyone done... Oh! Uhm you..."

    voice "voice/J_1_1.mp3"
    Jonathan "Yes, hello, Business Management major like all of you, Jonathan De Los Reyes..."

    voice "voice/A_1_7.mp3"
    Anthony "Oho... uhm... yes! Jonathan! So Jonathan what..."

    voice "voice/C_1_5.mp3"
    Celestia "Well, with that matter settled, let us begin the first material we will be covering, me and Luis have prepared some supporting items for everyone out of our good will. If you would like to..."

    scene bg studyroom

    "And so our first study session continued, with Celestia leading the discussion, only being interrupted by Anthony's attempts at making the atmosphere less stiff, to then being promptly told off by her. Rafael and I ended up pairing up as we used to back in grade school"

    voice "voice/R_2_1.mp3"
    Rafael "So.. Aurora, glad to see you here."

    Aurora "Glad to see you too. Funny we ended up as study buddies again after all these years."

    voice "voice/R_2_2.mp3"
    Rafael "Haha... Well I'm glad too... y'know, I never really did get to say a proper goodbye before moving to the city. I'm glad you didn't forget about me."

    Aurora "Aw, don't worry about it. And how could I forget about you..."

    voice "voice/L_2_1.mp3"
    Luis "Oh my? Ms. Aurora, I didn't know you had a childhood love, and what a genius he is..."

    Aurora "No. Haha! Erm... It's not like that Luis."

    voice "voice/R_2_3.mp3"
    Rafael "Yes Luis, it's not like that. Me and Aurora just have some shared history is all."

    voice "voice/L_2_2.mp3"
    Luis "Oh really? 'Just' some shared history? Well that's a good thing then. If I were you Rafael, and I had such a charming and earnest childhood love, I would never let her go. She would be mine and only mine."

    voice "voice/L_2_3.mp3"
    Luis "And you Ms. Aurora... What a charming and earnest person you are. I feel as though, I can depend on you should I ever need help. Would you like to maybe..."

    ## Maybe an SFX
    "Smack!"

    "A sharp pain hits my left cheek as Celestia steps between me and Luis."

    voice "voice/C_2_1.mp3"
    Celestia "Stop it! While I'm here dealing with this buffoon of an athlete, you two are... Ms. Aurora, Luis... I won't stop you two from... I'll be leaving..."

    "And so Celestia storms off out of the study room into the library. Luis, promptly leaves after her"

    voice "voice/A_2_1.mp3"
    Anthony "Well... That happened... Aurora! You're cheek... We have to..."

    "Anthony's face approaches a breath's distance away from mine as he holds my cheek with concern."

    Aurora "Oh no, no, it doesn't hurt, but I.. I didn't mean to..."

    voice "voice/R_2_4.mp3"
    Rafael "Don't worry about it Aurora."

    "Rafael steps between Anthony and me, as if protecting me from whatever Anthony might say"

    voice "voice/R_2_5.mp3"
    Rafael "Anthony, this isn't the time to try and make moves on Aurora."

    voice "voice/A_2_2.mp3"
    Anthony "Oh, no I mean... Ok, I guess, we should maybe talk to those two first. Two of us can go after them. How about, me and Jonathan go and Aurora you can stay here..."

    menu:
        "Actually, I think I should go.":
            jump route1
        "Actually, can you stay here Anthony?":
            jump route2
        "Uhm... Ok... I'll stay here with Rafael.":
            jump route3

label route1:
    Aurora "Actually, I think I should go."

    voice "voice/A_2_1_1.mp3"
    Anthony "Oh? Are you sure?"

    Aurora "Yes... I'm sure. It was my fault that they got into this situation."

    voice "voice/R_2_1_1.mp3"
    Rafael "Aurora. You don't have to. It's something that's just between them."

    Aurora "No, I insist."

    voice "voice/R_2_1_2.mp3"
    Rafael "Sigh... Ok fine, if you're sure about it. Jonathan, I think you should go."

    voice "voice/A_2_1_2.mp3"
    Anthony "Yes. Celestia can't stand me, and considering Luis was hitting on Aurora cause he obviously felt insecure about Rafael's relationship with her... It'd be best for you to be the one to join her."

    voice "voice/J_2_1_1.mp3"
    Jonathan "Uhm... Ok, sure I guess."

    scene library

    voice "voice/J_2_1_2.mp3"
    Jonathan "So, how do you want to go about this?"

    menu:
        "I'll look for Luis.":
            jump route11
        "I'll look for Celestia.":
            jump route12
        "Let's look for them together.":
            jump route13

label route11:

    scene library

    "So I scoured the library, eventually finding Luis sat at a tucked away window seat, staring off into the Manila skyline"

    Aurora "Luis..."

    voice "voice/L_2_11_1.mp3"
    Luis "Oh... Aurora... I mean..."

    voice "voice/L_2_11_2.mp3"
    Luis "Oh hello my beautiful Ms. Aurora. Apologies for that unfortunate display. I left to initially find my dearest Celestia and smooth things over."

    voice "voice/L_2_11_3.mp3"
    Luis "But, to be honest I had something to think about. About me and Ms. Celestia. And so, you find me here staring off into the distance."

    Aurora "How, surprisingly, self-reflective of you."

    voice "voice/L_2_11_4.mp3"
    Luis "Haha! You're right Aurora, I'm more than that playboy you fell in love with."

    Aurora "Falling in love... let's not stretch it."

    voice "voice/L_2_11_5.mp3"
    Luis "Haha! Yes, yes, just teasing. You see, Aurora, me and Celestia, we're heirs of two of the country's biggest companies, so naturally our families had gotten to know each other quite well. That includes me and Celestia."

    voice "voice/L_2_11_6.mp3"
    Luis "To tell you the truth, yes, although me and Celestia seem at odds now, we were once two peas in a pod, and perhaps I did like her back then. I miss the carefree and caring Celestia. But as we got older, she took on more and more responsibilities, and she emulated those, frankly, elitist attitudes both our parents held against others."

    voice "voice/L_2_11_7.mp3"
    Luis "In honesty, yes, I do find you cute Aurora, that was no lie. But, I must apologize for using you as my way of trying to re-awaken the Celestia I missed. Perhaps by showing Celestia my disregard for the family's formalities I could have her see the same."

    voice "voice/L_2_11_8.mp3"
    Luis "But, unfortunately, despite my best efforts, not just with you mind you, she has yet to drop her guard. And now, she stormed off in a way I never expected..."

    voice "voice/L_2_11_9.mp3"
    Luis "Hrm... I'm sorry for my rambling. Thank you for coming for me, but I am ok now. But perhaps, I do have advice to ask of you Ms. Aurora..."

    voice "voice/L_2_11_10.mp3"
    Luis "I believe I crossed a line with my dear Celestia, one I cannot go back on. I suspect she thinks only the worst of me and I cannot recover my relationship with her. What do you think I should do?"

    menu:
        "No Luis, it's not your fault. She slapped me!":
            jump route111
        "I'll support you Luis, now that I know the real you.":
            jump route112
        "You can still make things right with Celestia.":
            jump route113

label route111:
    Aurora "No Luis, it's not your fault. She slapped me! Yes, maybe you overstepped a little bit, but she slapped me!"

    "Luis looks at me taken aback with a seriousness behind it. His earlier warmth now surprisingly seemingly turning cold"

    voice "voice/L_2_111_1.mp3"
    Luis "I'm sorry Aurora, that was imprudent of me to ask you. You must also be somewhat emotional with what happened. I imagine that was not the best impression of Celestia, but I will reassure you, despite our lovers' spat, I love that woman deeply."

    Aurora "Luis? I thought..."

    voice "voice/L_2_111_2.mp3"
    Luis "We should go back, before they misinterpret us spending time together..."

    "Suddenly, Luis, visibly uncomfortable, swiftly heads back towards the study room. I quickly rush after him to catch up, with difficulty." 
    
    scene studyroom
    
    "The rest are already back, with Celestia looking serious, and what appears to be a fierce glare, at me..."

    voice "voice/C_2_111_1.mp3"
    Celestia "Ohmy, what do we have here, if it isn't..."

    voice "voice/L_2_111_3.mp3"
    Luis "Celestia, I have to apologize..."

    "The serious face Luis had previously shown me turned into one of deep regret, fixed towards the growingly stern face of Celestia."

    voice "voice/C_2_111_2.mp3"
    Celestia "Ohmy... Luis... I... What did you do to him Aurora!"

    Aurora "I... I..."

    ## Smack SFX Maybe
    "Smack!"

    "A second sharp pain today, once more on the same cheek. It stings, but all I can seem to focus on is Celestia's composure utterly gone with a mix of pain, sadness, confusion, and regret."

    voice "voice/C_2_111_3.mp3"
    Celestia "I... I... I... don't know anymore... If you want Luis that bad... I can't..."

    voice "voice/L_2_111_4.mp3"
    Luis "No! Love... it's not that... I'm sorry. I'm sorry for taking you for granted. I'm sorry for not thinking about your feelings. I'm sorry for breaking your heart all these years... I'm sorry..."

    "And with that, Celestia wraps her arms tightly around Luis, both of them crying. A silence in the room that no one dared to break... But for me, I feel mixed... How can this woman, who slapped me? Who made Luis cry... Be the one to cry? Is there something more that I am missing?"

    "We decided to disband for the day. Too much had gone down. For some reason, as our sessions continued, I felt more and more disconnected. At first it was just the couple, they seemed stronger than ever, but they seemed to pay less attention to me. Anthony and Jonathan followed, apparently Celestia, who I thought despised Anthony, had invited them on a few occasions and so they grew closer to her and further from me."

    "And as for Rafael... At first, he did try to talk to me... But as the atmosphere of the group turned more and more cold, Rafael decided to leave on his own. I too decided to leave..."

    return

label route112:
    Aurora "I'll support you Luis, now that I know the real you. Not the playboy you, but the thoughtful you who cares little for the formalities despite your status."

    voice "voice/L_2_112_1.mp3"
    Luis "Thanks Aurora. That makes me really happy, to know that, despite all that's happened, and me being admittedly rough around the edges, you'll back me."

    Aurora "Of course Luis..."

    "Luis' face turns warm, a genuine warmth I had never seen on his face before. You can tell, this was no act of his, he is genuinely grateful to you... And you feel likewise grateful to him..."

    voice "voice/L_2_112_2.mp3"
    Luis "Aurora! Look, can you see those clouds? They look beautiful, beautiful like you. Haha! Sorry, only teasing. Seriously though, I'm grateful to have you."

    "As the two of us stared off into the clouds for only a few moments which felt like an eternity together, we decided that it was about time to go back to the room. Celestia, with puffy eyes, seems to have been comforted by the rest of the group..."

    scene studyroom

    voice "voice/L_2_112_3.mp3"
    Luis "Celestia... I'm sorry..."

    voice "voice/C_2_112_1.mp3"
    Celestia "Luis... I... I... I'm sorry... I..."

    voice "voice/L_2_112_4.mp3"
    Luis "It's ok Celestia... I'm the one who should apologize. I played with your heart by pretending to like Aurora and not looking at you for who you are. And because of that... I hurt you... I am deeply sorry for what I've done and I cannot make it up to you... I am sorry."

    voice "voice/A_2_112_1.mp3"
    Anthony "Yes Luis, you should be sorry. You made your fiance cry. Cry!? You should be ashamed of yourself as a man, no... as a person! You should..."

    voice "voice/C_2_112_2.mp3"
    Celestia "Anthony... that is enough... Thanks to you, I... I... get it now. Luis... I'm sorry. I'm sorry I was so stubborn and didn't let myself see you for who you are, for what your heart was saying all this time. I think... it's best we call off the engagement..."

    "With that, Luis' face darkens, the woman who he cared for called their engagement off..."

    "A silence filled the room, a mournful silence. We decided to end today's session. We've gone through a lot already. As days passed, Luis would come to me, his heart broken, he was the one to tell me that the cancellation of their engagement was final."

    "As days turned to weeks, the study group disbanded. At first it was Celestia and Anthony. I think Celestia couldn't bear the heartbreak of seeing Luis again, and Anthony was supporting her. Then it was Rafael and Jonathan, they silently left too, I think, to join a different study group, perhaps with the extra baggage we carried they opted to take a step back."

    "As for me, I stayed behind to support Luis, like I promised that beautifully cloudy day..."

    return

label route113:
    $ went_route_113 = True
    Aurora "You can still make things right with Celestia, let's look for her."

    voice "voice/L_2_113_1.mp3"
    Luis "Do you really think so?"

    Aurora "Yes! Let's find her. With what I know now, I think you can give her the earnest apology she needs so you can both feel better."

    voice "voice/L_2_113_2.mp3"
    Luis "Ok, if you're sure. I'll do anything for my dear Celestia. And if it means opening my heart to her now, it will have to do."

    "And so me and Luis set off to find Celestia. We found her curled up in a hidden away aisle. Luis surprises her with a comforting hug and they have a heartfelt chat. I suspect they would appreciate the privacy, so I decide to leave them and return to the room alone, Jonathan had already gotten back. A few moments pass and with puffy eyes which looked like they had been thoroughly cried out, Celestia and Luis return to the room arm-in-arm."

    jump scene3

label route12:

    scene library

    "I looked throughout the library, and eventually stumbled into Celestia curled up in a random hidden aisle of bookshelves where she would be undisturbed. I approach her with caution... she is crying."

    Aurora "Celestia?... I hope I am not intruding."

    voice "voice/C_2_12_1.mp3"
    Celestia "Oh? Aurora... Well I guess it is too late now to keep up the facade. I'm sorry about the cheek..."

    "Celestia looks at me with a dejected look, it is one of sincerity and regret but also of pain."

    voice "voice/C_2_12_2.mp3"
    Celestia "I'm sorry about all that drama. To be honest, I think I got a bit too wound up with Luis. I'm sorry about being so protective about him. To be honest, I love that man way too much, and to be honest, more than he really deserves, but he is my light and I love him for it."

    voice "voice/C_2_12_3.mp3"
    Celestia "When each of our families started giving the two of us more responsibilities, I took on the brunt of the serious tasks out of obligation, and Luis, well... At first I found it charming that he was as carefree as ever. But eventually, I got frustrated at him, most especially with his playboy act. I know it's just an act but it hurts y'know."

    voice "voice/C_2_12_4.mp3"
    Celestia "And to be honest, I wish I could just escape this responsibility I found myself in. Carrying the responsibility of essentially both our families... not to mention being afraid of losing Luis... I just wish... he could just... be on my side..."

    menu:
        "Well, it's not too late to tell him that.":
            jump route121
        "He failed you Celestia, I think you should choose yourself.":
            jump route122

label route121:
    $ went_route_121 = True
    Aurora "Well, it's not too late to tell him that. That you need him. You can let down your refined facade and tell him honestly how you're hurting"

    voice "voice/C_2_121_1.mp3"
    Celestia "But... but... but... I guess... I can..."

    "Celestia takes a deep breath and her face changes to one of conviction"

    voice "voice/C_2_121_2.mp3"
    Celestia "You're right Aurora, it's not too late... I've been so preoccupied with putting up looks, making us look like a power couple, that I didn't consider starting with being honest with Luis. Let's go, I know just where that buffoon is sulking."

    "So Celestia promptly leads me to a secluded window seat, with determination behind her puffy red eyes. And like on cue, she finds Luis, dejected, and elegantly grasps his hands. They seem to start a heartfelt conversation, one I decide not to intrude on."

    scene studyroom

    "I return to the study room, where the rest remain quietly seated, perhaps unsure about the turnout of events. But I, I'm confident those two will be able to make up. And as a few moments pass, the power couple walks in, with puffy red eyes and arms linked tightly."

    jump scene3

label route122:
    Aurora "He failed you Celestia, I think you should choose yourself for once."

    voice "voice/C_2_122_1.mp3"
    Celestia "Sigh... I guess you're right. I've spent years trying to get him to notice me, to realize how much I care, and he never fails to tire me out... I'll give it a thought Aurora, I care for him oh so deeply, but he wont look my way..."

    "We sit there in silence for a moment. Celestia looks mournful but determined, it appears she really is thinking through what I said. After a moment, she stands up and we walk back to the room in silence. The weight is heavy in the air as we make it back to the room with Luis nowhere in sight."

    scene studyroom

    "Everyone sits in the silence for what feels like ages, until eventually Luis walks into the room with a bright confidence on his face, obviously fake, his eyes red much like Celestia's from crying."

    voice "voice/C_2_122_2.mp3"
    Celestia "Luis... drop the act..."

    voice "voice/L_2_122_1.mp3"
    Luis "What act do you mean love?"

    "Unlike Celestia, whose face is filled with a gentle concern towards Luis, I can only look at him in disappointment and disapproval. I speak with a coldness I didn't know I had"

    Aurora "Luis... that's enough."

    "A silence blankets the room once more. Moments pass, and Luis' voice breaks it..."

    voice "voice/L_2_122_2.mp3"
    Luis "Sigh... Ok, I guess I wont pretend anymore... I screwed up and I..."

    Aurora "No... Luis... You failed her, you..."

    voice "voice/C_2_122_3.mp3"
    Celestia "No, it... it's alright Aurora..."

    voice "voice/L_2_122_3.mp3"
    Luis "I'm deeply sorry Celestia... I... I... was a buffoon to play with your feelings like that. I... I know I do not deserve your forgiveness and am ready for whatever I must do to earn back your trust and I..."

    voice "voice/C_2_122_4.mp3"
    Celestia "No, it's alright Luis. I understand. Aurora made me realize that I cannot let myself be so easily hurt..."

    voice "voice/C_2_122_5.mp3"
    Celestia "And so... I have to apologize... I... I think... I... I have to call off our engagement... for both our sakes..."

    "And with that Luis breaks down in tears. A broken face I didn't expect to see. Celestia too, her face holding back tears which couldn't help but flow from her eyes, now hugging the sobbing Luis. I do not know why Celestia hugged the man who failed her... But it is not for me to tell her what to feel."

    "A lifetime seemed to pass as the two cried, with the room in silence, everyone unsure of what to do. Eventually, the group disbanded for the day."

    "Afterwards, I saw little of Luis, he no longer showed up at our study sessions. Celestia was visibly heartbroken for quite some time. But I think it was for the best. It was me and Anthony who would comfort her during this time. At some point, the two of them would spend more time together."

    "I couldn't help but think something went wrong then. I couldn't place it exactly. Celestia did regain her happiness, thanks to Anthony for the most part. But, something felt missing for quite some time..."

    return

label route13:

    scene library

    "Me and Jonathan went together looking for the two."

    Aurora "Jonathan, do you think it was my fault? Maybe I should have turned down Luis' advances early on? But I just couldn't. I was just too shy... and to be honest it felt good to be noticed for once."

    voice "voice/J_2_13_1.mp3"
    Jonathan "Well... I wasn't in the middle of everything, so I can't say for sure, but do you think you were making the situation worse?"

    Aurora "Well... no... not exactly. I did enjoy being noticed for once, and was honestly starstruck at the two, them being big names in business. But, I didn't want Luis to approach me like that, especially with how Celestia was reacting.."

    voice "voice/J_2_13_2.mp3"
    Jonathan "Yes, exactly, it wasn't your fault Aurora, they had some tension already existing and you just got in between them. It wasn't your fault at all."

    Aurora "You... you have a point Jonathan but there's just this feeling I can't shake..."

    voice "voice/J_2_13_3.mp3"
    Jonathan "Oh? Is it some kind of frustration? That things played out this way? That their lover's quarrel got you involved?"

    menu:
        "Yes, to be honest, I'm frustrated at both of them.":
            jump route131
        "No, I think I honestly feel sorry for them.":
            jump route132

label route131:
    $ went_route_131 = True
    Aurora "Well, to be honest Jonathan, I'm frustrated at both of them. I understand they have their own issues, but I don't want to be caught in the crossfire, I'm just an ordinary girl."

    voice "voice/J_2_131_1.mp3"
    Jonathan "Well, you're justified in feeling that way, but you never know what's going on in their heads or what history they might have. I guess we can only really just look for them for now."

    "And so, we continued to search for them for quite some time. All that I could think about was slap, the flirting, and the messiness of my own heart. I did not understand those two. I could not understand those two, afterall, they were in a world nowhere near mine."

    "We eventually gave up and made our way back to the room. It looks like both Celestia and Luis had already returned and the rest of the star-studded cast were able to talk to them."

    jump scene3

label route132:
    $ went_route_132 = True
    Aurora "Actually, I think I feel sorry for them, Jonathan. Yes, they may be so amazing and prestigious, much more amazing than me. But, they're just human too, with messy, vulnerable feelings."

    voice "voice/J_2_132_1.mp3"
    Jonathan "Yes, you're not wrong there. To be honest, I think I'm in the same boat as you, frankly pretty normal compared to the star power that is those two, not to mention both that hotshot Anthony and the genius that is your childhood friend."

    Aurora "Haha! You're not wrong there. We really are two average people in the middle of a star studded cast. But, despite that, they're just as human as we are."

    voice "voice/J_2_132_2.mp3"
    Jonathan "And that's why we have to find the two of them."

    "We put in our best effort to find Luis and Celestia. We eventually stumble into the two of them, they seem to have made up while we were looking for them. I can see they both had eyes red with tears."

    "Me and Jonathan finally catch their attention and beckon them over. The four of us walk in silence as we make our way back to the room."

    jump scene3

label route2:
    Aurora "Actually, can you stay here Anthony?"

    voice "voice/A_2_2_1.mp3"
    Anthony "Uh? Me? Uhm... ok why?"

    voice "voice/R_2_2_1.mp3"
    Rafael "Actually, I agree, I think you're the best bet if the two of them make it back before me and Jonathan can find them."

    voice "voice/A_2_2_2.mp3"
    Anthony "Well, uhm... Sure, I guess, I'll just sit here with Aurora. Do your best you two."

    voice "voice/R_2_2_2.mp3"
    Rafael "But don't try to do anything funny with Aurora ok?"

    "With that, Rafael leaves the room with a determined look, with Jonathan tailing meekly behind him"

    voice "voice/A_2_2_3.mp3"
    Anthony "Phew... to be honest Aurora, I didn't know what we should do there. Wait. Should I have gone instead? Does that make me a bad friend that I stayed behind so easily?"

    Aurora "Anthony??"

    voice "voice/A_2_2_4.mp3"
    Anthony "Ah. Sorry, the overthinking always gets me. I know I'm a hotshot model and athlete but that's all I'm good for. When it comes to studying or even being a friend I don't think I manage too well."

    Aurora "What are you saying Anthony?"

    voice "voice/A_2_2_5.mp3"
    Anthony "Well, to be honest, I only entered business school cause it was the only scholarship I could get. My school has a tie up with the university you see, coming from a small school makes your opportunities a lot more limited. And, to be honest, I'm way out of my depth here. I realized that in my first year. And, being here in this study group, to be honest, has been a reality check for me that I have to step up my game even harder."

    Aurora "Oh? I think you should have more confidence in yourself Anthony, I mean, you made it here after all."

    voice "voice/A_2_2_6.mp3"
    Anthony "Well, I did make it here, but like Rafael said, it's only the first step. Look at Celestia and Luis, they have so much confidence too, I'm jealous honestly. I don't think I can keep up. I'm just barely hanging on to a Dean's honors. Not to mention, I'm not doing as well as I was in high school in both modeling and athletics. I'm failing Aurora."

    Aurora "No Anthony, that's not failing, you're actually doing really well with all you're juggling."

    voice "voice/A_2_2_7.mp3"
    Anthony "But I'm not enough Aurora. I used to not have to try so hard. But now, I do, that's what I get for slacking off in high school. Now, I can't get the results I need, and the effort I put in, it's useless if I don't get results."

    Aurora "But you don't have to get results."

    voice "voice/A_2_2_8.mp3"
    Anthony "But results are what make people care about you, Aurora. If I can't get results then I'm worthless..."

    menu:
        "But I care for you Anthony.":
            jump route21
        "I'm sure the others care.":
            jump route22
        "Results don't matter!":
            jump route23

label route21:
    $ went_route_21 = True
    Aurora "But I care, Anthony! I know we only met today, but I'm amazed by who you are. Upbeat, outgoing, hardworking, caring, you have a heart of gold! And I know it's a bit forward... but, I admire you Anthony."

    voice "voice/A_2_21_1.mp3"
    Anthony "You admire me?"

    Aurora "Yes! I admire you Anthony! And despite what is going on, I want to be with you."

    voice "voice/A_2_21_2.mp3"
    Anthony "With me? Do you mean?"

    "Anthony's face inches closer to mine, his hand caressing my cheek which he held so caringly only a few minutes earlier. I can feel his breath, I can feel my heart."

    "But as he leans in, Luis and Celestia walk arm-in-arm with Rafael and Jonathan tailing them. They're eyes are slightly puffy from what looks to be crying."

    jump scene3

label route22:
    $ went_route_22 = True
    Aurora "Anthony... I'm sure the others care."

    voice "voice/A_2_22_1.mp3"
    Anthony "What do you mean?"

    Aurora "I mean Anthony, the fact that Celestia spent so much time trying to teach you and that Rafael trusts you enough to be here with me. I'm sure they can see how good of a heart you have."

    voice "voice/A_2_22_2.mp3"
    Anthony "Oh, well... I guess you're right. I guess I backed myself into a corner thinking I have to ace everything. But really, I guess I'm glad that I can be friends with such amazing people."

    "And as Anthony looks at me with a meek smile that contrasts starkly against the bravado he showed earlier today. Luis and Celestia walk in, arm-in-arm, their eyes visibly puffy after what looks like a long making up. Rafael and Jonathan follow after them."

    jump scene3

label route23:
    Aurora "But results don't matter Anthony!"

    voice "voice/A_2_23_1.mp3"
    Anthony "What do you mean?"

    Aurora "I mean, in the grand scheme of things, these results don't really matter."

    voice "voice/A_2_23_2.mp3"
    Anthony "What do you mean my results don't matter Aurora?"

    voice "voice/A_2_23_3.mp3"
    Anthony "Are you saying my efforts are wasted? Are you saying I'm a waste? That this is all a farce? That my time as a model is pointless? That my athletics are pointless? That my studies are pointless? Well, Aurora, you know what..."

    "And while Anthony's previously grief stricken face boils over into what looks to be some kind of boiling frustration with me, one I want to apologize for. Celestia storms in with Luis and the rest quickly tailing after her, Luis' face is clearly grief stricken."

    voice "voice/C_2_23_1.mp3"
    Celestia "Oh look who we have here... Ms Aurora, making her moves on Anthony this time I see!"

    voice "voice/L_2_23_1.mp3"
    Luis "Celestia! That's crossing the line! You crossed the line when you slapped her! Don't talk to Ms. Aurora like that!"

    voice "voice/C_2_23_2.mp3"
    Celestia "Ms. Aurora this. Ms. Aurora that. I don't know if she is a mastermind in emotional manipulation or if she is just a dense inconsiderate 'good girl.' But..."

    "Celestia's face is covered with an expression I cannot describe in any words other than disgust. I don't quite understand her reaction. Luis steps in between me and Celestia, as though to protect me."

    voice "voice/L_2_23_2.mp3"
    Luis "Celestia! You're being unreasonable! Can you stop..."

    "Suddenly, Anthony pushes me aside to defend Celestia from Luis, his face utterly boiling over."

    voice "voice/A_2_23_4.mp3"
    Anthony "Can it Luis! I don't know why you got the hots for Aurora, she's anything but charming. I for one agree with Celestia. This girl is a problem, and she's inconsiderate. Frankly she's..."

    "And as Anthony and Luis take a staredown which looks only like a fight coming, Rafael meekly sandwiches himself between the two of them."

    voice "voice/R_2_23_1.mp3"
    Rafael "Can you guys stop... Anthony! Celestia! Luis! Can you please just..."

    "And as Rafael says that, everyone comes to their senses and a silence blankets the room like a thick fog. Celestia is the first to leave. Followed by Anthony. Luis follows. Then Jonathan. Rafael turns to me trying to say something, but he hesitates."

    "I received a text, a reassignment to a different study group... I do not know where the rest were reassigned and I hear nothing of them again... Did I do something wrong?..."

    return

label route3:
    Aurora "Uhm... Ok... I'll stay here with Rafael."

    "Promptly, Anthony drags Jonathan along as they look for Luis and Celestia. Leaving me and Rafael in the room with an awkward silence, one that I didn't expect sitting here with my grade school best friend. Rafael's voice pierces the silence."

    voice "voice/R_2_3_1.mp3"
    Rafael "Hey, uhm. Aurora. I'm sorry, I think I got a bit worked up earlier."

    Aurora "I'm sorry? You? Got worked up? The coolest and most calm guy I know? I didn't even notice."

    voice "voice/R_2_3_2.mp3"
    Rafael "Yes Aurora, I think I did. To be honest, I.. I think I always get worked up... especially when it comes to you."

    Aurora "What do you mean?"

    voice "voice/R_2_3_3.mp3"
    Rafael "Well... To be honest Aurora, you're the only person I think I can feel comfortable with, ever since we used to study together. I'm always supposed to keep up this unaffected mask. Be it studies or socializing, people know me as the cool guy but I don't know how to get out."

    Aurora "Well, you are the cool guy. Remember all those girls who fell for you back in high school? We couldn't hang out much once that started happening. To be honest I missed our study chats. Haha!"

    voice "voice/R_2_3_4.mp3"
    Rafael "Well.. I'm glad you think that of me, Aurora, but.. I'm more than just the cool guy.. nor.. the smart guy. And no, I don't care about what those girls in high school thought."

    Aurora "What do you mean?"

    voice "voice/R_2_3_5.mp3"
    Rafael "I missed our chats in grade school, our friendship even. I missed being able to connect with you, and only you."

    voice "voice/R_2_3_6.mp3"
    Rafael "Remember the time we stayed up late studying for our science exam? The time you helped me out with my Filipino homework? The time I helped you with math, though you complained that you still hated math and look where you are! Now you're in business school."

    voice "voice/R_2_3_7.mp3"
    Rafael "How about the time you came to visit me in the hospital when I got sprained, or the time I visited your home when you were sick. We even played so many games together in between our study sessions. Those memories... They mean the world to me."

    voice "voice/R_2_3_8.mp3"
    Rafael "I never wanted to be the cool guy, Aurora, or rather... I became the cool guy for someone. And.. I hoped that someone would notice me and maybe fall for me. But, instead, it pushed her away."

    Aurora "Rafael?"

    voice "voice/R_2_3_9.mp3"
    Rafael "Yes, Aurora, this facade I'm putting up, I don't want to be like this anymore. Luis and Anthony showed me that I can't just sit back and watch. I have to make a move."

    Aurora "Wait... You like someone, Rafael?"

    "Rafael looks deeply into my eyes with a renewed conviction"

    voice "voice/R_2_3_10.mp3"
    Rafael "Yes, Aurora, I do like someone..."

    Aurora "Oho... Who... is uhm... who is she?"

    voice "voice/R_2_3_11.mp3"
    Rafael "You Aurora, I like you... I've loved you through all of our memories together."

    menu:
        "Me? Sorry Rafael, but we're just friends.":
            jump route31
        "Me? Well... I... I love you too.":
            jump route32
        "Me? But, it's been so long.":
            jump route33

label route31:
    $ went_route_31 = True
    Aurora "Me? Sorry Rafael, but we're just friends... I don't want to do anything that would damage our friendship. I'm not ready yet and I..."

    "Rafael's face darkens, the conviction which I had seen earlier disappears"

    voice "voice/R_2_31_1.mp3"
    Rafael "Ah... I see. You don't have to explain. I understand, we haven't kept contact in so long and I guess our relationship has always been as friends. Haha!"

    Aurora "I'm sorry Rafael, I... I..."

    voice "voice/R_2_31_2.mp3"
    Rafael "Don't worry about it Aurora. I just said that to get it off my chest, so.. don't be too worried about me."

    "And as I look at Rafael's normally calm face, still calm but somehow broken, I cannot help but feel sorry. Celestia and Luis walk in with puffy red eyes that seem to have come from a long heart-to-heart."

    jump scene3

label route32:
    $ went_route_32 = True
    Aurora "Me? Well... I... I love you too. I have for a while now actually."

    "And as I say that, I can feel my heart racing, my cheeks warming up, and a gladness I could not describe. I just confessed to Rafael, the boy, no man, who cherished the memories I also cherished."

    "His cool facade falls, and all I can see is his caring face, the face of the childhood friend, who I loved."

    voice "voice/R_2_32_1.mp3"
    Rafael "Aurora, I promise you, I love you... And I will protect you, despite my shortcomings."

    "And as our faces draw close together, staring longingly in each others' eyes like a stillshot moment in a romance movie, suddenly Luis and Celestia walk in, arm-in-arm, with visibly puffy eyes after what seems to have been an equally meaningful make up between them. Anthony and Jonathan tail closely after them."

    jump scene3

label route33:
    $ went_route_33 = True
    Aurora "Me? But, it's been so long since then Rafael. A lot has changed."

    voice "voice/R_2_33_1.mp3"
    Rafael "I know Aurora. But those memories mean the world to me. You mean the world to me. And if it means making new memories together, then... I will do everything I can."

    "With a face of conviction I was surprised to see on Rafael for the first time I could remember, I can't help but feel grateful to know him. And with that fleeting moment passing, Celestia and Luis walk in with puffy red eyes that seem to have come from a long heart-to-heart."

    jump scene3

label scene3:

    scene studyroom

    voice "voice/L_3_1.mp3"
    Luis "So... yes, hello everyone. Uhm... Me and Celestia. We... patched things up. Apologies for that uhm... fiasco."

    voice "voice/C_3_1.mp3"
    Celestia "Yes... We... Uh... We let the emotions we had pent up for years build up... And it kind of exploded. Our sincerest apologies."

    voice "voice/L_3_2.mp3"
    Luis "And... Aurora. I must apologize first and foremost for playing with your emotions. I did not mean to play with your heart."

    voice "voice/C_3_2.mp3"
    Celestia "And I... I am really truly sorry for slapping you Aurora. I lost my composure and lashed out."

    if went_route_113:
        jump end113
    if went_route_121:
        jump end121
    if went_route_131:
        jump end131
    if went_route_132:
        jump end132
    if went_route_21:
        jump end21
    if went_route_22:
        jump end22
    if went_route_31:
        jump end31
    if went_route_32:
        jump end32
    if went_route_33:
        jump end33

label end113:
    "I look to Luis glad I was able to be a bridge between the two of them"

    Aurora "Luis, Celestia, I accept your apologies."

    voice "voice/L_3_113_1.mp3"
    Luis "I hope we can all be good companions from this point onwards. Aurora, you were truly a good confidant and friend to me."

    voice "voice/C_3_113_1.mp3"
    Celestia "Yes Aurora, thank you. I... again... am truly sorry."

    "And without thinking, I give Celestia a tight hug as if acknowledging her pain. Luis is looking over our shoulders glad. I hope this can be the start of a truly powerful friendship with everyone. Looks like I did achieve my goal of making friends afterall, despite the chaos that is..."

    return

label end121:
    "I look to Celestia glad I was able to be a bridge between the two of them"

    Aurora "Celestia, Luis, I accept your apologies."

    voice "voice/L_3_121_1.mp3"
    Luis "Thank you Aurora. I truly did come short, but I am grateful to you and my dear Celestia for putting both your faiths in me."

    voice "voice/C_3_121_1.mp3"
    Celestia "Thank you Aurora. I misjudged you. Without you... You really saved us. Thank you..."

    "And without thinking, I give Celestia a tight hug, grateful. Luis is looking over our shoulders glad. I hope this can be the start of a truly powerful friendship with everyone. Looks like I did achieve my goal of making friends afterall, despite the chaos that is..."

    return

label end131:
    Aurora "I... I... uh..."

    "I did not know where this was coming from. Could they be pulling my leg? Did they pull theatrics? I didn't quite understand. And as I stood there honestly confused, perhaps my face gave me away."

    voice "voice/A_3_131_1.mp3"
    Anthony "Aurora? Are you ok?"

    "Anthony's face was concerned. I looked to Rafael, to everyone, even to Jonathan. They were all concerned. Do they not realize just how weird this all is?"

    "Moments that felt like lifetimes passed and I did not know what to do. I decided to just leave, an ordinary girl like me probably couldn't understand them anyway. And with that, I decided to go back to my tried and tested method of not drawing attention to myself anymore. I tried to make a splash but it wasn't for me afterall."

    return

label end132:
    Aurora "I... I... uh... appreciate it you guys... and I accept your apology."

    "And with that, all the tension left me and the others. Everything was relieved, I guess even the most prestigious cast you could find really were just people like me and like Jonathan. At that moment I thought to myself, why did I ever think they were any different from me? They were people afterall."

    "Holding that thought in my heart, I lived each day from then on grateful to have these people as study mates. I was grateful for their humanity. I was grateful for them as people. And I am grateful that I got to meet these people for who they were..."

    return

label end21:
    "And as those two extended a sincere apology, I couldn't help but look to Anthony for advice. His face was staring back at me with such care and gentleness you wouldn't expect from such a fiery person."

    voice "voice/A_3_21_1.mp3"
    Anthony "Go ahead..."

    "With a deep inhale, and for a split second realizing I had somehow confessed to Anthony just moments earlier, I put my best foot forward to Luis and Celestia"

    Aurora "Thank You! I appreciate your sincere apology."

    "Laughing, Anthony motions to pat my back quite forcefully, softens his pat and lands his arm on my shoulder. I couldn't help but think about the warmth coming from him."

    voice "voice/A_3_21_2.mp3"
    Anthony "Hahaha! You don't have to be so formal! Haha!"

    "And with that, and me now completely distracted by Anthony's musky but surprisingly warm and complex cologne he had on, we continued our study session renewed and glad. Me and Anthony would pair up for the rest of the session, secretly excited to get to talk about things besides studies once the session was over."

    "Once the session finished, Anthony invited me to his varsity training that he was going to. Of course, I said yes. Excited, I followed his lead, we would chat and talk about all sorts of things, from his childhood to mine, to our favorite restaurants in the area, and so on."

    "And as the Golden Hour set in, I couldn't help but think how grateful I was that I took a chance..."

    return

label end22:
    Aurora "Guys... I... I.. uh... Really appreciate your..."

    "And as eek out accepting their apology, Anthony suddenly pushes past me and hugs the two tightly"

    voice "voice/A_3_22_1.mp3"
    Anthony "Guys! Hahaha! I'm glad! Hahaha!"

    voice "voice/C_3_22_1.mp3"
    Celestia "Hey! Wait! Where are you..."

    voice "voice/L_3_22_1.mp3"
    Luis "Hahaha! Anthony! Haha! I... I... can't breathe!!!"

    voice "voice/A_3_22_2.mp3"
    Anthony "I'm so glad I have you guys!!! Just moments earlier I thought I was useless! But now... I'm so grateful to have friends! I love you guys!!"

    voice "voice/C_3_22_2.mp3"
    Celestia "Arghhh..."

    voice "voice/L_3_22_2.mp3"
    Luis "Arghhh...."

    Aurora "Anthony... I... Uh... I think you should let them go..."

    "And with Anthony ignoring me and maybe even hugging Celestia and Luis even tighter, and with Rafael and Jonathan stepping nowhere close to Anthony lest they also get bearhugged. I laugh to myself, grateful we were able to resolve our difficulties."

    "They say that we have to present our best selves to others, but I imagine, it's in presenting our worst selves that we learn who we can really rely on..."

    return

label end31:
    "I look at Celetia's tired and grief stricken face. I turn to Luis who is equally drained. I linger looking at Rafael's silently broken facade. I too feel tired."

    Aurora "I... I accept your apology... I hope... we can all still be good friends."

    voice "voice/R_3_31_1.mp3"
    Rafael "Friends... right..."

    "Rafael's facade, which had initially hidden his feelings, began to crack."

    voice "voice/A_3_31_1.mp3"
    Anthony "Rafael? Dude? Are you... ok?"

    voice "voice/L_3_31_1.mp3"
    Luis "He must be. He got to spend some quality time with his childhood love..."

    voice "voice/R_3_31_2.mp3"
    Rafael "... I've had enough with all of you... Luis, Anthony... I... I wish... I could be like you. And... Aurora... I think... it was nice spending some time with you after all this time, goodbye."

    "And with that, Rafael left the room melancholic, his eyes empty, his face blank. I could tell, he was holding all his insecurities in too keep up what little facade he could keep. He looked so serious that no one dared to try to stop him."

    "We decided to disband for the day, we were all so emotionally drained, though I felt the weight of Rafael's last words to me. Did I say something I shouldn't have? Was there something I didn't understand?"

    "Days passed, the group got back together for another session, with renewed energy we were all able to make amends fully. Rafael did come but he has disconnected, maybe tired?"

    "Weeks passed, we had more and more study sessions, even meetups outside of studying too! Though, Rafael showed up less and less, and eventually he just faded away."

    "At first we were concerned, eventually we lost hope, he never did respond to our attempts of contact. Then we forgot. We were happy, but in my heart of hearts I always wondered if things could have played out differently for my childhood friend."

    return

label end32:
    "In that moment, I felt a genuine sense of relief. Though things got rocky and unsure, things were able to work out in the end. And as I turn to Rafael, feeling my cheeks and my racing heart, realizing we had just confessed moments ago, he gazes back at me with a loving smile."

    voice "voice/R_3_32_1.mp3"
    Rafael "Aurora... I'm glad we ended up with these people... And I'm glad we ended up together..."

    "With a warm and fuzzy feeling deep in my heart, coming from the feelings I felt towards the coolest guy I know. I felt a deep sense of gladness that we ended up in this study group together..."

    return

label end33:
    "I look towards Celestia, unsure of myself. Then towards Rafael beside me, a face filled with a newfound determination, and I find in him newfound confidence in myself. That I was acknowledged by both Luis and Celestia, that I had been remembered all this time by even someone as amazing as Rafael."

    voice "voice/R_3_33_1.mp3"
    Rafael "Aurora...? What are you staring at me for? I... I... Uhm... I think you should accept their apology. And, once you do, we can all keep making memories together."

    voice "voice/L_3_33_1.mp3"
    Luis "Oh? Mr. Cool getting a little bit sentimental? Well... We truly are sorry Aurora."

    "And with that, I decided to accept Luis and Celestia's apology. Remembering my memories with Rafael, though having been a long time ago, only left me with the wish to make many more memories with my newfound friends."

    return
