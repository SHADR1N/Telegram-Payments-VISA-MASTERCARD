import configparser


def get_message(lang ,key):
    if lang == 'eng':

          config = configparser.ConfigParser()
          config.read(f"bot_text.ini", encoding="utf8")
          text1 = config['configENG']['text1']
          text2 = config['configENG']['text2']
          text3 = config['configENG']['text3']
          text4 = config['configENG']['text4']
          text5 = config['configENG']['text5']
          text6 = config['configENG']['text6']
          text7 = config['configENG']['text7']
          text8 = config['configENG']['text8']
          text9 = config['configENG']['text9']
          text10 = config['configENG']['text10']
          text11 = config['configENG']['text11']
          text12 = config['configENG']['text12']
          text13 = config['configENG']['text13']
          text14 = config['configENG']['text14']
          text15 = config['configENG']['text15']
          text16 = config['configENG']['text16']
          text17 = config['configENG']['text17']
          text18 = config['configENG']['text18']
          text19 = config['configENG']['text19']
          text20 = config['configENG']['text20']
          text21 = config['configENG']['text21']
          text22 = config['configENG']['text22']
          text23 = config['configENG']['text23']
          text24 = config['configENG']['text24']
          text25 = config['configENG']['text25']
          text26 = config['configENG']['text26']
          text27 = config['configENG']['text27']
          text28 = config['configENG']['text28']
          text29 = config['configENG']['text29']
          text30 = config['configENG']['text30']
          text31 = config['configENG']['text31']
          text32 = config['configENG']['text32']
          text33 = config['configENG']['text33']
          text34 = config['configENG']['text34']
          text35 = config['configENG']['text35']
          text36 = config['configENG']['text36']
          text37 = config['configENG']['text37']
          text38 = config['configENG']['text38']
          text39 = config['configENG']['text39']
          text40 = config['configENG']['text40']
          text41 = config['configENG']['text41']
          text42 = config['configENG']['text42']
          text43 = config['configENG']['text43']
          text44 = config['configENG']['text44']
          text45 = config['configENG']['text45']
          text46 = config['configENG']['text46']
          text47 = config['configENG']['text47']
          text48 = config['configENG']['text48']
          text49 = config['configENG']['text49']
          text50 = config['configENG']['text50']
          text51 = config['configENG']['text51']
          text52 = config['configENG']['text52']
          text53 = config['configENG']['text53']

          text60 = config['configENG']['text60']
          text62 = config['configENG']['text62']
          text70 = config['configENG']['text70']
          text65 = config['configENG']['text65']
          text66 = config['configENG']['text66']
          text67 = config['configENG']['text67']
          text68 = config['configENG']['text68']
          text69 = config['configENG']['text69']
          text100 = config['configENG']['text100']
          text101 = config['configENG']['text101']


          dictionary = {
               'text1': text1,               'text2': text2,               'text3': text3,               'text4': text4,
               'text5': text5,               'text6': text6,               'text7': text7,               'text8': text8,
               'text9': text9,               'text10': text10,               'text11': text11,               'text12': text12,
               'text13': text13,               'text14': text14,               'text15': text15,               'text16': text16,
               'text17': text17,               'text18': text18,               'text19': text19,               'text20': text20,
               'text21': text21,               'text22': text22,               'text23': text23,               'text24': text24,
               'text25': text25,               'text26': text26,               'text27': text27,               'text28': text28,
               'text29': text29,               'text30': text30,               'text31': text31,               'text32': text32,
               'text33': text33,               'text34': text34,               'text35': text35,               'text36': text36,
               'text37': text37,               'text38': text38,               'text39': text39,               'text40': text40,
               'text41': text41,               'text42': text42,               'text43': text43,               'text44': text44,
               'text45': text45,               'text46': text46,               'text47': text47,               'text48': text48,
               'text49': text49,               'text50': text50,               'text51': text51,               'text52': text52,
               'text53': text53,               'text60': text60,               'text62': text62,               'text70': text70,
               'text65': text65,               'text66': text66,               'text67': text67,               'text68': text68,
               'text69': text69,               'text100': text100,               'text101': text101,
          }

          return dictionary[key]


    if lang == 'ru':
          config = configparser.ConfigParser()
          config.read(f"bot_text.ini", encoding="utf8")
          text1 = config['configRU']['text1']
          text2 = config['configRU']['text2']
          text3 = config['configRU']['text3']
          text4 = config['configRU']['text4']
          text5 = config['configRU']['text5']
          text6 = config['configRU']['text6']
          text7 = config['configRU']['text7']
          text8 = config['configRU']['text8']
          text9 = config['configRU']['text9']
          text10 = config['configRU']['text10']
          text11 = config['configRU']['text11']
          text12 = config['configRU']['text12']
          text13 = config['configRU']['text13']
          text14 = config['configRU']['text14']
          text15 = config['configRU']['text15']
          text16 = config['configRU']['text16']
          text17 = config['configRU']['text17']
          text18 = config['configRU']['text18']
          text19 = config['configRU']['text19']
          text20 = config['configRU']['text20']
          text21 = config['configRU']['text21']
          text22 = config['configRU']['text22']
          text23 = config['configRU']['text23']
          text24 = config['configRU']['text24']
          text25 = config['configRU']['text25']
          text26 = config['configRU']['text26']
          text27 = config['configRU']['text27']
          text28 = config['configRU']['text28']
          text29 = config['configRU']['text29']
          text30 = config['configRU']['text30']
          text31 = config['configRU']['text31']
          text32 = config['configRU']['text32']
          text33 = config['configRU']['text33']
          text34 = config['configRU']['text34']
          text35 = config['configRU']['text35']
          text36 = config['configRU']['text36']
          text37 = config['configRU']['text37']
          text38 = config['configRU']['text38']
          text39 = config['configRU']['text39']
          text40 = config['configRU']['text40']
          text41 = config['configRU']['text41']
          text42 = config['configRU']['text42']
          text43 = config['configRU']['text43']
          text44 = config['configRU']['text44']
          text45 = config['configRU']['text45']
          text46 = config['configRU']['text46']
          text47 = config['configRU']['text47']
          text48 = config['configRU']['text48']
          text49 = config['configRU']['text49']
          text50 = config['configRU']['text50']
          text51 = config['configRU']['text51']
          text52 = config['configRU']['text52']
          text53 = config['configRU']['text53']

          text60 = config['configRU']['text60']
          text62 = config['configRU']['text62']
          text70 = config['configRU']['text70']
          text65 = config['configRU']['text65']
          text66 = config['configRU']['text66']
          text67 = config['configRU']['text67']
          text68 = config['configRU']['text68']
          text69 = config['configRU']['text69']
          text100 = config['configRU']['text100']
          text101 = config['configRU']['text101']

          dictionary = {
               'text1': text1,               'text2': text2,               'text3': text3,               'text4': text4,
               'text5': text5,               'text6': text6,               'text7': text7,               'text8': text8,
               'text9': text9,               'text10': text10,               'text11': text11,               'text12': text12,
               'text13': text13,               'text14': text14,               'text15': text15,               'text16': text16,
               'text17': text17,               'text18': text18,               'text19': text19,               'text20': text20,
               'text21': text21,               'text22': text22,               'text23': text23,               'text24': text24,
               'text25': text25,               'text26': text26,               'text27': text27,               'text28': text28,
               'text29': text29,               'text30': text30,               'text31': text31,               'text32': text32,
               'text33': text33,               'text34': text34,               'text35': text35,               'text36': text36,
               'text37': text37,               'text38': text38,               'text39': text39,               'text40': text40,
               'text41': text41,               'text42': text42,               'text43': text43,               'text44': text44,
               'text45': text45,               'text46': text46,               'text47': text47,               'text48': text48,
               'text49': text49,               'text50': text50,               'text51': text51,               'text52': text52,
               'text53': text53,               'text60': text60,               'text62': text62,               'text70': text70,
               'text65': text65,               'text66': text66,               'text67': text67,               'text68': text68,
               'text69': text69,               'text100': text100,               'text101': text101,
          }

          return dictionary[key]

    if lang == 'uz':
          config = configparser.ConfigParser()
          config.read(f"bot_text.ini", encoding="utf8")
          text1 = config['configUZ']['text1']
          text2 = config['configUZ']['text2']
          text3 = config['configUZ']['text3']
          text4 = config['configUZ']['text4']
          text5 = config['configUZ']['text5']
          text6 = config['configUZ']['text6']
          text7 = config['configUZ']['text7']
          text8 = config['configUZ']['text8']
          text9 = config['configUZ']['text9']
          text10 = config['configUZ']['text10']
          text11 = config['configUZ']['text11']
          text12 = config['configUZ']['text12']
          text13 = config['configUZ']['text13']
          text14 = config['configUZ']['text14']
          text15 = config['configUZ']['text15']
          text16 = config['configUZ']['text16']
          text17 = config['configUZ']['text17']
          text18 = config['configUZ']['text18']
          text19 = config['configUZ']['text19']
          text20 = config['configUZ']['text20']
          text21 = config['configUZ']['text21']
          text22 = config['configUZ']['text22']
          text23 = config['configUZ']['text23']
          text24 = config['configUZ']['text24']
          text25 = config['configUZ']['text25']
          text26 = config['configUZ']['text26']
          text27 = config['configUZ']['text27']
          text28 = config['configUZ']['text28']
          text29 = config['configUZ']['text29']
          text30 = config['configUZ']['text30']
          text31 = config['configUZ']['text31']
          text32 = config['configUZ']['text32']
          text33 = config['configUZ']['text33']
          text34 = config['configUZ']['text34']
          text35 = config['configUZ']['text35']
          text36 = config['configUZ']['text36']
          text37 = config['configUZ']['text37']
          text38 = config['configUZ']['text38']
          text39 = config['configUZ']['text39']
          text40 = config['configUZ']['text40']
          text41 = config['configUZ']['text41']
          text42 = config['configUZ']['text42']
          text43 = config['configUZ']['text43']
          text44 = config['configUZ']['text44']
          text45 = config['configUZ']['text45']
          text46 = config['configUZ']['text46']
          text47 = config['configUZ']['text47']
          text48 = config['configUZ']['text48']
          text49 = config['configUZ']['text49']
          text50 = config['configUZ']['text50']
          text51 = config['configUZ']['text51']
          text52 = config['configUZ']['text52']
          text53 = config['configUZ']['text53']

          text60 = config['configUZ']['text60']
          text62 = config['configUZ']['text62']
          text70 = config['configUZ']['text70']
          text65 = config['configUZ']['text65']
          text66 = config['configUZ']['text66']
          text67 = config['configUZ']['text67']
          text68 = config['configUZ']['text68']
          text69 = config['configUZ']['text69']
          text100 = config['configUZ']['text100']
          text101 = config['configUZ']['text101']

          dictionary = {
               'text1': text1,               'text2': text2,               'text3': text3,               'text4': text4,
               'text5': text5,               'text6': text6,               'text7': text7,               'text8': text8,
               'text9': text9,               'text10': text10,               'text11': text11,               'text12': text12,
               'text13': text13,               'text14': text14,               'text15': text15,               'text16': text16,
               'text17': text17,               'text18': text18,               'text19': text19,               'text20': text20,
               'text21': text21,               'text22': text22,               'text23': text23,               'text24': text24,
               'text25': text25,               'text26': text26,               'text27': text27,               'text28': text28,
               'text29': text29,               'text30': text30,               'text31': text31,               'text32': text32,
               'text33': text33,               'text34': text34,               'text35': text35,               'text36': text36,
               'text37': text37,               'text38': text38,               'text39': text39,               'text40': text40,
               'text41': text41,               'text42': text42,               'text43': text43,               'text44': text44,
               'text45': text45,               'text46': text46,               'text47': text47,               'text48': text48,
               'text49': text49,               'text50': text50,               'text51': text51,               'text52': text52,
               'text53': text53,               'text60': text60,               'text62': text62,               'text70': text70,
               'text65': text65,               'text66': text66,               'text67': text67,               'text68': text68,
               'text69': text69,               'text100': text100,               'text101': text101,
          }
          return dictionary[key]