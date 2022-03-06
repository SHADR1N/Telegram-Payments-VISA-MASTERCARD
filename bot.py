import telebot
from telebot import types
import peewee
import time
import re
import peewee
import configparser
from datetime import datetime
from pytz import timezone
from text import *



format = "%Y-%m-%d %H:%M"

db = peewee.SqliteDatabase('present.db')
class BaseModel(peewee.Model):
    class Meta:
        database = db

class NewUser(BaseModel):
    USERID = peewee.IntegerField( unique = True )
    Selected = peewee.TextField( default = 'None' )
    lang = peewee.TextField( default = 'eng' )

    @classmethod
    def get_row(cls, USERID):
        return cls.get(USERID == USERID)

    @classmethod
    def row_exists(cls, USERID):
        query = cls().select().where(cls.USERID == USERID)
        return query.exists()

    @classmethod
    def creat_row(cls, USERID):
        user, created = cls.get_or_create(USERID=USERID)




class PresentList(BaseModel):
    USERID = peewee.IntegerField()
    ChannelName = peewee.TextField(  default = '' )
    ChannelID = peewee.TextField(  default = '' )
    DateClose = peewee.TextField( default =  datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format) )
    PriceTicket = peewee.TextField( default = '' )
    AboutPresent = peewee.TextField( default = '' )
    WinnersCount = peewee.TextField( default = 1 )
    SubCheck = peewee.TextField( default = 'On' )
    ButText = peewee.TextField( default = 'Participate' )
    StatusRaffle = peewee.TextField( default = '' )

    @classmethod
    def get_row(cls, USERID):
        return cls.get(USERID == USERID)

    @classmethod
    def row_exists(cls, USERID):
        query = cls().select().where(cls.USERID == USERID)
        return query.exists()

    @classmethod
    def creat_row(cls, USERID):
        user, created = cls.get_or_create(USERID=USERID)


    @classmethod
    def row_exists__(cls, USERID, ChannelName):
        query = cls().select().where(cls.USERID == USERID, cls.ChannelName == ChannelName)
        return query.exists()

class ChannelList(BaseModel):
    USERID = peewee.IntegerField()
    ChannelName = peewee.TextField(  default = '' )
    ChannelID = peewee.TextField(  default = '' )
    @classmethod
    def get_row(cls, USERID):
        return cls.get(USERID == USERID)

    @classmethod
    def row_exists(cls, USERID, ChannelID, ChannelName):
        query = cls().select().where(cls.USERID == USERID, cls.ChannelID == ChannelID, cls.ChannelName == ChannelName )
        return query.exists()

    @classmethod
    def creat_row(cls, USERID, ChannelID, ChannelName):
        user, created = cls.get_or_create(USERID=USERID, ChannelID=ChannelID, ChannelName=ChannelName)

class AllMembersRaffle(BaseModel):
    USERID = peewee.IntegerField()
    ChannelName = peewee.TextField(  default = '' )
    UNtoken = peewee.TextField( default = '' )

    @classmethod
    def get_row(cls, USERID):
        return cls.get(USERID == USERID)

    @classmethod
    def row_exists(cls, USERID, ChannelName):
        query = cls().select().where(cls.USERID == USERID, cls.ChannelName == ChannelName)
        return query.exists()

    @classmethod
    def creat_row(cls, USERID, ChannelName):
        user, created = cls.get_or_create(USERID=USERID, ChannelName=ChannelName)


db.create_tables([AllMembersRaffle])
db.create_tables([ChannelList])
db.create_tables([PresentList])
db.create_tables([NewUser])

token = 
bot = telebot.TeleBot(token)
token_pay = 



@bot.message_handler(commands=["start"])
def start(message):


    UID = message.chat.id
    


    if not NewUser.row_exists(UID):
        NewUser.creat_row(UID)
    lang = NewUser.get(NewUser.USERID == UID).lang
    if len(message.text.split()) == 2:
        chan = message.text.split()[1]
        if not PresentList.select().where(PresentList.ChannelID == chan):
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['🇷🇺 Русский', '🇺🇸 English', '🇺🇿 Узбекский']])
            bot.send_message(message.chat.id, get_message(lang, 'text60'), reply_markup=keyboard, parse_mode="Html")


            bot.send_message(UID, get_message(lang,"text24"))
            return

        raffle = PresentList.get(PresentList.ChannelID == chan)
        ChannelName = raffle.ChannelName
        AboutPresent = raffle.AboutPresent
        DateClose = raffle.DateClose
        ButText = raffle.ButText
        PriceTicket = raffle.PriceTicket
        SubCheck = raffle.SubCheck
        WinnersCount = raffle.WinnersCount
        CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
        a = NewUser.get(NewUser.USERID == UID)
        a.Selected = ChannelName
        a.save()
        msg = gettext(lang, 'text4', DateClose, AboutPresent, ChannelName, WinnersCount, PriceTicket, SubCheck, CountUser, ButText, '', '')

        DateClose = raffle.DateClose
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = f'({CountUser}) {name}', callback_data = name) for name in [get_message(lang, 'text38')]])
        bot.send_message(UID, msg,reply_markup=keyboard, parse_mode="Html")


        return
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['🇷🇺 Русский', '🇺🇸 English', '🇺🇿 Узбекский']])
    bot.send_message(message.chat.id, get_message(lang, 'text60'), reply_markup=keyboard, parse_mode="Html")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text31')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text62')]])

    bot.send_message(UID, get_message(lang, 'text1'), reply_markup=keyboard, parse_mode="Html")

def editRaffle(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text33'), get_message(lang, 'text34')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text35'),get_message(lang, 'text36')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text32'), get_message(lang, 'text37')]])

    bot.send_message(UID, text, reply_markup = keyboard)

    new = PresentList.get(PresentList.USERID == message.chat.id, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected)
    DateClose = new.DateClose
    ChannelName = new.ChannelName
    WinnersCount = new.WinnersCount
    SubCheck = new.SubCheck
    CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
    ticket = new.PriceTicket
    AboutPresent = new.AboutPresent
    ButText = new.ButText

    msg = gettext(lang, 'text1', DateClose, AboutPresent, ChannelName, WinnersCount, ticket, SubCheck, CountUser, ButText, '', '')

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text39'), get_message(lang, 'text40')]])
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text41')]])
    if new.StatusRaffle == 'Published':
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text42')]])

    bot.send_message(message.chat.id, f'{msg}', reply_markup=keyboard, parse_mode="Html")


def creatRaffle(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text33'), get_message(lang, 'text34')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text35'),get_message(lang, 'text36')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text32'), get_message(lang, 'text37')]])

    bot.send_message(UID, text, reply_markup = keyboard)
    if text == get_message(lang, 'text27'):
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, message.text, reply_markup=keyboard, parse_mode="Html")

        my_chat = []
        [ my_chat.append(name.ChannelName) for name in ChannelList.select().where(ChannelList.USERID == UID)]
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text26')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in my_chat])

        bot.send_message(UID, get_message(lang, 'text2'), reply_markup=keyboard, parse_mode="Html")
        return

    else:
        if not PresentList.row_exists__(UID, NewUser.get(NewUser.USERID == message.chat.id).Selected):
            PresentList.creat_row(UID)
            rf = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == '')
            rf.ChannelName = NewUser.get(NewUser.USERID == message.chat.id).Selected
            rf.ChannelID = ChannelList.get(ChannelList.USERID == message.chat.id, ChannelList.ChannelName == rf.ChannelName).ChannelID
            rf.AboutPresent = text
            rf.PriceTicket = 1
            rf.save()

        new = PresentList.get(PresentList.USERID == message.chat.id, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected)
        DateClose = new.DateClose
        ChannelName = new.ChannelName
        WinnersCount = new.WinnersCount
        SubCheck = new.SubCheck
        CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
        ticket = new.PriceTicket
        AboutPresent = new.AboutPresent
        ButText = new.ButText

        msg = gettext(lang, 'text3', DateClose, AboutPresent, ChannelName, WinnersCount, ticket, SubCheck, CountUser, ButText, '', '')

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text39'), get_message(lang, 'text40')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text41')]])
        if new.StatusRaffle == 'Published':
            keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text42')]])

        bot.send_message(message.chat.id, f'{msg}', reply_markup=keyboard, parse_mode="Html")


def SendRaffle(message):
    UID = message.chat.id
    text = message.text
    lang = NewUser.get(NewUser.USERID == UID).lang
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text33'), get_message(lang, 'text34')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text35'),get_message(lang, 'text36')]])
    keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text32'), get_message(lang, 'text37')]])
    bot.send_message(UID, text, reply_markup = keyboard)

    new = PresentList.get(PresentList.USERID == message.chat.id, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected)
    DateClose = new.DateClose
    ChannelName = new.ChannelName
    WinnersCount = new.WinnersCount
    SubCheck = new.SubCheck
    CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
    ticket = new.PriceTicket
    AboutPresent = new.AboutPresent
    ButText = new.ButText
    
    msg = gettext(lang, 'text3', DateClose, AboutPresent, ChannelName, WinnersCount, ticket, SubCheck, CountUser, ButText, '', '')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text39'), get_message(lang, 'text40')]])
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text41')]])
    if new.StatusRaffle == 'Published':
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text42')]])
    bot.send_message(chat_id = UID,  text = msg, reply_markup=keyboard, parse_mode="Html")



def NewPrice(message):
  price = message.text
  UID = message.chat.id
  lang = NewUser.get(NewUser.USERID == UID).lang
  if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
      bot.send_message(message.chat.id, get_message(lang,"text23"))
      return
  if price == get_message(lang, 'text27'):
      SendRaffle(message)
      return


  if price.isdigit() == True:
      m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
      m.PriceTicket = price
      m.save()

      SendRaffle(message)

  else:
      keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
      sent = bot.send_message(UID, f'{get_message(lang, "text43")}\n{get_message(lang,"text8")}', reply_markup=keyboard, parse_mode="Html")
      bot.register_next_step_handler(sent, NewPrice) 

def NewTextRaffle(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return

    m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
    m.AboutPresent = text
    m.save()
    SendRaffle(message)

def NewTextButton(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return

    m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
    m.ButText = text
    m.save()
    SendRaffle(message)

def NewYear(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return
    format = "%Y"
    if text.isdigit() == True and int(text) >= int(datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format)):
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        date = m.DateClose
        date = date.replace(m.DateClose.split('-')[0], text)
        m.DateClose = date
        m.save()
        SendRaffle(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, f'{get_message(lang, "text100")}', reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewYear) 

def NewMonth(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return
    format = "%m"
    if text.isdigit() == True and int(text) >= int(datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format)) and int(text) <= 12 and int(text) >= 1:
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        date = m.DateClose
        date = date.replace(m.DateClose.split('-')[1], text)
        m.DateClose = date
        m.save()
        SendRaffle(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, f'{get_message(lang, "text100")}', reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewMonth) 


def NewDay(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return
    format = "%d"
    if text.isdigit() == True and int(text) >= int(datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format)) and int(text) <= 31 and int(text) >= 1:
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        date = m.DateClose
        date = date.replace(m.DateClose.split('-')[2].split(' ')[0], text)
        m.DateClose = date
        m.save()
        SendRaffle(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, f'{get_message(lang, "text100")}', reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewDay) 


def NewHour(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return
    format = "%d"
    if text.isdigit() == True and int(text) >= int(datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format)) and int(text) <= 24 and int(text) >= 1:
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        date = m.DateClose
        date = date.replace(m.DateClose.split(' ')[1].split(':')[0], text)
        m.DateClose = date
        m.save()
        SendRaffle(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, f'{get_message(lang, "text100")}', reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewDay) 

def NewMin(message):
    text = message.text
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
        bot.send_message(message.chat.id, get_message(lang,"text23"))
        return
    if text == get_message(lang, 'text27'):
        SendRaffle(message)
        return
    format = "%d"
    if text.isdigit() == True and int(text) >= int(datetime.now(timezone('Etc/GMT+3')).astimezone(timezone('EET')).strftime(format)) and int(text) <= 60 and int(text) >= 1:
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        date = m.DateClose
        date = date.replace(m.DateClose.split(' ')[1].split(':')[1], text)
        m.DateClose = date
        m.save()
        SendRaffle(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, f'{get_message(lang, "text100")}', reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewMin) 



@bot.message_handler(content_types=["text"])
def key(message):
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang

    if message.text == get_message(lang, 'text37'):
        if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
            bot.send_message(message.chat.id, get_message(lang,"text23"))
            return

        chn_name = NewUser.get(NewUser.USERID == UID).Selected
        raffle = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == chn_name)

        if raffle.StatusRaffle == 'Published':
            bot.send_message(UID, get_message(lang,"text16"))
            return

        raffle.StatusRaffle = 'Published'
        raffle.save()

        send_user = ChannelList.get(ChannelList.ChannelName == chn_name).ChannelID

        try:

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*[types.InlineKeyboardButton(text = name, url = f'https://t.me/{bot.get_me().username}?start={raffle.ChannelID}') for name in [f'{raffle.ButText}']])

            bot.send_message(send_user, f'{raffle.AboutPresent}', reply_markup=keyboard, parse_mode="Html")
            bot.send_message(UID, get_message(lang,"text15"))
        except:
            bot.send_message(UID, get_message(lang,"text7"))



    if message.text == get_message(lang, 'text35'):
        if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
            bot.send_message(message.chat.id, get_message(lang,"text23"))
            return

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang,"text8"), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewPrice)

    if message.text == get_message(lang, 'text33'):
        if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
            bot.send_message(message.chat.id, get_message(lang,"text23"))
            return
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang,"text9"), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewTextRaffle)

    if message.text == get_message(lang, 'text36'):
        if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
            bot.send_message(message.chat.id, get_message(lang,"text23"))
            return
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang,"text10"), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewTextButton)

    if message.text == get_message(lang, 'text65'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang, 'text70'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewYear)

    if message.text == get_message(lang, 'text66'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang, 'text70'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewMonth)


    if message.text == get_message(lang, 'text67'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang, 'text70'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewDay)


    if message.text == get_message(lang, 'text68'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang, 'text70'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewHour)


    if message.text == get_message(lang, 'text69'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        sent = bot.send_message(UID, get_message(lang, 'text70'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, NewMin)


    if message.text == get_message(lang, 'text34'):
        if not PresentList.select().where(PresentList.USERID==UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == message.chat.id).Selected):
            bot.send_message(message.chat.id, get_message(lang,"text23"))
            return

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text65'),get_message(lang, 'text66'),get_message(lang, 'text67'),get_message(lang, 'text68'),get_message(lang, 'text69'),get_message(lang, 'text101') ]])
        bot.send_message(UID, f'{get_message(lang,"text11")}', reply_markup=keyboard, parse_mode="Html")
        #bot.register_next_step_handler(sent, NewDate)

    if message.text == get_message(lang, 'text62'):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['🇷🇺 Русский', '🇺🇸 English', '🇺🇿 Узбекский']])
        bot.send_message(message.chat.id, get_message(lang, 'text60'), reply_markup=keyboard, parse_mode="Html")


    if message.text == get_message(lang, 'text32'):

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text31')]])
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text62')]])

        bot.send_message(UID, get_message(lang, 'text1'), reply_markup=keyboard, parse_mode="Html")

    if message.text == get_message(lang, 'text29'):

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])

        sent = bot.send_message(UID, get_message(lang,'text13'), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, creatRaffle)

    if message.text == get_message(lang, 'text30') or message.text == get_message(lang, 'text101'):
        editRaffle(message)


    if message.text == get_message(lang, 'text31'):
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, message.text, reply_markup=keyboard, parse_mode="Html")

        my_chat = []
        [ my_chat.append(name.ChannelName) for name in ChannelList.select().where(ChannelList.USERID == UID)]
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text26')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in my_chat])

        bot.send_message(UID, get_message(lang, 'text2'), reply_markup=keyboard, parse_mode="Html")


@bot.callback_query_handler(func=lambda c: True)
def inline(x):
    UID = x.message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    MESSAGE = x.message.message_id

    if x.data in ['🇷🇺 Русский', '🇺🇸 English', '🇺🇿 Узбекский']:
        if x.data == '🇷🇺 Русский':
            a = NewUser.get(NewUser.USERID == UID)
            a.lang = 'ru'
            a.save()


        if x.data == '🇺🇸 English':
            a = NewUser.get(NewUser.USERID == UID)
            a.lang = 'eng'
            a.save()

        if x.data == '🇺🇿 Узбекский':
            a = NewUser.get(NewUser.USERID == UID)
            a.lang = 'uz'
            a.save()

        lang = NewUser.get(NewUser.USERID == UID).lang
        bot.delete_message(chat_id = UID, message_id = MESSAGE)
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, x.data, reply_markup=keyboard, parse_mode="Html")

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text31')]])
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text62')]])
        bot.send_message(UID, get_message(lang, 'text1'), reply_markup=keyboard, parse_mode="Html")


    if x.data == get_message(lang, 'text42'):
        if not PresentList.select().where(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected):
            bot.edit_message_text(chat_id = UID, message_id = MESSAGE, text = get_message(lang,"text21"))
            return


        _all_ = AllMembersRaffle.select().where(AllMembersRaffle.ChannelName == NewUser.get(NewUser.USERID == UID).Selected)
        WinnersCount = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected).WinnersCount
        chaname = NewUser.get(NewUser.USERID == UID)
        import random
        winners = []
        while True:
            if len(_all_) == 0:
                bot.send_message(UID, get_message(lang, 'text25'), parse_mode = 'Html')
                break
            countAll = len(_all_)
            ran = random.randrange(countAll)
            if _all_[ran].USERID not in winners:
                winners.append(_all_[ran].USERID)
            if len(winners) == int(WinnersCount) or len(_all_) < int(WinnersCount):
              break

        for winners in winners:
            usname = bot.get_chat_member(ChannelList.get(ChannelList.USERID == UID, ChannelList.ChannelName == chaname.Selected).ChannelID, winners)
            username = usname.user.first_name
            AboutPresent = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == chaname.Selected).AboutPresent
            code = AllMembersRaffle.get(AllMembersRaffle.USERID == winners, AllMembersRaffle.ChannelName == NewUser.get(NewUser.USERID == UID).Selected).UNtoken

            msg = gettext(lang, 'text2', UID, AboutPresent, 'ChannelName', 'WinnersCount', 'ticket', 'SubCheck', 'CountUser', 'ButText', username, code)
            bot.send_message(UID, msg, parse_mode = 'Html')
            bot.send_message(winners, msg, parse_mode = 'Html')

        cat = PresentList.select().where(PresentList.USERID == UID, PresentList.ChannelName == chaname.Selected)
        for car in cat:
            car.delete_instance()
            car.save()

        cat = AllMembersRaffle.select().where(AllMembersRaffle.ChannelName == chaname.Selected)
        for car in cat:
            car.delete_instance()
            car.save()

    if x.data == get_message(lang, 'text38'):
        if AllMembersRaffle.select().where(AllMembersRaffle.USERID == UID, AllMembersRaffle.ChannelName == NewUser.get(NewUser.USERID == UID).Selected):
            bot.send_message(UID, get_message(lang,"text20"))
            return

        raffle = PresentList.get(PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected)
        ChannelName = raffle.ChannelName
        AboutPresent = raffle.AboutPresent
        ButText = raffle.ButText
        PriceTicket = raffle.PriceTicket
        SubCheck = raffle.SubCheck
        WinnersCount = raffle.WinnersCount
        CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
        if SubCheck == 'On':
            status = ['creator', 'administrator', 'member']
            if bot.get_chat_member(chat_id=ChannelList.get(ChannelList.ChannelID == raffle.ChannelID).ChannelID, user_id=x.message.chat.id).status in status:
        
                if int(PriceTicket) == 0:
                    if not AllMembersRaffle.row_exists(UID, NewUser.get(NewUser.USERID == UID).Selected):
                      AllMembersRaffle.creat_row(UID, NewUser.get(NewUser.USERID == UID).Selected)

                    import random

                    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                    for n in range(1):
                        password =''
                        for i in range(15):
                            password += random.choice(chars)


                    a = AllMembersRaffle.get(AllMembersRaffle.USERID == UID)
                    a.UNtoken = password
                    a.save()

                    bot.send_message(UID, f'{get_message(lang,"text18")}\n\n{get_message(lang,"text19")}:')
                    bot.send_message(UID, f'{password}')
                    return

                #keyboard = types.InlineKeyboardMarkup(row_width=2)
                #keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['Visa/MasterCard']])
                #bot.edit_message_text(chat_id = UID, message_id = MESSAGE, text = , reply_markup = keyboard, parse_mode = 'Html')
                
                PRICE = [ 
                types.LabeledPrice(label='Raffle', amount= 100 * int(PriceTicket) ),
                ]

                bot.send_invoice(x.message.chat.id,
                                   title=ChannelName,
                                   description={AboutPresent},
                                   provider_token= token_pay,
                                   currency= 'usd',
                                   prices= PRICE,
                                   start_parameter='time-machine-example',
                                   invoice_payload = 'asdsad')


                    
            else:

                keyboard = types.InlineKeyboardMarkup(row_width=2)
                keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text38')]])
                msg = gettext(lang, 'text5', 'DateClose', AboutPresent, ChannelList.get(ChannelList.ChannelID == raffle.ChannelID).ChannelName, WinnersCount, 'ticket', SubCheck, CountUser, ButText, '', '')
                bot.edit_message_text(chat_id = UID, message_id = MESSAGE,text = msg, reply_markup = keyboard, parse_mode = 'Html')
                

        else:
            if int(PriceTicket) == 0:
                if not AllMembersRaffle.row_exists(UID, NewUser.get(NewUser.USERID == UID).Selected):
                  AllMembersRaffle.creat_row(UID, NewUser.get(NewUser.USERID == UID).Selected)

                import random

                chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                for n in range(1):
                    password =''
                    for i in range(15):
                        password += random.choice(chars)


                a = AllMembersRaffle.get(AllMembersRaffle.USERID == UID)
                a.UNtoken = password
                a.save()

                bot.send_message(UID, f'{get_message(lang,"text18")}\n\n{get_message(lang,"text19")}:')
                bot.send_message(UID, f'{password}')
                return


            PRICE = [ 
            types.LabeledPrice(label='Raffle', amount= 100 * int(PriceTicket) ),
            ]

            bot.send_invoice(x.message.chat.id,
                               title=ChannelName,
                               description={AboutPresent},
                               provider_token= token_pay,
                               currency= 'usd',
                               prices= PRICE,
                               start_parameter='time-machine-example',
                               invoice_payload = 'asdsad')


    if x.data == get_message(lang, 'text62'):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in ['🇷🇺 Русский', '🇺🇸 English', '🇺🇿 Узбекский']])
        bot.send_message(UID, get_message(lang, 'text60'), reply_markup=keyboard, parse_mode="Html")

    if x.data == get_message(lang, 'text39') or x.data == get_message(lang, 'text40') or x.data == get_message(lang, 'text41'):
        m = PresentList.get(PresentList.USERID == UID, PresentList.ChannelName == NewUser.get(NewUser.USERID == UID).Selected )
        if x.data == get_message(lang, 'text39'):
            
            if m.WinnersCount == '1':
                return 
            else:
                new_m = int(m.WinnersCount) - 1
                m.WinnersCount = new_m
                m.save()

        if x.data == get_message(lang, 'text40'):
            new_m = int(m.WinnersCount) + 1
            m.WinnersCount = new_m
            m.save()

        if x.data == get_message(lang, 'text41'):
            if m.SubCheck == 'On':
                m.SubCheck = 'Off'
                m.save()
            elif m.SubCheck == 'Off':
                m.SubCheck = 'On'
                m.save()

        new = PresentList.get(PresentList.USERID == x.message.chat.id, PresentList.ChannelName == NewUser.get(NewUser.USERID == x.message.chat.id).Selected)
        DateClose = new.DateClose
        ChannelName = new.ChannelName
        WinnersCount = new.WinnersCount
        SubCheck = new.SubCheck
        CountUser = len( AllMembersRaffle.select().where(  AllMembersRaffle.ChannelName == ChannelName  ) )
        ticket = new.PriceTicket
        AboutPresent = new.AboutPresent
        ButText = new.ButText
        
        msg = gettext(lang, 'text3', DateClose, AboutPresent, ChannelName, WinnersCount, ticket, SubCheck, CountUser, ButText, '', '')
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text39'), get_message(lang, 'text40')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text41')]])
        if new.StatusRaffle == 'Published':
            keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text42')]])
        bot.edit_message_text(chat_id = UID, message_id = MESSAGE, text = msg, reply_markup=keyboard, parse_mode="Html")




    if x.data == get_message(lang, 'text26'):

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text27')]])
        
        sent = bot.send_message(chat_id = UID, text = get_message(lang,"text6"), reply_markup=keyboard, parse_mode="Html")
        bot.register_next_step_handler(sent, AddChat)

    my_channel = []
    for name in ChannelList.select().where(ChannelList.USERID == UID):
        if name.ChannelName not in my_channel:
          my_channel.append(name.ChannelName)


    if x.data in my_channel:
        sel = NewUser.get(NewUser.USERID == UID)
        sel.Selected = x.data
        sel.save()


        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text29')]])
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text30')]])
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text32')]])

        bot.send_message(chat_id = UID, text = f'{ get_message(lang,"text5") } {x.data}', reply_markup=keyboard, parse_mode="Html")


def AddChat(message):
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if message.text == get_message(lang, 'text27'):
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, message.text, reply_markup=keyboard, parse_mode="Html")

        my_chat = []
        [ my_chat.append(name.ChannelName) for name in ChannelList.select().where(ChannelList.USERID == UID)]
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text26')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in my_chat])

        bot.send_message(UID, get_message(lang,'text2'), reply_markup=keyboard, parse_mode="Html")
        return

    if message.forward_from_chat != None:
        ChannelID = message.forward_from_chat.id
        ChannelName = message.forward_from_chat.title

        if not ChannelList.row_exists(UID, ChannelID, ChannelName):
            ChannelList.creat_row(UID, ChannelID, ChannelName)

        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, str(get_message(lang,'text3')) +' '+str(ChannelName), reply_markup=keyboard, parse_mode="Html")
        my_chat = []
        [ my_chat.append(name.ChannelName) for name in ChannelList.select().where(ChannelList.USERID == UID)]
        
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in [get_message(lang, 'text26')]])
        keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name) for name in my_chat])

        bot.send_message(UID, get_message(lang,'text2'), reply_markup=keyboard, parse_mode="Html")

    else:
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(UID, get_message(lang, 'text28'), reply_markup=keyboard, parse_mode="Html")

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(*[types.KeyboardButton(name) for name in [get_message(lang, 'text31')]])
        bot.send_message(UID, get_message(lang,'text4'), reply_markup=keyboard, parse_mode="Html")





@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def process_successful_payment(message):
    UID = message.chat.id
    lang = NewUser.get(NewUser.USERID == UID).lang
    if not AllMembersRaffle.row_exists(UID, NewUser.get(NewUser.USERID == UID).Selected):
      AllMembersRaffle.creat_row(UID, NewUser.get(NewUser.USERID == UID).Selected)

    import random

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for n in range(1):
        password =''
        for i in range(15):
            password += random.choice(chars)


    a = AllMembersRaffle.get(AllMembersRaffle.USERID == UID)
    a.UNtoken = password
    a.save()

    bot.send_message(UID, f'{get_message(lang,"text18")}\n\n{get_message(lang,"text19")}:')
    bot.send_message(UID, f'{password}')



def gettext(lang, key, DateClose, AboutPresent, ChannelName, WinnersCount, ticket, SubCheck, CountUser, ButText, username, code):
      dictionary = {
        'text1': f'{get_message(lang, "text14")}\n{get_message(lang, "text44")}: {DateClose}\n\n{get_message(lang, "text45")}: {AboutPresent}\n{get_message(lang, "text46")}: {ChannelName}\n{get_message(lang, "text47")}: {WinnersCount}\n{get_message(lang, "text48")}: {ticket} $\n{get_message(lang, "text49")}: {SubCheck}\n{get_message(lang, "text50")}: ({CountUser}) {ButText}',
        'text2': f'{get_message(lang, "text45")}: {AboutPresent}\n\n{get_message(lang, "text51")}: <a href="tg://user?id={DateClose}">{username}</a>\n{get_message(lang, "text52")}: <code>{ code }</code>',
        'text3': f'{get_message(lang, "text14")}\n{get_message(lang, "text44")}: {DateClose}\n\n{get_message(lang, "text45")}: {AboutPresent}\n{get_message(lang, "text46")}: {ChannelName}\n{get_message(lang, "text47")}: {WinnersCount}\n{get_message(lang, "text48")}: {ticket} $\n{get_message(lang, "text49")}: {SubCheck}\n{get_message(lang, "text50")}: ({CountUser}) {ButText}',
        'text4': f'{get_message(lang, "text44")}: {DateClose}\n{get_message(lang, "text48")}: {ticket}\n{get_message(lang, "text53")}: {WinnersCount}\n\n{AboutPresent}',
        'text5': f'❗️{get_message(lang,"text17")}: {ChannelName}\n\n{AboutPresent}',
      }
      return dictionary[key]



if __name__ == '__main__':
    bot.polling(none_stop=True)
