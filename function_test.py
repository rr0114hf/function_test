import pygame as pg

# マウスで操作するオブジェクトの宣言
class MouseControl:
    # プログラム内のパラメータを初期化する関数
    def __init__(self,width = 400, height=600, font=50, str_img="hello, pygame", str_color="green", path = "../../assets/player/p1_walk01.png"):
        pg.init()
        self._screen = None
        self._font = None
        self._text_image = None
        self._player_image = None
        self._width = width
        self._height = height
        self._fonts = font
        self._str_img = str_img
        self._str_color = str_color
        self._path = path
        self.n = 0
    
    # Pygameオブジェクトの作成
    def create_object(self, width, height, font, str_img, str_color, path):
        self. _screen = pg.display.set_mode((width, height))
        self._font = pg.font.Font(None, font)
        self._text_image = self._font.render(str_img, True, pg.Color(str_color))
        self._player_image = pg.image.load(path)
    
    # アニメーションの作成
    def draw(self, screen, player_image, text_image, mouse_pos):
        screen.fill(pg.Color("black"))
        screen.blit(player_image, mouse_pos)
        mouse_x, mouse_y = mouse_pos
        text_offset_x = 180
        screen.blit(text_image, (mouse_x + text_offset_x, mouse_y))
        pg.display.update()
        
    # キーボード操作の処理（停止するかどうかを判断する関数）
    def event_control(self):
        should_quit = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                should_quit = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    should_quit = True
                if event.key == pg.K_SPACE:
                    self.n = self.n  + 1
                    if self.n%2 == 0:
                        self._str_color="blue"
                    else:
                        self._str_color="red"
                    font2 = self._fonts + self.n  + 10 
                    self.create_object(self._width, self._height, font2, self._str_img, self._str_color, self._path)
                if event.key == pg.K_BACKSPACE:
                    font2 = self._fonts
                    self.n = 0
                    self._str_color="green"
                    self.create_object(self._width, self._height, font2, self._str_img, self._str_color, self._path)
                else:
                    pass                    
        return should_quit
    
    # メイン関数
    def MouseCtrl_main(self):
        self.create_object(self._width, self._height, self._fonts, self._str_img, self._str_color, self._path)
        while True:
            if self.event_control():
                break
            mouse_pos = pg.mouse.get_pos()
            
            self.draw(self._screen, self._player_image, self._text_image, mouse_pos)
        pg.quit()

if __name__=="__main__":
    MouseCtrl = MouseControl(width=600, height=600, font=20)
    MouseCtrl.MouseCtrl_main()
    