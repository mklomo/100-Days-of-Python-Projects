"""
    This is a python implementation
    of the Treasure Island game.
"""

# Welcome statement
print("\nWelcome to the Treasure Island!\n")


# Insert an ASCII Art
print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
""")


print("\n")


print("Your mission is to find the treasure\n")


# Would you like to move to the left or right
first_decision = input("Would you like to move to the left or right?\n")

# Convert the decsion to a lower case
first_decision = first_decision.lower()

if first_decision == "right":
    print("You fell into an underground cave. Game over!")
    print("""
          ..          ...        .....,.,....,,..,.......... .....,....        ,,,......:,...   .,,,..  
           ..  ...  ..       .,,,,,,...............,,..... . ...,,,....  ....,,...,,:,,,::.. ,:..   
  ..... .   .......     .... ........,,..,,,::,:,,:,,,.,,..... ...,,,........,,,...,,.,,,:...,,,.   
     .......... ...    ...,........,;;:,..,,,,:;:::,,.,.....,,.............,,,:::,::::;;;,...,,,....
....     .,,.... ...,.......,::,,:,,;,........,,,,,,,,,.....,,,,::::;iiiiii1tttt11tttftt1i:..,..,.  
. ... ..,,,..    .,,,... ...:;;:,,,;:.,,..,,.,,,,.,,.,,,,::;;i11tt111111i;;iiii;;;iiii;;;,......... 
    .,,:,......,. ....... ..,,....:i;,,,,.,,,,,,,,,,,,:i111111ii;;:::::,,,,,,,,,,,,,,...............
.. .,::,,.   .,,,.,,,,,,,,....,.,,,,,,:,,,,,:;:,::ii1111i;::,,,,,,,,,,,,,,,:,,,,,,,.......... ...  .
 .,,,.,:,... ,,..,:::;ii:::...,,,,,,,:,,,,,:11;:i1t1;:,,,,,,::,,,,.,,,,...,,,,,,,::,,,..........,.  
 .,.  ........,,,,,:i;:,,:::::,,::::,;,,:,,,,,,,::,,,,;:,,,,,,,,,,.....,,.,,:;;:,.,,:,...,.,,,..,...
... ... ...,::,,.,i1;,,,.,,,::,,,;,,,,,,,,.,,,,,,,,,,,:;:::,,,,,,,,,...,,.,,,:ii;,......,,,,,...,,..
..   ..  ,,,....:;:;:,,,,,:,:,,:,,,,,,,,,,,,,,,,,,::,::i11i1i:,,,,,,,,,.,,,,,,,;1:,,...,:,..,,,,,,,.
.........,....:ii;,.,,,,,::,,,,:,,,,,,,,,::,,:,:::::i1ii;:;i1i1i,,,,,,,,,,,,,:,,;ii;,..,:,,,,,,,,:. 
   ....,,.....:;;:,.,,,,,,,,:,,,,,,,,,:;i11ttttft1t11;:,,::,,:;11::,,,,,,,,::::,,:ii:,::,,,,....,:,.
  ....,,,...,,,,::,,..,,,.,,:::::::;i1fftt1tffLfttt11;:;::::::,i1:if1;:,::::;1;::,,::;;:,..,,...,,:.
......,....:;;::,.....,..,,1;,:::ifff1i;iit1ttt1tt1ii1t1iii;;;;ti:;itff1;:::it:::::::;:,....,:,..,,,
... .,....::;:......,...,,,ii:;1fLt111ttLGCffftfftttt111ttLffftffti::;itfffitt;;::::,::;;,,,.,:,....
 ...,,...,..........,,,,,,,;iifLftLCCtttff111tffttti;;;i1tttfC0L1tLf;;;:;tCCCLi;::,:,:;;ii;:,,,:,.,,
  ..::;,.............,,,,,::1LLLGGLti1t1ii11;;;;i1ttttti1fft111tt;;tL1i;;:iLGti;;::::::::i11:,.,:,,,
 ....:;:.......,,..,,...,,:;111LC1iift1iitf1iii1i1111tt111ttttfi;i;;tG1i;;;;fL1i;;;:;;:::::;;,.,,,,,
 ..................,,..,,,,::;ifi;1f1ittff11iii;;;;;;:;;;;i11t1ft;1i;fC1i;;;iLCf1;;::;:,,,,:,....,,,
   ....................,,,,:::1Lifft1iff1i;;;;;i111iii;::;iii1titt;11iLC1i;;;1GGfi;;:::::::,.....,..
      ...............,,,:,,,::i;tftLifLii;;;i11i111iii11;:;i;;;ti1iitiiGLi11iiLGf1i;;;;::::.....,:,.
      .,.,,............,,,,,:::itiLf1tti;;:it1iiiiiiiii1ti:;;;:11:i1tiiLGiiiiiLCfLCti;;:::;:,....::,
    ....,:,..............,,::;;ftifff1i;:;:i1;iiiiiiiii;i1;::;:it;;itiifG1;i;;fGG0Gfi;;:::i;,,..,,,:
  .....,;:............,,;;,::;;LttL11Lti:;;t1;1ii;;iiii;i1;::;;11;;;1LG1Cf;;iftt1ii;;;;;::;:,,,,,.,,
     .,;;.....,........,::;::::tfLCiitfi;;:1ti;;;1i111i1t1::;;;;;;;ifGfiff;;tL;:;;;;::::,,:;,,,::,..
     .........,........,,,::;ii1LfGti1t1;::;i1i;i11111ttti;;ii1;1t;ifGfiLf;1f;:::::::::,,:::,,.....,
........,,,...,,.......,,,,::;i1fCLLt1ttii;:;;;11tttt11i;:;1itfiff11Cf1;t11f;:::::,,,,,,,;i:,,::,...
.,......,:............,i;,:::::;iLt;tt1t1;;;;;::;;i;;;;:;1t1tt1CCttLfi;1ttf;::::::,,,,,,,::,.,;:,,..
 ..    .,:.........,.,,;i,,,:::i111;:i;;ti;;::;iii;;ii11ftftfC0GffL1;;1LfCi:::::,:::::,,:;,.,,:,,...
  ,......:,...........,:i;,,,::i1i;;;::i1t1111111tfffffft11ttLffLLtiifL1iG1i;;i;:::,::::;:,..,:,....
. .......,:..........,,,:1:,,,::;ifi;;;;;i1t1ii1tttt1fftt1i1i;1t1iiift;;fC;;;fLt;:,,:,,:,....,,.....
.. .,..,:::.......,..,..,1f:,,,:::fLi;11i;;i1ii1tfLffttt11i;;;i;;;i11;;;t1;;:1L;;::::::,.....::.....
   .:. .,..,..,,........,,;1;,,:::;i1t1;;iitLffftffffffftti;;;;;iLfi:::;;::::1Ct;;:,,;;:,...,,,.,,:,
  ...,....,,......,,.,,,,,,;i;:,:::::ii1111f0ftttftLft11;;;::::;ft;;;;::::;1LCfi;;;;i:,,...,,,...,,,
.    ,,...,.,::,.....,,,,,,,,tt;:::::::;i111tiii1iit111111i:::;;tftfi::;ifC0C1;;;;i;:,....:::,....  
...... ,,...,it1:...,,,...,,,:;1t11ttttf1:;i;;::::;i11111i;:::1ft;;ii1tLCCCtii;;:,:,,,,,,:::::,,.,..
..,.   .,,..,,::::,,,,:,.,.,,,:;CffCfi;;i:;i::;1i;::,,,,,,,:::iiittfLLt1i;;;;::;:,,,,,,::,.,.,::,.  
  ..... .:,......,;:,,,,,,,,,,:::::;:::,::,,::;itt1tt1iii1tfffLLLLt1t1;;;:;::::,,.,,::,::....,,,,,,.
 .  .,.. .,,,.....,;i;:,,,,,,,,,,,,,,,,,,,,::,,,,,:;iiittftt11ti;::;:::::;;::,,,,,.,,,,::....,,,,.,:
   . ..,,,..,:,..,,,::;:,,:::,,.,,,,,,,,,,,,::,,,,,,,,,:::::::::,,,::,,,:1i,,:,,,,.,:,,,,......... .
  ..  ..,,,..,:,::......,:,,,,,,,...,::,,,,:;i,,,,,,,,,,,,,,,::,,,,,,,,,,::,;i:,,...,,.  .,. ... .:.
  .,,,.....,,...,,,,.,. ...,,.:i:,,,,,,.,..,,,,,,,,,,,,,,,,,,,,,......,,.,,;1i:,,,......,:,..... .:.
.....,:,.  .,:.  ,:,,...  ....,,..,,,,.........,,,,,,...,,,,,,.,,......,,:::;;,.......,,..........:.
...  .::,....... .. .,,.....,,..   .........,,,,,,:,,,...,,..........,,,:;,..::......,,. .      .,;.
..    ...,,,..  ... .. . .,:,..,,,,,,.......,,,,,,,,,....,.........,,,..;1;,...  .,,...........,,,: 
.         .,::,,..       .::,....,.,,,,,,,.,..,,,,,,,:,,,,...,::::,,, ...,,. ...,:,........,,,.,.,:.
,.   ..    .....,...     ..  . ......,...,:;:,,::,,,.,,..:;,,ii1;,....    ...,.....,,....,,....  .:.
..,.....       ......,.          ...:,..;i11;::;:::..   .;1:,;;;:,....,...,,,,.,...,....,,.       . 

    """)

elif first_decision == "left":
    # Insert waterfall
    print("""
                _.-'\
        _.-'     \
    _.-'          \
_.-_-'\         _.-'`-._
  |\ _-|    _.-'_.-'`-._`-._
  | |  |   |_.-'        `-._`-._|`-._
\ \ |  |  /    /     _      ``---._  `-._
 \ \|_-' | / /    .-' `-._|`-._    ``-._ `-._
  \     || ||  / /|-'|`-._     `-._     `--._`-._|`-._
   \_.-'   | |      |||   `-._     `-._      ``---._  `-._
   |    |   | | |   |||    |||`-._     `-._|`-._    ``-._ `-._
   |        |    __ |||    |||    `-._          `-._     `-._ `-._
   |    |    |  |_.-|||.   |||        `-._       _.-'|       `-_.'|
   |    |   |  ||/  ||| \  |||          _.-'|_.-'_.-'      _.-'   |
   |     | | |  .   |||  . |||      _.-' __.---''      _.-'       |
   |    |   |  ||   |||    |||'|_.-'_.-''     _.-'|_.-'        _.'
   |    ||    ||    |||  |'|||----''      _.-'             _.-'
   |       | |  |   |||   '|||   _.-'|_.-'             _.-'
   |    |  ||  _.\  ||| /  |||.-'                  _.-'
   |    | |  '  |_`.|||' _.-'                  _.-'
   | _.-||  |  |    ||`-'                  _.-'
   |`-._     |   _.-'                  _.-'
   |    `-._ _.-'                  _.-'
   |        |                  _.-'       VK
   |        |              _.-'
-._|        |          _.-'
   `-._     |     _.-'
       `-._ | _.-'
           `|'
    
    """)
    second_decision = input("You get to a waterfall, will you swim or wait?\n")

    # Lowercase second decision
    second_decision = second_decision.lower() 

    if second_decision == "swim":
        print("Game over!\n")
        print("You were devoured by a giant snake_object!\n")
        print("""
                          _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              \'   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`\
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
       \:   .:. ''' .:| .:, _:./':.|
    jgs '--.:::...---'\:'.:`':`':./
        """)

    elif second_decision == "wait":
        third_decision = int(input("""\nYou get to a castle! You are presented with three doors, 
        which would you enter? 1, 2 or 3?\n"""))

        if third_decision != 2:
            print("\n Game Over")

        else:
            print("Congratulations, You won!")
            print("""
                               ,.%`
               ,;%%',  __%%%;,
              ,%%%\___/%%%
              '   %   \    %% _ %_-%% %%,'
                 %/%%% \,%%%%;%_/%%
               ,%/% '%%;\%%%  ;%,
               `;'  `%-\_\ \%;_%/%
                    ,,%_/%\|\%%`%
                       %,%%|\%\,'
                       `%% |-%%\%\%%%
                           | %-_\%\`_',
                           |    '%`%'%
                           |     ,%%%%%,
                      _____O_____  ,%%%`
                     /\_________/\
                    /\/         \/\
                   /\/   ~;@;~   \/\   
                  /\/    .-_-.    \/\
                 /\/    : ('< :    \/\
                /\/     '.(_).'     \/\
                \/:                 :\/ 
                   \ ~;@;~ o ~;@;~ /
                    '.           .'
                      '._______.' lc
    
            """)

