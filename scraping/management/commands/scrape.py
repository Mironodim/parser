from django.core.management.base import BaseCommand
import requests
import datetime
from bs4 import BeautifulSoup
from scraping.models import Job
import csv


class MyBetting:
    def my_data(self):
        intelligence = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'accept': '*/*'
        }
        link = []
        link1 = []
        a = 0
        while a <= 35:
            url = f'https://www.marathonbet.ru/su/popular/Football+-+11?page={a}'
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            try:
                cotent = soup.find_all('a', class_='member-link')
                cotent = cotent[::2]
                for i in cotent:
                    link.append(f"https://www.marathonbet.ru{i.get('href')}")
            except AttributeError:
                link = []
            a += 1
        for i in link:
            if i[:70] == 'https://www.marathonbet.ru/su/betting/Football/England/Premier+League/':
                link1.append(i)
            if i[:84] == 'https://www.marathonbet.ru/su/betting/Football/Republic+of+Ireland/Premier+Division/':
                link1.append(i)
            if i[:75] == 'https://www.marathonbet.ru/su/betting/Football/Internationals/Copa+America/':
                link1.append(i)
            elif i[:72] == 'https://www.marathonbet.ru/su/betting/Football/Internationals/UEFA+Euro/':
                link1.append(i)
            elif i[:72] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/CONCACAF+Champions+League/':  # gggggg
                link1.append(i)
            elif i[:81] == 'https://www.marathonbet.ru/su/betting/Football/Internationals/UEFA+Nations+Leagu/':
                link1.append(i)
            elif i[:90] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/CAF+Confederation+Cup/':  # dfgh
                link1.append(i)
            elif i[:90] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/UEFA+Champions+League/':  # ecnm
                link1.append(i)
            elif i[:87] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/UEFA+Europa+League/':  # hhgfghgf
                link1.append(i)
            elif i[:86] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/Copa+Libertadores/':  # ghjj
                link1.append(i)
            elif i[:58] == 'https://www.marathonbet.ru/su/betting/Football/Russia/FNL/':  # ghjj
                link1.append(i)
            elif i[:85] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/Sudamericana+Cup/':  # есть
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Peru/Liga+1/':  # есть
                link1.append(i)
            elif i[:89] == 'https://www.marathonbet.ru/su/betting/Football/Clubs.+International/AFC+Champions+League/':  # ghjjj
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Russia/Premier+League/':
                link1.append(i)
            elif i[:58] == 'https://www.marathonbet.ru/su/betting/Football/Russia/Cup/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/England/FA+Cup/':
                link1.append(i)
            elif i[:64] == 'https://www.marathonbet.ru/su/betting/Football/England/League+1/':
                link1.append(i)
            elif i[:64] == 'https://www.marathonbet.ru/su/betting/Football/England/League+2/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Germany/3+Liga/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Germany/Bundesliga/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/England/Championship/':
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Germany/Cup/':
                link1.append(i)
            elif i[:71] == 'https://www.marathonbet.ru/su/betting/Football/Belarus/Vysshaya+League/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Germany/Bundesliga+2/':  # dfghj
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Spain/Primera+Division/':  # hghg
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Spain/Segunda+Division/':
                link1.append(i)
            elif i[:61] == 'https://www.marathonbet.ru/su/betting/Football/Italy/Serie+A/':
                link1.append(i)
            elif i[:57] == 'https://www.marathonbet.ru/su/betting/Football/Italy/Cup/':
                link1.append(i)
            elif i[:61] == 'https://www.marathonbet.ru/su/betting/Football/Italy/Serie+B/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/France/Ligue+1/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/France/Ligue+2/':  # fghjk
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Australia/A-League/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Austria/Bundesliga/':  # fghjk
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Austria/Cup/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Argentina/League+Cup/':
                link1.append(i)
            elif i[:74] == 'https://www.marathonbet.ru/su/betting/Football/Argentina/Primera+Nacional/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Armenia/Premier+League/':
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Armenia/Cup/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Belgium/1st+Division+A/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Bulgaria/1st+League/':
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Hungary/Cup/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Greece/Super+League/':
                link1.append(i)
            elif i[:58] == 'https://www.marathonbet.ru/su/betting/Football/Greece/Cup/':
                link1.append(i)
            elif i[:65] == 'https://www.marathonbet.ru/su/betting/Football/Denmark/Superliga/':
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Denmark/Cup/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Egypt/Premier+League/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Israel/Premier+League/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Israel/Liga+Leumit/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Austria/2+Liga/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Kazakhstan/Premier+League/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Cyprus/1st+Division/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/China+PR/Super+League/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/China+PR/League+One/':
                link1.append(i)
            elif i[:63] == 'https://www.marathonbet.ru/su/betting/Football/Latvia/Virsliga/':
                link1.append(i)
            elif i[:71] == 'https://www.marathonbet.ru/su/betting/Football/Mexico/Primera+Division/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Netherlands/Eredivisie/':
                link1.append(i)
            elif i[:74] == 'https://www.marathonbet.ru/su/betting/Football/Netherlands/Eerste+Divisie/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Paraguay/Primera+A/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Poland/Ekstraklasa/':
                link1.append(i)
            elif i[:58] == 'https://www.marathonbet.ru/su/betting/Football/Poland/Cup/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Portugal/Primeira+Liga/':  # oiuyty
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Portugal/Segunda+Liga/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Korea+Republic/K+League+1/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Romania/Liga+I/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Slovenia/1st+League/':
                link1.append(i)
            elif i[:55] == 'https://www.marathonbet.ru/su/betting/Football/USA/MLS/':
                link1.append(i)
            elif i[:64] == 'https://www.marathonbet.ru/su/betting/Football/Turkey/Super+Lig/':  # iuyt
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Ukraine/Premier+League/':  # dfghj
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Finland/Veikkausliiga/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Croatia/1st+League/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Czech+Republic/1st+League/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Chile/Primera+Division/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Sweden/Allsvenskan/':
                link1.append(i)
            elif i[:58] == 'https://www.marathonbet.ru/su/betting/Football/Sweden/Cup/':
                link1.append(i)
            elif i[:65] == 'https://www.marathonbet.ru/su/betting/Football/Sweden/Superettan/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Scotland/Premiership/':
                link1.append(i)
            elif i[:63] == 'https://www.marathonbet.ru/su/betting/Football/Scotland/FA+Cup/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Scotland/Championship/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Japan/J.League/Division+1/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Japan/J.League/Division+2/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Japan/League+Cup/':
                link1.append(i)
            elif i[:81] == 'https://www.marathonbet.ru/su/popular/Football/Australia/National+Premier+League/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Azerbaijan/Cup/':
                link1.append(i)
            elif i[:60] == 'https://www.marathonbet.ru/su/betting/Football/Hungary/NB+I/':
                link1.append(i)
            elif i[:74] == 'https://www.marathonbet.ru/su/betting/Football/Venezuela/Primera+Division/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Denmark/1st+Division/':
                link1.append(i)
            elif i[:57] == 'https://www.marathonbet.ru/su/betting/Football/Egypt/Cup/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Colombia/Primera+B/':
                link1.append(i)
            elif i[:64] == 'https://www.marathonbet.ru/su/betting/Football/Lithuania/A+Lyga/':
                link1.append(i)
            elif i[:71] == 'https://www.marathonbet.ru/su/betting/Football/Saudi+Arabia/Pro+League/':
                link1.append(i)
            elif i[:65] == 'https://www.marathonbet.ru/su/betting/Football/Serbia/Super+Liga/':
                link1.append(i)
            elif i[:60] == 'https://www.marathonbet.ru/su/betting/Football/Slovakia/Cup/':
                link1.append(i)
            elif i[:62] == 'https://www.marathonbet.ru/su/betting/Football/Kazakhstan/Cup/':
                link1.append(i)
            elif i[:73] == 'https://www.marathonbet.ru/su/betting/Football/Korea+Republic/K+League+2/':
                link1.append(i)
            elif i[:76] == 'https://www.marathonbet.ru/su/betting/Football/Northern+Ireland/Premiership/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Slovakia/Fortuna+Liga/':
                link1.append(i)
            elif i[:60] == 'https://www.marathonbet.ru/su/betting/Football/Turkey/1+Lig/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Wales/Premier+League/':
                link1.append(i)
            elif i[:63] == 'https://www.marathonbet.ru/su/betting/Football/France/National/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Czech+Republic/FNL/':
                link1.append(i)
            elif i[:72] == 'https://www.marathonbet.ru/su/betting/Football/Switzerland/Super+League/':
                link1.append(i)
            elif i[:76] == 'https://www.marathonbet.ru/su/betting/Football/Switzerland/Challenge+League/':
                link1.append(i)
            elif i[:72] == 'https://www.marathonbet.ru/su/betting/Football/Mexico/Liga+de+Expansion/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Colombia/Primera+A/':
                link1.append(i)
            elif i[:80] == 'https://www.marathonbet.ru/su/betting/Football/Republic+of+Ireland/1st+Division/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Iceland/Premier+League/':
                link1.append(i)
            elif i[:71] == 'https://www.marathonbet.ru/su/betting/Football/England/National+League/':
                link1.append(i)
            elif i[:60] == 'https://www.marathonbet.ru/su/betting/Football/Bolivia/LFPB/':
                link1.append(i)
            elif i[:70] == 'https://www.marathonbet.ru/su/betting/Football/Bosnia+and+Herzegovina/':
                link1.append(i)
            elif i[:68] == 'https://www.marathonbet.ru/su/betting/Football/Germany/Regionalliga/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Jordan/Premier+League/':
                link1.append(i)
            elif i[:72] == 'https://www.marathonbet.ru/su/betting/Football/Spain/Segunda+Division+B/':
                link1.append(i)
            elif i[:66] == 'https://www.marathonbet.ru/su/betting/Football/Qatar/Stars+League/':
                link1.append(i)
            elif i[:75] == 'https://www.marathonbet.ru/su/betting/Football/Costa+Rica/Primera+Division/':
                link1.append(i)
            elif i[:69] == 'https://www.marathonbet.ru/su/betting/Football/Malaysia/Super+League/':
                link1.append(i)
            elif i[:59] == 'https://www.marathonbet.ru/su/betting/Football/Morocco/Cup/':
                link1.append(i)
            elif i[:71] == 'https://www.marathonbet.ru/su/betting/Football/UAE/Arabian+Gulf+League/':
                link1.append(i)
            elif i[:67] == 'https://www.marathonbet.ru/su/betting/Football/Russia/2nd+Division/':
                link1.append(i)
            elif i[:65] == 'https://www.marathonbet.ru/su/betting/Football/Scotland/League+1/':
                link1.append(i)
            elif i[:63] == 'https://www.marathonbet.ru/su/betting/Football/Ecuador/Serie+A/':
                link1.append(i)
            elif i[:75] == 'https://www.marathonbet.ru/su/betting/Football/South+Africa/Premier+League/':
                link1.append(i)

        print(f'Всего {len(link1)} ')
        link1 = list(set(link1))
        print(f'Мои {len(link1)}')
        my_day = ''
        score_1 = ''
        score_2 = ''
        score1t_1 = ''
        score1t_2 = ''
        items1 = ''
        items2 = ''
        my_time = ''
        strana = ''
        championat = ''
        p1 = ''
        x = ''
        p2 = ''
        f1_0 = ''
        f2_0 = ''
        p1x = ''
        xp2 = ''
        tm = ''
        tb = ''
        oz = ''
        p1_p1 = ''
        x_p1 = ''
        p2_p1 = ''
        p1_x = ''
        x_x = ''
        p2_x = ''
        p1_p2 = ''
        x_p2 = ''
        p2_p2 = ''
        a = 1
        data1 = datetime.date.today()

        for i in link1:
            r = requests.get(i, 'html.parser')
            soup = BeautifulSoup(r.content, 'html.parser')
            try:
                strana1 = soup.find('h1', class_='category-label')
                strana1 = strana1.find_all('span', class_='nowrap')
                strana = strana1[0].text
                strana = strana.replace('.', '')
                championat = strana1[1].text
            except AttributeError:
                strana = ''
                championat = ''
            try:
                items = soup.find('table', class_='member-area-content-table')
                items = items.find_all('span')
                items1 = items[0]
                items2 = items[1]
                items1 = items1.text
                items2 = items2.text
            except AttributeError:
                items1 = ''
                items2 = ''
            soup2 = soup.find('div', class_='category-container')
            try:
                time = soup.find('td', class_='date').getText()
                time = time.strip()
                if len(time) == 5:
                    my_time = f'{data1} {time}'
                    my_day = datetime.datetime.today().isoweekday()
                    if my_day == 1:
                        my_day = 'ПН'
                    elif my_day == 2:
                        my_day = 'ВТ'
                    elif my_day == 3:
                        my_day = 'СР'
                    elif my_day == 4:
                        my_day = 'ЧТ'
                    elif my_day == 5:
                        my_day = 'ПТ'
                    elif my_day == 6:
                        my_day = 'СБ'
                    elif my_day == 7:
                        my_day = 'ВС'
                elif len(time) > 5:
                    time2 = datetime.date.today() + datetime.timedelta(days=1)
                    my_time = f'{time2} {time[7:]}'
                    my_day = datetime.datetime.today().isoweekday() + 1
                    if my_day == 1:
                        my_day = 'ПН'
                    elif my_day == 2:
                        my_day = 'ВТ'
                    elif my_day == 3:
                        my_day = 'СР'
                    elif my_day == 4:
                        my_day = 'ЧТ'
                    elif my_day == 5:
                        my_day = 'ПТ'
                    elif my_day == 6:
                        my_day = 'СБ'
                    elif my_day == 7:
                        my_day = 'ВС'
                    elif my_day == 8:
                        my_day = 'ПН'
            except AttributeError:
                my_time = ''
                my_day = ''
            try:
                text44 = soup.find('div', attrs={'data-mutable-id': "MG236_-1953818769"})
            except AttributeError:
                text44 = []
            try:
                text8 = text44.find_all('tr', attrs={'data-header-highlighted-bounded': "true"})
            except AttributeError:
                text8 = []
            # text6 = text1.find_all('div')
            a = []
            for i in text8:
                a.append(i.text)
            a = ','.join(a)
            a = a.replace("\n", "").replace('(', '').replace(')', '')
            a1 = a.split(',')
            aaa = ''
            try:
                for int in a1:
                    if int[1] == '0':
                        aaa = int
                f1_0 = aaa[3:8].strip(' ')
                f2_0 = aaa[-5:].strip(' ')
            except IndexError:
                f1_0 = []
                f2_0 = []

            g = soup2.find_all('span', class_="selection-link active-selection")
            for i in g:
                try:
                    if '@Match_Result.1' in str(i):
                        p1 = ''.join(i)
                except:
                    p1 = ''
                try:
                    if '@Match_Result.draw' in str(i):
                        x = ''.join(i)
                except:
                    x = ''
                try:
                    if '@Match_Result.3' in str(i):
                        p2 = ''.join(i)
                except:
                    p2 = ''
                try:
                    if '@Result.HD' in str(i):
                        p1x = ''.join(i)
                except:
                    p1x = ''
                try:
                    if '@Result.AD' in str(i):
                        xp2 = ''.join(i)
                except:
                    xp2 = ''
                try:
                    if '@Both_Teams_To_Score.yes' in str(i):
                        oz = ''.join(i)
                except:
                    oz = ''
                try:
                    if '@1st_Half___Full_Time.HH' in str(i):
                        p1_p1 = ''.join(i)
                except:
                    p1_p1 = ''
                try:
                    if '@1st_Half___Full_Time.DH' in str(i):
                        x_p1 = ''.join(i)
                except:
                    x_p1 = ''
                try:
                    if '@1st_Half___Full_Time.AH' in str(i):
                        p2_p1 = ''.join(i)
                except:
                    p2_p1 = ''
                try:
                    if '@1st_Half___Full_Time.HD' in str(i):
                        p1_x = ''.join(i)
                except:
                    p1_x = ''
                try:
                    if '@1st_Half___Full_Time.DD' in str(i):
                        x_x = ''.join(i)
                except:
                    x_x = ''
                try:
                    if '@1st_Half___Full_Time.AD' in str(i):
                        p2_x = ''.join(i)
                except:
                    p2_x = ''
                try:
                    if '@1st_Half___Full_Time.HA' in str(i):
                        p1_p2 = ''.join(i)
                except:
                    p1_p2 = ''
                try:
                    if '@1st_Half___Full_Time.DA' in str(i):
                        x_p2 = ''.join(i)
                except:
                    x_p2 = ''
                try:
                    if '@1st_Half___Full_Time.AA' in str(i):
                        p2_p2 = ''.join(i)
                except:
                    p2_p2 = ''
                try:
                    if '@Total_Goals.Under_2.5' in str(i):
                        tm = ''.join(i)
                except:
                    tm = ''
                try:
                    if '@Total_Goals0.Under_2.5' in str(i):
                        tm = ''.join(i)
                except:
                    tm = ''
                try:
                    if '@Total_Goals.Over_2.5' in str(i):
                        tb = ''.join(i)
                except:
                    tb = ''
                try:
                    if '@Total_Goals0.Over_2.5' in str(i):
                        tb = ''.join(i)
                except:
                    tb = ''



            Job.objects.create(
                    my_day=my_day,
                    my_time=my_time,
                    strana=strana,
                    championat=championat,
                    items1=items1,
                    items2=items2,
                    p1=p1,
                    x=x,
                    p2=p2,
                    f1_0=f1_0,
                    f2_0=f2_0,
                    p1x=p1x,
                    xp2=xp2,
                    tm=tm,
                    tb=tb,
                    oz=oz,
                    p1_p1=p1_p1,
                    x_p1=x_p1,
                    p2_p1=p2_p1,
                    p1_x=p1_x,
                    x_x=x_x,
                    p2_x=p2_x,
                    p1_p2=p1_p2,
                    x_p2=x_p2,
                    p2_p2=p2_p2)
            intelligence = [{
                    'my_day': my_day,
                    'my_time': my_time,
                    'strana': strana,
                    'championat': championat,
                    'items1': items1,
                    'items2': items2,
                    'p1': p1,
                    'x': x,
                    'p2': p2,
                    'f1_0': f1_0,
                    'f2_0': f2_0,
                    'p1x': p1x,
                    'xp2': xp2,
                    'tm': tm,
                    'tb': tb,
                    'oz': oz,
                    'p1_p1': p1_p1,
                    'x_p1': x_p1,
                    'p2_p1': p2_p1,
                    'p1_x': p1_x,
                    'x_x': x_x,
                    'p2_x': p2_x,
                    'p1_p2': p1_p2,
                    'x_p2': x_p2,
                    'p2_p2': p2_p2,
                }]
            print(intelligence)

            # def save_file(items):
            #     with open('1', 'a', newline='', encoding='utf-8')as file:
            #         writer = csv.writer(file, delimiter=';')
            #         for i in items:
            #             writer.writerow(
            #                 [i['my_day'], i['my_time'], i['strana'], i['championat'], i['items1'], i['items2'], i['p1'],
            #                  i['x'], i['p2'], i['f1_0'], i['f2_0'], i['p1x'], i['xp2'], i['tm'],
            #                  i['tb'], i['oz'], i['p1_p1'], i['x_p1'], i['p2_p1'], i['p1_x'], i['x_x'],
            #                  i['p2_x'], i['p1_p2'], i['x_p2'], i['p2_p2']])
            #
            # save_file(intelligence)
        print('конец')


class Command(BaseCommand):
    help = "collect jobs"

    # определяем логику команд
    def handle(self, *args, **options):
        p = MyBetting()
        p.my_data()