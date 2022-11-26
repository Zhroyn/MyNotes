import pygame
import sys
import json
import random
import time
from settings import Setting
from button import Text, Button, InputBox



def sort_records(setting, records):
    sorted_records = sorted(records, key=lambda n:n['time'])
    if len(sorted_records) <=3:
        setting.top_records = sorted_records
    else:
        setting.top_records = sorted_records[:3]

def read_out_data(setting):
    try:
        with open('data', 'r') as file:
            setting.data = json.load(file)
    except FileNotFoundError:
        setting.data = {}
        
    if str(setting.n) in setting.data.keys():
        setting.records = setting.data[str(setting.n)]
        sort_records(setting, setting.records)
    else:
        setting.top_records = []

def read_in_data(setting):
    if str(setting.n) in setting.data.keys():
        setting.records.append(setting.new_record)
        setting.data[str(setting.n)] = setting.records
    else:
        setting.data[str(setting.n)] = [setting.new_record]
        
    if len(setting.data[str(setting.n)]) > 10:
        sorted_records = sorted(setting.records, key=lambda n:n['time'])
        top_records = sorted_records[:10]
        setting.data[str(setting.n)] = top_records
    
    with open('data', 'w') as file:
        json.dump(setting.data, file)





def form_lists(setting):
    ord_list = list(range(1,setting.n**2+1))
    ran_list = random.sample(ord_list,setting.n**2)
    setting.ord_list = [str(i) for i in ord_list]
    setting.ran_list = [str(i) for i in ran_list]
    setting.ran_list_copy = []

def form_choose_caption(setting, text):
    f_size = 0.08 * setting.sc_h
    setting.choose_caption = Text(0, 0, f_size)
    setting.choose_caption.form_text(setting.te_color, text)
    
    weight = setting.choose_caption.text_image_rect.w
    setting.choose_caption.x = setting.margin_centerx - 0.5*weight
    setting.choose_caption.y = 0.18 * setting.sc_h
    setting.choose_caption.form_text(setting.te_color, text)

def form_game_caption(setting, text):
    setting.game_caption = Text(0.7*setting.sc_w, 0.24*setting.sc_h,
                                0.06*setting.sc_h)
    setting.game_caption.form_text(setting.te_color, text)

def form_choose_inputbuttons(setting):
    setting.choose_inputbox = InputBox(0,0,0.15*setting.sc_w,0.1*setting.sc_h,7)
    setting.choose_inputbox.rect.centerx = setting.margin_centerx
    setting.choose_inputbox.rect.centery = 0.3 * setting.sc_h
    setting.choose_inputbox.form_text(setting.te_color, '')
    
    setting.choose_ok_button = Button(0, 0, 0.12*setting.sc_w, 0.1*setting.sc_h)
    setting.choose_ok_button.rect.centerx = setting.margin_centerx
    setting.choose_ok_button.rect.centery = 0.42*setting.sc_h
    setting.choose_ok_button.form_text((255,255,255), 'Yes')

def form_game_inputbuttons(setting):
    setting.game_inputbox = InputBox(0.7*setting.sc_w, 0.29*setting.sc_h,
                                     0.28*setting.sc_w, 0.07*setting.sc_h,18)
    setting.game_inputbox.form_text(setting.te_color, '')
    
    setting.game_ok_button = Button(0.7*setting.sc_w, 0.375*setting.sc_h,
                                    0.08*setting.sc_w, 0.07*setting.sc_h)
    setting.game_ok_button.form_text((255,255,255), 'OK')

def form_set_buttons(setting):
    set_buttons = []
    set_list = list(range(4,13))
    margin_len = setting.sc_h / (3*3 + 8)
    bu_len = 3 * margin_len
    setting.margin_centerx = 6.5*margin_len + 0.5*setting.sc_w
    for col_num in range(1,4):
        for row_num in range(1,4):
            text = set_list.pop(0)
            x = 2*margin_len + (row_num-1)*(margin_len+bu_len) 
            y = 3*margin_len + (col_num-1)*(margin_len+bu_len) 
            button = Button(x, y, bu_len, bu_len)
            button.form_text((255,255,255), str(text))
            set_buttons.append(button)
    setting.set_buttons = set_buttons

def form_game_buttons(setting):
    game_buttons = []
    margin_len = setting.sc_h / (4*setting.n + 1)
    bu_len = 3 * margin_len
    setting.margin_centerx = 2*setting.n*margin_len + 0.5*setting.sc_w
    for col_num in range(1,setting.n+1):
        for row_num in range(1,setting.n+1):
            text = setting.ran_list.pop(0)
            setting.ran_list_copy.append(text)
            x = row_num * (margin_len + bu_len) - bu_len
            y = col_num * (margin_len + bu_len) - bu_len
            button = Button(x ,y, bu_len, bu_len)
            button.form_text((255,255,255), text)
            game_buttons.append(button)
    setting.game_buttons = game_buttons
    setting.ran_list = setting.ran_list_copy
    setting.ran_list_copy = []

def form_time_text(setting, time):
    f_size = 0.1*setting.sc_h
    setting.time_text = Text(0, 0, f_size)
    setting.time_text.form_text(setting.te_color, time)
    
    weight = setting.time_text.text_image_rect.w
    setting.time_text.x = setting.margin_centerx - 0.5*weight
    setting.time_text.y = 0.12*setting.sc_h
    setting.time_text.form_text(setting.te_color, time)

def form_restart_button(setting):
    weight, height = 0.2*setting.sc_w, 0.12*setting.sc_h
    x = setting.margin_centerx - 0.5*weight
    y = 0.81* setting.sc_h
    setting.restart_button = Button(x, y, weight, height)
    setting.restart_button.form_text((255,255,255), 'Restart')

def form_ranking_text(setting):
    if setting.top_records:
        setting.ranking_text = Text(0.7*setting.sc_w, 0.56*setting.sc_h,
                               0.08*setting.sc_h)
        setting.ranking_text.form_text(setting.te_color, 'Ranking:')
        setting.record_texts = []
        for record_num in range(len(setting.top_records)):
            x = 0.7 * setting.sc_w
            y = (0.63 +0.06*record_num) * setting.sc_h
            time = setting.top_records[record_num]['time']
            name = setting.top_records[record_num]['name']
            text = str(record_num+1)+'.  '+str(time) +'  '+name
            record_text = Text(x, y, 0.05*setting.sc_h)
            record_text.form_text(setting.te_color, text)
            setting.record_texts.append(record_text)



def form_choose_interface(setting):
    form_set_buttons(setting)
    form_choose_caption(setting, 'Customize Number')
    form_choose_inputbuttons(setting)

def form_game_interface(setting):
    setting.game_mark = True
    setting.time_mark = True
    setting.starttime = time.time()
    setting.passtime = str(round(time.time()-setting.starttime,1))
    
    form_lists(setting)
    form_game_buttons(setting)
    form_time_text(setting, setting.passtime)
    form_restart_button(setting)
    form_ranking_text(setting)
    







def update_time(setting):
    if setting.time_mark:
        setting.record_time = str(round(time.time()-setting.starttime,2))
        setting.passtime = str(round(time.time()-setting.starttime,1))
        setting.time_text.form_text(setting.te_color, setting.passtime)

def update_choose_interface(setting):
    cap_text = setting.choose_caption.text
    inp_text = setting.choose_inputbox.text
    
    form_set_buttons(setting)
    form_choose_inputbuttons(setting)
    form_choose_caption(setting, cap_text)
    setting.choose_inputbox.form_text(setting.te_color, inp_text)

def update_game_interface(setting):
    form_game_buttons(setting)
    form_time_text(setting, setting.passtime)
    form_ranking_text(setting)
    form_restart_button(setting)

    if setting.over_mark:
        cap_text = setting.game_caption.text
        inp_text = setting.game_inputbox.text
        
        form_game_inputbuttons(setting)
        form_game_caption(setting, cap_text)
        setting.game_inputbox.form_text(setting.te_color, inp_text)

def update_screen(setting):
    if setting.sc_r_mark == True and setting.sc_w <= setting.sc_max:
        setting.sc_w *= 1.01
        setting.sc_h = 0.7*setting.sc_w
        setting.update_screen()
        if setting.game_mark:
            update_game_interface(setting)
        else:
            update_choose_interface(setting)
    if setting.sc_l_mark == True and setting.sc_w >= setting.sc_min:
        setting.sc_w /= 1.01
        setting.sc_h = 0.7*setting.sc_w
        setting.update_screen()
        if setting.game_mark:
            update_game_interface(setting)
        else:
            update_choose_interface(setting)

def update_ranking(setting):
    if str(setting.n) in setting.data.keys():
        records = setting.data[str(setting.n)][:]
        records.append(setting.new_record)
        sort_records(setting, records)
        form_ranking_text(setting)
    else:
        setting.top_records = [setting.new_record]
        form_ranking_text(setting)






def draw_choose_interface(setting):
    for button in setting.set_buttons:
        button.draw(setting.screen, setting.bu_color)
    setting.choose_caption.draw(setting.screen)
    setting.choose_inputbox.draw(setting.screen, setting.bu_color,
                                 setting.bu_active_color)
    setting.choose_ok_button.draw(setting.screen, setting.bu_active_color)


def draw_game_interface(setting):
    for button in setting.game_buttons:
            button.draw(setting.screen, setting.bu_color)
    setting.time_text.draw(setting.screen)
    setting.restart_button.draw(setting.screen, setting.bu_active_color)
    
    if setting.top_records:
        setting.ranking_text.draw(setting.screen)
        for record_text in setting.record_texts:
            record_text.draw(setting.screen)
    
    if setting.over_mark:
        setting.game_caption.draw(setting.screen)
        setting.game_inputbox.draw(setting.screen, setting.bu_color,
                                   setting.bu_active_color)
        setting.game_ok_button.draw(setting.screen, setting.bu_active_color)

def draw_game(setting):
    setting.screen.fill(setting.bg_color)
    if setting.game_mark:
        draw_game_interface(setting)
    else:
        draw_choose_interface(setting)
    






def check_over(setting):
    if (setting.game_mark
        and not setting.ord_list and not setting.over_mark):
        setting.time_mark = False
        setting.over_mark = True
        
        form_time_text(setting, setting.record_time)
        form_game_caption(setting, 'Your Name:')
        form_game_inputbuttons(setting)

def check_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def check_choose_inputbox(setting, event):
    if setting.choose_inputbox.active:
        if event.key == pygame.K_BACKSPACE:
            setting.choose_inputbox.cancel_letter(setting.te_color,
                                                  event.unicode)
        else:
            setting.choose_inputbox.add_letter(setting.te_color,
                                               event.unicode)

def check_game_inputbox(setting, event):
    if setting.over_mark:
        if setting.game_inputbox.active:
            if event.key == pygame.K_BACKSPACE:
                setting.game_inputbox.cancel_letter(setting.te_color,
                                                    event.unicode)
            else:
                setting.game_inputbox.add_letter(setting.te_color,
                                                 event.unicode)

def check_keydowm(setting,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            setting.sc_r_mark = True
        if event.key == pygame.K_LEFT:
            setting.sc_l_mark = True
        check_choose_inputbox(setting, event)
        check_game_inputbox(setting, event)

def check_keyup(setting,event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            setting.sc_r_mark = False
        if event.key == pygame.K_LEFT:
            setting.sc_l_mark = False


def check_choose_inputbuttons(setting, event, mouse_x, mouse_y):
    if setting.choose_inputbox.rect.collidepoint(mouse_x,mouse_y):
        setting.choose_inputbox.active = True
    else:
        setting.choose_inputbox.active = False
    
    if setting.choose_ok_button.rect.collidepoint(mouse_x,mouse_y):
        try:
            n = int(setting.choose_inputbox.text)
        except ValueError:
            form_choose_caption(setting, 'Please check input')
        else:
            if n > 32:
                form_choose_caption(setting, 'Number too large')
            else:
                setting.n = n
                read_out_data(setting)
                form_game_interface(setting)

def check_game_inputbuttons(setting, event, mouse_x, mouse_y):
    if setting.game_inputbox.rect.collidepoint(mouse_x,mouse_y):
        setting.game_inputbox.active = True
    else:
        setting.game_inputbox.active = False
    
    if setting.game_ok_button.rect.collidepoint(mouse_x,mouse_y):
        if not setting.game_inputbox.text:
            form_game_caption(setting, 'Please input name')
        else:
            form_game_caption(setting, 'Your name:')
            setting.new_record = {'time': float(setting.record_time),
                                  'name': setting.game_inputbox.text}
            update_ranking(setting)

def check_setting_buttons(setting, event, mouse_x, mouse_y):
    for button in setting.set_buttons:
        if button.text and button.rect.collidepoint(mouse_x,mouse_y):
            setting.n = int(button.text)
            read_out_data(setting)
            form_game_interface(setting)

def check_game_buttons(setting, event, mouse_x, mouse_y):
    for button in setting.game_buttons:
        if (button.text
        and button.rect.collidepoint(mouse_x,mouse_y)
        and int(button.text) == int(setting.ord_list[0])):
            setting.ord_list.remove(button.text)
            setting.ran_list = ['' if i == button.text else i
                                for i in setting.ran_list]
            button.form_text((255,255,255), '')

def check_restart_button(setting, event, mouse_x, mouse_y):
    if setting.restart_button.rect.collidepoint(mouse_x,mouse_y):
        if setting.over_mark and setting.game_inputbox.text:
            read_in_data(setting)
        setting.init()
        form_choose_interface(setting)


def check_mousedown(setting,event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if setting.game_mark:
            check_game_buttons(setting, event, mouse_x, mouse_y)
            check_restart_button(setting, event, mouse_x, mouse_y)
            if setting.over_mark:
                check_game_inputbuttons(setting, event, mouse_x, mouse_y)
        else:
            check_setting_buttons(setting, event, mouse_x, mouse_y)
            check_choose_inputbuttons(setting, event, mouse_x, mouse_y)


      
def check_events(setting):
    for event in pygame.event.get():
        check_over(setting)
        check_quit(event)
        check_keydowm(setting,event)
        check_keyup(setting,event)
        check_mousedown(setting,event)
        
            



        
def except_action_1(err):
    print(str(err))
    pygame.quit()
    sys.exit()
def except_action_2(err,setting):
    print(str(err))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

        setting.screen.fill(setting.bg_color)
        pygame.display.flip()




    
