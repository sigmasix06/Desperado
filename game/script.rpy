define j = Character("Juarez")
define i = Character("Ivan Ivanov, Professional Guard")
define p = Character("[player_name]")
define g = Character("Shop Guard")
define s = Character("Shopkeep")
label start:

    play music "audio/ambient.mp3" volume 0.75
    play sound "audio/trucksound.mp3" volume 0.5

    scene none

    "Prologue: The Journey"

    scene bg harper

    j "We've arrived at Harper's. After coming through here, it should only be a slight more distance to the capital."

    j "How are you doing back there? I never got your name, buddy. What is it?"

    screen enterName:
        vbox:
            xalign 0.5
            yalign 0.5
            text "What is your name?":
                size 20
            input default "":
                pixel_width(500)
                value VariableInputValue("player_name")
            textbutton "OK":
                action Jump("continue")
                keysym('K_RETURN', 'K_KP_ENTER') 
    "Ah? Oh, my name is..."
    scene none
    $ quick_menu = False
    $ player_name = ""
    show screen enterName
    $ ui.interact()
return
label continue:
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Veteran"
    hide screen enterName
    $ quick_menu = True
    $ _skipping = True
    scene bg harper st
    p "It's [player_name], sorry for not telling you sooner."
    p "Why are we stopped in Harper's? Thought we were making a beeline towards the capital?"
    j "Well, there is a Republic checkpoint up ahead and we are stopping to make sure our goods are in order. Can't have trouble with the URA, not with the current tensions between them and the Empire."
    p "Ah, I see. Well, thanks for checking up on me. I'll just be taking a nap while I wait for the convoy to begin again."
    "You climb back into the truck bed, and as you are getting back in, the guard sitting next to you asks:"
    i "What is your name, friend? It seems to haf passed my mind to ask."
    p "Ah, its [player_name]."
    i "That is great name! You must be war-hero with how rugged you are. That would explain missing arm!"
    p "Well, I don't think warhero is an apt term for it, "
    "{i}You slowly begin to close your eyes and fall back asleep, trying to get some shut eye during the grueling travel you have undertaken.{/i}"
    scene none
    "You begin to ponder your past experiences, going over the painful time you spent in the Empire's army."
    "You recall the long treks and marches the army went through, travelling from state to state through the old-world. You remember the awful battles with the United Republic of America's forces."
    "You can feel the burning pain, the seering agony from when a legionnaire from the URA took his broadsword and swung it with great fervor, taking your arm with it. You remember the sticky red blood, oozing from your wound."
    "You feel the hatred as you take your revolver and arm directly for his head, pulling the trigger with no hesitation. You can smell the gunsmoke, the burning of gunpowder."
    "You'll never forget the acrid smell of it all, all around you was death and destruction, with you contributing to it. It hits you, that you have been doing nothing with your life."
    "Senseless killing and winning battles was all you knew, and so you took the chance that losing your arm gave you: a chance for redemption. After getting a medical discharge, you took the first caravan out of town, heading to the URA."
    "You're entire goal for leaving the army is to settle somewhere nice, build something, start a family. You wanted to create something for once, instead of just killing everything you touch."
    "Although, firstly, you figured that you needed to get your arm back. So, you set your sights on the URA's capital of Kerry. It was rumoured that a cybernetics maker lived there, and he could fix your arm."
    scene convoy with vpunch
    play sound "audio/explosion.mp3" volume 0.5
    "You are woken with a loud bang, and a massive jolt, as you can feel the convoy speed up. Confused, you turn to the guard next to you."
    p "What is going on? That was no ordinary bump in the road I just felt..."
    i "I haf no idea, my friend. All I hear is explosion, and BAM! The convoy shake! Shook me greatly."
    play sound "audio/explosion.mp3" volume 0.5
    "You hear another explosion go off, around 50 meters behind the convoy. You can see the last truck in the convoy, which is filled with guards, stand up and begin firing at something."
    scene raider
    play sound "<from 0 to 15>audio/gunfight.mp3" volume 0.5
    "You stand up to get a better look at what the guards are shooting at, only to see a raider band with their truck, and a mounted HMG on top of it."
    "They seem to be tearing up the guard unit, and you get the thought of helping them."
    label choiceraider:
        "Should I help them?"
        menu:
            "Yes":
                "You stand up and using your singular arm, reach for your trusty revolver. You can feel the weight of the gun resting in your hand, as you bring it up and aim directly for the head of the gunner."
                play sound "audio/revolvercock.mp3"
                queue sound "audio/gunshot.mp3"
                queue sound "audio/shell.mp3"
                "Taking a deep breath, you slowly steady your hand and pull the trigger. The gun fires, letting loose a loud bang. The bullet catches your mark directly in the head, exactly where you wanted it to go."
                "The driver, now deceased, falls on the steering wheel, turning the vehicle off the main road and directly into a tree. The gunner, shaken by the crash, loses control of the mounted HMG and begins firing randomly."
                play sound "audio/crash.mp3" volume 0.5
                "A stray bullet hits the now leaking oil from the engine compartment, setting the entire vehicle ablaze. The entire crew begins panicking and screaming profanities. Moments later, the car explodes."
                play sound "audio/explosion.mp3" volume 0.5
                jump c1y
            "No":
                "You decide it would be best to let the guards handle the issue, seeing as it is their job and not yours."
                jump c1n

label c1y:
    scene crash
    "You stare in awe at what you have just caused. Unable to comprehend, you stand there just staring, with a dumb look on your face."
    i "Wow! ебать, брат! You are incredible my friend!"
    p "I, uh, thanks I suppose? I really wasn't expecting that much of a show..."
    i "Whatever you were trying to do, thank you for saving our hides."
    "You take a seat back down into your chair in the truck, and let out a breath of relief."
    scene convoy
    "After being so hopped up on adrenaline, you find it hard to get back to sleep and instead decide to just relax for the rest of the trip."
    scene none
    "A couple hours pass in silence, without much happening, besides the occasional wild animal appearing."
    "The caravan comes to a stop outside the final destination, right at the customs checkpoint: Kerry. The capitol of the URA, situated in the exact area where the old city of Washington stood."
    "You get out of the back of the truck and take a look at the scenery. The city proper is on the other side of a bridge, directly above the Potomac River."
    "After taking in the beauty of your surroundings, you decide to go talk to the caravan leader, Juarez."
    scene bg kerry
    p "Hey boss, is this where we part ways? I would like to get your payment sorted before heading seperate."
    j "Oh! [player_name]! Don't worry about payment. Your fancy shooting saved our caravan, or so I was told. Ivan was singing your praises to me just a couple moments ago! Say, you ever think about taking up caravan guarding? You could make a killing-"
    p "I'm gonna cut you off there. No thanks, my travelling days are over. I am trying to get my arm fixed, then settle down somewhere nice. Just hope the URA is safer than the Empire."
    j "Well, between you and me? Not much of a difference. At least the URA doesn't keep slaves."
    p "Yeah, that was certainly one of the reasons I left. We all have our circumstances, and mine were never in my favor. Growing up in the Empire was never easy."
    j "I could only imagine... -well, I'll get out of your hair. Oh, but before you leave, please, take this. I hope you find what you're looking for out here, and may we both survive long enough to meet each other."
    "Juarez hands you pouch with 200 silver coins inside, the URA's official currency. It has the face of one of their many presidents on it."
    p "Likewise. Take care."
    "With your conversation finished, and payment squared away, you head to the customs inspection. You don't know what awaits you inside the city, but you can only hope you will find the cybernetics craftsman, and perhaps a new lease of life."
    jump end 
label c1n:
    scene convoy
    play sound "<from 15>audio/gunfight.mp3"
    "You sit back down and continue to listen to the ongoing gunfight, trying to relax in this tense situation."
    "However, this turns out to be a very bad idea, as immediately as you sit down, the rear truck has been completely destroyed. With the truck out of commission, your truck is the next target."
    "The raider gunner begins to shoot out the truck's tires, leading to the truck driver losing control and running the car off road. With a missing tire, you don't get very far and end up crashing into a nearby ditch."
    "The shock from the crash breaks loose a crate in the truck bed, sending it flying toward your face-"
    scene none
    "And then - nothing. You have gone unconcious, knocked out by the force of the crate hitting your head."
    "When you wake up, you find yourself staring at the sky. You have no sense of time, and don't know how long you've been out. It would appear that everyone else with you in the truck died in the crash, and the truck is now on fire."
    p "Ughhh, pull yourself together, [player_name]..."
    scene crash2
    "You sit up and begin to stretch your limbs. Everything is sore and hurts like hell, but you are determined to not let that get you out for the count."
    "Standing up, [player_name] begins walking, on their long journey to Kerry."
    scene none
    "15 miles down the road..."
    scene storeapproach
    "You've come across a shop in a small town with not many residents milling about. The houses look worn down and in disrepair."
    "As you approach the shop, you notice a guard outside."
    scene storeguard
    g "Hold up, before you go in I gotta pat you down. Do you have any weapons on you?"
    p "Uh, yes? I have a revolver in my holster, but I am not planning to use it..."
    g "Thank you for cooperating, this will only take a second."
    "The guard shakes you down for anything dangerous."
    g "Alright, you're good to go."
    "You walk inside the shop, and check left side of the shop for anything interesting."
    scene storeleft
    "After finding nothing particularly of value, you turn your attention to the shopkeep."
    scene storefront
    s "Hello, dear customer! What can this humble merchant offer you today?"
    p "Hi, I am looking for transport to Kerry, anything coming through here?"
    s "No sir, I am afraid not. We are but a backwater town, no major caravans run through here. Though, I am selling a car if you have the coin!"
    "You ponder for a moment and realize that your revolver is probably worth a fortune, considering it's engraved and a service revolver from the Empire."
    "You take your revolver out of the holster and place it on the counter."
    p "Will you sell the car to me for this?"
    "The shopkeep picks up the revolver and looks at it intensely. After seeing that it is the real deal, and not a fake, the man's eyes go wide."
    s "Yes! You can take the car, and please keep it. Never come back! I don't know where you got this weapon, but I don't care. Just get out of my store!"
    p "Calm down, calm down. I am leaving now."
    "You turn around to leave, and grab the keys the man hands to you."
    "You walk towards where the car was parked, and it seems to be an old Jeep Wrangler, kept in almost pristine condition, save for some cosmetic wear."
    "You hop inside and turn the engine on, shifting into gear, and begin to set off toward Kerry."
    scene carsecured
    "With a car, you can make it rather far in a single day. You relax in the seat and just drive, letting the air flowing by cool you down from the raging summer heat."
    "You drive for miles, through forests and by rivers, for hours."
    "Finally, you have spotted a sign, telling you that you are a mere 2 miles away from Kerry."
    "You can see the city in the distance, it's towering skyscrapers alight with movement and people."
    scene bg kerry
    "Finally, you have made it to your destination. You pull up to the customs checkpoint just a mile outside the city and park the car in the designated spot."
    "AFter an arduous trip and much trouble, you have arrived at Kerry, and you make your way to the customs office..."
    jump end

label end:
    scene tbc
    "Thank you for playing the demo of my game! It may not be much, but this surprisingly took awhile to make, and I would be super happy if you enjoyed your experience."
    "If you would kindly, please write a critique on the review sheet included with the presentation. I would super appreciate that, to help me better my development. Thanks!"