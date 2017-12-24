def make_colors(string, foreground = '', background = '', attrs = '', color_type = 'termcolor'):
    """
        attributes termcolor [attrs]:
        ============ ======= ==== ========= ========== ======= =========
        Terminal     bold    dark underline blink      reverse concealed
        ------------ ------- ---- --------- ---------- ------- ---------
        xterm        yes     no   yes       bold       yes     yes
        linux        yes     yes  bold      yes        yes     no
        rxvt         yes     no   yes       bold/black yes     no
        dtterm       yes     yes  yes       reverse    yes     yes
        teraterm     reverse no   yes       rev/red    yes     no
        aixterm      normal  no   yes       no         yes     yes
        PuTTY        color   no   yes       no         yes     no
        Windows      no      no   no        no         yes     no
        Cygwin SSH   yes     no   color     color      color   yes
        Mac Terminal yes     no   yes       yes        yes     yes
        ============ ======= ==== ========= ========== ======= =========
    """
    if not background:
        background = ''
    if not foreground:
        foreground = ''
    if not attrs:
        attrs = []                
    def set_colorama(foreground = foreground, background = background):
        try:
            import colorama
            colorama.init(True, autoreset= True, wrap= True)
            colors_fore = {
                "white": colorama.Fore.WHITE,
                "black": colorama.Fore.BLACK,
                "blue": colorama.Fore.BLUE,
                "cyan": colorama.Fore.CYAN,
                "green": colorama.Fore.GREEN,
                "red": colorama.Fore.RED,
                "magenta": colorama.Fore.MAGENTA,
                "yellow": colorama.Fore.YELLOW,
                "lightwhite": colorama.Fore.LIGHTWHITE_EX,
                "lightblack": colorama.Fore.LIGHTBLACK_EX,
                "lightblue": colorama.Fore.LIGHTBLUE_EX,
                "lightcyan": colorama.Fore.LIGHTCYAN_EX,
                "lightgreen": colorama.Fore.LIGHTGREEN_EX,
                "lightred": colorama.Fore.LIGHTRED_EX,
                "lightmagenta": colorama.Fore.LIGHTMAGENTA_EX,
                "lightyellow": colorama.Fore.LIGHTYELLOW_EX,                    
            }
            
            colors_back = {
                'white': colorama.Back.WHITE,
                'black': colorama.Back.BLACK,
                'blue': colorama.Back.BLUE,
                'cyan': colorama.Back.CYAN,
                'green': colorama.Back.GREEN,
                'red': colorama.Back.RED,
                'magenta': colorama.Back.MAGENTA,
                'yellow': colorama.Back.YELLOW,
                'lightwhite': colorama.Back.LIGHTWHITE_EX,
                'lightblack': colorama.Back.LIGHTBLACK_EX,
                'lightblue': colorama.Back.LIGHTBLUE_EX,
                'lightcyan': colorama.Back.LIGHTCYAN_EX,
                'lightgreen': colorama.Back.LIGHTGREEN_EX,
                'lightred': colorama.Back.LIGHTRED_EX,
                'lightmagenta': colorama.Back.LIGHTMAGENTA_EX,
                'lightyellow': colorama.Back.LIGHTYELLOW_EX,                    
            }
            
            foreground1 = colors_fore.get(str(foreground))
            background1 = colors_back.get(str(background))
            if not foreground1:
                foreground1 = ''
            if not background1:
                background1 = ''
            return foreground1 + background1 + string 
        except ImportError:
            print 'NO MODULE NAME: "colorama"'
            return string

    def set_termcolor(foreground = foreground, background = background, attrs = attrs):        
        try:
            import termcolor
            colors_fore = {
                    'white': 'white',
                    'grey': 'grey', 
                    'blue': 'blue', 
                    'cyan': 'cyan', 
                    'green': 'green', 
                    'red': 'red', 
                    'magenta': 'magenta', 
                    'yellow': 'yellow',
                    "lightwhite": 'white',
                    "lightblack": 'grey',
                    "lightblue": 'blue',
                    "lightcyan": 'cyan',
                    "lightgreen": 'green',
                    "lightred": 'red',
                    "lightmagenta": 'magent',
                    "lightyellow": 'yellow',                                        
            }
            
            colors_back = {
                    'white': 'on_white',
                    'grey': 'on_grey', 
                    'blue': 'on_blue', 
                    'cyan': 'on_cyan', 
                    'green': 'on_green', 
                    'red': 'on_red', 
                    'magenta': 'on_magenta', 
                    'yellow': 'on_yellow',
                    "lightwhite": 'on_white',
                    "lightblack": 'on_grey',
                    "lightblue": 'on_blue',
                    "lightcyan": 'on_cyan',
                    "lightgreen": 'on_green',
                    "lightred": 'on_red',
                    "lightmagenta": 'on_magent',
                    "lightyellow": 'on_yellow',                                        
            }
            if 'light'in foreground or 'light' in background:
                if attrs:
                    if not 'bold' in attrs:
                        attrs.append('bold')
                else:
                    attrs = ['bold']
            if foreground:
                return termcolor.colored(string, colors_fore.get(str(foreground).strip()), colors_back.get(str(background).strip()), attrs)                
        except ImportError:
            print 'NO MODULE NAME: "termcolor'
            return string
            
    if color_type == 'colorama':
        try:
            return set_colorama()
        except:
            return set_termcolor()
    elif color_type == 'termcolor':
        try:
            return set_termcolor()
        except:
            return set_colorama()
